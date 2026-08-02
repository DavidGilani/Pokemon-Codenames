-- 23_updates.sql
--
-- Daily-puzzle upgrades:
--   • Conditional extra clues (change #4): hints now carry target positions, and
--     a new RPC serves the extra clue that helps most with the tiles you still
--     have LEFT to find. Every blue is covered by at least one hint (some
--     grouped), so players can keep asking for as many extra clues as they need.
--   • Clue → Pokémon reveal (change #5): daily_solution now also returns the
--     base clues WITH their target positions, so the end screen can show which
--     Pokémon each clue was pointing to.
--   • get_daily_puzzle strips the hidden target positions from the base clues
--     it serves mid-game (they must not leak which tiles are blue).
--
-- Re-seeds today's two puzzles + the next two days' batch in the new format
-- (base clues and hints both carry "t": the blue positions they cover). Safe to
-- re-run; supersedes the rows from 20/21/22_updates.sql via upsert.
--
-- Note: "5 strikes and you're out" is a client-only change — no schema impact.

-- ----------------------------------------------------------------------------
-- get_daily_puzzle: serve today's board + base clues WITHOUT target positions.
-- ----------------------------------------------------------------------------
create or replace function public.get_daily_puzzle(p_pool text)
returns table(puzzle_date date, clues jsonb, tiles jsonb)
language sql
security definer
set search_path = public
as $$
  select dp.puzzle_date,
    (
      -- strip the hidden "t" (target positions) from each base clue
      select jsonb_agg((c - 't') order by ord)
      from jsonb_array_elements(dp.clues) with ordinality as x(c, ord)
    ) as clues,
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
-- daily_hint_next: the most helpful still-relevant extra clue (change #4).
-- p_revealed = positions the player has already turned over.
-- p_shown    = 0-based indices of hints already given this attempt.
-- Picks the unshown hint covering the most STILL-UNREVEALED blue targets
-- (tie-break: easier category first, then order). Returns null when none help.
-- The returned clue omits "t" so it never leaks tile positions.
-- ----------------------------------------------------------------------------
create or replace function public.daily_hint_next(
  p_date date, p_pool text, p_revealed int[], p_shown int[]
)
returns jsonb
language sql
security definer
set search_path = public
as $$
  with h as (
    select (ord - 1) as idx, hint,
      coalesce((
        select count(*)
        from jsonb_array_elements_text(hint->'t') tt
        where (tt::int) <> all (coalesce(p_revealed, '{}'::int[]))
      ), 0) as unrevealed_cnt,
      coalesce((hint->>'cat')::int, 1) as cat
    from jsonb_array_elements(
      (select hints from daily_puzzles where puzzle_date = p_date and pool = p_pool)
    ) with ordinality as x(hint, ord)
  )
  select jsonb_build_object(
    'word',   hint->>'word',
    'number', (hint->>'number')::int,
    'cat',    coalesce((hint->>'cat')::int, 1),
    'idx',    idx
  )
  from h
  where idx <> all (coalesce(p_shown, '{}'::int[]))
    and unrevealed_cnt > 0
  order by unrevealed_cnt desc, cat asc, idx asc
  limit 1;
$$;

-- ----------------------------------------------------------------------------
-- daily_solution: full board with colours + sprites, AND the base clues with
-- their target positions, for the end-of-game reveal (change #5).
-- ----------------------------------------------------------------------------
create or replace function public.daily_solution(p_date date, p_pool text)
returns jsonb
language sql
security definer
set search_path = public
as $$
  select jsonb_build_object(
    'tiles', (
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
    ),
    'clues', dp.clues
  )
  from daily_puzzles dp
  where dp.puzzle_date = p_date and dp.pool = p_pool;
$$;

grant execute on function public.get_daily_puzzle(text)                      to authenticated;
grant execute on function public.daily_hint_next(date, text, int[], int[])   to authenticated;
grant execute on function public.daily_solution(date, text)                  to authenticated;

-- ============================================================================
-- Re-seed puzzles in the new format (base clues + hints carry target "t").
-- ============================================================================
insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values

-- ── TODAY · Gen I ───────────────────────────────────────────────────────────
(
  current_date, 'gen1',
  '[
    {"word":"BUG","number":4,"cat":1,"t":[0,2,4,6]},
    {"word":"BIRD","number":3,"cat":1,"t":[8,10,12]},
    {"word":"LEGENDARY","number":0,"cat":5,"anti":true},
    {"word":"SKULL","number":1,"cat":2,"t":[14]},
    {"word":"DIGGER","number":1,"cat":3,"t":[16]}
  ]'::jsonb,
  '[
    {"word":"MANTIS","number":1,"cat":2,"t":[0]},
    {"word":"WASP","number":1,"cat":2,"t":[2]},
    {"word":"FUNGUS","number":1,"cat":3,"t":[4]},
    {"word":"PUPA","number":1,"cat":2,"t":[6]},
    {"word":"LEEK","number":1,"cat":4,"t":[8]},
    {"word":"PECK","number":2,"cat":2,"t":[10,12]},
    {"word":"ORPHAN","number":1,"cat":4,"t":[14]},
    {"word":"MOUSE","number":1,"cat":2,"t":[16]}
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

-- ── TODAY · Mixed ─────────────────────────────────────────────────────────────
(
  current_date, 'mixed',
  '[
    {"word":"FIRE","number":3,"cat":1,"t":[0,2,4]},
    {"word":"GHOST","number":2,"cat":1,"t":[4,6]},
    {"word":"WYRM","number":3,"cat":1,"t":[8,10,12]},
    {"word":"AURA","number":1,"cat":4,"t":[14]},
    {"word":"FROG","number":1,"cat":2,"t":[16]}
  ]'::jsonb,
  '[
    {"word":"FLAME","number":1,"cat":2,"t":[0]},
    {"word":"KICK","number":1,"cat":3,"t":[2]},
    {"word":"GLOW","number":1,"cat":2,"t":[4]},
    {"word":"GRIN","number":1,"cat":3,"t":[6]},
    {"word":"FINS","number":1,"cat":2,"t":[8]},
    {"word":"RESCUE","number":1,"cat":4,"t":[10]},
    {"word":"HEADS","number":1,"cat":2,"t":[12]},
    {"word":"JACKAL","number":1,"cat":2,"t":[14]},
    {"word":"TONGUE","number":1,"cat":2,"t":[16]}
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
),

-- ── Day +1 · Gen I ────────────────────────────────────────────────────────────
(
  current_date + 1, 'gen1',
  '[
    {"word":"BLAZE","number":3,"cat":3,"t":[0,2,4]},
    {"word":"HORN","number":3,"cat":2,"t":[6,8,10]},
    {"word":"OPERA","number":1,"cat":4,"t":[12]},
    {"word":"BULK","number":2,"cat":5,"t":[14,16]},
    {"word":"MYTH","number":0,"cat":5,"anti":true}
  ]'::jsonb,
  '[
    {"word":"FLAME","number":1,"cat":2,"t":[0]},
    {"word":"HOUND","number":1,"cat":3,"t":[2]},
    {"word":"MANE","number":1,"cat":2,"t":[4]},
    {"word":"DRILL","number":1,"cat":2,"t":[6]},
    {"word":"BULL","number":1,"cat":2,"t":[8]},
    {"word":"STAG","number":1,"cat":2,"t":[10]},
    {"word":"DIVA","number":1,"cat":4,"t":[12]},
    {"word":"MAMA","number":1,"cat":4,"t":[14]},
    {"word":"NAP","number":1,"cat":3,"t":[16]}
  ]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Magmar','blue'),(1,'Golduck','neutral'),(2,'Arcanine','blue'),(3,'Slowbro','neutral'),
     (4,'Ponyta','blue'),(5,'Dewgong','neutral'),(6,'Rhydon','blue'),(7,'Cloyster','neutral'),
     (8,'Tauros','blue'),(9,'Shellder','neutral'),(10,'Pinsir','blue'),(11,'Gastly','neutral'),
     (12,'Jynx','blue'),(13,'Haunter','neutral'),(14,'Kangaskhan','blue'),(15,'Gengar','neutral'),
     (16,'Snorlax','blue'),(17,'Onix','neutral'),(18,'Drowzee','neutral'),(19,'Hypno','neutral'),
     (20,'Articuno','neutral'),(21,'Electrode','neutral'),(22,'Exeggcute','neutral'),(23,'Chansey','neutral'),
     (24,'Blissey','neutral')
   ) v(position,name,colour))
),

-- ── Day +1 · Mixed ──────────────────────────────────────────────────────────
(
  current_date + 1, 'mixed',
  '[
    {"word":"JAWS","number":3,"cat":2,"t":[0,2,6]},
    {"word":"DESERT","number":2,"cat":3,"t":[2,8]},
    {"word":"FANG","number":2,"cat":2,"t":[4,6]},
    {"word":"SHADE","number":3,"cat":3,"t":[10,12,14]},
    {"word":"THIEF","number":1,"cat":4,"t":[16]}
  ]'::jsonb,
  '[
    {"word":"FOSSIL","number":1,"cat":4,"t":[0]},
    {"word":"FINS","number":1,"cat":2,"t":[2]},
    {"word":"CRESCENT","number":1,"cat":2,"t":[4]},
    {"word":"AXE","number":1,"cat":4,"t":[6]},
    {"word":"OASIS","number":1,"cat":4,"t":[8]},
    {"word":"WITCH","number":1,"cat":2,"t":[10]},
    {"word":"CURSE","number":1,"cat":4,"t":[12]},
    {"word":"BLADE","number":1,"cat":2,"t":[14]},
    {"word":"CLAWS","number":1,"cat":2,"t":[16]}
  ]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Tyranitar','blue'),(1,'Blissey','neutral'),(2,'Garchomp','blue'),(3,'Togekiss','neutral'),
     (4,'Salamence','blue'),(5,'Clefable','neutral'),(6,'Haxorus','blue'),(7,'Sylveon','neutral'),
     (8,'Flygon','blue'),(9,'Gardevoir','neutral'),(10,'Mismagius','blue'),(11,'Florges','neutral'),
     (12,'Spiritomb','blue'),(13,'Arcanine','neutral'),(14,'Aegislash','blue'),(15,'Ninetales','neutral'),
     (16,'Weavile','blue'),(17,'Rapidash','neutral'),(18,'Luxray','neutral'),(19,'Raichu','neutral'),
     (20,'Ampharos','neutral'),(21,'Goodra','neutral'),(22,'Dragapult','neutral'),(23,'Snorlax','neutral'),
     (24,'Chansey','neutral')
   ) v(position,name,colour))
),

-- ── Day +2 · Gen I ────────────────────────────────────────────────────────────
(
  current_date + 2, 'gen1',
  '[
    {"word":"EVOLVE","number":3,"cat":5,"t":[0,2,4]},
    {"word":"LULL","number":2,"cat":3,"t":[6,8]},
    {"word":"ROYALS","number":2,"cat":4,"t":[10,12]},
    {"word":"LAZY","number":2,"cat":3,"t":[14,16]},
    {"word":"STARLET","number":1,"cat":4,"t":[6]}
  ]'::jsonb,
  '[
    {"word":"EEVEE","number":3,"cat":5,"t":[0,2,4]},
    {"word":"BALLOON","number":1,"cat":2,"t":[6]},
    {"word":"EARS","number":1,"cat":2,"t":[8]},
    {"word":"SPEAR","number":1,"cat":2,"t":[10]},
    {"word":"MAMA","number":1,"cat":4,"t":[12]},
    {"word":"CLAM","number":1,"cat":2,"t":[14]},
    {"word":"ICEBERG","number":1,"cat":3,"t":[16]}
  ]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Jolteon','blue'),(1,'Pikachu','neutral'),(2,'Vaporeon','blue'),(3,'Raichu','neutral'),
     (4,'Flareon','blue'),(5,'Vulpix','neutral'),(6,'Jigglypuff','blue'),(7,'Ninetales','neutral'),
     (8,'Wigglytuff','blue'),(9,'Growlithe','neutral'),(10,'Nidoking','blue'),(11,'Arcanine','neutral'),
     (12,'Nidoqueen','blue'),(13,'Meowth','neutral'),(14,'Slowbro','blue'),(15,'Persian','neutral'),
     (16,'Dewgong','blue'),(17,'Psyduck','neutral'),(18,'Golduck','neutral'),(19,'Poliwag','neutral'),
     (20,'Poliwhirl','neutral'),(21,'Tentacool','neutral'),(22,'Tentacruel','neutral'),(23,'Horsea','neutral'),
     (24,'Seaking','neutral')
   ) v(position,name,colour))
),

-- ── Day +2 · Mixed ──────────────────────────────────────────────────────────
(
  current_date + 2, 'mixed',
  '[
    {"word":"BOND","number":3,"cat":5,"t":[0,2,4]},
    {"word":"GRACE","number":3,"cat":3,"t":[4,6,8]},
    {"word":"MOONLIGHT","number":1,"cat":4,"t":[10]},
    {"word":"DIRT","number":3,"cat":1,"t":[12,14,16]},
    {"word":"JAWS","number":1,"cat":2,"t":[12]}
  ]'::jsonb,
  '[
    {"word":"RINGS","number":1,"cat":2,"t":[0]},
    {"word":"SUN","number":1,"cat":4,"t":[2]},
    {"word":"RIBBON","number":1,"cat":2,"t":[4]},
    {"word":"ANGEL","number":1,"cat":2,"t":[6]},
    {"word":"GOWN","number":1,"cat":2,"t":[8]},
    {"word":"STAR","number":1,"cat":4,"t":[10]},
    {"word":"FINS","number":1,"cat":2,"t":[12]},
    {"word":"CROC","number":1,"cat":2,"t":[14]},
    {"word":"DIG","number":1,"cat":2,"t":[16]}
  ]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Umbreon','blue'),(1,'Lucario','neutral'),(2,'Espeon','blue'),(3,'Zoroark','neutral'),
     (4,'Sylveon','blue'),(5,'Bisharp','neutral'),(6,'Togekiss','blue'),(7,'Weavile','neutral'),
     (8,'Gardevoir','blue'),(9,'Absol','neutral'),(10,'Clefable','blue'),(11,'Incineroar','neutral'),
     (12,'Garchomp','blue'),(13,'Metagross','neutral'),(14,'Krookodile','blue'),(15,'Dragonite','neutral'),
     (16,'Excadrill','blue'),(17,'Salamence','neutral'),(18,'Hydreigon','neutral'),(19,'Snorlax','neutral'),
     (20,'Blissey','neutral'),(21,'Chansey','neutral'),(22,'Alomomola','neutral'),(23,'Audino','neutral'),
     (24,'Arcanine','neutral')
   ) v(position,name,colour))
)

on conflict (puzzle_date, pool) do update
  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;
