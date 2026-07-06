-- ============================================================================
-- Pokemon Codenames - update 03
-- Adds: deal-at-room-creation, a two-player mode, a round counter, and
-- mode-aware turn logic. Paste the whole file into the Supabase SQL Editor
-- and run once. Everything is create-or-replace / add-if-not-exists, so it is
-- safe to run on top of what you already have.
-- ============================================================================

-- Round counter (used mainly by two-player mode's "fewest rounds" goal).
alter table public.rooms add column if not exists clue_count integer not null default 0;

-- ----------------------------------------------------------------------------
-- _deal_board: deal 25 Pokemon + the secret key for a room, based on its mode
-- and settings. Called internally at room creation. Not exposed to clients.
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

  if v_room.mode = 'two_player' then
    -- one team of 9, one assassin, the rest neutral
    v_starting := 'red'; v_red := 9; v_blue := 0; v_neutral := 15;
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
    array_fill('red'::text, array[v_red]) ||
    (case when v_blue > 0 then array_fill('blue'::text, array[v_blue]) else array[]::text[] end) ||
    array_fill('neutral'::text, array[v_neutral]) ||
    array['assassin']
  ) as colour;

  update rooms
     set starting_team = v_starting,
         current_team = v_starting,
         current_clue = null,
         guesses_remaining = 0,
         clue_count = 0,
         winner = null
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- create_room: now also deals the board immediately, so the grid is visible
-- in the lobby before anyone picks a team.
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
  if p_mode not in ('online', 'in_person', 'two_player') then
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
-- join_room: unchanged, except a two-player room is capped at 2 people.
-- ----------------------------------------------------------------------------
create or replace function public.join_room(
  p_code text,
  p_nickname text
)
returns table (room_id uuid, player_id uuid)
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room rooms;
  v_player_id uuid;
begin
  if auth.uid() is null then
    raise exception 'Must be signed in';
  end if;

  select * into v_room from rooms where code = upper(p_code);
  if not found then
    raise exception 'Room not found';
  end if;

  select id into v_player_id
    from players
   where players.room_id = v_room.id and user_id = auth.uid();
  if found then
    return query select v_room.id, v_player_id;
    return;
  end if;

  if v_room.status <> 'lobby' then
    raise exception 'Game already started';
  end if;

  if v_room.mode = 'two_player'
     and (select count(*) from players where players.room_id = v_room.id) >= 2 then
    raise exception 'This two-player room is full';
  end if;

  insert into players (room_id, user_id, nickname)
  values (v_room.id, auth.uid(), p_nickname)
  returning id into v_player_id;

  return query select v_room.id, v_player_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- start_game: the board is already dealt, so this just moves the room into
-- play (which also locks out further joiners). Mode-aware readiness check.
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

  if v_room.mode = 'two_player' then
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

-- ----------------------------------------------------------------------------
-- submit_clue: unchanged, plus it bumps the round counter.
-- ----------------------------------------------------------------------------
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

-- ----------------------------------------------------------------------------
-- reveal_card: mode-aware. In two-player, the turn always returns to the same
-- clue giver, the assassin is an outright loss, and clearing the team wins.
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
  if v_room.mode = 'two_player' then
    v_other := 'red';                    -- turn returns to the same clue giver
  else
    v_other := case when v_current = 'red' then 'blue' else 'red' end;
  end if;

  if v_room.mode in ('online', 'two_player') then
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

  -- assassin
  if v_colour = 'assassin' then
    if v_room.mode = 'two_player' then
      update rooms set status = 'finished', winner = null,
             current_clue = null, guesses_remaining = 0 where id = p_room_id;
    else
      update rooms set status = 'finished', winner = v_other,
             current_clue = null, guesses_remaining = 0 where id = p_room_id;
    end if;
    return;
  end if;

  -- win: a team's whole set revealed
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

  -- turn continuation
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

grant execute on function public.create_room(text, text, jsonb) to authenticated;
grant execute on function public.join_room(text, text) to authenticated;
grant execute on function public.start_game(uuid) to authenticated;
grant execute on function public.submit_clue(uuid, text, int) to authenticated;
grant execute on function public.reveal_card(uuid, int) to authenticated;
