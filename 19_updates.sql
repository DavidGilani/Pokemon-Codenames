-- 19_updates.sql
--
-- Two-player vs AI improvements:
--
-- 1. The AI's turn is now a SEPARATE step (public.ai_take_turn) instead of
--    happening instantly inside reveal_card / end_turn. When a human turn ends
--    the room simply moves to current_team = 'red' (the AI's pending turn); the
--    client waits a couple of seconds ("AI is choosing…") and then calls
--    ai_take_turn, which reveals the red tile(s) and hands the turn back to
--    blue. This gives the AI a visible, deliberate turn.
--
-- 2. Each tile the AI reveals is appended to guess_log (with "ai": true) so the
--    turn log can show which Pokémon the AI flipped to red.

-- ----------------------------------------------------------------------------
-- reveal_card — in two_player_ai, end of a human turn parks on current_team=red
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
    if not exists (select 1 from players where room_id = p_room_id and user_id = auth.uid() and role = 'operative') then
      raise exception 'Only the clue receiver can reveal a tile';
    end if;
  elsif v_is_ai then
    if not exists (select 1 from players where room_id = p_room_id and user_id = auth.uid() and role = 'operative' and team = 'blue') then
      raise exception 'Only the clue receiver can reveal a tile';
    end if;
  elsif v_room.mode = 'online' then
    if not exists (select 1 from players where room_id = p_room_id and user_id = auth.uid() and team = v_current and role = 'operative') then
      raise exception 'Only a guessing-team clue receiver can reveal a tile';
    end if;
  else
    if not exists (select 1 from players where room_id = p_room_id and user_id = auth.uid() and (is_host or team = v_current)) then
      raise exception 'Not allowed to reveal a tile';
    end if;
  end if;

  if not exists (select 1 from cards where room_id = p_room_id and position = p_position and not revealed) then
    raise exception 'That tile is not available';
  end if;

  select colour into v_colour from card_key where room_id = p_room_id and position = p_position;
  select name into v_card_name from cards where room_id = p_room_id and position = p_position;

  update cards set revealed = true, revealed_colour = v_colour
   where room_id = p_room_id and position = p_position;

  update rooms
     set guess_log = guess_log || jsonb_build_array(jsonb_build_object(
           'clue_index', greatest(v_room.clue_count - 1, 0),
           'team', v_current, 'name', v_card_name, 'colour', v_colour,
           'correct', v_colour = v_current))
   where id = p_room_id;

  if v_colour = 'assassin' then
    update rooms set status = 'finished', winner = null, finished_at = now(),
        current_clue = null, guesses_remaining = 0, turn_started_at = null
     where id = p_room_id;
    return;
  end if;

  if v_colour in ('red', 'blue') then
    select
      (select count(*) from card_key where room_id = p_room_id and colour = v_colour),
      (select count(*) from cards c join card_key k on k.room_id = c.room_id and k.position = c.position
         where c.room_id = p_room_id and k.colour = v_colour and c.revealed)
    into v_team_total, v_team_revealed;
    if v_team_revealed >= v_team_total then
      update rooms set status = 'finished', winner = v_colour, finished_at = now(),
          current_clue = null, guesses_remaining = 0, turn_started_at = null
       where id = p_room_id;
      return;
    end if;
  end if;

  if v_colour = v_current then
    update rooms set guesses_remaining = guesses_remaining - 1
     where id = p_room_id returning guesses_remaining into v_new_remaining;
    if v_new_remaining <= 0 then
      -- Turn ends. In vs-AI, park on the AI's (red) turn; the client will
      -- trigger ai_take_turn after a short "thinking" pause.
      update rooms set current_team = v_other, current_clue = null,
          guesses_remaining = 0, turn_started_at = null
       where id = p_room_id;
    end if;
  else
    update rooms set current_team = v_other, current_clue = null,
        guesses_remaining = 0, turn_started_at = null
     where id = p_room_id;
  end if;
end;
$$;

-- ----------------------------------------------------------------------------
-- end_turn — vs-AI pass parks on current_team = 'red' (AI pending)
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
    if not exists (select 1 from players where room_id = p_room_id and user_id = auth.uid() and role = 'operative') then
      raise exception 'Only the clue receiver can pass';
    end if;
    update rooms set current_team = 'red', current_clue = null,
        guesses_remaining = 0, turn_started_at = null
     where id = p_room_id;
    return;
  elsif v_room.mode in ('two_player', 'turn_by_turn') then
    if not exists (select 1 from players where room_id = p_room_id and user_id = auth.uid() and role = 'operative') then
      raise exception 'Only the clue receiver can pass';
    end if;
    v_next_team := v_room.current_team;
  elsif v_room.mode = 'online' then
    if not exists (select 1 from players where room_id = p_room_id and user_id = auth.uid() and team = v_room.current_team and role = 'operative') then
      raise exception 'Only a guessing-team operative can pass';
    end if;
    v_next_team := case when v_room.current_team = 'red' then 'blue' else 'red' end;
  else
    if not exists (select 1 from players where room_id = p_room_id and user_id = auth.uid() and (is_host or team = v_room.current_team)) then
      raise exception 'Not allowed to pass';
    end if;
    v_next_team := case when v_room.current_team = 'red' then 'blue' else 'red' end;
  end if;

  update rooms set current_team = v_next_team, current_clue = null,
      guesses_remaining = 0, turn_started_at = null
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- ai_take_turn — the AI reveals its red tile(s) and hands the turn back to blue
--                Any player in the room may call it; it only acts while it is
--                the AI's (red) pending turn, so it is safe if both clients call.
-- ----------------------------------------------------------------------------
create or replace function public.ai_take_turn(p_room_id uuid)
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
  -- Atomically claim the AI turn: only proceed if it is currently red's turn.
  update rooms set turn_started_at = turn_started_at
   where id = p_room_id and mode = 'two_player_ai'
     and status = 'in_progress' and current_team = 'red';
  if not found then return; end if;

  select * into v_room from rooms where id = p_room_id;

  v_diff := coalesce(v_room.settings->>'ai_difficulty', 'easy');
  if v_diff = 'hard' then      v_count := 2 + floor(random() * 2)::int;   -- 2 or 3
  elsif v_diff = 'medium' then v_count := 1 + floor(random() * 2)::int;   -- 1 or 2
  else                         v_count := 1;                              -- easy
  end if;

  for r in
    select c.position, c.name
    from cards c
    join card_key k on k.room_id = c.room_id and k.position = c.position
    where c.room_id = p_room_id and not c.revealed and k.colour = 'red'
    order by random()
    limit v_count
  loop
    update cards set revealed = true, revealed_colour = 'red'
     where room_id = p_room_id and position = r.position;
    update rooms
       set guess_log = guess_log || jsonb_build_array(jsonb_build_object(
             'clue_index', greatest(clue_count - 1, 0),
             'team', 'red', 'name', r.name, 'colour', 'red',
             'correct', true, 'ai', true))
     where id = p_room_id;
  end loop;

  select
    (select count(*) from card_key where room_id = p_room_id and colour = 'red'),
    (select count(*) from cards c join card_key k on k.room_id = c.room_id and k.position = c.position
       where c.room_id = p_room_id and k.colour = 'red' and c.revealed)
  into v_red_total, v_red_revealed;

  if v_red_revealed >= v_red_total then
    update rooms set status = 'finished', winner = 'red', finished_at = now(),
        current_team = 'blue', current_clue = null, guesses_remaining = 0, turn_started_at = null
     where id = p_room_id;
    return;
  end if;

  update rooms set current_team = 'blue', current_clue = null,
      guesses_remaining = 0, turn_started_at = null
   where id = p_room_id;
end;
$$;

grant execute on function public.reveal_card(uuid, int) to authenticated;
grant execute on function public.end_turn(uuid)         to authenticated;
grant execute on function public.ai_take_turn(uuid)     to authenticated;
