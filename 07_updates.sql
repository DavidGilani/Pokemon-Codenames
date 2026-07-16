-- 07_updates.sql
-- 1. Add turn_by_turn as a valid play mode (same game logic as two_player,
--    different client-side UX: elapsed-time timer, auto-share on actions).
-- 2. Allow all players to read card_key once the game is finished, so the
--    "See the board" button can reveal unrevealed tile colours after game over.

-- ----------------------------------------------------------------------------
-- 1. turn_by_turn mode support
--    All server-side functions that gate on 'two_player' are updated to also
--    accept 'turn_by_turn'. The game logic is identical.
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
  if p_mode not in ('online', 'in_person', 'two_player', 'turn_by_turn') then
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

  update rooms set status = 'in_progress' where id = p_room_id;
end;
$$;

create or replace function public.submit_clue(
  p_room_id uuid,
  p_word text,
  p_number int
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

  if not exists (
    select 1 from players
    where room_id = p_room_id and user_id = auth.uid()
      and role = 'spymaster' and team = v_room.current_team
  ) then
    raise exception 'Only the current team clue giver can give a clue';
  end if;

  update rooms
     set current_clue = jsonb_build_object('word', p_word, 'number', p_number),
         guesses_remaining = p_number + 1,
         clue_count = clue_count + 1
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
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then raise exception 'Room not found'; end if;
  if v_room.status <> 'in_progress' then raise exception 'Game is not in progress'; end if;
  if v_room.current_clue is null then raise exception 'Wait for a clue before guessing'; end if;

  v_current := v_room.current_team;
  if v_room.mode in ('two_player', 'turn_by_turn') then
    v_other := 'red';
  else
    v_other := case when v_current = 'red' then 'blue' else 'red' end;
  end if;

  if v_room.mode in ('online', 'two_player', 'turn_by_turn') then
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
    if v_room.mode in ('two_player', 'turn_by_turn') then
      update rooms set status = 'finished', winner = null,
             current_clue = null, guesses_remaining = 0 where id = p_room_id;
    else
      update rooms set status = 'finished', winner = v_other,
             current_clue = null, guesses_remaining = 0 where id = p_room_id;
    end if;
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

-- ----------------------------------------------------------------------------
-- 2. card_key RLS: allow reads once the game is finished so all players can
--    see the full board via the "See the board" button on the end screen.
-- ----------------------------------------------------------------------------

drop policy if exists "Spymasters can view card key" on public.card_key;
drop policy if exists "spymasters_select_card_key" on public.card_key;

create policy "spymasters_select_card_key" on public.card_key
  for select
  using (
    exists (
      select 1 from players p
      join rooms r on r.id = p.room_id
      where p.room_id = card_key.room_id
        and p.user_id = auth.uid()
        and (p.role = 'spymaster' or r.status = 'finished')
    )
  );

grant execute on function public.create_room(text, text, jsonb) to authenticated;
grant execute on function public.start_game(uuid) to authenticated;
grant execute on function public.submit_clue(uuid, text, int) to authenticated;
grant execute on function public.reveal_card(uuid, int) to authenticated;
