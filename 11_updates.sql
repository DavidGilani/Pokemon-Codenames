-- 11_updates.sql
-- Fix two bugs in reveal_card / submit_clue that could end a turn early:
--
-- 1. submit_clue: clue number 0 (unlimited guesses) was setting
--    guesses_remaining = 1, so the first correct guess would immediately
--    end the turn. Now uses 99 as a sentinel for unlimited.
--
-- 2. reveal_card: guesses_remaining was decremented in one UPDATE then
--    re-read in a separate SELECT, leaving a theoretical race window.
--    Replaced with a single UPDATE … RETURNING so the check is atomic.

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
  else
    if not exists (
      select 1 from players
      where room_id = p_room_id and user_id = auth.uid()
        and role = 'spymaster' and team = v_room.current_team
    ) then
      raise exception 'Only the current team clue giver can give a clue';
    end if;
  end if;

  -- Number 0 means unlimited guesses; use 99 as a sentinel so the
  -- guesses_remaining check in reveal_card never triggers prematurely.
  v_remaining := case when p_number = 0 then 99 else p_number + 1 end;

  update rooms
     set current_clue      = jsonb_build_object('word', p_word, 'number', p_number),
         guesses_remaining = v_remaining,
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
  v_new_remaining int;
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
    -- Atomic decrement: read the new value in the same statement to avoid
    -- any race between a separate UPDATE and SELECT.
    update rooms
       set guesses_remaining = guesses_remaining - 1
     where id = p_room_id
     returning guesses_remaining into v_new_remaining;

    if v_new_remaining <= 0 then
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

grant execute on function public.submit_clue(uuid, text, int) to authenticated;
grant execute on function public.reveal_card(uuid, int)       to authenticated;
