-- 24_updates.sql
--
-- Daily puzzles for Aug 4-9 (current_date+1 .. +6), regenerated to obey the
-- NO-DISGUISED-TYPE rule: higher-category clues never just restate a type
-- (no BLAZE=Fire, SHADE=Ghost, WYRM=Dragon, DIRT=Ground). Each board uses at
-- most 1-2 honest type/colour anchors; the rest group blues by sprite / lore /
-- pun / stat, spanning multiple types. Base clues + hints carry hidden target
-- positions ("t") for the conditional-hint RPC (23_updates.sql) and the
-- end-of-game clue reveal. Supersedes the Aug 4/5 rows from 22/23_updates.sql.
-- Today's puzzle (current_date) is intentionally left untouched.
--
-- Difficulty (from clue-category spread), for reference:
--   +1 gen1   -> Hard
--   +1 mixed  -> Hard
--   +2 gen1   -> Hard
--   +2 mixed  -> Brutal
--   +3 gen1   -> Evil
--   +3 mixed  -> Hard
--   +4 gen1   -> Hard
--   +4 mixed  -> Hard
--   +5 gen1   -> Brutal
--   +5 mixed  -> Hard
--   +6 gen1   -> Challenging
--   +6 mixed  -> Evil

insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values
(
  current_date + 1, 'gen1',
  '[{"word": "WIELD", "number": 4, "cat": 4, "t": [0, 2, 4, 6]}, {"word": "ARMS", "number": 1, "cat": 2, "t": [8]}, {"word": "POUCH", "number": 1, "cat": 4, "t": [10]}, {"word": "HORN", "number": 2, "cat": 2, "t": [12, 14]}, {"word": "BLADES", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  '[{"word": "SPOON", "number": 1, "cat": 2, "t": [0]}, {"word": "GLOVES", "number": 1, "cat": 2, "t": [2]}, {"word": "SKULL", "number": 1, "cat": 2, "t": [4]}, {"word": "LEEK", "number": 1, "cat": 4, "t": [6]}, {"word": "MUSCLE", "number": 1, "cat": 3, "t": [8]}, {"word": "BABY", "number": 1, "cat": 4, "t": [10]}, {"word": "DRILL", "number": 1, "cat": 2, "t": [12]}, {"word": "SPIKES", "number": 1, "cat": 2, "t": [14]}, {"word": "MANTIS", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Alakazam','blue'),(1,'Gengar','neutral'),(2,'Hitmonchan','blue'),(3,'Haunter','neutral'),(4,'Cubone','blue'),(5,'Gastly','neutral'),(6,'Farfetch''d','blue'),(7,'Koffing','neutral'),(8,'Machamp','blue'),(9,'Weezing','neutral'),(10,'Kangaskhan','blue'),(11,'Magneton','neutral'),(12,'Rhydon','blue'),(13,'Electrode','neutral'),(14,'Nidoking','blue'),(15,'Jolteon','neutral'),(16,'Scyther','blue'),(17,'Vaporeon','neutral'),(18,'Flareon','neutral'),(19,'Lapras','neutral'),(20,'Dewgong','neutral'),(21,'Cloyster','neutral'),(22,'Seel','neutral'),(23,'Persian','neutral'),(24,'Meowth','neutral')
   ) v(position,name,colour))
),
(
  current_date + 1, 'mixed',
  '[{"word": "THREE", "number": 4, "cat": 2, "t": [0, 2, 4, 6]}, {"word": "AURA", "number": 1, "cat": 4, "t": [8]}, {"word": "GOWN", "number": 1, "cat": 2, "t": [10]}, {"word": "BLADES", "number": 2, "cat": 2, "t": [12, 14]}, {"word": "FROG", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  '[{"word": "BEAKS", "number": 1, "cat": 2, "t": [0]}, {"word": "BOLTS", "number": 1, "cat": 2, "t": [2]}, {"word": "DIG", "number": 1, "cat": 2, "t": [4]}, {"word": "VIOLENT", "number": 1, "cat": 4, "t": [6]}, {"word": "JACKAL", "number": 1, "cat": 2, "t": [8]}, {"word": "PSYCHIC", "number": 1, "cat": 1, "t": [10]}, {"word": "CLAWS", "number": 1, "cat": 2, "t": [12]}, {"word": "SWORD", "number": 1, "cat": 2, "t": [14]}, {"word": "WATER", "number": 1, "cat": 1, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Dodrio','blue'),(1,'Pikachu','neutral'),(2,'Magneton','blue'),(3,'Raichu','neutral'),(4,'Dugtrio','blue'),(5,'Snorlax','neutral'),(6,'Hydreigon','blue'),(7,'Blissey','neutral'),(8,'Lucario','blue'),(9,'Togekiss','neutral'),(10,'Gardevoir','blue'),(11,'Sylveon','neutral'),(12,'Scizor','blue'),(13,'Umbreon','neutral'),(14,'Aegislash','blue'),(15,'Arcanine','neutral'),(16,'Greninja','blue'),(17,'Ninetales','neutral'),(18,'Gengar','neutral'),(19,'Dragonite','neutral'),(20,'Salamence','neutral'),(21,'Tyranitar','neutral'),(22,'Garchomp','neutral'),(23,'Rhyperior','neutral'),(24,'Luxray','neutral')
   ) v(position,name,colour))
),
(
  current_date + 2, 'gen1',
  '[{"word": "FOSSIL", "number": 3, "cat": 4, "t": [0, 2, 4]}, {"word": "SHELL", "number": 2, "cat": 2, "t": [6, 8]}, {"word": "HORN", "number": 2, "cat": 2, "t": [10, 12]}, {"word": "ORPHAN", "number": 1, "cat": 4, "t": [14]}, {"word": "ARMS", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  '[{"word": "SICKLE", "number": 1, "cat": 2, "t": [0]}, {"word": "SPIRAL", "number": 1, "cat": 2, "t": [2]}, {"word": "FANGS", "number": 1, "cat": 2, "t": [4]}, {"word": "TURTLE", "number": 1, "cat": 2, "t": [6]}, {"word": "PEARL", "number": 1, "cat": 4, "t": [8]}, {"word": "DRILL", "number": 1, "cat": 2, "t": [10]}, {"word": "BARBS", "number": 1, "cat": 2, "t": [12]}, {"word": "SKULL", "number": 1, "cat": 2, "t": [14]}, {"word": "MUSCLE", "number": 1, "cat": 3, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Kabutops','blue'),(1,'Pikachu','neutral'),(2,'Omastar','blue'),(3,'Raichu','neutral'),(4,'Aerodactyl','blue'),(5,'Meowth','neutral'),(6,'Blastoise','blue'),(7,'Persian','neutral'),(8,'Cloyster','blue'),(9,'Gengar','neutral'),(10,'Rhydon','blue'),(11,'Haunter','neutral'),(12,'Nidoking','blue'),(13,'Koffing','neutral'),(14,'Cubone','blue'),(15,'Weezing','neutral'),(16,'Machamp','blue'),(17,'Vulpix','neutral'),(18,'Ninetales','neutral'),(19,'Growlithe','neutral'),(20,'Arcanine','neutral'),(21,'Jolteon','neutral'),(22,'Vaporeon','neutral'),(23,'Snorlax','neutral'),(24,'Electabuzz','neutral')
   ) v(position,name,colour))
),
(
  current_date + 2, 'mixed',
  '[{"word": "BOND", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "GRACE", "number": 2, "cat": 3, "t": [6, 8]}, {"word": "TAILS", "number": 1, "cat": 4, "t": [10]}, {"word": "MOONLIGHT", "number": 1, "cat": 4, "t": [12]}, {"word": "BLADES", "number": 2, "cat": 2, "t": [14, 16]}]'::jsonb,
  '[{"word": "RINGS", "number": 1, "cat": 2, "t": [0]}, {"word": "SUN", "number": 1, "cat": 4, "t": [2]}, {"word": "RIBBON", "number": 1, "cat": 2, "t": [4]}, {"word": "ANGEL", "number": 1, "cat": 2, "t": [6]}, {"word": "GOWN", "number": 1, "cat": 2, "t": [8]}, {"word": "FOX", "number": 1, "cat": 2, "t": [10]}, {"word": "FAIRY", "number": 1, "cat": 1, "t": [12]}, {"word": "CLAWS", "number": 1, "cat": 2, "t": [14]}, {"word": "SWORD", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Umbreon','blue'),(1,'Snorlax','neutral'),(2,'Espeon','blue'),(3,'Blissey','neutral'),(4,'Sylveon','blue'),(5,'Chansey','neutral'),(6,'Togekiss','blue'),(7,'Audino','neutral'),(8,'Gardevoir','blue'),(9,'Alomomola','neutral'),(10,'Ninetales','blue'),(11,'Pikachu','neutral'),(12,'Clefable','blue'),(13,'Raichu','neutral'),(14,'Scizor','blue'),(15,'Luxray','neutral'),(16,'Aegislash','blue'),(17,'Arcanine','neutral'),(18,'Incineroar','neutral'),(19,'Lucario','neutral'),(20,'Rhyperior','neutral'),(21,'Dragonite','neutral'),(22,'Salamence','neutral'),(23,'Garchomp','neutral'),(24,'Tyranitar','neutral')
   ) v(position,name,colour))
),
(
  current_date + 3, 'gen1',
  '[{"word": "PINK", "number": 3, "cat": 1, "t": [0, 2, 4]}, {"word": "RIVALS", "number": 2, "cat": 4, "t": [6, 8]}, {"word": "WIELD", "number": 2, "cat": 4, "t": [10, 12]}, {"word": "POUCH", "number": 1, "cat": 4, "t": [14]}, {"word": "BARRIER", "number": 1, "cat": 4, "t": [16]}]'::jsonb,
  '[{"word": "EGG", "number": 1, "cat": 2, "t": [0]}, {"word": "BALLOON", "number": 1, "cat": 2, "t": [2]}, {"word": "SLURP", "number": 1, "cat": 2, "t": [4]}, {"word": "PLUG", "number": 1, "cat": 2, "t": [6]}, {"word": "FLAME", "number": 1, "cat": 2, "t": [8]}, {"word": "SPOON", "number": 1, "cat": 2, "t": [10]}, {"word": "SKULL", "number": 1, "cat": 2, "t": [12]}, {"word": "BABY", "number": 1, "cat": 4, "t": [14]}, {"word": "CLOWN", "number": 1, "cat": 3, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Chansey','blue'),(1,'Gengar','neutral'),(2,'Jigglypuff','blue'),(3,'Haunter','neutral'),(4,'Lickitung','blue'),(5,'Gastly','neutral'),(6,'Electabuzz','blue'),(7,'Grimer','neutral'),(8,'Magmar','blue'),(9,'Muk','neutral'),(10,'Alakazam','blue'),(11,'Ekans','neutral'),(12,'Cubone','blue'),(13,'Arbok','neutral'),(14,'Kangaskhan','blue'),(15,'Machoke','neutral'),(16,'Mr. Mime','blue'),(17,'Onix','neutral'),(18,'Golem','neutral'),(19,'Graveler','neutral'),(20,'Voltorb','neutral'),(21,'Electrode','neutral'),(22,'Magnemite','neutral'),(23,'Magneton','neutral'),(24,'Zubat','neutral')
   ) v(position,name,colour))
),
(
  current_date + 3, 'mixed',
  '[{"word": "STARTER", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "SLEEP", "number": 2, "cat": 3, "t": [6, 8]}, {"word": "GRIN", "number": 1, "cat": 3, "t": [10]}, {"word": "MASCOT", "number": 1, "cat": 4, "t": [12]}, {"word": "SERPENT", "number": 2, "cat": 3, "t": [14, 16]}]'::jsonb,
  '[{"word": "FLOWER", "number": 1, "cat": 2, "t": [0]}, {"word": "CANNON", "number": 1, "cat": 2, "t": [2]}, {"word": "FLAME", "number": 1, "cat": 2, "t": [4]}, {"word": "BELLY", "number": 1, "cat": 3, "t": [6]}, {"word": "PENDULUM", "number": 1, "cat": 4, "t": [8]}, {"word": "PURPLE", "number": 1, "cat": 1, "t": [10]}, {"word": "CHEEKS", "number": 1, "cat": 2, "t": [12]}, {"word": "FURY", "number": 1, "cat": 4, "t": [14]}, {"word": "ROCKS", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Venusaur','blue'),(1,'Raichu','neutral'),(2,'Blastoise','blue'),(3,'Meowth','neutral'),(4,'Charizard','blue'),(5,'Persian','neutral'),(6,'Snorlax','blue'),(7,'Weezing','neutral'),(8,'Hypno','blue'),(9,'Kingler','neutral'),(10,'Gengar','blue'),(11,'Electabuzz','neutral'),(12,'Pikachu','blue'),(13,'Dewgong','neutral'),(14,'Gyarados','blue'),(15,'Seaking','neutral'),(16,'Onix','blue'),(17,'Vaporeon','neutral'),(18,'Jolteon','neutral'),(19,'Golduck','neutral'),(20,'Ampharos','neutral'),(21,'Dragonite','neutral'),(22,'Metagross','neutral'),(23,'Blissey','neutral'),(24,'Chansey','neutral')
   ) v(position,name,colour))
),
(
  current_date + 4, 'gen1',
  '[{"word": "THREE", "number": 3, "cat": 2, "t": [0, 2, 4]}, {"word": "SIX", "number": 1, "cat": 2, "t": [6]}, {"word": "BALL", "number": 2, "cat": 3, "t": [8, 10]}, {"word": "SIBLINGS", "number": 2, "cat": 4, "t": [12, 14]}, {"word": "BARRIER", "number": 1, "cat": 4, "t": [16]}]'::jsonb,
  '[{"word": "DIG", "number": 1, "cat": 2, "t": [0]}, {"word": "BEAKS", "number": 1, "cat": 2, "t": [2]}, {"word": "SCREWS", "number": 1, "cat": 2, "t": [4]}, {"word": "SEEDS", "number": 1, "cat": 2, "t": [6]}, {"word": "SPHERE", "number": 1, "cat": 2, "t": [8]}, {"word": "DYNAMITE", "number": 1, "cat": 4, "t": [10]}, {"word": "KICK", "number": 1, "cat": 3, "t": [12]}, {"word": "GLOVES", "number": 1, "cat": 2, "t": [14]}, {"word": "INVISIBLE", "number": 1, "cat": 4, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Dugtrio','blue'),(1,'Gengar','neutral'),(2,'Dodrio','blue'),(3,'Haunter','neutral'),(4,'Magneton','blue'),(5,'Gastly','neutral'),(6,'Exeggcute','blue'),(7,'Grimer','neutral'),(8,'Voltorb','blue'),(9,'Muk','neutral'),(10,'Electrode','blue'),(11,'Ekans','neutral'),(12,'Hitmonlee','blue'),(13,'Arbok','neutral'),(14,'Hitmonchan','blue'),(15,'Machoke','neutral'),(16,'Mr. Mime','blue'),(17,'Onix','neutral'),(18,'Golem','neutral'),(19,'Graveler','neutral'),(20,'Cubone','neutral'),(21,'Marowak','neutral'),(22,'Lapras','neutral'),(23,'Persian','neutral'),(24,'Meowth','neutral')
   ) v(position,name,colour))
),
(
  current_date + 4, 'mixed',
  '[{"word": "SWORDS", "number": 3, "cat": 2, "t": [0, 2, 4]}, {"word": "AURA", "number": 1, "cat": 4, "t": [6]}, {"word": "GOWN", "number": 1, "cat": 2, "t": [8]}, {"word": "PSEUDO", "number": 3, "cat": 5, "t": [10, 12, 14]}, {"word": "FROG", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  '[{"word": "CLAWS", "number": 1, "cat": 2, "t": [0]}, {"word": "SWORD", "number": 1, "cat": 2, "t": [2]}, {"word": "ELBOWS", "number": 1, "cat": 2, "t": [4]}, {"word": "JACKAL", "number": 1, "cat": 2, "t": [6]}, {"word": "DRESS", "number": 1, "cat": 2, "t": [8]}, {"word": "RAMPAGE", "number": 1, "cat": 4, "t": [10]}, {"word": "FINS", "number": 1, "cat": 2, "t": [12]}, {"word": "CRESCENT", "number": 1, "cat": 2, "t": [14]}, {"word": "TONGUE", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Scizor','blue'),(1,'Pikachu','neutral'),(2,'Aegislash','blue'),(3,'Raichu','neutral'),(4,'Gallade','blue'),(5,'Snorlax','neutral'),(6,'Lucario','blue'),(7,'Blissey','neutral'),(8,'Gardevoir','blue'),(9,'Chansey','neutral'),(10,'Tyranitar','blue'),(11,'Audino','neutral'),(12,'Garchomp','blue'),(13,'Togekiss','neutral'),(14,'Salamence','blue'),(15,'Sylveon','neutral'),(16,'Greninja','blue'),(17,'Umbreon','neutral'),(18,'Espeon','neutral'),(19,'Arcanine','neutral'),(20,'Ninetales','neutral'),(21,'Gengar','neutral'),(22,'Charizard','neutral'),(23,'Luxray','neutral'),(24,'Rillaboom','neutral')
   ) v(position,name,colour))
),
(
  current_date + 5, 'gen1',
  '[{"word": "FOSSIL", "number": 3, "cat": 4, "t": [0, 2, 4]}, {"word": "MORPH", "number": 1, "cat": 5, "t": [6]}, {"word": "PIXEL", "number": 1, "cat": 4, "t": [8]}, {"word": "HORN", "number": 2, "cat": 2, "t": [10, 12]}, {"word": "SPOONS", "number": 2, "cat": 2, "t": [14, 16]}]'::jsonb,
  '[{"word": "SICKLE", "number": 1, "cat": 2, "t": [0]}, {"word": "SPIRAL", "number": 1, "cat": 2, "t": [2]}, {"word": "FANGS", "number": 1, "cat": 2, "t": [4]}, {"word": "COPY", "number": 1, "cat": 4, "t": [6]}, {"word": "DIGITAL", "number": 1, "cat": 4, "t": [8]}, {"word": "DRILL", "number": 1, "cat": 2, "t": [10]}, {"word": "BARBS", "number": 1, "cat": 2, "t": [12]}, {"word": "SMART", "number": 1, "cat": 4, "t": [14]}, {"word": "PSYCHIC", "number": 1, "cat": 1, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Kabutops','blue'),(1,'Gengar','neutral'),(2,'Omastar','blue'),(3,'Haunter','neutral'),(4,'Aerodactyl','blue'),(5,'Gastly','neutral'),(6,'Ditto','blue'),(7,'Koffing','neutral'),(8,'Porygon','blue'),(9,'Weezing','neutral'),(10,'Rhydon','blue'),(11,'Grimer','neutral'),(12,'Nidoking','blue'),(13,'Muk','neutral'),(14,'Alakazam','blue'),(15,'Machamp','neutral'),(16,'Kadabra','blue'),(17,'Machoke','neutral'),(18,'Snorlax','neutral'),(19,'Lapras','neutral'),(20,'Dewgong','neutral'),(21,'Cloyster','neutral'),(22,'Seel','neutral'),(23,'Persian','neutral'),(24,'Meowth','neutral')
   ) v(position,name,colour))
),
(
  current_date + 5, 'mixed',
  '[{"word": "PSEUDO", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "HEADS", "number": 1, "cat": 2, "t": [6]}, {"word": "AURA", "number": 1, "cat": 4, "t": [8]}, {"word": "GOWN", "number": 1, "cat": 2, "t": [10]}, {"word": "SWORDS", "number": 3, "cat": 2, "t": [12, 14, 16]}]'::jsonb,
  '[{"word": "FINS", "number": 1, "cat": 2, "t": [0]}, {"word": "ROBOT", "number": 1, "cat": 3, "t": [2]}, {"word": "RAMPAGE", "number": 1, "cat": 4, "t": [4]}, {"word": "VIOLENT", "number": 1, "cat": 4, "t": [6]}, {"word": "JACKAL", "number": 1, "cat": 2, "t": [8]}, {"word": "DANCER", "number": 1, "cat": 3, "t": [10]}, {"word": "CLAWS", "number": 1, "cat": 2, "t": [12]}, {"word": "SWORD", "number": 1, "cat": 2, "t": [14]}, {"word": "ELBOWS", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Garchomp','blue'),(1,'Pikachu','neutral'),(2,'Metagross','blue'),(3,'Raichu','neutral'),(4,'Tyranitar','blue'),(5,'Snorlax','neutral'),(6,'Hydreigon','blue'),(7,'Blissey','neutral'),(8,'Lucario','blue'),(9,'Chansey','neutral'),(10,'Gardevoir','blue'),(11,'Audino','neutral'),(12,'Scizor','blue'),(13,'Togekiss','neutral'),(14,'Aegislash','blue'),(15,'Sylveon','neutral'),(16,'Gallade','blue'),(17,'Umbreon','neutral'),(18,'Espeon','neutral'),(19,'Arcanine','neutral'),(20,'Ninetales','neutral'),(21,'Gengar','neutral'),(22,'Lapras','neutral'),(23,'Charizard','neutral'),(24,'Rillaboom','neutral')
   ) v(position,name,colour))
),
(
  current_date + 6, 'gen1',
  '[{"word": "YELLOW", "number": 3, "cat": 1, "t": [0, 2, 4]}, {"word": "HORN", "number": 2, "cat": 2, "t": [6, 8]}, {"word": "SKULL", "number": 1, "cat": 2, "t": [10]}, {"word": "POUCH", "number": 1, "cat": 4, "t": [12]}, {"word": "NIPPERS", "number": 2, "cat": 2, "t": [14, 16]}]'::jsonb,
  '[{"word": "CHEEKS", "number": 1, "cat": 2, "t": [0]}, {"word": "PLUG", "number": 1, "cat": 2, "t": [2]}, {"word": "SPOON", "number": 1, "cat": 2, "t": [4]}, {"word": "DRILL", "number": 1, "cat": 2, "t": [6]}, {"word": "BARBS", "number": 1, "cat": 2, "t": [8]}, {"word": "HELMET", "number": 1, "cat": 2, "t": [10]}, {"word": "BABY", "number": 1, "cat": 4, "t": [12]}, {"word": "STAG", "number": 1, "cat": 2, "t": [14]}, {"word": "CLAW", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Pikachu','blue'),(1,'Gengar','neutral'),(2,'Electabuzz','blue'),(3,'Haunter','neutral'),(4,'Kadabra','blue'),(5,'Gastly','neutral'),(6,'Rhydon','blue'),(7,'Koffing','neutral'),(8,'Nidoking','blue'),(9,'Weezing','neutral'),(10,'Cubone','blue'),(11,'Grimer','neutral'),(12,'Kangaskhan','blue'),(13,'Muk','neutral'),(14,'Pinsir','blue'),(15,'Snorlax','neutral'),(16,'Kingler','blue'),(17,'Lapras','neutral'),(18,'Dewgong','neutral'),(19,'Cloyster','neutral'),(20,'Seel','neutral'),(21,'Golem','neutral'),(22,'Zubat','neutral'),(23,'Machamp','neutral'),(24,'Onix','neutral')
   ) v(position,name,colour))
),
(
  current_date + 6, 'mixed',
  '[{"word": "BOND", "number": 3, "cat": 5, "t": [0, 2, 4]}, {"word": "TRICKSTER", "number": 3, "cat": 5, "t": [6, 8, 10]}, {"word": "NIGHTMARE", "number": 1, "cat": 4, "t": [12]}, {"word": "SWIFT", "number": 1, "cat": 5, "t": [14]}, {"word": "THIEF", "number": 1, "cat": 4, "t": [16]}]'::jsonb,
  '[{"word": "RINGS", "number": 1, "cat": 2, "t": [0]}, {"word": "SUN", "number": 1, "cat": 4, "t": [2]}, {"word": "RIBBON", "number": 1, "cat": 2, "t": [4]}, {"word": "COPY", "number": 1, "cat": 4, "t": [6]}, {"word": "FOX", "number": 1, "cat": 2, "t": [8]}, {"word": "CLOTH", "number": 1, "cat": 3, "t": [10]}, {"word": "GRIN", "number": 1, "cat": 3, "t": [12]}, {"word": "ROCKET", "number": 1, "cat": 4, "t": [14]}, {"word": "CLAWS", "number": 1, "cat": 2, "t": [16]}]'::jsonb,
  (select jsonb_agg(jsonb_build_object('position',v.position,'name',v.name,'colour',v.colour) order by v.position)
   from (values
     (0,'Umbreon','blue'),(1,'Snorlax','neutral'),(2,'Espeon','blue'),(3,'Blissey','neutral'),(4,'Sylveon','blue'),(5,'Chansey','neutral'),(6,'Ditto','blue'),(7,'Audino','neutral'),(8,'Zoroark','blue'),(9,'Togekiss','neutral'),(10,'Mimikyu','blue'),(11,'Clefable','neutral'),(12,'Gengar','blue'),(13,'Gardevoir','neutral'),(14,'Dragapult','blue'),(15,'Lucario','neutral'),(16,'Weavile','blue'),(17,'Garchomp','neutral'),(18,'Tyranitar','neutral'),(19,'Metagross','neutral'),(20,'Dragonite','neutral'),(21,'Salamence','neutral'),(22,'Pikachu','neutral'),(23,'Raichu','neutral'),(24,'Rillaboom','neutral')
   ) v(position,name,colour))
)
on conflict (puzzle_date, pool) do update
  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;
