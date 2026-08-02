-- 21_updates.sql
--
-- 1. Daily-puzzle attempt tracking (daily_attempts) + RPCs so we learn how
--    players do: when they start, which tiles they tap, time taken, hints used,
--    mistakes, outcome, and a post-game difficulty rating.
-- 2. Re-seed today's two daily puzzles with NO assassin (all non-blue tiles are
--    neutral now) — fixes rows already inserted by 20_updates.sql.

-- ----------------------------------------------------------------------------
-- 1. Attempt tracking
-- ----------------------------------------------------------------------------
create table if not exists public.daily_attempts (
  id           uuid primary key default gen_random_uuid(),
  user_id      uuid not null default auth.uid(),
  puzzle_date  date not null,
  pool         text not null,
  started_at   timestamptz not null default now(),
  finished_at  timestamptz,
  duration_ms  int,
  outcome      text,          -- 'win' | 'lose'
  blues_found  int,
  mistakes     int,
  hints_used   int,
  taps         jsonb,         -- [{position, name, colour}] in tap order
  rating       text           -- 'way_too_easy'|'slightly_easy'|'just_right'|'slightly_hard'|'way_too_hard'
);

alter table public.daily_attempts enable row level security;

-- Owners may read their own attempts (analytics can read via service role).
drop policy if exists daily_attempts_select_own on public.daily_attempts;
create policy daily_attempts_select_own on public.daily_attempts
  for select using (user_id = auth.uid());

-- Start an attempt (logs the start time); returns the attempt id.
create or replace function public.daily_start_attempt(p_date date, p_pool text)
returns uuid
language plpgsql
security definer
set search_path = public
as $$
declare v_id uuid;
begin
  insert into daily_attempts (user_id, puzzle_date, pool)
  values (auth.uid(), p_date, p_pool)
  returning id into v_id;
  return v_id;
end;
$$;

-- Finish an attempt with the full record.
create or replace function public.daily_finish_attempt(
  p_id uuid, p_outcome text, p_blues int, p_mistakes int,
  p_hints int, p_duration int, p_taps jsonb
)
returns void
language plpgsql
security definer
set search_path = public
as $$
begin
  update daily_attempts
     set finished_at = now(), outcome = p_outcome, blues_found = p_blues,
         mistakes = p_mistakes, hints_used = p_hints, duration_ms = p_duration,
         taps = coalesce(p_taps, '[]'::jsonb)
   where id = p_id and user_id = auth.uid();
end;
$$;

-- Record the player's difficulty rating.
create or replace function public.daily_rate_attempt(p_id uuid, p_rating text)
returns void
language plpgsql
security definer
set search_path = public
as $$
begin
  update daily_attempts set rating = p_rating
   where id = p_id and user_id = auth.uid();
end;
$$;

grant execute on function public.daily_start_attempt(date, text)                      to authenticated;
grant execute on function public.daily_finish_attempt(uuid, text, int, int, int, int, jsonb) to authenticated;
grant execute on function public.daily_rate_attempt(uuid, text)                       to authenticated;

-- ----------------------------------------------------------------------------
-- 2. Re-seed today's puzzles with no assassin (all non-blue = neutral)
-- ----------------------------------------------------------------------------
insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values
(
  current_date, 'gen1',
  '[
    {"word":"BUG","number":4,"cat":1},
    {"word":"BIRD","number":3,"cat":1},
    {"word":"LEGENDARY","number":0,"cat":5,"anti":true},
    {"word":"SKULL","number":1,"cat":2},
    {"word":"DIGGER","number":1,"cat":3}
  ]'::jsonb,
  '[
    {"word":"WASP","number":1,"cat":2},
    {"word":"ORPHAN","number":1,"cat":4},
    {"word":"PECK","number":2,"cat":2}
  ]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Scyther','blue'),(1,'Meowth','neutral'),(2,'Beedrill','blue'),(3,'Victreebel','neutral'),
     (4,'Parasect','blue'),(5,'Magnemite','neutral'),(6,'Kakuna','blue'),(7,'Tentacool','neutral'),
     (8,'Farfetch''d','blue'),(9,'Kabuto','neutral'),(10,'Fearow','blue'),(11,'Exeggutor','neutral'),
     (12,'Pidgeotto','blue'),(13,'Koffing','neutral'),(14,'Cubone','blue'),(15,'Lapras','neutral'),
     (16,'Sandshrew','blue'),(17,'Seel','neutral'),(18,'Persian','neutral'),(19,'Gastly','neutral'),
     (20,'Vaporeon','neutral'),(21,'Articuno','neutral'),(22,'Jolteon','neutral'),(23,'Graveler','neutral'),
     (24,'Haunter','neutral')
   ) v(position,name,colour))
),
(
  current_date, 'mixed',
  '[
    {"word":"FIRE","number":3,"cat":1},
    {"word":"GHOST","number":2,"cat":1},
    {"word":"WYRM","number":3,"cat":1},
    {"word":"AURA","number":1,"cat":4},
    {"word":"FROG","number":1,"cat":2}
  ]'::jsonb,
  '[
    {"word":"JACKAL","number":1,"cat":2},
    {"word":"HEADS","number":1,"cat":2},
    {"word":"KICK","number":1,"cat":3}
  ]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Charizard','blue'),(1,'Squirtle','neutral'),(2,'Blaziken','blue'),(3,'Pikachu','neutral'),
     (4,'Chandelure','blue'),(5,'Snorlax','neutral'),(6,'Gengar','blue'),(7,'Lapras','neutral'),
     (8,'Garchomp','blue'),(9,'Umbreon','neutral'),(10,'Dragonite','blue'),(11,'Sceptile','neutral'),
     (12,'Hydreigon','blue'),(13,'Swampert','neutral'),(14,'Lucario','blue'),(15,'Metagross','neutral'),
     (16,'Greninja','blue'),(17,'Empoleon','neutral'),(18,'Luxray','neutral'),(19,'Roserade','neutral'),
     (20,'Sylveon','neutral'),(21,'Corviknight','neutral'),(22,'Rillaboom','neutral'),(23,'Toxtricity','neutral'),
     (24,'Gardevoir','neutral')
   ) v(position,name,colour))
)
on conflict (puzzle_date, pool) do update
  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;
