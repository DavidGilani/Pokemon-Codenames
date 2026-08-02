-- 20_updates.sql
--
-- 1-player DAILY PUZZLE.
--
-- A solo, same-for-everyone daily. 5x5 board: 9 blue, 15 neutral, 1 assassin
-- (no red). The player gets 5 pre-written clues that cover all 9 blues, one
-- turn, 2 mistakes allowed (3rd ends), assassin = instant end, and may reveal
-- up to 3 extra "hint" clues. Two puzzles per day: pool 'gen1' and 'mixed'.
--
-- The colour key is hidden: the table has RLS with no policies (so no direct
-- reads), and everything goes through security-definer RPCs. get_daily_puzzle
-- returns the board WITHOUT colours; daily_reveal returns one tile's colour;
-- daily_hint returns one extra clue on request; daily_solution returns the full
-- key for the end-of-game board reveal.

-- ----------------------------------------------------------------------------
-- Table
-- ----------------------------------------------------------------------------
create table if not exists public.daily_puzzles (
  puzzle_date date not null,
  pool        text not null check (pool in ('gen1', 'mixed')),
  clues       jsonb not null,           -- 5 base clues: [{word, number, cat, anti?}]
  hints       jsonb not null default '[]'::jsonb,  -- up to 3 extra clues, same shape
  tiles       jsonb not null,           -- 25 tiles: [{position, name, colour}]
  primary key (puzzle_date, pool)
);

alter table public.daily_puzzles enable row level security;
-- No policies => no direct selects for anon/authenticated. Access via RPCs only.

-- ----------------------------------------------------------------------------
-- get_daily_puzzle: today's (or latest) puzzle for a pool, WITHOUT the colours.
-- Resolves each tile's pokemon_id + sprite_url from the pokemon table by name.
-- ----------------------------------------------------------------------------
create or replace function public.get_daily_puzzle(p_pool text)
returns table(puzzle_date date, clues jsonb, tiles jsonb)
language sql
security definer
set search_path = public
as $$
  select dp.puzzle_date, dp.clues,
    (
      select jsonb_agg(
        jsonb_build_object(
          'position',   (t->>'position')::int,
          'name',       t->>'name',
          'pokemon_id', pk.id,
          'sprite_url', pk.sprite_url
        ) order by (t->>'position')::int
      )
      from jsonb_array_elements(dp.tiles) t
      left join pokemon pk on lower(pk.name) = lower(t->>'name')
    ) as tiles
  from daily_puzzles dp
  where dp.pool = p_pool and dp.puzzle_date <= current_date
  order by dp.puzzle_date desc
  limit 1;
$$;

-- ----------------------------------------------------------------------------
-- daily_reveal: the colour of one tile (called when the player taps it).
-- ----------------------------------------------------------------------------
create or replace function public.daily_reveal(p_date date, p_pool text, p_position int)
returns text
language sql
security definer
set search_path = public
as $$
  select t->>'colour'
  from daily_puzzles dp,
       lateral jsonb_array_elements(dp.tiles) t
  where dp.puzzle_date = p_date and dp.pool = p_pool
    and (t->>'position')::int = p_position;
$$;

-- ----------------------------------------------------------------------------
-- daily_hint: one extra clue (0-based index), revealed on request.
-- ----------------------------------------------------------------------------
create or replace function public.daily_hint(p_date date, p_pool text, p_index int)
returns jsonb
language sql
security definer
set search_path = public
as $$
  select dp.hints -> p_index
  from daily_puzzles dp
  where dp.puzzle_date = p_date and dp.pool = p_pool;
$$;

-- ----------------------------------------------------------------------------
-- daily_solution: full board with colours + sprite, for the end-of-game reveal.
-- ----------------------------------------------------------------------------
create or replace function public.daily_solution(p_date date, p_pool text)
returns jsonb
language sql
security definer
set search_path = public
as $$
  select (
    select jsonb_agg(
      jsonb_build_object(
        'position',   (t->>'position')::int,
        'name',       t->>'name',
        'colour',     t->>'colour',
        'pokemon_id', pk.id,
        'sprite_url', pk.sprite_url
      ) order by (t->>'position')::int
    )
    from jsonb_array_elements(dp.tiles) t
    left join pokemon pk on lower(pk.name) = lower(t->>'name')
  )
  from daily_puzzles dp
  where dp.puzzle_date = p_date and dp.pool = p_pool;
$$;

grant execute on function public.get_daily_puzzle(text)            to authenticated;
grant execute on function public.daily_reveal(date, text, int)     to authenticated;
grant execute on function public.daily_hint(date, text, int)       to authenticated;
grant execute on function public.daily_solution(date, text)        to authenticated;

-- ----------------------------------------------------------------------------
-- Seed: two puzzles for today (pool 'gen1' and 'mixed').
-- cat = clue-difficulty category (1 easiest … 5 hardest); anti = anti-clue.
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
     (24,'Haunter','assassin')
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
     (24,'Gardevoir','assassin')
   ) v(position,name,colour))
)
on conflict (puzzle_date, pool) do update
  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;
