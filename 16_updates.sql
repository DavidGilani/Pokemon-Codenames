-- 16_updates.sql
--
-- 1. Add guess_log column to rooms (tracks every tile reveal with clue context).
-- 2. reveal_card: append each guess to guess_log.
-- 3. _deal_board: reset guess_log on new game.
-- 4. join_room: allow joining a running or finished-guessing game as an observer
--    (team=null, role=null) instead of throwing. Observers see the board without
--    colours, can see who has each role, and can read the clue + guess log.

-- ----------------------------------------------------------------------------
-- 1. New column
-- ----------------------------------------------------------------------------

alter table public.rooms
  add column if not exists guess_log jsonb not null default '[]'::jsonb;

-- ----------------------------------------------------------------------------
-- 2. reveal_card — append guess to guess_log on every tile reveal
-- ----------------------------------------------------------------------------

create or replace function public.reveal_card(
  p_room_id  uuid,
  p_position int
)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room           rooms;
  v_colour         text;
  v_current        text;
  v_other          text;
  v_team_total     int;
  v_team_revealed  int;
  v_new_remaining  int;
  v_card_name      text;
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

  -- Fetch the Pokémon name so we can record it in guess_log
  select name into v_card_name
    from cards where room_id = p_room_id and position = p_position;

  update cards
     set revealed = true, revealed_colour = v_colour
   where room_id = p_room_id and position = p_position;

  -- Record the guess (clue_index is 0-based index into clue_log)
  update rooms
     set guess_log = guess_log || jsonb_build_array(
       jsonb_build_object(
         'clue_index', greatest(v_room.clue_count - 1, 0),
         'team',       v_current,
         'name',       v_card_name,
         'colour',     v_colour,
         'correct',    v_colour = v_current
       )
     )
   where id = p_room_id;

  if v_colour = 'assassin' then
    update rooms
       set status = 'finished', winner = null, finished_at = now(),
           current_clue = null, guesses_remaining = 0, turn_started_at = null
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
             current_clue = null, guesses_remaining = 0, turn_started_at = null
       where id = p_room_id;
      return;
    end if;
  end if;

  if v_colour = v_current then
    update rooms
       set guesses_remaining = guesses_remaining - 1
     where id = p_room_id
     returning guesses_remaining into v_new_remaining;

    if v_new_remaining <= 0 then
      update rooms
         set current_team = v_other, current_clue = null,
             guesses_remaining = 0, turn_started_at = null
       where id = p_room_id;
    end if;
  else
    update rooms
       set current_team = v_other, current_clue = null,
           guesses_remaining = 0, turn_started_at = null
     where id = p_room_id;
  end if;
end;
$$;

-- ----------------------------------------------------------------------------
-- 3. _deal_board — reset guess_log on new game
-- ----------------------------------------------------------------------------

create or replace function public._deal_board(p_room_id uuid)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room        rooms;
  v_generations int[];
  v_wko         boolean;
  v_starting    text;
  v_red         int;
  v_blue        int;
  v_neutral     int;
  v_pool        int;
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

  delete from cards    where room_id = p_room_id;
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
         guess_log         = '[]'::jsonb,
         winner            = null,
         started_at        = null,
         finished_at       = null,
         turn_started_at   = null,
         remaining_red     = v_red,
         remaining_blue    = v_blue
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- 4. join_room — allow joining as observer when all seats are taken
--    Observers get team=null, role=null (same as a fresh lobby join) so
--    isObserver() in the client detects them and shows the observer banner.
-- ----------------------------------------------------------------------------

create or replace function public.join_room(
  p_code     text,
  p_nickname text
)
returns table(room_id uuid, player_id uuid)
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room   rooms;
  v_player players;
begin
  select * into v_room
  from rooms
  where code = upper(trim(p_code));

  if not found then
    raise exception 'Room not found — check the code and try again';
  end if;

  -- Already in this room? Update nickname and return existing record.
  select * into v_player
  from players
  where players.room_id = v_room.id and players.user_id = auth.uid();

  if found then
    update players set nickname = p_nickname where id = v_player.id;
    return query select v_room.id, v_player.id;
    return;
  end if;

  if v_room.status = 'lobby' then
    -- Standard lobby join — role chosen afterwards in the lobby.
    insert into players (room_id, user_id, nickname, is_host, team, role)
    values (v_room.id, auth.uid(), p_nickname, false, null, null)
    returning * into v_player;

  elsif v_room.status = 'in_progress' then
    if v_room.mode = 'turn_by_turn' and not exists (
      select 1 from players
      where players.room_id = v_room.id and players.role = 'operative'
    ) then
      -- Operative slot is open — join as clue receiver.
      insert into players (room_id, user_id, nickname, is_host, team, role)
      values (v_room.id, auth.uid(), p_nickname, false, 'blue', 'operative')
      returning * into v_player;
    else
      -- All seats filled (or classic/two_player in_progress) — join as observer.
      insert into players (room_id, user_id, nickname, is_host, team, role)
      values (v_room.id, auth.uid(), p_nickname, false, null, null)
      returning * into v_player;
    end if;

  else
    raise exception 'This game has ended and is no longer accepting new players';
  end if;

  return query select v_room.id, v_player.id;
end;
$$;

grant execute on function public.reveal_card(uuid, int)  to authenticated;
grant execute on function public._deal_board(uuid)       to authenticated;
grant execute on function public.join_room(text, text)   to authenticated;
