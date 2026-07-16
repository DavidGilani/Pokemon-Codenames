-- 10_updates.sql
-- 1. Add started_at / finished_at to rooms so the timer works in all modes.
-- 2. Add clue_log jsonb array so every clue is recorded for the in-game log.
-- 3. Update start_game, submit_clue, reveal_card, _deal_board accordingly.

-- ----------------------------------------------------------------------------
-- 1. New columns
-- ----------------------------------------------------------------------------

alter table public.rooms
  add column if not exists started_at  timestamptz,
  add column if not exists finished_at timestamptz,
  add column if not exists clue_log    jsonb not null default '[]'::jsonb;

-- ----------------------------------------------------------------------------
-- 2. start_game — stamp started_at when the game begins
-- ----------------------------------------------------------------------------

create or replace function public.start_game(p_room_id uuid)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room rooms;
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then raise exception 'Room not found'; end if;

  if not exists (
    select 1 from players
    where room_id = p_room_id and user_id = auth.uid() and is_host
  ) then
    raise exception 'Only the host can start the game';
  end if;
  if v_room.status <> 'lobby' then
    raise exception 'Game already started';
  end if;

  if v_room.mode in ('two_player', 'turn_by_turn') then
    if not exists (select 1 from players where room_id = p_room_id and role = 'spymaster')
       or not exists (select 1 from players where room_id = p_room_id and role = 'operative') then
      raise exception 'Need a clue giver and a clue receiver before starting';
    end if;
  else
    if (
      select count(distinct team) from players
      where room_id = p_room_id and role = 'spymaster' and team in ('red', 'blue')
    ) < 2 then
      raise exception 'Each team needs a clue giver before starting';
    end if;
  end if;

  update rooms
     set status     = 'in_progress',
         started_at = now()
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- 3. submit_clue — append each clue to the log
-- ----------------------------------------------------------------------------

create or replace function public.submit_clue(
  p_room_id uuid,
  p_word    text,
  p_number  int
)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room rooms;
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then raise exception 'Room not found'; end if;
  if v_room.status <> 'in_progress' then raise exception 'Game is not in progress'; end if;
  if v_room.current_clue is not null then raise exception 'A clue is already in play'; end if;
  if p_number < 0 then raise exception 'Clue number must be zero or more'; end if;

  if v_room.mode in ('two_player', 'turn_by_turn') then
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid() and role = 'spymaster'
    ) then
      raise exception 'Only the clue giver can give a clue';
    end if;
  else
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid()
        and role = 'spymaster' and team = v_room.current_team
    ) then
      raise exception 'Only the current team clue giver can give a clue';
    end if;
  end if;

  update rooms
     set current_clue      = jsonb_build_object('word', p_word, 'number', p_number),
         guesses_remaining = p_number + 1,
         clue_count        = clue_count + 1,
         clue_log          = clue_log || jsonb_build_array(
           jsonb_build_object(
             'team',   v_room.current_team,
             'word',   p_word,
             'number', p_number
           )
         )
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- 4. reveal_card — stamp finished_at on game-over paths
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
    v_other := v_current;
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
    update rooms
       set status = 'finished', winner = null, finished_at = now(),
           current_clue = null, guesses_remaining = 0
     where id = p_room_id;
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
      update rooms
         set status = 'finished', winner = v_colour, finished_at = now(),
             current_clue = null, guesses_remaining = 0
       where id = p_room_id;
      return;
    end if;
  end if;

  if v_colour = v_current then
    update rooms set guesses_remaining = guesses_remaining - 1 where id = p_room_id;
    if (select guesses_remaining from rooms where id = p_room_id) <= 0 then
      update rooms
         set current_team = v_other, current_clue = null, guesses_remaining = 0
       where id = p_room_id;
    end if;
  else
    update rooms
       set current_team = v_other, current_clue = null, guesses_remaining = 0
     where id = p_room_id;
  end if;
end;
$$;

-- ----------------------------------------------------------------------------
-- 5. _deal_board — reset clue_log on new game
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
         clue_log          = '[]'::jsonb,
         winner            = null,
         started_at        = null,
         finished_at       = null,
         remaining_red     = v_red,
         remaining_blue    = v_blue
   where id = p_room_id;
end;
$$;

grant execute on function public.start_game(uuid)           to authenticated;
grant execute on function public.submit_clue(uuid, text, int) to authenticated;
grant execute on function public.reveal_card(uuid, int)     to authenticated;
