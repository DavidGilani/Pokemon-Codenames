-- 26_updates.sql
--
-- Rework of the daily puzzles for 2026-08-09 .. 2026-08-16 to the full updated
-- ruleset: no-disguised-type clues, new harder categories (Connection: MEGA /
-- TRADE / STONE / MOONSTONE / INTIMIDATE / GENIUS / IMPOSTER; Mythology: KITSUNE;
-- Real-world archetype: HOUND / PANTHER / SERPENT / CEPHALOPOD / GRIZZLY / HAWK /
-- HORSE), the per-tier category-mix caps, RANDOMISED clue order, no (word->exact
-- Pokemon / exact group) reuse within the rolling fortnight, and the Brutal/Evil
-- structural gate (<=1 single-tile clue, clue-numbers sum >= 11). Explicit dates
-- so it is unambiguous regardless of when run. Upserts over prior rows.
--
-- Difficulty per day (Mon->Sun ramp Easy..Evil, both weeks):
--   2026-08-09 gen1   Evil
--   2026-08-09 mixed  Evil
--   2026-08-10 gen1   Easy
--   2026-08-10 mixed  Easy
--   2026-08-11 gen1   Medium
--   2026-08-11 mixed  Medium
--   2026-08-12 gen1   Challenging
--   2026-08-12 mixed  Challenging
--   2026-08-13 gen1   Hard
--   2026-08-13 mixed  Hard
--   2026-08-14 gen1   Hard
--   2026-08-14 mixed  Hard
--   2026-08-15 gen1   Brutal
--   2026-08-15 mixed  Brutal
--   2026-08-16 gen1   Evil
--   2026-08-16 mixed  Evil

insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values
(
  '2026-08-09', 'gen1',
  '[{"word": "GENIUS", "number": 1, "cat": 5, "t": [16]}, {"word": "RIVALS", "number": 2, "cat": 4, "t": [12, 14]}, {"word": "ROYALS", "number": 2, "cat": 4, "t": [0, 2]}, {"word": "MOONSTONE", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "FOSSIL", "number": 3, "cat": 4, "t": [6, 8, 10]}]'::jsonb,
  '[{"word": "FLAME", "number": 1, "cat": 2, "t": [14]}, {"word": "SHELL", "number": 1, "cat": 2, "t": [8]}, {"word": "SPIRAL", "number": 1, "cat": 2, "t": [6]}, {"word": "FANGS", "number": 1, "cat": 2, "t": [10]}, {"word": "SPOON", "number": 1, "cat": 2, "t": [16]}, {"word": "PLUG", "number": 1, "cat": 2, "t": [12]}, {"word": "STAR", "number": 1, "cat": 4, "t": [4]}, {"word": "BARBS", "number": 1, "cat": 2, "t": [0]}, {"word": "ARMOR", "number": 1, "cat": 2, "t": [2]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Nidoking','blue'),(1,'Pikachu','neutral'),(2,'Nidoqueen','blue'),(3,'Raichu','neutral'),(4,'Clefable','blue'),(5,'Weezing','neutral'),(6,'Omanyte','blue'),(7,'Haunter','neutral'),(8,'Kabuto','blue'),(9,'Snorlax','neutral'),(10,'Aerodactyl','blue'),(11,'Lapras','neutral'),(12,'Electabuzz','blue'),(13,'Machamp','neutral'),(14,'Magmar','blue'),(15,'Onix','neutral'),(16,'Alakazam','blue'),(17,'Golem','neutral'),(18,'Slowbro','neutral'),(19,'Tentacruel','neutral'),(20,'Vaporeon','neutral'),(21,'Jolteon','neutral'),(22,'Muk','neutral'),(23,'Scyther','neutral'),(24,'Gyarados','neutral')) v(position,name,colour))
),
(
  '2026-08-09', 'mixed',
  '[{"word": "TRICKSTER", "number": 3, "cat": 5, "t": [8, 10, 12]}, {"word": "NIGHTMARE", "number": 1, "cat": 4, "t": [14]}, {"word": "STEALTH", "number": 2, "cat": 4, "t": [8, 16]}, {"word": "PSEUDO", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "INTIMIDATE", "number": 2, "cat": 5, "t": [0, 6]}]'::jsonb,
  '[{"word": "ROBOT", "number": 1, "cat": 2, "t": [2]}, {"word": "ROCKET", "number": 1, "cat": 4, "t": [16]}, {"word": "HAIR", "number": 1, "cat": 2, "t": [10]}, {"word": "SERPENT", "number": 1, "cat": 3, "t": [6]}, {"word": "SMILE", "number": 1, "cat": 3, "t": [14]}, {"word": "CRESCENT", "number": 1, "cat": 2, "t": [0]}, {"word": "FOX", "number": 1, "cat": 2, "t": [8]}, {"word": "HEADS", "number": 1, "cat": 2, "t": [4]}, {"word": "COPY", "number": 1, "cat": 4, "t": [12]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Salamence','blue'),(1,'Pikachu','neutral'),(2,'Metagross','blue'),(3,'Raichu','neutral'),(4,'Hydreigon','blue'),(5,'Snorlax','neutral'),(6,'Gyarados','blue'),(7,'Blissey','neutral'),(8,'Zoroark','blue'),(9,'Chansey','neutral'),(10,'Grimmsnarl','blue'),(11,'Audino','neutral'),(12,'Ditto','blue'),(13,'Togekiss','neutral'),(14,'Gengar','blue'),(15,'Sylveon','neutral'),(16,'Dragapult','blue'),(17,'Umbreon','neutral'),(18,'Espeon','neutral'),(19,'Clefable','neutral'),(20,'Gardevoir','neutral'),(21,'Rillaboom','neutral'),(22,'Ampharos','neutral'),(23,'Lapras','neutral'),(24,'Wailord','neutral')) v(position,name,colour))
),
(
  '2026-08-10', 'gen1',
  '[{"word": "COIN", "number": 1, "cat": 2, "t": [16]}, {"word": "FIRE", "number": 2, "cat": 1, "t": [0, 2]}, {"word": "BUG", "number": 2, "cat": 1, "t": [12, 14]}, {"word": "WATER", "number": 2, "cat": 1, "t": [4, 6]}, {"word": "ELECTRIC", "number": 2, "cat": 1, "t": [8, 10]}]'::jsonb,
  '[{"word": "GEM", "number": 1, "cat": 2, "t": [6]}, {"word": "FLAME", "number": 1, "cat": 2, "t": [2]}, {"word": "BARB", "number": 1, "cat": 2, "t": [14]}, {"word": "FOX", "number": 1, "cat": 2, "t": [0]}, {"word": "KITTEN", "number": 1, "cat": 2, "t": [16]}, {"word": "SHELL", "number": 1, "cat": 2, "t": [4]}, {"word": "SPHERE", "number": 1, "cat": 2, "t": [8]}, {"word": "COCOON", "number": 1, "cat": 2, "t": [12]}, {"word": "POLES", "number": 1, "cat": 2, "t": [10]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Vulpix','blue'),(1,'Rattata','neutral'),(2,'Charmander','blue'),(3,'Ekans','neutral'),(4,'Squirtle','blue'),(5,'Sandshrew','neutral'),(6,'Staryu','blue'),(7,'Zubat','neutral'),(8,'Voltorb','blue'),(9,'Diglett','neutral'),(10,'Magnemite','blue'),(11,'Mankey','neutral'),(12,'Metapod','blue'),(13,'Machop','neutral'),(14,'Weedle','blue'),(15,'Geodude','neutral'),(16,'Meowth','blue'),(17,'Gastly','neutral'),(18,'Onix','neutral'),(19,'Drowzee','neutral'),(20,'Cubone','neutral'),(21,'Koffing','neutral'),(22,'Grimer','neutral'),(23,'Persian','neutral'),(24,'Jigglypuff','neutral')) v(position,name,colour))
),
(
  '2026-08-10', 'mixed',
  '[{"word": "WATER", "number": 2, "cat": 1, "t": [4, 6]}, {"word": "FIRE", "number": 2, "cat": 1, "t": [0, 2]}, {"word": "GRASS", "number": 2, "cat": 1, "t": [8, 10]}, {"word": "PSYCHIC", "number": 2, "cat": 1, "t": [12, 14]}, {"word": "JACKAL", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  '[{"word": "SERPENT", "number": 1, "cat": 3, "t": [6]}, {"word": "EMBER", "number": 1, "cat": 2, "t": [0]}, {"word": "GOWN", "number": 1, "cat": 2, "t": [14]}, {"word": "FOX", "number": 1, "cat": 2, "t": [2]}, {"word": "PLANT", "number": 1, "cat": 2, "t": [10]}, {"word": "SUN", "number": 1, "cat": 4, "t": [12]}, {"word": "PENGUIN", "number": 1, "cat": 2, "t": [4]}, {"word": "AURA", "number": 1, "cat": 4, "t": [16]}, {"word": "GECKO", "number": 1, "cat": 2, "t": [8]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Charizard','blue'),(1,'Snorlax','neutral'),(2,'Ninetales','blue'),(3,'Blissey','neutral'),(4,'Empoleon','blue'),(5,'Chansey','neutral'),(6,'Milotic','blue'),(7,'Audino','neutral'),(8,'Sceptile','blue'),(9,'Togekiss','neutral'),(10,'Leafeon','blue'),(11,'Sylveon','neutral'),(12,'Espeon','blue'),(13,'Umbreon','neutral'),(14,'Gardevoir','blue'),(15,'Pikachu','neutral'),(16,'Lucario','blue'),(17,'Raichu','neutral'),(18,'Luxray','neutral'),(19,'Garchomp','neutral'),(20,'Tyranitar','neutral'),(21,'Dragonite','neutral'),(22,'Salamence','neutral'),(23,'Rhyperior','neutral'),(24,'Machamp','neutral')) v(position,name,colour))
),
(
  '2026-08-11', 'gen1',
  '[{"word": "HORN", "number": 2, "cat": 2, "t": [8, 10]}, {"word": "ELECTRIC", "number": 2, "cat": 1, "t": [4, 6]}, {"word": "FIRE", "number": 2, "cat": 1, "t": [0, 2]}, {"word": "BURROW", "number": 2, "cat": 3, "t": [12, 14]}, {"word": "BABY", "number": 1, "cat": 4, "t": [16]}]'::jsonb,
  '[{"word": "DRILL", "number": 1, "cat": 2, "t": [8]}, {"word": "DUCK", "number": 1, "cat": 2, "t": [0]}, {"word": "CURL", "number": 1, "cat": 3, "t": [12]}, {"word": "MOLE", "number": 1, "cat": 2, "t": [14]}, {"word": "SPARK", "number": 1, "cat": 2, "t": [6]}, {"word": "FLUFFY", "number": 1, "cat": 2, "t": [2]}, {"word": "CHEEKS", "number": 1, "cat": 2, "t": [4]}, {"word": "POUCH", "number": 1, "cat": 4, "t": [16]}, {"word": "ARMOR", "number": 1, "cat": 2, "t": [10]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Magmar','blue'),(1,'Gengar','neutral'),(2,'Flareon','blue'),(3,'Haunter','neutral'),(4,'Pikachu','blue'),(5,'Gastly','neutral'),(6,'Jolteon','blue'),(7,'Koffing','neutral'),(8,'Rhydon','blue'),(9,'Weezing','neutral'),(10,'Nidoqueen','blue'),(11,'Grimer','neutral'),(12,'Sandshrew','blue'),(13,'Muk','neutral'),(14,'Diglett','blue'),(15,'Snorlax','neutral'),(16,'Kangaskhan','blue'),(17,'Lapras','neutral'),(18,'Machop','neutral'),(19,'Machamp','neutral'),(20,'Persian','neutral'),(21,'Kingler','neutral'),(22,'Slowbro','neutral'),(23,'Tentacruel','neutral'),(24,'Meowth','neutral')) v(position,name,colour))
),
(
  '2026-08-11', 'mixed',
  '[{"word": "ICICLE", "number": 1, "cat": 2, "t": [16]}, {"word": "WATER", "number": 2, "cat": 1, "t": [0, 2]}, {"word": "CEPHALOPOD", "number": 2, "cat": 3, "t": [8, 10]}, {"word": "PSEUDO", "number": 2, "cat": 5, "t": [12, 14]}, {"word": "GHOST", "number": 2, "cat": 1, "t": [4, 6]}]'::jsonb,
  '[{"word": "GRIN", "number": 1, "cat": 3, "t": [4]}, {"word": "ROBOT", "number": 1, "cat": 2, "t": [14]}, {"word": "FROG", "number": 1, "cat": 2, "t": [0]}, {"word": "SQUID", "number": 1, "cat": 2, "t": [8]}, {"word": "SNEASEL", "number": 1, "cat": 4, "t": [16]}, {"word": "WITCH", "number": 1, "cat": 2, "t": [6]}, {"word": "SUCKERS", "number": 1, "cat": 2, "t": [10]}, {"word": "MUD", "number": 1, "cat": 2, "t": [2]}, {"word": "FINS", "number": 1, "cat": 2, "t": [12]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Greninja','blue'),(1,'Pikachu','neutral'),(2,'Swampert','blue'),(3,'Raichu','neutral'),(4,'Gengar','blue'),(5,'Snorlax','neutral'),(6,'Mismagius','blue'),(7,'Blissey','neutral'),(8,'Malamar','blue'),(9,'Togekiss','neutral'),(10,'Grapploct','blue'),(11,'Sylveon','neutral'),(12,'Garchomp','blue'),(13,'Umbreon','neutral'),(14,'Metagross','blue'),(15,'Espeon','neutral'),(16,'Weavile','blue'),(17,'Arcanine','neutral'),(18,'Ninetales','neutral'),(19,'Luxray','neutral'),(20,'Rillaboom','neutral'),(21,'Charizard','neutral'),(22,'Audino','neutral'),(23,'Chansey','neutral'),(24,'Lapras','neutral')) v(position,name,colour))
),
(
  '2026-08-12', 'gen1',
  '[{"word": "PUNCH", "number": 2, "cat": 3, "t": [6, 8]}, {"word": "WIELD", "number": 2, "cat": 4, "t": [10, 12]}, {"word": "TRAP", "number": 1, "cat": 4, "t": [16]}, {"word": "BURROW", "number": 1, "cat": 3, "t": [14]}, {"word": "WATER", "number": 3, "cat": 1, "t": [0, 2, 4]}]'::jsonb,
  '[{"word": "ARMS", "number": 1, "cat": 2, "t": [8]}, {"word": "SNOUT", "number": 1, "cat": 2, "t": [2]}, {"word": "SWIRL", "number": 1, "cat": 2, "t": [0]}, {"word": "SPOON", "number": 1, "cat": 2, "t": [10]}, {"word": "CLAW", "number": 1, "cat": 2, "t": [4]}, {"word": "MOLE", "number": 1, "cat": 2, "t": [14]}, {"word": "PLANT", "number": 1, "cat": 2, "t": [16]}, {"word": "MUSCLE", "number": 1, "cat": 2, "t": [6]}, {"word": "SKULL", "number": 1, "cat": 2, "t": [12]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Poliwag','blue'),(1,'Pikachu','neutral'),(2,'Horsea','blue'),(3,'Raichu','neutral'),(4,'Krabby','blue'),(5,'Gengar','neutral'),(6,'Machop','blue'),(7,'Golbat','neutral'),(8,'Machamp','blue'),(9,'Gastly','neutral'),(10,'Alakazam','blue'),(11,'Onix','neutral'),(12,'Cubone','blue'),(13,'Kingler','neutral'),(14,'Diglett','blue'),(15,'Geodude','neutral'),(16,'Victreebel','blue'),(17,'Meowth','neutral'),(18,'Persian','neutral'),(19,'Weezing','neutral'),(20,'Lapras','neutral'),(21,'Slowbro','neutral'),(22,'Tentacruel','neutral'),(23,'Zubat','neutral'),(24,'Pinsir','neutral')) v(position,name,colour))
),
(
  '2026-08-12', 'mixed',
  '[{"word": "SNOW", "number": 1, "cat": 2, "t": [2]}, {"word": "BLADES", "number": 2, "cat": 2, "t": [14, 16]}, {"word": "TRICKSTER", "number": 3, "cat": 5, "t": [8, 10, 12]}, {"word": "ICE", "number": 2, "cat": 1, "t": [0, 2]}, {"word": "MEGA", "number": 2, "cat": 5, "t": [4, 6]}]'::jsonb,
  '[{"word": "GOWN", "number": 1, "cat": 2, "t": [6]}, {"word": "KIMONO", "number": 1, "cat": 2, "t": [2]}, {"word": "FINS", "number": 1, "cat": 2, "t": [4]}, {"word": "BLADE", "number": 1, "cat": 2, "t": [14]}, {"word": "SNEASEL", "number": 1, "cat": 4, "t": [0]}, {"word": "PAPER", "number": 1, "cat": 2, "t": [16]}, {"word": "COPY", "number": 1, "cat": 4, "t": [12]}, {"word": "FOX", "number": 1, "cat": 2, "t": [8]}, {"word": "CLOTH", "number": 1, "cat": 3, "t": [10]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Weavile','blue'),(1,'Pikachu','neutral'),(2,'Froslass','blue'),(3,'Raichu','neutral'),(4,'Garchomp','blue'),(5,'Wailord','neutral'),(6,'Gardevoir','blue'),(7,'Blissey','neutral'),(8,'Zoroark','blue'),(9,'Chansey','neutral'),(10,'Mimikyu','blue'),(11,'Audino','neutral'),(12,'Ditto','blue'),(13,'Togekiss','neutral'),(14,'Bisharp','blue'),(15,'Sylveon','neutral'),(16,'Kartana','blue'),(17,'Umbreon','neutral'),(18,'Espeon','neutral'),(19,'Luxray','neutral'),(20,'Rillaboom','neutral'),(21,'Incineroar','neutral'),(22,'Dragapult','neutral'),(23,'Klefki','neutral'),(24,'Grimmsnarl','neutral')) v(position,name,colour))
),
(
  '2026-08-13', 'gen1',
  '[{"word": "WIELD", "number": 2, "cat": 4, "t": [12, 14]}, {"word": "CURL", "number": 1, "cat": 3, "t": [10]}, {"word": "SPHERE", "number": 1, "cat": 2, "t": [16]}, {"word": "FOSSIL", "number": 3, "cat": 4, "t": [4, 6, 8]}, {"word": "HOUND", "number": 2, "cat": 3, "t": [0, 2]}]'::jsonb,
  '[{"word": "STRIPES", "number": 1, "cat": 2, "t": [2]}, {"word": "SPOON", "number": 1, "cat": 2, "t": [12]}, {"word": "BOMB", "number": 1, "cat": 3, "t": [16]}, {"word": "PUPPY", "number": 1, "cat": 2, "t": [0]}, {"word": "SHELL", "number": 1, "cat": 2, "t": [8]}, {"word": "SPIRAL", "number": 1, "cat": 2, "t": [6]}, {"word": "SICKLE", "number": 1, "cat": 2, "t": [4]}, {"word": "SCALY", "number": 1, "cat": 2, "t": [10]}, {"word": "BONE", "number": 1, "cat": 2, "t": [14]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Growlithe','blue'),(1,'Pikachu','neutral'),(2,'Arcanine','blue'),(3,'Raichu','neutral'),(4,'Kabutops','blue'),(5,'Gengar','neutral'),(6,'Omastar','blue'),(7,'Haunter','neutral'),(8,'Omanyte','blue'),(9,'Gastly','neutral'),(10,'Sandshrew','blue'),(11,'Machop','neutral'),(12,'Alakazam','blue'),(13,'Machamp','neutral'),(14,'Marowak','blue'),(15,'Onix','neutral'),(16,'Voltorb','blue'),(17,'Golem','neutral'),(18,'Snorlax','neutral'),(19,'Lapras','neutral'),(20,'Meowth','neutral'),(21,'Persian','neutral'),(22,'Slowbro','neutral'),(23,'Tentacruel','neutral'),(24,'Rhydon','neutral')) v(position,name,colour))
),
(
  '2026-08-13', 'mixed',
  '[{"word": "SERPENT", "number": 3, "cat": 3, "t": [0, 2, 4]}, {"word": "PSEUDO", "number": 2, "cat": 5, "t": [10, 12]}, {"word": "PANTHER", "number": 2, "cat": 3, "t": [6, 8]}, {"word": "COILS", "number": 1, "cat": 2, "t": [2]}, {"word": "TRICKSTER", "number": 2, "cat": 5, "t": [14, 16]}]'::jsonb,
  '[{"word": "FURY", "number": 1, "cat": 4, "t": [2]}, {"word": "CRESCENT", "number": 1, "cat": 2, "t": [12]}, {"word": "GEMS", "number": 1, "cat": 4, "t": [16]}, {"word": "SPOTS", "number": 1, "cat": 2, "t": [8]}, {"word": "FINS", "number": 1, "cat": 2, "t": [10]}, {"word": "SCALES", "number": 1, "cat": 2, "t": [0]}, {"word": "ORBS", "number": 1, "cat": 2, "t": [4]}, {"word": "LION", "number": 1, "cat": 2, "t": [6]}, {"word": "FOX", "number": 1, "cat": 2, "t": [14]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Milotic','blue'),(1,'Pikachu','neutral'),(2,'Gyarados','blue'),(3,'Raichu','neutral'),(4,'Dragonair','blue'),(5,'Snorlax','neutral'),(6,'Luxray','blue'),(7,'Blissey','neutral'),(8,'Liepard','blue'),(9,'Chansey','neutral'),(10,'Garchomp','blue'),(11,'Audino','neutral'),(12,'Salamence','blue'),(13,'Togekiss','neutral'),(14,'Zoroark','blue'),(15,'Sylveon','neutral'),(16,'Sableye','blue'),(17,'Umbreon','neutral'),(18,'Espeon','neutral'),(19,'Clefable','neutral'),(20,'Gardevoir','neutral'),(21,'Rillaboom','neutral'),(22,'Ampharos','neutral'),(23,'Lapras','neutral'),(24,'Lucario','neutral')) v(position,name,colour))
),
(
  '2026-08-14', 'gen1',
  '[{"word": "CURL", "number": 2, "cat": 3, "t": [12, 14]}, {"word": "KITSUNE", "number": 2, "cat": 5, "t": [0, 2]}, {"word": "WIELD", "number": 2, "cat": 4, "t": [4, 6]}, {"word": "WHISKERS", "number": 1, "cat": 2, "t": [16]}, {"word": "PUNCH", "number": 2, "cat": 3, "t": [8, 10]}]'::jsonb,
  '[{"word": "COIN", "number": 1, "cat": 2, "t": [16]}, {"word": "ARMS", "number": 1, "cat": 2, "t": [10]}, {"word": "BONE", "number": 1, "cat": 2, "t": [6]}, {"word": "FOX", "number": 1, "cat": 2, "t": [0]}, {"word": "SCALY", "number": 1, "cat": 2, "t": [12]}, {"word": "SPIKES", "number": 1, "cat": 2, "t": [14]}, {"word": "MUSCLE", "number": 1, "cat": 2, "t": [8]}, {"word": "SPOON", "number": 1, "cat": 2, "t": [4]}, {"word": "FLAMES", "number": 1, "cat": 2, "t": [2]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Vulpix','blue'),(1,'Gengar','neutral'),(2,'Ninetales','blue'),(3,'Haunter','neutral'),(4,'Kadabra','blue'),(5,'Gastly','neutral'),(6,'Marowak','blue'),(7,'Koffing','neutral'),(8,'Machoke','blue'),(9,'Weezing','neutral'),(10,'Machamp','blue'),(11,'Grimer','neutral'),(12,'Sandshrew','blue'),(13,'Muk','neutral'),(14,'Sandslash','blue'),(15,'Snorlax','neutral'),(16,'Meowth','blue'),(17,'Lapras','neutral'),(18,'Onix','neutral'),(19,'Golem','neutral'),(20,'Slowbro','neutral'),(21,'Tentacruel','neutral'),(22,'Rhydon','neutral'),(23,'Nidoking','neutral'),(24,'Scyther','neutral')) v(position,name,colour))
),
(
  '2026-08-14', 'mixed',
  '[{"word": "PSEUDO", "number": 2, "cat": 5, "t": [8, 10]}, {"word": "TONGUE", "number": 1, "cat": 2, "t": [16]}, {"word": "HAWK", "number": 2, "cat": 4, "t": [12, 14]}, {"word": "CEPHALOPOD", "number": 2, "cat": 3, "t": [4, 6]}, {"word": "HORSE", "number": 2, "cat": 3, "t": [0, 2]}]'::jsonb,
  '[{"word": "EAGLE", "number": 1, "cat": 2, "t": [14]}, {"word": "CLAWS", "number": 1, "cat": 2, "t": [12]}, {"word": "MANE", "number": 1, "cat": 2, "t": [0]}, {"word": "FROG", "number": 1, "cat": 2, "t": [16]}, {"word": "FRIENDLY", "number": 1, "cat": 4, "t": [10]}, {"word": "REVERSE", "number": 1, "cat": 3, "t": [6]}, {"word": "SQUID", "number": 1, "cat": 2, "t": [4]}, {"word": "GALLOP", "number": 1, "cat": 3, "t": [2]}, {"word": "FINS", "number": 1, "cat": 2, "t": [8]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Rapidash','blue'),(1,'Pikachu','neutral'),(2,'Zebstrika','blue'),(3,'Raichu','neutral'),(4,'Octillery','blue'),(5,'Snorlax','neutral'),(6,'Malamar','blue'),(7,'Blissey','neutral'),(8,'Garchomp','blue'),(9,'Chansey','neutral'),(10,'Dragonite','blue'),(11,'Audino','neutral'),(12,'Staraptor','blue'),(13,'Togekiss','neutral'),(14,'Braviary','blue'),(15,'Sylveon','neutral'),(16,'Greninja','blue'),(17,'Umbreon','neutral'),(18,'Espeon','neutral'),(19,'Arcanine','neutral'),(20,'Ninetales','neutral'),(21,'Luxray','neutral'),(22,'Rillaboom','neutral'),(23,'Gardevoir','neutral'),(24,'Lucario','neutral')) v(position,name,colour))
),
(
  '2026-08-15', 'gen1',
  '[{"word": "WIELD", "number": 2, "cat": 4, "t": [10, 12]}, {"word": "GRIN", "number": 1, "cat": 3, "t": [8]}, {"word": "MEGA", "number": 3, "cat": 5, "t": [2, 6, 8]}, {"word": "FOSSIL", "number": 3, "cat": 4, "t": [0, 2, 4]}, {"word": "FISTS", "number": 2, "cat": 3, "t": [14, 16]}]'::jsonb,
  '[{"word": "PURPLE", "number": 1, "cat": 2, "t": [8]}, {"word": "CLUB", "number": 1, "cat": 2, "t": [12]}, {"word": "ARMS", "number": 1, "cat": 2, "t": [16]}, {"word": "FANGS", "number": 1, "cat": 2, "t": [2]}, {"word": "LEEK", "number": 1, "cat": 2, "t": [10]}, {"word": "SICKLE", "number": 1, "cat": 2, "t": [0]}, {"word": "GLOVES", "number": 1, "cat": 2, "t": [14]}, {"word": "HORNS", "number": 1, "cat": 2, "t": [6]}, {"word": "SPIRAL", "number": 1, "cat": 2, "t": [4]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Kabutops','blue'),(1,'Pikachu','neutral'),(2,'Aerodactyl','blue'),(3,'Raichu','neutral'),(4,'Omanyte','blue'),(5,'Haunter','neutral'),(6,'Pinsir','blue'),(7,'Gastly','neutral'),(8,'Gengar','blue'),(9,'Koffing','neutral'),(10,'Farfetch''d','blue'),(11,'Weezing','neutral'),(12,'Cubone','blue'),(13,'Slowbro','neutral'),(14,'Hitmonchan','blue'),(15,'Muk','neutral'),(16,'Machamp','blue'),(17,'Meowth','neutral'),(18,'Persian','neutral'),(19,'Snorlax','neutral'),(20,'Lapras','neutral'),(21,'Onix','neutral'),(22,'Golem','neutral'),(23,'Geodude','neutral'),(24,'Tentacruel','neutral')) v(position,name,colour))
),
(
  '2026-08-15', 'mixed',
  '[{"word": "SERPENT", "number": 2, "cat": 3, "t": [6, 8]}, {"word": "GRIZZLY", "number": 2, "cat": 4, "t": [10, 12]}, {"word": "PSEUDO", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "CEPHALOPOD", "number": 2, "cat": 3, "t": [14, 16]}, {"word": "MEGA", "number": 4, "cat": 5, "t": [0, 2, 4, 6]}]'::jsonb,
  '[{"word": "GRIP", "number": 1, "cat": 2, "t": [16]}, {"word": "ICE", "number": 1, "cat": 2, "t": [12]}, {"word": "SUCKERS", "number": 1, "cat": 2, "t": [14]}, {"word": "ORBS", "number": 1, "cat": 2, "t": [8]}, {"word": "CUB", "number": 1, "cat": 2, "t": [10]}, {"word": "FINS", "number": 1, "cat": 2, "t": [0]}, {"word": "ROBOT", "number": 1, "cat": 2, "t": [4]}, {"word": "WHIRLPOOL", "number": 1, "cat": 2, "t": [6]}, {"word": "CRESCENT", "number": 1, "cat": 2, "t": [2]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Garchomp','blue'),(1,'Pikachu','neutral'),(2,'Salamence','blue'),(3,'Raichu','neutral'),(4,'Metagross','blue'),(5,'Snorlax','neutral'),(6,'Gyarados','blue'),(7,'Blissey','neutral'),(8,'Dragonair','blue'),(9,'Chansey','neutral'),(10,'Ursaring','blue'),(11,'Audino','neutral'),(12,'Beartic','blue'),(13,'Togekiss','neutral'),(14,'Octillery','blue'),(15,'Sylveon','neutral'),(16,'Grapploct','blue'),(17,'Umbreon','neutral'),(18,'Espeon','neutral'),(19,'Rillaboom','neutral'),(20,'Luxray','neutral'),(21,'Wailord','neutral'),(22,'Emboar','neutral'),(23,'Samurott','neutral'),(24,'Feraligatr','neutral')) v(position,name,colour))
),
(
  '2026-08-16', 'gen1',
  '[{"word": "PIXIE", "number": 2, "cat": 4, "t": [6, 8]}, {"word": "IMPOSTER", "number": 1, "cat": 5, "t": [16]}, {"word": "TRADE", "number": 2, "cat": 5, "t": [12, 14]}, {"word": "STONE", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "MOONSTONE", "number": 3, "cat": 5, "t": [6, 8, 10]}]'::jsonb,
  '[{"word": "ARMS", "number": 1, "cat": 2, "t": [12]}, {"word": "STAR", "number": 1, "cat": 4, "t": [6]}, {"word": "KITSUNE", "number": 1, "cat": 5, "t": [0]}, {"word": "BALLOON", "number": 1, "cat": 2, "t": [8]}, {"word": "ARMOR", "number": 1, "cat": 2, "t": [10]}, {"word": "BOULDER", "number": 1, "cat": 2, "t": [14]}, {"word": "BLOOM", "number": 1, "cat": 2, "t": [4]}, {"word": "COPY", "number": 1, "cat": 4, "t": [16]}, {"word": "CHEEKS", "number": 1, "cat": 2, "t": [2]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Ninetales','blue'),(1,'Pikachu','neutral'),(2,'Raichu','blue'),(3,'Gastly','neutral'),(4,'Vileplume','blue'),(5,'Snorlax','neutral'),(6,'Clefable','blue'),(7,'Lapras','neutral'),(8,'Wigglytuff','blue'),(9,'Slowbro','neutral'),(10,'Nidoqueen','blue'),(11,'Tentacruel','neutral'),(12,'Machamp','blue'),(13,'Onix','neutral'),(14,'Golem','blue'),(15,'Scyther','neutral'),(16,'Ditto','blue'),(17,'Pinsir','neutral'),(18,'Kangaskhan','neutral'),(19,'Tauros','neutral'),(20,'Kabuto','neutral'),(21,'Aerodactyl','neutral'),(22,'Meowth','neutral'),(23,'Seel','neutral'),(24,'Dewgong','neutral')) v(position,name,colour))
),
(
  '2026-08-16', 'mixed',
  '[{"word": "PSEUDO", "number": 2, "cat": 5, "t": [10, 16]}, {"word": "MEGA", "number": 6, "cat": 5, "t": [0, 2, 4, 6, 8, 10]}, {"word": "STARTER", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "CLONE", "number": 1, "cat": 5, "t": [14]}, {"word": "TRICKSTER", "number": 2, "cat": 5, "t": [12, 14]}]'::jsonb,
  '[{"word": "COPY", "number": 1, "cat": 4, "t": [14]}, {"word": "PUNCH", "number": 1, "cat": 3, "t": [6]}, {"word": "BOG", "number": 1, "cat": 2, "t": [4]}, {"word": "KICK", "number": 1, "cat": 3, "t": [2]}, {"word": "FOX", "number": 1, "cat": 2, "t": [12]}, {"word": "FINS", "number": 1, "cat": 2, "t": [10]}, {"word": "GOWN", "number": 1, "cat": 2, "t": [8]}, {"word": "GECKO", "number": 1, "cat": 2, "t": [0]}, {"word": "HEADS", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values (0,'Sceptile','blue'),(1,'Pikachu','neutral'),(2,'Blaziken','blue'),(3,'Raichu','neutral'),(4,'Swampert','blue'),(5,'Snorlax','neutral'),(6,'Lucario','blue'),(7,'Blissey','neutral'),(8,'Gardevoir','blue'),(9,'Chansey','neutral'),(10,'Garchomp','blue'),(11,'Audino','neutral'),(12,'Zoroark','blue'),(13,'Togekiss','neutral'),(14,'Ditto','blue'),(15,'Sylveon','neutral'),(16,'Hydreigon','blue'),(17,'Umbreon','neutral'),(18,'Espeon','neutral'),(19,'Luxray','neutral'),(20,'Corviknight','neutral'),(21,'Frosmoth','neutral'),(22,'Klefki','neutral'),(23,'Mudsdale','neutral'),(24,'Bruxish','neutral')) v(position,name,colour))
)
on conflict (puzzle_date, pool) do update
  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;
