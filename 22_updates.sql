-- 22_updates.sql
--
-- Harder daily puzzle batch (v3). Four puzzles for the next two days:
--   current_date+1 gen1, current_date+1 mixed
--   current_date+2 gen1, current_date+2 mixed
--
-- Design principles:
--   • Board-first: blues cluster into natural groups absent from neutrals.
--   • Skewed harder: at most 1 Cat-1 anchor per puzzle; majority are Cat 3–5
--     and each covers MULTIPLE blues. Overlap between clues for depth.
--   • Strict 3-char letter rule verified (no clue shares 3+ consecutive chars
--     with any board Pokémon name, case-insensitive, in either direction).
--   • No assassin: 9 blue + 16 neutral.
--
-- Clue → blue mappings (for puzzle authors; never sent to client):
--
-- Day+1 Gen I:
--   BLAZE  × 3  → Magmar, Arcanine, Ponyta           (Fire types, no neutral is Fire)
--   HORN   × 3  → Rhydon, Tauros, Pinsir             (prominent horns in sprite)
--   STRIPED× 1  → Electabuzz                         (black/yellow stripe sprite)
--   OPERA  × 1  → Jynx                               (Pokédex: sings operatically)
--   BULK   × 2  → Kangaskhan, Snorlax               (two of heaviest Gen I)
--   Hints: FLAME×1→Magmar  MAMA×1→Kangaskhan  CATTLE×1→Tauros
--
-- Day+1 Mixed:
--   JAWS   × 3  → Tyranitar, Garchomp, Haxorus       (massive jaws in sprite)
--   DESERT × 2  → Flygon, Garchomp                   (desert habitat; Garchomp overlaps JAWS)
--   FANG   × 2  → Salamence, Haxorus                 (giant fangs; Haxorus overlaps JAWS)
--   SHADE  × 3  → Mismagius, Spiritomb, Aegislash     (ghost/shadow category)
--   THIEF  × 1  → Weavile                            (Pokédex: steals food in groups)
--   Hints: FOSSIL×1→Tyranitar  WITCH×1→Mismagius  BLADE×1→Aegislash
--
-- Day+2 Gen I:
--   EVOLVE × 3  → Jolteon, Vaporeon, Flareon         (all evolve from Eevee – Cat 5 link)
--   LULL   × 2  → Jigglypuff, Wigglytuff             (lullaby singers)
--   ROYALS × 2  → Nidoking, Nidoqueen               (the royal Nido pair)
--   LAZY   × 2  → Slowbro, Dewgong                  (famously laid-back Pokédex entries)
--   STARLET× 1  → Jigglypuff                        (performer/star; overlaps LULL)
--   Hints: THUNDER×1→Jolteon  LANCE×1→Nidoking  CLAM×1→Slowbro
--
-- Day+2 Mixed:
--   BOND   × 3  → Umbreon, Espeon, Sylveon           (all evolve from Eevee via friendship/affection)
--   GRACE  × 3  → Togekiss, Gardevoir, Sylveon        (graceful/elegant trio; Sylveon overlaps BOND)
--   MOONLIGHT×1 → Clefable                           (Pokédex: appears on full-moon nights)
--   DIRT   × 3  → Garchomp, Krookodile, Excadrill     (Ground-type; no neutral is Ground)
--   JAWS   × 1  → Garchomp                           (shark-jaw sprite; overlaps DIRT)
--   Hints: TWILIGHT×1→Umbreon  DIG×1→Excadrill  CROC×1→Krookodile

insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values

-- ────────────────────────────────────────────────────────────────────────────
-- Day +1 · Gen I
-- Blues: Magmar, Arcanine, Ponyta, Rhydon, Tauros, Pinsir, Electabuzz, Jynx, Kangaskhan, Snorlax
-- Wait: that is 10. Drop Electabuzz to keep 9 blues and fold into STRIPED alone.
-- Blues (9): Magmar, Arcanine, Ponyta, Rhydon, Tauros, Pinsir, Jynx, Kangaskhan, Snorlax
-- STRIPED is dropped (only one target); use MYTH × 0 anti-clue instead.
-- Board: neutrals include Articuno so MYTH × 0 is useful.
-- Revised clues: BLAZE×3, HORN×3, OPERA×1, BULK×2, MYTH×0
-- ────────────────────────────────────────────────────────────────────────────
(
  current_date + 1, 'gen1',
  '[
    {"word":"BLAZE",  "number":3,"cat":3},
    {"word":"HORN",   "number":3,"cat":2},
    {"word":"OPERA",  "number":1,"cat":4},
    {"word":"BULK",   "number":2,"cat":5},
    {"word":"MYTH",   "number":0,"cat":5,"anti":true}
  ]'::jsonb,
  '[
    {"word":"FLAME",  "number":1,"cat":2},
    {"word":"MAMA",   "number":1,"cat":4},
    {"word":"CATTLE", "number":1,"cat":3}
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

-- ────────────────────────────────────────────────────────────────────────────
-- Day +1 · Mixed
-- Blues: Tyranitar, Garchomp, Haxorus, Flygon, Salamence,
--        Mismagius, Spiritomb, Aegislash, Weavile
-- ────────────────────────────────────────────────────────────────────────────
(
  current_date + 1, 'mixed',
  '[
    {"word":"JAWS",   "number":3,"cat":2},
    {"word":"DESERT", "number":2,"cat":3},
    {"word":"FANG",   "number":2,"cat":2},
    {"word":"SHADE",  "number":3,"cat":3},
    {"word":"THIEF",  "number":1,"cat":4}
  ]'::jsonb,
  '[
    {"word":"FOSSIL", "number":1,"cat":4},
    {"word":"WITCH",  "number":1,"cat":2},
    {"word":"BLADE",  "number":1,"cat":2}
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

-- ────────────────────────────────────────────────────────────────────────────
-- Day +2 · Gen I
-- Blues: Jolteon, Vaporeon, Flareon, Jigglypuff, Wigglytuff,
--        Nidoking, Nidoqueen, Slowbro, Dewgong
-- ────────────────────────────────────────────────────────────────────────────
(
  current_date + 2, 'gen1',
  '[
    {"word":"EVOLVE",  "number":3,"cat":5},
    {"word":"LULL",    "number":2,"cat":3},
    {"word":"ROYALS",  "number":2,"cat":4},
    {"word":"LAZY",    "number":2,"cat":3},
    {"word":"STARLET", "number":1,"cat":4}
  ]'::jsonb,
  '[
    {"word":"THUNDER", "number":1,"cat":1},
    {"word":"LANCE",   "number":1,"cat":2},
    {"word":"CLAM",    "number":1,"cat":2}
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

-- ────────────────────────────────────────────────────────────────────────────
-- Day +2 · Mixed
-- Blues: Umbreon, Espeon, Sylveon, Togekiss, Gardevoir, Clefable,
--        Garchomp, Krookodile, Excadrill
-- ────────────────────────────────────────────────────────────────────────────
(
  current_date + 2, 'mixed',
  '[
    {"word":"BOND",      "number":3,"cat":5},
    {"word":"GRACE",     "number":3,"cat":3},
    {"word":"MOONLIGHT", "number":1,"cat":4},
    {"word":"DIRT",      "number":3,"cat":1},
    {"word":"JAWS",      "number":1,"cat":2}
  ]'::jsonb,
  '[
    {"word":"TWILIGHT",  "number":1,"cat":4},
    {"word":"DIG",       "number":1,"cat":2},
    {"word":"CROC",      "number":1,"cat":2}
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
