-- 18_updates.sql
--
-- Big batch:
--
-- A. New mode: two_player_ai — two humans (blue) vs an AI opponent (red).
--    The board is classic-style (9 blue, 8 red, 7 neutral, 1 assassin, blue
--    starts). After each human turn ends, the AI reveals some red tiles
--    (1 on easy, 1-2 on medium, 2-3 on hard) and hands the turn back to blue.
--    The AI never gives clues. Humans win by clearing all blue; the AI wins by
--    clearing all red (or if a human hits the assassin).
--
-- B. Remove the "start game" step for all two-player modes. Claiming the clue
--    giver seat now auto-starts the game (board is already dealt at creation).
--
-- C. The two-player timer now starts from the FIRST clue, not from game start:
--    submit_clue stamps started_at the first time it is called.
--
-- Run the whole file in the Supabase SQL editor.

-- ----------------------------------------------------------------------------
-- create_room — allow the new two_player_ai mode
-- ----------------------------------------------------------------------------

create or replace function public.create_room(
  p_nickname text,
  p_mode text,
  p_settings jsonb
)
returns table (room_id uuid, room_code text, player_id uuid)
language plpgsql
security definer
set search_path = public
as $$
declare
  v_code text;
  v_room_id uuid;
  v_player_id uuid;
begin
  if auth.uid() is null then
    raise exception 'Must be signed in';
  end if;
  if p_mode not in ('online', 'in_person', 'two_player', 'turn_by_turn', 'two_player_ai') then
    raise exception 'Invalid mode';
  end if;

  loop
    v_code := upper(substr(md5(random()::text), 1, 4));
    exit when not exists (select 1 from rooms where code = v_code);
  end loop;

  insert into rooms (code, mode, settings, status)
  values (v_code, p_mode, coalesce(p_settings, '{}'::jsonb), 'lobby')
  returning id into v_room_id;

  insert into players (room_id, user_id, nickname, is_host)
  values (v_room_id, auth.uid(), p_nickname, true)
  returning id into v_player_id;

  perform _deal_board(v_room_id);

  return query select v_room_id, v_code, v_player_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- _deal_board — add a classic-style board for two_player_ai
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
    -- Cooperative blue-only board.
    v_starting := 'blue'; v_red := 0; v_blue := 9; v_neutral := 15;
  elsif v_room.mode = 'two_player_ai' then
    -- Classic-style board: humans are blue and go first.
    v_starting := 'blue'; v_blue := 9; v_red := 8; v_neutral := 7;
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
-- _ai_reveal — the AI opponent's turn: reveal some red tiles, then hand back
-- ----------------------------------------------------------------------------

create or replace function public._ai_reveal(p_room_id uuid)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room          rooms;
  v_diff          text;
  v_count         int;
  v_red_total     int;
  v_red_revealed  int;
  r               record;
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then return; end if;
  if v_room.mode <> 'two_player_ai' then return; end if;
  if v_room.status <> 'in_progress' then return; end if;

  v_diff := coalesce(v_room.settings->>'ai_difficulty', 'easy');
  if v_diff = 'hard' then
    v_count := 2 + floor(random() * 2)::int;   -- 2 or 3
  elsif v_diff = 'medium' then
    v_count := 1 + floor(random() * 2)::int;   -- 1 or 2
  else
    v_count := 1;                              -- easy
  end if;

  -- Reveal up to v_count random unrevealed red tiles.
  for r in
    select c.position
    from cards c
    join card_key k on k.room_id = c.room_id and k.position = c.position
    where c.room_id = p_room_id and not c.revealed and k.colour = 'red'
    order by random()
    limit v_count
  loop
    update cards set revealed = true, revealed_colour = 'red'
     where room_id = p_room_id and position = r.position;
  end loop;

  -- Did the AI clear all its red tiles?
  select
    (select count(*) from card_key where room_id = p_room_id and colour = 'red'),
    (select count(*) from cards c
       join card_key k on k.room_id = c.room_id and k.position = c.position
     where c.room_id = p_room_id and k.colour = 'red' and c.revealed)
  into v_red_total, v_red_revealed;

  if v_red_revealed >= v_red_total then
    update rooms
       set status = 'finished', winner = 'red', finished_at = now(),
           current_team = 'blue', current_clue = null,
           guesses_remaining = 0, turn_started_at = null
     where id = p_room_id;
    return;
  end if;

  -- Hand the turn back to the humans and wait for the next clue.
  update rooms
     set current_team = 'blue', current_clue = null,
         guesses_remaining = 0, turn_started_at = null
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- submit_clue — stamp started_at on the first clue (two-player timer start)
--               and gate two_player_ai (blue clue giver only)
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
  v_room      rooms;
  v_remaining int;
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
  elsif v_room.mode = 'two_player_ai' then
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid()
        and role = 'spymaster' and team = 'blue'
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

  v_remaining := case when p_number = 0 then 99 else p_number + 1 end;

  update rooms
     set current_clue      = jsonb_build_object('word', p_word, 'number', p_number),
         guesses_remaining = v_remaining,
         clue_count        = clue_count + 1,
         turn_started_at   = now(),
         started_at        = coalesce(started_at, now()),
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
-- reveal_card — record guesses, and trigger the AI turn when a human turn ends
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
  v_is_ai          boolean;
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then raise exception 'Room not found'; end if;
  if v_room.status <> 'in_progress' then raise exception 'Game is not in progress'; end if;
  if v_room.current_clue is null then raise exception 'Wait for a clue before guessing'; end if;

  v_is_ai   := v_room.mode = 'two_player_ai';
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
  elsif v_is_ai then
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid()
        and role = 'operative' and team = 'blue'
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

  select name into v_card_name
    from cards where room_id = p_room_id and position = p_position;

  update cards
     set revealed = true, revealed_colour = v_colour
   where room_id = p_room_id and position = p_position;

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
    -- Correct guess: use up one guess; continue unless exhausted.
    update rooms
       set guesses_remaining = guesses_remaining - 1
     where id = p_room_id
     returning guesses_remaining into v_new_remaining;

    if v_new_remaining <= 0 then
      if v_is_ai then
        perform _ai_reveal(p_room_id);
      else
        update rooms
           set current_team = v_other, current_clue = null,
               guesses_remaining = 0, turn_started_at = null
         where id = p_room_id;
      end if;
    end if;
  else
    -- Wrong guess (neutral or opponent colour): turn ends.
    if v_is_ai then
      perform _ai_reveal(p_room_id);
    else
      update rooms
         set current_team = v_other, current_clue = null,
             guesses_remaining = 0, turn_started_at = null
       where id = p_room_id;
    end if;
  end if;
end;
$$;

-- ----------------------------------------------------------------------------
-- end_turn — human pass triggers the AI turn in two_player_ai
-- ----------------------------------------------------------------------------

create or replace function public.end_turn(p_room_id uuid)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room      rooms;
  v_next_team text;
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then raise exception 'Room not found'; end if;
  if v_room.status <> 'in_progress' then raise exception 'Game is not in progress'; end if;
  if v_room.current_clue is null then raise exception 'No clue is active'; end if;

  if v_room.mode = 'two_player_ai' then
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid() and role = 'operative'
    ) then
      raise exception 'Only the clue receiver can pass';
    end if;
    perform _ai_reveal(p_room_id);
    return;

  elsif v_room.mode in ('two_player', 'turn_by_turn') then
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid() and role = 'operative'
    ) then
      raise exception 'Only the clue receiver can pass';
    end if;
    v_next_team := v_room.current_team;
  elsif v_room.mode = 'online' then
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid()
        and team = v_room.current_team and role = 'operative'
    ) then
      raise exception 'Only a guessing-team operative can pass';
    end if;
    v_next_team := case when v_room.current_team = 'red' then 'blue' else 'red' end;
  else -- in_person
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid()
        and (is_host or team = v_room.current_team)
    ) then
      raise exception 'Not allowed to pass';
    end if;
    v_next_team := case when v_room.current_team = 'red' then 'blue' else 'red' end;
  end if;

  update rooms
     set current_team      = v_next_team,
         current_clue      = null,
         guesses_remaining = 0,
         turn_started_at   = null
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- claim_seat — auto-start two-player modes when the clue giver is claimed,
--              and treat two_player_ai like the other two-player modes.
-- ----------------------------------------------------------------------------

create or replace function public.claim_seat(
  p_room_id uuid,
  p_team    text,
  p_role    text
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

  if p_role not in ('spymaster', 'operative') then
    raise exception 'Invalid role';
  end if;
  if p_team not in ('red', 'blue') then
    raise exception 'Invalid team';
  end if;

  -- Turn-by-turn / vs-AI: allow the operative to claim while in progress
  -- (observer → operative), e.g. when joining via the room code.
  if v_room.mode in ('turn_by_turn', 'two_player_ai') and v_room.status = 'in_progress' then
    if p_role <> 'operative' then
      raise exception 'Only the clue receiver seat can be claimed once the game has started';
    end if;
    if exists (
      select 1 from players
      where room_id = p_room_id and role = 'operative' and user_id <> auth.uid()
    ) then
      raise exception 'There is already a clue receiver in this game';
    end if;
  elsif v_room.status <> 'lobby' then
    raise exception 'The game has already started';
  end if;

  if v_room.mode in ('two_player', 'turn_by_turn', 'two_player_ai') then
    if p_role = 'spymaster' and exists (
      select 1 from players
      where room_id = p_room_id and role = 'spymaster' and user_id <> auth.uid()
    ) then
      raise exception 'There is already a clue giver in this game';
    end if;
  else
    if p_role = 'spymaster' and exists (
      select 1 from players
      where room_id = p_room_id and team = p_team and role = 'spymaster' and user_id <> auth.uid()
    ) then
      raise exception 'There is already a clue giver for this team';
    end if;
  end if;

  update players
     set team = p_team,
         role = p_role
   where room_id = p_room_id
     and user_id = auth.uid();

  if not found then
    raise exception 'You are not in this room';
  end if;

  -- Auto-start: in two-player modes there is no separate "start" step. As soon
  -- as a clue giver is seated, the game begins (the board is already dealt).
  if v_room.mode in ('two_player', 'turn_by_turn', 'two_player_ai')
     and p_role = 'spymaster'
     and v_room.status = 'lobby' then
    update rooms set status = 'in_progress' where id = p_room_id;
  end if;
end;
$$;

-- ----------------------------------------------------------------------------
-- join_room — for any two-player mode, drop arrivals straight into the open
--             clue-receiver seat; otherwise join as an observer.
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

  select * into v_player
  from players
  where players.room_id = v_room.id and players.user_id = auth.uid();

  if found then
    update players set nickname = p_nickname where id = v_player.id;
    return query select v_room.id, v_player.id;
    return;
  end if;

  if v_room.status = 'lobby' then
    insert into players (room_id, user_id, nickname, is_host, team, role)
    values (v_room.id, auth.uid(), p_nickname, false, null, null)
    returning * into v_player;

  elsif v_room.status = 'in_progress' then
    if v_room.mode in ('two_player', 'turn_by_turn', 'two_player_ai')
       and not exists (
         select 1 from players
         where players.room_id = v_room.id and players.role = 'operative'
       ) then
      insert into players (room_id, user_id, nickname, is_host, team, role)
      values (v_room.id, auth.uid(), p_nickname, false, 'blue', 'operative')
      returning * into v_player;
    else
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

grant execute on function public.create_room(text, text, jsonb)  to authenticated;
grant execute on function public._deal_board(uuid)               to authenticated;
grant execute on function public._ai_reveal(uuid)                to authenticated;
grant execute on function public.submit_clue(uuid, text, int)    to authenticated;
grant execute on function public.reveal_card(uuid, int)          to authenticated;
grant execute on function public.end_turn(uuid)                  to authenticated;
grant execute on function public.claim_seat(uuid, text, text)    to authenticated;
grant execute on function public.join_room(text, text)           to authenticated;
