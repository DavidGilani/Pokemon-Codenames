# Rescheduled boards 2026-08-22 .. 2026-09-06 (loaded by schedule_v2.py).
# Tier fixed by weekday: Mon Easy / Tue Medium / Wed Challenging / Thu Hard /
# Fri Hard / Sat Brutal / Sun Evil. Brutal/Evil pass the overlap gate
# (clue numbers sum >= 11, <= 1 single-tile clue).

# ===== 08-22 Sat : BRUTAL =====
board("2026-08-22","gen1","Brutal",[
  ("FIGHTING",1,"type:fighting",["Machop","Machoke","Poliwrath"]),
  ("SUMO",3,"based:sumo",["Machop","Machoke"]),
  ("FOX-SPIRIT",5,"myth:kitsune",["Vulpix","Ninetales"]),
  ("OPERA",4,"lore:jynx",["Jynx"]),
  ("LUCKY",4,"lore:lucky",["Chansey","Clefairy","Clefable"]),
], exclude=["Ekans","Koffing","Weezing","Machamp","Primeape","Mankey","Arcanine","Growlithe","Blissey","Wigglytuff"])
board("2026-08-22","mixed","Brutal",[
  ("GRIM-REAPER",4,"based:reaper",["Duskull","Dusknoir"]),
  ("STINGER",4,"arch:scorpion",["Skorupi","Drapion"]),
  ("DOODLEBUG",4,"arch:antlion",["Trapinch","Flygon"]),
  ("DESERT",3,"arch:desert",["Drapion","Flygon","Cranidos"]),
  ("GILLS",2,"sprite:gills",["Tympole","Palpitoad"]),
], exclude=["Spiritomb","Sableye","Vibrava","Krokorok","Sandile","Rampardos","Shieldon","Seismitoad"])

# ===== 08-23 Sun : EVIL =====
board("2026-08-23","gen1","Evil",[
  ("LEVIATHAN",4,"lore:sea-serpent",["Dratini","Dragonair","Dragonite"]),
  ("GENIE",5,"lore:mythical",["Dragonair","Dragonite"]),
  ("SHADOW",4,"lore:shadow",["Gastly","Haunter"]),
  ("EXPERIMENT",5,"lore:clone",["Mewtwo","Mew"]),
  ("FROGSPAWN",3,"arch:tadpole",["Poliwag","Poliwhirl"]),
], exclude=["Gyarados","Gengar","Seadra","Horsea","Kingdra","Snorlax","Poliwrath","Politoed"])
board("2026-08-23","mixed","Evil",[
  ("WITCH",5,"lore:witch",["Mismagius","Gothitelle"]),
  ("HEX",4,"lore:curse",["Mismagius","Spiritomb"]),
  ("FAIRY-TALE",5,"lore:fairy-tale",["Hatterene","Grimmsnarl"]),
  ("HAG",4,"lore:hag",["Grimmsnarl","Delphox"]),
  ("BANDIT",3,"arch:raccoon",["Zigzagoon","Linoone","Nickit"]),
], exclude=["Gothita","Gothorita","Gardevoir","Gallade","Impidimp","Morgrem","Thievul","Diggersby"])

# ===== 08-24 Mon : EASY =====
board("2026-08-24","gen1","Easy",[
  ("FIRE",1,"type:fire",["Growlithe","Arcanine"]),
  ("GRASS",1,"type:grass",["Oddish","Gloom"]),
  ("ROCK",1,"type:rock",["Geodude","Golem"]),
  ("TUNNELER",3,"arch:mole",["Diglett","Dugtrio"]),
  ("FANG",2,"sprite:fangs",["Nidorino"]),
], exclude=["Vileplume","Bellossom","Graveler","Onix","Ekans","Vulpix","Ninetales","Nidorina"])
board("2026-08-24","mixed","Easy",[
  ("ELECTRIC",1,"type:electric",["Yamper","Pichu"]),
  ("BUG",1,"type:bug",["Grubbin","Karrablast"]),
  ("PSEUDO-LEGENDARY",1,"group:pseudo",["Gible","Deino","Jangmo-o"]),
  ("FOX",3,"arch:fox",["Fennekin"]),
  ("MOLE",3,"arch:mole",["Drilbur"]),
], exclude=["Boltund","Charjabug","Gabite","Zweilous","Hakamo-o","Braixen","Excadrill","Nickit"])

# ===== 08-25 Tue : MEDIUM =====
board("2026-08-25","gen1","Medium",[
  ("POISON",1,"type:poison",["Ekans","Grimer"]),
  ("PSYCHIC",1,"type:psychic",["Abra","Slowpoke"]),
  ("ECHINODERM",4,"arch:starfish",["Staryu","Starmie"]),
  ("PUGILIST",3,"based:boxer",["Hitmonlee","Primeape"]),
  ("MUSHROOM",2,"sprite:mushroom",["Paras"]),
], exclude=["Muk","Arbok","Slowbro","Kadabra","Alakazam","Hitmonchan","Mankey","Machop","Parasect"])
board("2026-08-25","mixed","Medium",[
  ("WATER",1,"type:water",["Wooper","Mudkip"]),
  ("DRAGON",1,"type:dragon",["Axew","Goomy"]),
  ("SANTA",4,"based:santa",["Delibird"]),
  ("LAMB",3,"arch:sheep",["Mareep","Wooloo"]),
  ("POLLEN",3,"arch:flower",["Sunflora","Cottonee"]),
], exclude=["Quagsire","Marshtomp","Fraxure","Sliggoo","Dragonair","Flaaffy","Dubwool","Sunkern","Whimsicott"])

# ===== 08-26 Wed : CHALLENGING =====
board("2026-08-26","gen1","Challenging",[
  ("FIRST-PARTNER",1,"group:starter",["Bulbasaur","Charmander","Squirtle"]),
  ("CAT",3,"arch:feline",["Meowth","Persian"]),
  ("SKULL",3,"based:bone",["Cubone","Marowak"]),
  ("DUMBBELL",2,"sprite:muscle",["Machamp"]),
  ("JOEY",3,"arch:kangaroo",["Kangaskhan"]),
], exclude=["Ivysaur","Venusaur","Charmeleon","Wartortle","Blastoise","Persian-Alola","Machoke","Cubone-Alola"])
board("2026-08-26","mixed","Challenging",[
  ("FAIRY",1,"type:fairy",["Togepi","Togetic"]),
  ("RAVEN",3,"arch:crow",["Murkrow","Honchkrow"]),
  ("OTTER",3,"arch:otter",["Buizel","Floatzel"]),
  ("CANDLE",4,"based:candle",["Litwick","Lampent"]),
  ("STAR",2,"sprite:star",["Minior"]),
], exclude=["Togekiss","Corviknight","Rookidee","Chandelure","Cottonee","Whimsicott","Floette"])

# ===== 08-27 Thu : HARD =====
board("2026-08-27","gen1","Hard",[
  ("COCOON",2,"sprite:cocoon",["Metapod","Kakuna"]),
  ("WATERFOWL",3,"arch:duck",["Psyduck","Golduck","Farfetch'd"]),
  ("SEAL",3,"arch:seal",["Seel","Dewgong"]),
  ("PLESIOSAUR",4,"arch:plesiosaur",["Lapras"]),
  ("VENUS-FLYTRAP",4,"based:flytrap",["Victreebel"]),
], exclude=["Beedrill","Butterfree","Cloyster","Shellder","Bellsprout","Weepinbell","Golbat","Slowbro"])
board("2026-08-27","mixed","Hard",[
  ("SWORD",4,"based:sword",["Honedge","Doublade"]),
  ("MIMIC",4,"lore:colour-change",["Kecleon"]),
  ("KOI",2,"sprite:fins",["Magikarp","Feebas"]),
  ("LIZARD",3,"arch:gecko",["Treecko","Grovyle"]),
  ("HERMIT-CRAB",3,"arch:hermit-crab",["Dwebble","Crustle"]),
], exclude=["Aegislash","Sceptile","Milotic","Gyarados","Boldore","Roggenrola","Ditto"])

# ===== 08-28 Fri : HARD =====
board("2026-08-28","gen1","Hard",[
  ("JELLYFISH",4,"arch:jellyfish",["Tentacool","Tentacruel"]),
  ("GAS",4,"lore:poison-gas",["Koffing","Weezing"]),
  ("SPHERE",2,"sprite:ball",["Voltorb","Electrode"]),
  ("HORSESHOE",3,"arch:magnet",["Magnemite","Magneton"]),
  ("SEED-BOMB",3,"lore:seeds",["Exeggcute"]),
], exclude=["Cloyster","Shellder","Muk","Grimer","Magnezone","Exeggutor","Electabuzz","Magmar"])
board("2026-08-28","mixed","Hard",[
  ("DINOSAUR",3,"arch:dinosaur",["Tyrunt","Tyrantrum"]),
  ("AUTOMATON",4,"based:golem",["Golett","Golurk"]),
  ("SPOTS",2,"sprite:spots",["Ledyba","Ledian"]),
  ("STEAM",3,"lore:smoke",["Torkoal"]),
  ("ANGLERFISH",4,"arch:anglerfish",["Chinchou","Lanturn"]),
], exclude=["Rampardos","Cranidos","Volbeat","Illumise","Baltoy","Claydol","Stonjourner"])

# ===== 08-29 Sat : BRUTAL =====
board("2026-08-29","gen1","Brutal",[
  ("NORMAL",1,"type:normal",["Doduo","Dodrio","Chansey","Tauros"]),
  ("OSTRICH",4,"arch:ratite",["Doduo","Dodrio"]),
  ("BRUTE",4,"lore:brute",["Rhyhorn","Rhydon"]),
  ("CLOWN",4,"based:mime",["Mr. Mime"]),
  ("STAG-BEETLE",3,"arch:beetle",["Pinsir","Scyther"]),
], exclude=["Nidoking","Nidoqueen","Rhyperior","Jynx","Heracross","Fearow","Pidgey","Kangaskhan","Snorlax"])
board("2026-08-29","mixed","Brutal",[
  ("STEEL",1,"type:steel",["Klink","Bronzor","Escavalier","Bisharp"]),
  ("KNIGHT",4,"based:knight",["Escavalier","Bisharp"]),
  ("GEAR",4,"lore:gears",["Klink","Bronzor"]),
  ("TOMB",4,"based:coffin",["Yamask","Cofagrigus","Runerigus"]),
  ("GATOR",3,"arch:crocodile",["Totodile","Croconaw"]),
], exclude=["Klang","Klinklang","Bronzong","Pawniard","Kingambit","Feraligatr","Sandygast","Cursola"])

# ===== 08-30 Sun : EVIL =====
board("2026-08-30","gen1","Evil",[
  ("LEGEND-TRIO",5,"lore:legendary-birds",["Articuno","Zapdos","Moltres"]),
  ("BLIZZARD",4,"lore:ice-storm",["Articuno","Jynx"]),
  ("VOLCANO",4,"lore:volcano",["Moltres","Magmar"]),
  ("TEST-TUBE",5,"lore:clone",["Mewtwo","Mew"]),
  ("SLEEPER",3,"lore:sleep",["Drowzee","Hypno"]),
], exclude=["Electabuzz","Machop","Hitmonlee","Hitmonchan","Primeape","Mankey","Slowpoke","Zapdos-Galar"])
board("2026-08-30","mixed","Evil",[
  ("DIG-SITE",5,"lore:fossil",["Shieldon","Bastiodon","Rampardos"]),
  ("CERATOPS",4,"arch:ceratopsian",["Shieldon","Bastiodon"]),
  ("CURSE-DOLL",5,"lore:cursed-doll",["Mimikyu","Banette"]),
  ("FUSED",4,"lore:fused-fossil",["Dracovish","Dracozolt"]),
  ("LAZYBONES",3,"arch:sloth",["Slakoth","Vigoroth"]),
], exclude=["Cranidos","Shuppet","Slaking","Arctovish","Arctozolt","Aurorus","Tyrunt","Bastiodon-x"])

# ===== 08-31 Mon : EASY =====
board("2026-08-31","gen1","Easy",[
  ("FLYING",1,"type:flying",["Pidgey","Pidgeotto"]),
  ("BRANCHER",1,"family:eevee",["Vaporeon","Jolteon","Flareon"]),
  ("ICE",1,"type:ice",["Cloyster"]),
  ("MOUSE",3,"arch:rodent",["Rattata","Raticate"]),
  ("SEED",2,"sprite:seeds",["Bellsprout"]),
], exclude=["Pidgeot","Spearow","Eevee","Espeon","Umbreon","Dewgong","Lapras","Weepinbell"])
board("2026-08-31","mixed","Easy",[
  ("GROUND",1,"type:ground",["Phanpy","Hippopotas"]),
  ("ICE",1,"type:ice",["Snom","Cubchoo"]),
  ("MULTIFORM",1,"family:eevee",["Espeon","Umbreon"]),
  ("SCAVENGER",3,"arch:hyena",["Poochyena","Mightyena"]),
  ("SNAIL",3,"arch:snail",["Shellos"]),
], exclude=["Donphan","Hippowdon","Frosmoth","Beartic","Sylveon","Leafeon","Gastrodon","Linoone"])

# ===== 09-01 Tue : MEDIUM =====
board("2026-09-01","gen1","Medium",[
  ("ROCK",1,"type:rock",["Geodude","Graveler"]),
  ("STARTER",1,"group:starter",["Bulbasaur","Charmander","Squirtle"]),
  ("STALLION",3,"arch:equine",["Ponyta","Rapidash"]),
  ("TONGUE",2,"sprite:tongue",["Lickitung"]),
  ("VINES",3,"arch:vine",["Tangela"]),
], exclude=["Golem","Onix","Ivysaur","Charmeleon","Wartortle","Weepinbell","Vileplume","Tauros"])
board("2026-09-01","mixed","Medium",[
  ("ELECTRIC",1,"type:electric",["Blitzle","Emolga"]),
  ("FIGHTING",1,"type:fighting",["Makuhita","Meditite"]),
  ("MONKEY",3,"arch:monkey",["Pansage","Panpour","Pansear"]),
  ("KEYRING",4,"based:keyring",["Klefki"]),
  ("ACORN",2,"sprite:acorn",["Seedot"]),
], exclude=["Zebstrika","Pachirisu","Hariyama","Medicham","Simisage","Simipour","Simisear","Nuzleaf"])

# ===== 09-02 Wed : CHALLENGING =====
board("2026-09-02","gen1","Challenging",[
  ("POISON",1,"type:poison",["Nidorino","Nidorina"]),
  ("FELINE",3,"arch:feline",["Meowth","Persian"]),
  ("MUMMY",4,"myth:mummy",["Marowak","Cubone"]),
  ("BALLOON",2,"sprite:balloon",["Jigglypuff"]),
  ("DABBLER",3,"arch:duck",["Psyduck","Golduck"]),
], exclude=["Nidoking","Nidoqueen","Wigglytuff","Arbok","Persian-Alola","Marowak-Alola","Psyduck-x","Golduck-x"])
board("2026-09-02","mixed","Challenging",[
  ("PSEUDO-LEGENDARY",1,"group:pseudo",["Larvitar","Bagon","Beldum"]),
  ("SEA-WEASEL",3,"arch:otter",["Oshawott","Dewott"]),
  ("FIREFLY",3,"arch:firefly",["Volbeat","Illumise"]),
  ("LANTERN",4,"based:lantern",["Chandelure"]),
  ("PINNIPED",3,"arch:seal",["Spheal"]),
], exclude=["Pupitar","Tyranitar","Shelgon","Salamence","Metang","Metagross","Samurott","Sealeo"])

# ===== 09-03 Thu : HARD =====
board("2026-09-03","gen1","Hard",[
  ("KUNG-FU",4,"lore:martial-arts",["Mankey","Machop"]),
  ("GENIUS",4,"lore:high-iq",["Alakazam","Kadabra"]),
  ("HIPPOCAMPUS",3,"arch:seahorse",["Horsea","Seadra"]),
  ("MOLLUSK",3,"arch:shellfish",["Shellder","Omastar"]),
  ("PETALS",2,"sprite:petals",["Vileplume"]),
], exclude=["Machamp","Machoke","Poliwrath","Primeape","Abra","Goldeen","Seaking","Gloom"])
board("2026-09-03","mixed","Hard",[
  ("SQUID",4,"arch:squid",["Inkay","Malamar"]),
  ("MEDUSA",4,"myth:jellyfish",["Frillish","Jellicent"]),
  ("MOLTEN",3,"lore:lava",["Slugma","Magcargo"]),
  ("HIVE",3,"arch:bee",["Combee","Vespiquen"]),
  ("SPARK",2,"sprite:spark",["Pincurchin"]),
], exclude=["Octillery","Tentacruel","Torkoal","Ninjask","Mareanie","Toxapex","Frillish-x"])

# ===== 09-04 Fri : HARD =====
board("2026-09-04","gen1","Hard",[
  ("VENOM-ROYALTY",4,"lore:poison-royalty",["Nidoking","Nidoqueen"]),
  ("BRAWLER",4,"lore:brawl",["Machamp","Machoke"]),
  ("RHINO",3,"arch:rhino",["Rhyhorn","Rhydon"]),
  ("FROGLET",3,"arch:tadpole",["Poliwag","Poliwhirl"]),
  ("TUSKS",2,"sprite:tusks",["Dewgong"]),
], exclude=["Nidorino","Nidorina","Rhyperior","Machop","Seel","Cloyster","Politoed","Slowbro"])
board("2026-09-04","mixed","Hard",[
  ("WHALE",4,"arch:whale",["Wailmer","Wailord"]),
  ("BELL",4,"lore:bell-spirit",["Chingling","Chimecho"]),
  ("PRIMATE",3,"arch:gorilla",["Grookey","Thwackey"]),
  ("MOTH",3,"arch:moth",["Dustox","Beautifly"]),
  ("SPIKE-BALL",2,"sprite:spikes",["Togedemaru"]),
], exclude=["Bronzong","Rillaboom","Wormadam","Mothim","Ferroseed","Sandygast","Wailord-x"])

# ===== 09-05 Sat : BRUTAL =====
board("2026-09-05","gen1","Brutal",[
  ("GHOST",1,"type:ghost",["Gastly","Haunter","Gengar"]),
  ("CURSE",4,"lore:curse",["Gastly","Gengar"]),
  ("TRANSFORM",5,"lore:transform",["Ditto","Mew"]),
  ("FLYTRAP",4,"based:flytrap",["Victreebel"]),
  ("PUGILIST",3,"based:boxer",["Hitmonlee","Hitmonchan","Primeape"]),
], exclude=["Gloom","Weepinbell","Mewtwo","Machamp","Machoke","Machop","Poliwrath","Bellsprout"])
board("2026-09-05","mixed","Brutal",[
  ("DARK",1,"type:dark",["Purrloin","Liepard","Sneasel"]),
  ("THIEF",4,"lore:thief",["Purrloin","Liepard"]),
  ("SAMURAI",4,"based:samurai",["Kubfu","Urshifu","Ceruledge"]),
  ("GHOST-FOREST",5,"lore:haunted-tree",["Phantump","Trevenant"]),
  ("FROST",3,"arch:snowman",["Vanilluxe"]),
], exclude=["Weavile","Sneasler","Zoroark","Liepard-x","Aegislash","Honedge","Vanillite","Vanillish"])

# ===== 09-06 Sun : EVIL =====
board("2026-09-06","gen1","Evil",[
  ("RELIC",5,"lore:fossil",["Omanyte","Kabuto","Aerodactyl"]),
  ("SEA-FOSSIL",4,"arch:ammonite",["Omanyte","Kabuto"]),
  ("MESMERIST",5,"lore:hypnosis",["Drowzee","Hypno"]),
  ("LEVIATHAN",4,"lore:sea-serpent",["Gyarados","Dragonite"]),
  ("CORE-GEM",3,"lore:core",["Staryu","Starmie"]),
], exclude=["Kabutops","Omastar","Dratini","Dragonair","Magnemite","Magneton","Slowpoke","Slowbro"])
board("2026-09-06","mixed","Evil",[
  ("FROZEN-RELIC",5,"lore:fossil",["Arctovish","Arctozolt"]),
  ("CHIMERA",4,"lore:fused-fossil",["Arctovish","Arctozolt"]),
  ("CURSED-CUP",5,"lore:haunted-object",["Sinistcha","Polteageist"]),
  ("WEASEL",4,"lore:mischief",["Nickit","Thievul"]),
  ("PENGUIN",3,"arch:penguin",["Eiscue","Empoleon","Prinplup"]),
], exclude=["Dracovish","Dracozolt","Sinistea","Rabsca","Grimmsnarl","Zorua","Piplup","Arctozolt-x"])
