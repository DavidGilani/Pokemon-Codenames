-- 09_updates.sql
-- Fix two_player and turn_by_turn board layout and reveal logic.
--
-- In 2-player modes both players are assigned team='blue', so the 9
-- secret tiles must be BLUE in the card_key (not red). v_other must
-- also be 'blue' in reveal_card so a wrong guess keeps the turn at
-- the single team rather than flipping to a non-existent 'red' side.

-- ----------------------------------------------------------------------------
-- 1. _deal_board: use blue tiles for 2-player modes
-- ----------------------------------------------------------------------------

create or replace function public._deal_board(p_room_id uuid)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room rooms;
  v_generations int[];
  v_wko boolean;
  v_starting text;
  v_red int;
  v_blue int;
  v_neutral int;
  v_pool int;
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then raise exception 'Room not found'; end if;

  v_generations := coalesce(
    (select array_agg(g::int) from jsonb_array_elements_text(v_room.settings->'generations') g),
    array[1]
  );
  v_wko := coalesce((v_room.settings->>'well_known_only')::boolean, false);

  select count(*) into v_pool
  from pokemon
  where generation = any(v_generations)
    and (not v_wko or is_well_known);
  if v_pool < 25 then
    raise exception 'Not enough Pokemon in the selected pool (need 25, found %)', v_pool;
  end if;

  if v_room.mode in ('two_player', 'turn_by_turn') then
    -- Single team (blue), 9 tiles to find, rest are bystanders + assassin
    v_starting := 'blue'; v_red := 0; v_blue := 9; v_neutral := 15;
  else
    v_starting := (array['red', 'blue'])[1 + floor(random() * 2)::int];
    if v_starting = 'red' then v_red := 9; v_blue := 8; else v_red := 8; v_blue := 9; end if;
    v_neutral := 7;
  end if;

  delete from cards where room_id = p_room_id;
  delete from card_key where room_id = p_room_id;

  insert into cards (room_id, position, pokemon_id, name, sprite_url)
  select p_room_id, (row_number() over ()) - 1, id, name, sprite_url
  from (
    select id, name, sprite_url
    from pokemon
    where generation = any(v_generations)
      and (not v_wko or is_well_known)
    order by random()
    limit 25
  ) p;

  insert into card_key (room_id, position, colour)
  select p_room_id, (row_number() over (order by random())) - 1, colour
  from unnest(
    (case when v_red > 0 then array_fill('red'::text, array[v_red]) else array[]::text[] end) ||
    array_fill('blue'::text, array[v_blue]) ||
    array_fill('neutral'::text, array[v_neutral]) ||
    array['assassin']
  ) as colour;

  update rooms
     set starting_team     = v_starting,
         current_team      = v_starting,
         current_clue      = null,
         guesses_remaining = 0,
         clue_count        = 0,
         winner            = null,
         remaining_red     = v_red,
         remaining_blue    = v_blue
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- 2. reveal_card: in 2-player modes the "other team" after a wrong guess is
--    still 'blue' (there is only one team), so the turn never flips away.
-- ----------------------------------------------------------------------------

create or replace function public.reveal_card(
  p_room_id uuid,
  p_position int
)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room rooms;
  v_colour text;
  v_current text;
  v_other text;
  v_team_total int;
  v_team_revealed int;
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then raise exception 'Room not found'; end if;
  if v_room.status <> 'in_progress' then raise exception 'Game is not in progress'; end if;
  if v_room.current_clue is null then raise exception 'Wait for a clue before guessing'; end if;

  v_current := v_room.current_team;
  if v_room.mode in ('two_player', 'turn_by_turn') then
    v_other := v_current;  -- single team: wrong guess ends the turn but team stays the same
  else
    v_other := case when v_current = 'red' then 'blue' else 'red' end;
  end if;

  if v_room.mode in ('two_player', 'turn_by_turn') then
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid() and role = 'operative'
    ) then
      raise exception 'Only the clue receiver can reveal a tile';
    end if;
  elsif v_room.mode = 'online' then
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid()
        and team = v_current and role = 'operative'
    ) then
      raise exception 'Only a guessing-team clue receiver can reveal a tile';
    end if;
  else
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid()
        and (is_host or team = v_current)
    ) then
      raise exception 'Not allowed to reveal a tile';
    end if;
  end if;

  if not exists (
    select 1 from cards
    where room_id = p_room_id and position = p_position and not revealed
  ) then
    raise exception 'That tile is not available';
  end if;

  select colour into v_colour
    from card_key where room_id = p_room_id and position = p_position;

  update cards
     set revealed = true, revealed_colour = v_colour
   where room_id = p_room_id and position = p_position;

  if v_colour = 'assassin' then
    update rooms set status = 'finished', winner = null,
           current_clue = null, guesses_remaining = 0 where id = p_room_id;
    return;
  end if;

  if v_colour in ('red', 'blue') then
    select
      (select count(*) from card_key where room_id = p_room_id and colour = v_colour),
      (select count(*) from cards c
         join card_key k on k.room_id = c.room_id and k.position = c.position
       where c.room_id = p_room_id and k.colour = v_colour and c.revealed)
    into v_team_total, v_team_revealed;

    if v_team_revealed >= v_team_total then
      update rooms set status = 'finished', winner = v_colour,
             current_clue = null, guesses_remaining = 0 where id = p_room_id;
      return;
    end if;
  end if;

  if v_colour = v_current then
    update rooms set guesses_remaining = guesses_remaining - 1 where id = p_room_id;
    if (select guesses_remaining from rooms where id = p_room_id) <= 0 then
      update rooms set current_team = v_other, current_clue = null, guesses_remaining = 0
       where id = p_room_id;
    end if;
  else
    update rooms set current_team = v_other, current_clue = null, guesses_remaining = 0
     where id = p_room_id;
  end if;
end;
$$;

grant execute on function public.reveal_card(uuid, int) to authenticated;
