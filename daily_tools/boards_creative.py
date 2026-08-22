# Creative hand-authored boards Aug 22-30 (loaded by schedule_aug22.py).
# clue = (word, cat, concept, [members]). Saturdays are always Brutal/Evil;
# the rest ramp Easy -> Hard.
# Anti-rep aware: clue words spaced >7d, concepts >5d, blues respect the
# per-mon cap, no dual-type Rule-0 overlaps, letter-safe clue words.

# ===== 08-22 Sat : BRUTAL (Saturdays are always Brutal/Evil) =====
board("2026-08-22","gen1","Brutal",[
  ("SUMO",3,"based:sumo",["Machop","Poliwrath","Machoke"]),
  ("FOX-SPIRIT",5,"myth:kitsune",["Vulpix","Ninetales"]),
  ("GHOST",1,"type:ghost",["Gastly","Haunter"]),
  ("OPERA",4,"lore:jynx",["Jynx"]),
  ("NURSE",4,"lore:nurse",["Chansey"]),
], exclude=["Ekans","Koffing","Weezing","Machamp","Primeape","Arcanine","Flareon","Gengar","Blissey","Kingler","Slowbro"])
board("2026-08-22","mixed","Brutal",[
  ("GRIM-REAPER",4,"based:reaper",["Duskull","Dusknoir"]),
  ("THIEF",4,"lore:thief",["Scraggy","Scrafty"]),
  ("DOODLEBUG",4,"arch:antlion",["Trapinch","Vibrava"]),
  ("HEADBUTT",3,"arch:dinosaur",["Cranidos","Rampardos"]),
  ("MANDIBLES",2,"sprite:jaws",["Durant"]),
], exclude=["Sableye","Spiritomb","Flygon","Shieldon","Bastiodon","Krokorok","Sandile","Skarmory","Sneasel","Weavile","Meowth"])

# ===== 08-23 Sun : MEDIUM =====
board("2026-08-23","gen1","Medium",[
  ("POISON",1,"type:poison",["Ekans","Grimer"]),
  ("PSYCHIC",1,"type:psychic",["Abra","Slowpoke"]),
  ("ECHINODERM",4,"arch:starfish",["Staryu","Starmie"]),
  ("PUGILIST",3,"based:boxer",["Hitmonlee","Primeape"]),
  ("MUSHROOM",2,"sprite:mushroom",["Paras"]),
], exclude=["Muk","Arbok","Slowbro","Kadabra","Alakazam","Hitmonchan","Mankey","Machop","Parasect"])
board("2026-08-23","mixed","Medium",[
  ("GRASS",1,"type:grass",["Sunflora","Cottonee"]),
  ("DRAGON",1,"type:dragon",["Axew","Goomy"]),
  ("SANTA",4,"based:santa",["Delibird"]),
  ("LAMB",3,"arch:sheep",["Mareep","Wooloo"]),
  ("GILLS",2,"sprite:gills",["Wooper","Mudkip"]),
], exclude=["Petilil","Whimsicott","Lilligant","Fraxure","Sliggoo","Dragonair","Flaaffy","Dubwool","Quagsire"])

# ===== 08-24 Mon : EASY =====
board("2026-08-24","gen1","Medium",[
  ("ROCK",1,"type:rock",["Geodude","Graveler","Golem"]),
  ("BUG",1,"type:bug",["Caterpie","Weedle","Venonat"]),
  ("BURROWER",3,"arch:mole",["Diglett"]),
  ("FIST",2,"sprite:fist",["Hitmonchan"]),
  ("ORIGAMI",4,"based:polygon",["Porygon"]),
], exclude=["Onix","Dugtrio","Kingler","Krabby","Butterfree","Beedrill","Metapod","Kakuna","Parasect","Venomoth"])
board("2026-08-24","mixed","Easy",[
  ("ELECTRIC",1,"type:electric",["Blitzle","Tynamo"]),
  ("FAIRY",1,"type:fairy",["Snubbull","Spritzee"]),
  ("GROUND",1,"type:ground",["Drilbur","Mudbray"]),
  ("DESERT",3,"arch:cactus",["Cacnea","Cacturne"]),
  ("SLOTH",3,"arch:sloth",["Slaking"]),
], exclude=["Zebstrika","Eelektrik","Granbull","Aromatisse","Excadrill","Mudsdale","Maractus","Vigoroth","Slakoth"])

# ===== 08-25 Tue : CHALLENGING / MEDIUM =====
board("2026-08-25","gen1","Challenging",[
  ("NORMAL",1,"type:normal",["Lickitung","Tauros","Kangaskhan"]),
  ("ANCIENT",5,"lore:fossil",["Omanyte","Kabuto"]),
  ("POKEBALL",2,"sprite:ball",["Voltorb","Electrode"]),
  ("CRUSTACEAN",3,"arch:crab",["Krabby"]),
  ("HYPNOTIST",4,"lore:hypnosis",["Drowzee"]),
], exclude=["Snorlax","Kabutops","Omastar","Aerodactyl","Chansey","Kingler","Hypno","Slowpoke","Jynx"])
board("2026-08-25","mixed","Medium",[
  ("ICE",1,"type:ice",["Snom","Cubchoo"]),
  ("FIGHTING",1,"type:fighting",["Timburr","Mienfoo"]),
  ("KEYRING",4,"based:keyring",["Klefki"]),
  ("STINGER",3,"arch:scorpion",["Skorupi","Drapion"]),
  ("COBWEB",2,"sprite:web",["Joltik","Spinarak"]),
], exclude=["Frosmoth","Beartic","Conkeldurr","Mienshao","Krookodile","Galvantula","Sawk","Throh","Ariados"])

# ===== 08-26 Wed : CHALLENGING =====
board("2026-08-26","gen1","Challenging",[
  ("FIRST-PARTNER",1,"group:starter",["Bulbasaur","Charmander","Squirtle"]),
  ("FELINE",3,"arch:feline",["Meowth","Persian"]),
  ("STALLION",3,"arch:equine",["Rapidash"]),
  ("BALLOON",2,"sprite:balloon",["Koffing"]),
  ("MUMMY",4,"myth:mummy",["Marowak","Cubone"]),
], exclude=["Ivysaur","Venusaur","Charmeleon","Charizard","Wartortle","Blastoise","Ponyta","Weezing"])
board("2026-08-26","mixed","Challenging",[
  ("LEGENDARY",1,"group:legendary",["Cobalion","Terrakion","Virizion"]),
  ("VOLCANO",3,"arch:volcano",["Camerupt"]),
  ("SIMIAN",3,"arch:monkey",["Chimchar","Mankey"]),
  ("CANDLE",4,"based:candle",["Litwick","Lampent"]),
  ("MEDUSA",4,"myth:jellyfish",["Tentacruel"]),
], exclude=["Keldeo","Numel","Infernape","Ambipom","Chandelure","Jellicent","Frillish","Monferno","Tentacool"])

# ===== 08-27 Thu : CHALLENGING =====
board("2026-08-27","gen1","Challenging",[
  ("EVOLUTIONS",1,"family:eevee",["Eevee","Vaporeon","Jolteon"]),
  ("SEA-SERPENT",3,"arch:eel",["Gyarados","Dratini"]),
  ("SPOON-BENDER",4,"lore:uri-geller",["Kadabra","Alakazam"]),
  ("POWDER",3,"lore:powder",["Venomoth"]),
  ("FROGLET",3,"arch:tadpole",["Poliwhirl"]),
], exclude=["Flareon","Espeon","Umbreon","Leafeon","Glaceon","Sylveon","Magikarp","Dragonair","Dragonite","Poliwag","Poliwrath","Venonat"])
board("2026-08-27","mixed","Hard",[
  ("SWORD",3,"based:sword",["Honedge","Doublade"]),
  ("KOI",2,"sprite:fins",["Magikarp","Feebas"]),
  ("LIZARD",3,"arch:gecko",["Treecko","Grovyle"]),
  ("HERMIT-CRAB",3,"arch:hermit-crab",["Dwebble","Crustle"]),
  ("MIMIC",4,"lore:colour-change",["Kecleon"]),
], exclude=["Aegislash","Sceptile","Milotic","Gyarados","Boldore","Roggenrola","Ditto"])

# ===== 08-28 Fri : HARD =====
board("2026-08-28","gen1","Hard",[
  ("COCOON",2,"sprite:cocoon",["Metapod","Kakuna"]),
  ("WATERFOWL",3,"arch:duck",["Psyduck","Golduck","Farfetch'd"]),
  ("SEAL",3,"arch:seal",["Seel","Dewgong"]),
  ("PLESIOSAUR",4,"arch:plesiosaur",["Lapras"]),
  ("VENUS-FLYTRAP",4,"based:flytrap",["Victreebel"]),
], exclude=["Beedrill","Butterfree","Cloyster","Shellder","Bellsprout","Weepinbell","Golduck","Slowbro"])
board("2026-08-28","mixed","Hard",[
  ("DINOSAUR",3,"arch:dinosaur",["Tyrunt","Tyrantrum"]),
  ("AUTOMATON",4,"based:golem",["Golett","Golurk"]),
  ("SPOTS",2,"sprite:spots",["Ledyba","Ledian"]),
  ("STEAM",3,"lore:smoke",["Torkoal"]),
  ("ANGLERFISH",4,"arch:anglerfish",["Chinchou","Lanturn"]),
], exclude=["Rampardos","Cranidos","Volbeat","Illumise","Ledyba","Baltoy","Claydol"])

# ===== 08-29 Sat : BRUTAL (Saturdays are always Brutal/Evil) =====
board("2026-08-29","gen1","Brutal",[
  ("OSTRICH",4,"arch:ratite",["Doduo","Dodrio"]),
  ("MANTIS",4,"arch:mantis",["Scyther"]),
  ("CLOWN",4,"based:mime",["Mr. Mime"]),
  ("SNAKE",3,"arch:serpent",["Ekans","Arbok","Onix"]),
  ("AUGER",2,"sprite:drill",["Rhyhorn","Rhydon"]),
], exclude=["Nidoking","Nidoqueen","Rhyperior","Jynx","Heracross","Fearow","Pidgey","Pinsir","Steelix"])
board("2026-08-29","mixed","Brutal",[
  ("KNIGHT",4,"based:knight",["Escavalier","Bisharp"]),
  ("TOMB",4,"based:coffin",["Yamask","Cofagrigus"]),
  ("FORTUNE-TELLER",5,"lore:tarot",["Xatu"]),
  ("TURTLE",3,"arch:turtle",["Tirtouga","Carracosta"]),
  ("FRILL",2,"sprite:frill",["Helioptile","Heliolisk"]),
], exclude=["Kingambit","Pawniard","Runerigus","Natu","Relicanth","Charjabug","Vikavolt","Accelgor"])

# ===== 08-30 Sun : MEDIUM =====
board("2026-08-30","gen1","Medium",[
  ("FIRE",1,"type:fire",["Charmeleon","Charizard","Ninetales"]),
  ("GHOST",1,"type:ghost",["Gengar","Haunter"]),
  ("BOXER",3,"based:boxer",["Hitmonlee","Primeape"]),
  ("FLOWER",2,"sprite:petals",["Vileplume"]),
  ("GLUTTON",3,"lore:glutton",["Snorlax"]),
], exclude=["Charmander","Vulpix","Growlithe","Arcanine","Gastly","Gloom","Oddish","Bellossom","Munchlax"])
board("2026-08-30","mixed","Medium",[
  ("STEEL",1,"type:steel",["Aron","Beldum"]),
  ("DARK",1,"type:dark",["Nickit","Impidimp","Zorua"]),
  ("ORCHARD",3,"based:apple",["Applin"]),
  ("JACK-O-LANTERN",4,"based:pumpkin",["Pumpkaboo","Gourgeist"]),
  ("DOLPHIN",4,"arch:dolphin",["Finizen"]),
], exclude=["Lairon","Aggron","Metang","Metagross","Thievul","Grimmsnarl","Flapple","Appletun","Trevenant"])
