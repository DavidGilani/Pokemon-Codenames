-- 15_updates.sql
--
-- Turn-by-turn "clue-first, invite-second" flow:
--
-- 1. start_game: turn_by_turn only requires a clue giver to start.
--    The operative joins later via the share link.
--
-- 2. join_room: allow joining a running turn_by_turn game.
--    The arriving player is automatically assigned as operative (team=blue,
--    role=operative) if the seat is open, so they land directly in the
--    game — no extra claim_seat step needed.
--
-- 3. claim_seat: allow claiming the operative seat in a running turn_by_turn
--    game as a belt-and-suspenders fallback (e.g. if someone joins via
--    the room code rather than a direct link and lands as an observer).

-- ----------------------------------------------------------------------------
-- 1. start_game
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

  if v_room.mode = 'turn_by_turn' then
    -- Solo start: only the clue giver is required. The operative joins later
    -- by clicking the share link after the first clue is submitted.
    if not exists (
      select 1 from players where room_id = p_room_id and role = 'spymaster'
    ) then
      raise exception 'Claim the clue giver role before starting';
    end if;

  elsif v_room.mode = 'two_player' then
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
-- 2. join_room
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

  elsif v_room.status = 'in_progress' and v_room.mode = 'turn_by_turn' then
    -- Allow joining a running turn-by-turn game as the operative if the slot
    -- is still open.
    if exists (
      select 1 from players
      where players.room_id = v_room.id and players.role = 'operative'
    ) then
      raise exception 'The guessing seat is already taken in this game';
    end if;

    insert into players (room_id, user_id, nickname, is_host, team, role)
    values (v_room.id, auth.uid(), p_nickname, false, 'blue', 'operative')
    returning * into v_player;

  else
    raise exception 'This game is no longer accepting new players';
  end if;

  return query select v_room.id, v_player.id;
end;
$$;

-- ----------------------------------------------------------------------------
-- 3. claim_seat — allow claiming operative in a running turn_by_turn game
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

  -- Turn-by-turn: allow operative claim while in_progress (observer → operative)
  if v_room.mode = 'turn_by_turn' and v_room.status = 'in_progress' then
    if p_role <> 'operative' then
      raise exception 'Only the operative seat can be claimed once the game has started';
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

  if v_room.mode in ('two_player', 'turn_by_turn') then
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
end;
$$;

grant execute on function public.start_game(uuid)             to authenticated;
grant execute on function public.join_room(text, text)        to authenticated;
grant execute on function public.claim_seat(uuid, text, text) to authenticated;
