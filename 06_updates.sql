-- 06_updates.sql
-- 1. Add remaining_red / remaining_blue to rooms so any player (including
--    observers) can see how many team tiles are left without needing the card key.
-- 2. Fix the cards SELECT policy so observers (team=null) can read the board.

-- ----------------------------------------------------------------------------
-- 1. Remaining-tile counters on rooms
-- ----------------------------------------------------------------------------

alter table public.rooms
  add column if not exists remaining_red  integer not null default 0,
  add column if not exists remaining_blue integer not null default 0;

-- Trigger function: when a card is revealed, decrement the matching counter.
create or replace function public._update_remaining_counts()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
declare
  v_colour text;
begin
  -- Only act when revealed flips from false → true
  if not (NEW.revealed and not OLD.revealed) then
    return NEW;
  end if;

  select colour into v_colour
  from card_key
  where room_id = NEW.room_id and position = NEW.position;

  if v_colour = 'red' then
    update rooms set remaining_red = greatest(remaining_red - 1, 0) where id = NEW.room_id;
  elsif v_colour = 'blue' then
    update rooms set remaining_blue = greatest(remaining_blue - 1, 0) where id = NEW.room_id;
  end if;

  return NEW;
end;
$$;

drop trigger if exists trg_update_remaining on public.cards;
create trigger trg_update_remaining
  after update on public.cards
  for each row execute function public._update_remaining_counts();

-- Backfill existing rooms with correct remaining counts based on current state.
update public.rooms r
set
  remaining_red = (
    select count(*) from card_key k
    left join cards c on c.room_id = k.room_id and c.position = k.position
    where k.room_id = r.id and k.colour = 'red'
      and (c.revealed is null or not c.revealed)
  ),
  remaining_blue = (
    select count(*) from card_key k
    left join cards c on c.room_id = k.room_id and c.position = k.position
    where k.room_id = r.id and k.colour = 'blue'
      and (c.revealed is null or not c.revealed)
  );

-- Also initialise these counts in _deal_board after inserting the card key.
-- (We recreate _deal_board with remaining counts set at deal time.)
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
     set starting_team    = v_starting,
         current_team     = v_starting,
         current_clue     = null,
         guesses_remaining = 0,
         clue_count       = 0,
         winner           = null,
         remaining_red    = v_red,
         remaining_blue   = v_blue
   where id = p_room_id;
end;
$$;

-- ----------------------------------------------------------------------------
-- 2. Cards RLS: allow any authenticated player in the room to read cards,
--    regardless of whether they have a team assignment (covers observers).
-- ----------------------------------------------------------------------------

-- Drop the existing select policy and replace it.
drop policy if exists "Players can view cards in their room" on public.cards;
drop policy if exists "players_select_cards" on public.cards;

create policy "players_select_cards" on public.cards
  for select
  using (
    exists (
      select 1 from players
      where players.room_id = cards.room_id
        and players.user_id = auth.uid()
    )
  );
