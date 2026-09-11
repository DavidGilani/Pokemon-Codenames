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


# ===== 08-27 Thu : HARD (re-authored under evolution-family cap) =====
board("2026-08-27","gen1","Hard",[
  ("COILS",3,"arch:serpent",["Onix","Arbok","Gyarados"]),
  ("MESMERIST",4,"lore:hypnosis",["Hypno"]),
  ("FLYTRAP",4,"based:flytrap",["Victreebel"]),
  ("SICKLE",2,"sprite:scythe-arms",["Scyther","Kabutops"]),
  ("MOLLUSC",3,"arch:mollusc",["Shellder","Omanyte"]),
], exclude=["Ekans","Dratini","Dragonair","Dragonite","Weepinbell","Bellsprout","Cloyster","Omastar","Kabuto","Pinsir"])
board("2026-08-27","mixed","Hard",[
  ("KRAKEN",4,"arch:cephalopod",["Octillery","Malamar"]),
  ("SWORD",4,"based:sword",["Kartana","Doublade"]),
  ("LIZARD",3,"arch:reptile",["Kecleon","Heliolisk"]),
  ("CRUSTACEAN",3,"arch:crustacean",["Corphish","Dwebble"]),
  ("SPARK",2,"sprite:spark",["Pincurchin"]),
], exclude=["Inkay","Grapploct","Clobbopus","Aegislash","Honedge","Crawdaunt","Crustle","Kingler","Krabby"])

# ===== 08-28 Fri : HARD =====
board("2026-08-28","gen1","Hard",[
  ("FISH",3,"arch:fish",["Horsea","Goldeen","Magikarp"]),
  ("PACHYDERM",3,"arch:pachyderm",["Rhyhorn","Nidoking"]),
  ("DIGITAL",5,"lore:polygon",["Porygon"]),
  ("SUNDEW",4,"based:pitcher",["Weepinbell"]),
  ("CLAWS",2,"sprite:claws",["Sandshrew","Krabby"]),
], exclude=["Seadra","Seaking","Gyarados","Rhydon","Nidoqueen","Nidorino","Bellsprout","Victreebel","Sandslash","Kingler"])
board("2026-08-28","mixed","Hard",[
  ("WHALE",4,"arch:cetacean",["Wailord","Cetitan"]),
  ("RAPTOR",4,"arch:raptor",["Skarmory","Braviary"]),
  ("TOADSTOOL",3,"arch:fungus",["Amoonguss","Shiinotic"]),
  ("SPIDER",3,"arch:spider",["Galvantula","Araquanid"]),
  ("GEM",2,"sprite:gem",["Carbink"]),
], exclude=["Wailmer","Kyogre","Rufflet","Talonflame","Morelull","Spinarak","Joltik","Dewpider","Sableye"])

# ===== 08-29 Sat : BRUTAL =====
board("2026-08-29","gen1","Brutal",[
  ("NORMAL",1,"type:normal",["Tauros","Ditto","Lickitung"]),
  ("WRESTLER",4,"based:sumo",["Poliwrath","Sandslash"]),
  ("MARTIAL",4,"lore:martial-arts",["Hitmonchan","Machoke","Poliwrath"]),
  ("MENTALIST",5,"lore:mind",["Kadabra","Drowzee"]),
  ("MIGHT",3,"lore:strength",["Machoke","Tauros"]),
], exclude=["Kangaskhan","Snorlax","Chansey","Eevee","Porygon","Machop","Machamp","Hitmonlee","Alakazam","Hypno"])
board("2026-08-29","mixed","Brutal",[
  ("WARRIOR",4,"based:samurai",["Kubfu","Ceruledge","Samurott"]),
  ("KNIGHT",4,"based:knight",["Escavalier","Bisharp"]),
  ("ROBOT",5,"arch:automaton",["Klink","Varoom","Golurk"]),
  ("GEARS",3,"lore:gears",["Klink","Bronzong"]),
  ("SWORDS",2,"sprite:blades",["Samurott","Bisharp"]),
], exclude=["Urshifu","Oshawott","Pawniard","Kingambit","Karrablast","Klang","Klinklang","Bronzor","Golett","Aegislash"])

# ===== 08-30 Sun : EVIL =====
board("2026-08-30","gen1","Evil",[
  ("MOLTEN",3,"lore:lava",["Magmar","Flareon"]),
  ("FOSSIL",5,"lore:fossil",["Omastar","Kabuto","Aerodactyl"]),
  ("HEAVYWEIGHT",5,"stat:heavy",["Snorlax","Golem"]),
  ("SLUDGE",4,"lore:poison-gas",["Weezing","Muk"]),
  ("BEDROCK",4,"stat:defense",["Golem","Kabuto","Omastar"]),
], exclude=["Magby","Omanyte","Kabutops","Graveler","Geodude","Koffing","Grimer","Rhydon","Ponyta","Charmander"])
board("2026-08-30","mixed","Evil",[
  ("FOSSIL",5,"lore:fossil",["Rampardos","Archeops","Bastiodon"]),
  ("CHIMERA",4,"arch:chimera",["Dracozolt","Arctovish"]),
  ("CURSED-DOLL",5,"based:doll",["Mimikyu","Banette"]),
  ("ALIEN",4,"arch:alien",["Beheeyem","Necrozma"]),
  ("ANCIENT",3,"lore:ancient",["Rampardos","Dracozolt"]),
], exclude=["Cranidos","Tyrunt","Tyrantrum","Dracovish","Arctozolt","Shuppet","Elgyem","Shieldon","Aerodactyl","Golett"])

# ===== 08-31 Mon : EASY =====
board("2026-08-31","gen1","Easy",[
  ("AVIAN",1,"type:flying",["Pidgey","Spearow","Dodrio"]),
  ("ICE",1,"type:ice",["Jynx","Dewgong"]),
  ("PURPLE",1,"colour:purple",["Koffing","Nidorino"]),
  ("COCOON",2,"sprite:hard-shell",["Kakuna","Metapod"]),
], exclude=["Pidgeot","Fearow","Articuno","Zapdos","Moltres","Weezing","Nidoking","Beedrill","Butterfree","Seel"])
board("2026-08-31","mixed","Easy",[
  ("GROUND",1,"type:ground",["Phanpy","Hippopotas","Swinub"]),
  ("ICE",1,"type:ice",["Swinub","Cubchoo"]),
  ("GHOST",1,"type:ghost",["Drifloon","Yamask"]),
  ("SPIKES",2,"sprite:spikes",["Ferroseed","Qwilfish"]),
  ("TAIL",2,"sprite:tail",["Sentret"]),
], exclude=["Donphan","Hippowdon","Piloswine","Beartic","Drifblim","Cofagrigus","Ferrothorn","Overqwil","Furret","Dedenne"])

# ===== 09-01 Tue : MEDIUM =====
board("2026-09-01","gen1","Medium",[
  ("BROWN",1,"colour:brown",["Cubone","Diglett"]),
  ("YELLOW",1,"colour:yellow",["Electabuzz","Jolteon"]),
  ("PLANT",3,"arch:plant",["Vileplume","Exeggcute","Ivysaur"]),
  ("HIPPOCAMPUS",3,"arch:seahorse",["Seadra"]),
  ("BALLOON",2,"sprite:big-eyes",["Wigglytuff"]),
], exclude=["Marowak","Dugtrio","Electivire","Flareon","Gloom","Exeggutor","Venusaur","Horsea","Jigglypuff","Raichu"])
board("2026-09-01","mixed","Medium",[
  ("BUG",1,"type:bug",["Ledyba","Wurmple"]),
  ("FIGHTING",1,"type:fighting",["Makuhita","Timburr"]),
  ("DEER",3,"arch:deer",["Stantler","Sawsbuck"]),
  ("GATOR",3,"arch:crocodile",["Sandile","Fuecoco"]),
  ("FRUIT",2,"sprite:cherries",["Cherubi"]),
], exclude=["Glalie","Avalugg","Hariyama","Conkeldurr","Wyrdeer","Deerling","Krokorok","Crocalor","Skeledirge","Forretress"])

# ===== 09-02 Wed : CHALLENGING =====
board("2026-09-02","gen1","Challenging",[
  ("POISON",1,"type:poison",["Zubat","Nidorina","Grimer"]),
  ("WHISKERS",2,"sprite:whiskers",["Rattata","Meowth"]),
  ("TWINKLE",3,"lore:star",["Staryu"]),
  ("SHELL",2,"sprite:shell",["Cloyster","Wartortle"]),
  ("MINDBENDER",3,"lore:teleport",["Alakazam"]),
], exclude=["Golbat","Nidoqueen","Muk","Raticate","Persian","Starmie","Shellder","Blastoise","Kadabra","Ekans"])
board("2026-09-02","mixed","Challenging",[
  ("DARK",1,"type:dark",["Poochyena","Purrloin"]),
  ("WEASEL",3,"arch:mustelid",["Furret","Zangoose"]),
  ("AMPHIBIAN",3,"arch:frog",["Croagunk","Froakie"]),
  ("WISP",4,"lore:willowisp",["Chandelure"]),
  ("HORNS",2,"sprite:horns",["Skiddo","Bouffalant"]),
], exclude=["Mightyena","Liepard","Sneasel","Weavile","Toxicroak","Greninja","Litwick","Lampent","Gogoat","Tauros"])

# ===== 09-03 Thu : HARD =====
board("2026-09-03","gen1","Hard",[
  ("WYVERN",4,"arch:dragon",["Dragonite","Charizard"]),
  ("BEETLE",3,"arch:beetle",["Pinsir","Scyther"]),
  ("FANGS",2,"sprite:fangs",["Arbok","Nidoking"]),
  ("ROYALTY",4,"lore:royalty",["Nidoking","Nidoqueen"]),
  ("CRAB",3,"arch:crab",["Kingler","Parasect"]),
], exclude=["Dratini","Dragonair","Charmeleon","Heracross","Ekans","Nidorino","Nidorina","Krabby","Paras","Gyarados"])
board("2026-09-03","mixed","Hard",[
  ("GORGON",4,"myth:jellyfish",["Jellicent","Nihilego"]),
  ("TURTLE",3,"arch:turtle",["Torkoal","Drednaw"]),
  ("MOTH",3,"arch:moth",["Dustox","Volcarona"]),
  ("SQUID",4,"arch:cephalopod",["Grapploct"]),
  ("JAWS",2,"sprite:jaws",["Sharpedo","Mawile"]),
], exclude=["Frillish","Tentacruel","Chewtle","Turtwig","Beautifly","Mothim","Malamar","Inkay","Carvanha","Mightyena","Guzzlord","Golbat","Carnivine","Crabrawler","Trevenant"])

# ===== 09-04 Fri : HARD =====
board("2026-09-04","gen1","Hard",[
  ("SERPENT",3,"arch:serpent",["Ekans","Gyarados"]),
  ("BIRD",3,"arch:bird",["Fearow","Doduo","Pidgeot"]),
  ("VAMPIRE",4,"lore:vampire",["Golbat"]),
  ("MANEATER",4,"based:flytrap",["Victreebel"]),
  ("MANE",2,"sprite:mane",["Ninetales","Rapidash"]),
], exclude=["Arbok","Onix","Dratini","Spearow","Pidgeotto","Zubat","Weepinbell","Bellsprout","Arcanine","Ponyta","Pidgey","Porygon","Farfetch'd","Dodrio"])
board("2026-09-04","mixed","Hard",[
  ("AUTOMATON",4,"arch:automaton",["Golett","Magearna"]),
  ("CETACEAN",4,"arch:cetacean",["Wailmer","Kyogre"]),
  ("SHARK",3,"arch:shark",["Gible","Frigibax"]),
  ("WOLF",3,"arch:wolf",["Lycanroc","Zacian"]),
  ("KEYS",2,"sprite:keys",["Klefki"]),
], exclude=["Golurk","Klink","Klang","Klinklang","Bronzong","Beldum","Metang","Metagross","Wailord","Gabite","Garchomp","Arctibax","Baxcalibur","Rockruff","Zamazenta","Registeel"])

# ===== 09-05 Sat : BRUTAL =====
board("2026-09-05","gen1","Brutal",[
  ("BRAWLER",4,"lore:brawl",["Machamp","Hitmonlee","Primeape"]),
  ("OOZE",3,"arch:amorphous",["Weezing","Muk"]),
  ("CURSE",5,"lore:curse",["Gengar","Marowak"]),
  ("VENOM",4,"lore:poison-gas",["Weezing","Gengar"]),
  ("TELEPATH",3,"lore:mind",["Slowbro","Starmie"]),
], exclude=["Machoke","Machop","Hitmonchan","Mankey","Grimer","Koffing","Haunter","Gastly","Cubone","Slowpoke"])
board("2026-09-05","mixed","Brutal",[
  ("GENIE",5,"arch:genie",["Tornadus","Thundurus","Landorus"]),
  ("DEITY",5,"arch:deity",["Tapu Koko","Tapu Bulu"]),
  ("UFO",4,"arch:alien",["Elgyem","Guzzlord"]),
  ("MYTHIC",3,"lore:mythical",["Celebi","Jirachi"]),
  ("COSMIC",3,"lore:cosmic",["Elgyem","Jirachi"]),
], exclude=["Enamorus","Tapu Lele","Tapu Fini","Beheeyem","Necrozma","Mew","Uxie","Mesprit","Azelf","Deoxys"])

# ===== 09-06 Sun : EVIL =====
# New Evil gen1 (the too-easy fossil/legendary board moved to 09-17, below).
board("2026-09-06","gen1","Evil",[
  ("CLONE",5,"lore:clone",["Mewtwo","Mew"]),
  ("ARTIFICIAL",5,"lore:artificial",["Porygon","Magneton","Mewtwo"]),
  ("TRANSFORM",5,"lore:transform",["Ditto","Mew"]),
  ("MOLLUSC",4,"arch:mollusc",["Shellder","Omanyte"]),
  ("CANINE",3,"arch:canine",["Growlithe","Vulpix"]),
], exclude=["Voltorb","Electrode","Magnemite","Cloyster","Omastar","Kabuto","Kabutops","Arcanine","Ninetales","Eevee","Vaporeon","Jolteon","Flareon","Vulpix-x","Seadra"])

# ===== 09-17 Thu : HARD (the too-easy Evil gen1 board, re-tiered + relocated) =====
board("2026-09-17","gen1","Hard",[
  ("RELIC",4,"lore:fossil",["Aerodactyl","Omastar","Kabutops"]),
  ("LEGEND",3,"lore:legendary",["Articuno","Zapdos","Moltres"]),
  ("FROST",4,"lore:ice-storm",["Articuno","Lapras"]),
  ("VOLCANO",3,"lore:volcano",["Moltres","Magmar"]),
  ("TUSKS",2,"sprite:tusks",["Dewgong"]),
], exclude=["Omanyte","Kabuto","Mewtwo","Mew","Jynx","Cloyster","Seel","Magby","Ponyta","Vulpix","Rhyhorn","Rhydon","Nidoking"])
# QA flourish (owner-approved): kept as Evil with 4 clues even though it misses
# the 3-distinct-cats / sum>=11 gates — Arctozolt folded into REVENANT (it's a
# revived fossil) so FUSION is redundant. See FLOURISH in schedule_v2.py.
board("2026-09-06","mixed","Evil",[
  ("REVENANT",5,"lore:fossil",["Tirtouga","Archen","Dracovish","Arctozolt"]),
  ("FROZEN",4,"lore:ice-storm",["Arctozolt","Eiscue"]),
  ("POSSESSED",5,"lore:haunted-object",["Polteageist","Sinistcha"]),
  ("ROBIN-HOOD",4,"based:robin-hood",["Thievul","Zoroark"]),
], exclude=["Carracosta","Archeops","Dracozolt","Arctovish","Sinistea","Zorua","Nickit","Delphox","Vulpix","Ninetales"])

# ===== 09-08 Tue : MEDIUM =====
# The "way too easy" Sep-04 board, re-tiered to a legit Medium (two type
# anchors: FIRE=Tepig, NORMAL=Lechonk) so the difficulty badge reads Medium.
board("2026-09-08","mixed","Medium",[
  ("HALLOWEEN",4,"based:pumpkin",["Cacturne","Gourgeist"]),
  ("PRIMATE",3,"arch:monkey",["Grookey","Pansage","Panpour"]),
  ("PINCERS",2,"sprite:claws",["Crawdaunt","Klawf"]),
  ("FIRE",1,"type:fire",["Tepig"]),
  ("NORMAL",1,"type:normal",["Lechonk"]),
], exclude=["Simisage","Simipour","Chimchar","Monferno","Infernape","Aipom","Ambipom","Oranguru","Passimian","Mankey","Primeape","Thwackey","Rillaboom","Pumpkaboo","Cacnea","Sandygast","Palossand","Krabby","Kingler","Corphish","Crabrawler","Crabominable","Clauncher","Pignite","Emboar","Oinkologne","Trevenant","Phantump","Gliscor","Gligar","Skorupi","Drapion","Weavile","Sneasel","Drifloon","Drifblim","Greavard","Houndstone","Mimikyu","Banette","Misdreavus","Mismagius","Sableye","Chandelure","Kleavor"])

# ===== FEEDBACK FIX 2026-09-18 gen1 : removed 3-dragon WYVERN clue (too many
# dragons in one day) and the BIPEDAL/humanoid clue's neutral conflict
# (Magmar is also arch:humanoid, Charmeleon flagged by QA too). =====
board("2026-09-18","gen1","Hard",[
  ("CRAB",2,"sprite:pincers",["Kingler"]),
  ("ANTENNAE",3,"sprite:antennae",["Venomoth"]),
  ("MOLLUSC",4,"arch:mollusc",["Shellder"]),
  ("BIPEDAL",4,"arch:humanoid",["Jynx","Mr. Mime","Electabuzz"]),
  ("AVIAN",3,"arch:bird",["Farfetch'd","Spearow","Pidgey"]),
], exclude=["Mewtwo","Machop","Hitmonlee","Hitmonchan","Magmar","Machoke","Machamp",
            "Doduo","Articuno","Fearow","Zapdos","Pidgeotto","Moltres","Pidgeot","Dodrio",
            "Omanyte","Cloyster","Omastar","Parasect","Krabby","Paras",
            "Kakuna","Beedrill","Pinsir","Caterpie","Butterfree","Metapod","Scyther","Weedle","Venonat",
            "Charmeleon"])

# ===== 09-28 Mon : EASY (gap fill) =====
board("2026-09-28","gen1","Easy",[
  ("WATER",1,"type:water",["Squirtle","Poliwag","Horsea"]),
  ("GRASS",1,"type:grass",["Bulbasaur","Bellsprout"]),
  ("ROCK",1,"type:rock",["Geodude","Onix"]),
  ("PSYCHIC",1,"type:psychic",["Abra","Drowzee"]),
], exclude=["Wartortle","Blastoise","Victreebel","Weepinbell","Oddish","Gloom","Vileplume",
            "Graveler","Golem","Kadabra","Alakazam","Slowpoke","Slowbro","Exeggcute","Exeggutor",
            "Tangela","Ivysaur","Venusaur","Rhyhorn","Rhydon","Seadra","Poliwhirl","Poliwrath"])
board("2026-09-28","mixed","Easy",[
  ("WATER",1,"type:water",["Piplup","Mudkip"],"Both are Water-types."),
  ("GRASS",1,"type:grass",["Turtwig","Cottonee","Bounsweet"],"All three are Grass-types."),
  ("PSYCHIC",1,"type:psychic",["Ralts","Munna"],"Both are Psychic-types."),
  ("ROCK",1,"type:rock",["Shieldon"],"Shieldon is a Rock-type."),
  ("TUFT",2,"sprite:head-tuft",["Rookidee"],"Look for the tuft of feathers on Rookidee's head."),
], exclude=["Prinplup","Empoleon","Swampert","Marshtomp","Torterra","Grotle","Whimsicott",
            "Tsareena","Kirlia","Gardevoir","Gallade","Musharna","Bastiodon","Fletchling",
            "Fletchinder","Talonflame","Pikipek","Trumbeak","Toucannon","Corvisquire","Corviknight"])

# ===== 09-29 Tue : MEDIUM (gap fill) =====
board("2026-09-29","gen1","Medium",[
  ("NORMAL",1,"type:normal",["Chansey","Tauros","Kangaskhan"]),
  ("AERIAL",1,"type:flying",["Golbat"]),
  ("CARAPACE",2,"sprite:shell",["Kabuto","Shellder"]),
  ("NIPPERS",3,"arch:crab",["Krabby"]),
  ("FISH",3,"arch:fish",["Magikarp","Goldeen"],"Magikarp and Goldeen are both based on plain real-world fish."),
], exclude=["Blissey","Miltank","Zubat","Crobat","Kabutops","Cloyster","Kingler","Koffing","Muk",
            "Nidoking","Nidoqueen","Rhydon","Rhyhorn","Persian","Raichu","Grimer","Weezing",
            "Omanyte","Omastar","Seaking","Gyarados"])
board("2026-09-29","mixed","Medium",[
  ("NORMAL",1,"type:normal",["Furfrou","Miltank"]),
  ("DARK",1,"type:dark",["Purrloin"]),
  ("CRUSTACEAN",3,"arch:crustacean",["Clauncher","Crabrawler","Corphish"]),
  ("SPIRIT",4,"based:a-haunted-sandcastle",["Sandygast"]),
  ("MARKED",2,"sprite:stripes",["Zebstrika","Basculin"],"Zebstrika has zebra stripes, and Basculin has a bold racing stripe along its side."),
], exclude=["Liepard","Clawitzer","Crabominable","Crawdaunt","Palossand","Blitzle","Basculegion",
            "Chansey","Tauros","Kangaskhan","Girafarig","Furret","Greavard","Houndstone"])

# ===== 09-30 Wed : CHALLENGING (gap fill) =====
board("2026-09-30","gen1","Challenging",[
  ("FIRE",1,"type:fire",["Vulpix","Growlithe"]),
  ("POKEBALL",4,"based:pokeball",["Voltorb"]),
  ("RATTLE",2,"sprite:rattle-tail",["Ekans"]),
  ("MOLE",3,"arch:mole",["Diglett","Sandshrew"]),
  ("FLOCK",3,"arch:bird",["Pidgeotto","Fearow","Doduo"]),
], exclude=["Dugtrio","Sandslash","Electrode","Arcanine","Ninetales","Pidgeot","Pidgey","Spearow","Dodrio","Farfetch'd"])
board("2026-09-30","mixed","Challenging",[
  ("STARTER",1,"group:starter",["Sceptile","Infernape","Feraligatr","Chesnaught","Delphox"]),
  ("YAKUZA",3,"based:panda-brawler",["Pangoro"],"Pangoro's Japanese name and design evoke a brawling yakuza enforcer -- a tough panda gangster with a leaf 'toothpick' for swagger."),
  ("SIX",2,"sprite:formation",["Falinks"]),
  ("EAGLE",3,"based:eagle",["Braviary"]),
  ("KEYRING",4,"based:keyring",["Klefki"]),
], exclude=["Pancham","Rufflet",
            "Bulbasaur","Ivysaur","Venusaur","Charmander","Charizard","Squirtle","Blastoise",
            "Chikorita","Meganium","Cyndaquil","Typhlosion","Totodile","Croconaw",
            "Treecko","Grovyle","Torchic","Blaziken","Mudkip","Swampert",
            "Turtwig","Torterra","Chimchar","Piplup","Empoleon",
            "Snivy","Serperior","Tepig","Oshawott","Samurott",
            "Chespin","Fennekin","Braixen","Froakie","Greninja",
            "Rowlet","Decidueye","Litten","Incineroar","Popplio","Primarina",
            "Grookey","Rillaboom","Scorbunny","Cinderace","Sobble","Inteleon",
            "Sprigatito","Meowscarada","Fuecoco","Skeledirge","Quaxly","Quaquaval"])

# ===== 10-01 Thu : HARD (gap fill) =====
board("2026-10-01","gen1","Hard",[
  ("GLOOPY",4,"arch:amorphous",["Ditto","Koffing","Muk"]),
  ("GRUB",3,"arch:caterpillar",["Caterpie","Weedle"]),
  ("MALLARD",3,"arch:duck",["Farfetch'd","Psyduck"]),
  # Owner override: INTIMIDATE shares "ate" with Caterpie (a blue on this board);
  # the letter rule is waived here per explicit owner request. Board is already
  # live, so schedule_v2 skips it (this tuple is not re-verified).
  ("INTIMIDATE",5,"lore:intimidate",["Arbok","Gyarados"],"Both share the Ability Intimidate, which cuts an opposing Pokémon's Attack the moment they enter battle."),
], exclude=["Grimer","Weezing","Kakuna","Metapod","Venonat","Paras","Parasect","Golduck","Arcanine","Ekans","Growlithe","Tauros"])
board("2026-10-01","mixed","Hard",[
  ("INKWELL",4,"arch:cephalopod",["Malamar","Octillery"]),
  ("RAVEN",3,"arch:corvid",["Corviknight","Honchkrow"]),
  ("DJINN",5,"arch:genie",["Landorus","Enamorus"]),
  ("PINCER",3,"arch:scorpion",["Drapion","Gligar"]),
  ("COSTUME",2,"sprite:pikachu-costume",["Mimikyu"]),
], exclude=["Inkay","Clobbopus","Grapploct","Murkrow","Corvisquire","Tornadus","Thundurus","Hoopa","Skorupi","Gliscor"])

# ===== 09-25 Fri : HARD (fresh -- old board moved to 10-02, see below; QA asked to move it "to
# the end of all available boards" + fix the Kappa explanation) =====
board("2026-09-25","gen1","Hard",[
  ("SEAL",3,"arch:pinniped",["Seel","Dewgong"],"Seel and its evolution Dewgong are both based on real-world seals."),
  ("MOTH",3,"arch:moth",["Venonat"],"Venonat is based on a fuzzy moth, complete with big compound eyes."),
  ("PITCHER",3,"based:pitcher-plant",["Weepinbell"],"Weepinbell's design is based on a carnivorous pitcher plant."),
  ("HUMANOID",4,"arch:humanoid",["Machop","Magmar","Electabuzz"],"All three are upright, humanoid brawlers -- Magmar and Electabuzz are even based on fire and thunder oni (Japanese demons)."),
  ("TRADE",5,"connection:evolve-by-trade",["Golem","Kadabra"],"Both only evolve when traded to another trainer -- Graveler becomes Golem, and Kadabra becomes Alakazam."),
], exclude=["Slowbro","Slowpoke","Slowking","Dugtrio","Sandslash","Hitmonlee","Hitmonchan",
            "Venomoth","Bellsprout","Victreebel","Oddish","Gloom","Vileplume","Tangela",
            "Machoke","Machamp","Graveler","Haunter","Gengar","Alakazam","Abra",
            "Wartortle","Blastoise","Dewgong"])

# ===== 09-25 Fri : HARD (relocated from the original 09-25 gen1 board -- content unchanged
# except the Kappa clue's explanation, which QA flagged as too thin) =====
board("2026-10-02","gen1","Hard",[
  ("MARTIAL-ARTIST",5,"lore:martial-artist",["Hitmonchan","Machamp","Hitmonlee"]),
  ("FANGS",2,"sprite:fangs",["Raticate"]),
  ("KAPPA",3,"lore:kappa",["Golduck"],"Golduck is based on the kappa, a Japanese river spirit said to have webbed hands, a duck-like bill, and a water-filled dish on its head that's the source of its power."),
  ("DIGGER",3,"arch:mole",["Dugtrio","Sandslash"]),
  ("ORB",4,"based:orb",["Electrode","Magnemite"]),
], exclude=["Poliwrath","Machop","Machoke","Golbat","Zubat","Primeape","Mankey","Persian","Meowth",
            "Raichu","Pikachu","Nidoking","Nidoqueen","Psyduck"])

# ===== 09-25 Fri (mixed) : HARD -- QA fixes: magma-shell -> magma (no hyphen-smushing),
# Omen -> Disaster (clearer, still Absol's real Pokedex genus), and Gourgeist swapped out
# (used too recently with a similar clue) for Drifblim =====
board("2026-09-25","mixed","Hard",[
  ("MAGMA",4,"arch:volcanic",["Camerupt","Numel","Torkoal"],"All three are based on active volcanoes -- Camerupt even erupts from the humps on its back."),
  ("WANDERER",5,"lore:drifting-spirit",["Drifblim"],"Drifblim is said to be the spirit of someone who wandered too far and died, now drifting wherever the wind takes it."),
  ("DISASTER",3,"lore:disaster-pokemon",["Absol"],"Absol's official Pokedex category is literally the 'Disaster Pokemon' -- it appears before storms and earthquakes, though it's really just trying to warn people."),
  ("TWO-FACED",2,"sprite:second-head",["Girafarig","Mawile"]),
  ("FIREFLY",3,"arch:firefly",["Illumise","Volbeat"]),
], exclude=["Gourgeist","Pumpkaboo","Slugma","Magcargo","Zweilous","Doduo","Dodrio",
            "Drifloon","Duskull","Dusclops","Banette"])

# ===== 09-26 Sat : BRUTAL (re-port of the live board -- QA fix: Tauros has a very prominent
# tail and was appearing as a tempting neutral under the TAILED clue; excluded) =====
board("2026-09-26","gen1","Brutal",[
  ("MINDBENDER",5,"lore:hypnosis",["Alakazam","Hypno"]),
  ("ELECTRIC",1,"type:electric",["Raichu","Magneton"]),
  ("TAILED",2,"sprite:tail",["Ninetales","Charizard"]),
  ("SIMIAN",4,"arch:primate",["Machoke","Mankey"]),
  ("SPECIAL",5,"stat:special",["Alakazam","Exeggutor","Magneton"]),
], exclude=["Tauros","Rapidash","Vaporeon","Persian","Primeape","Machop","Kadabra",
            "Drowzee","Golduck"])

# ===== 09-27 Sun (mixed) : EVIL (re-port of the live board -- QA fixes: quicksilver -> speed-stat,
# screech -> nocturnal) =====
board("2026-09-27","mixed","Evil",[
  ("MUSKETEERS",4,"lore:legendary-trio",["Terrakion","Cobalion","Virizion"]),
  ("RUINOUS",5,"mythology:treasures-of-ruin",["Ting-Lu","Chien-Pao","Wo-Chien","Virizion"]),
  ("HEAVYWEIGHT",5,"stat:weight",["Ting-Lu","Terrakion","Cobalion"]),
  ("SPEED-STAT",5,"stat:speed",["Virizion","Chi-Yu"]),
  ("TWILIGHT",3,"arch:owl",["Rowlet","Noctowl"]),
], exclude=["Hoothoot","Zubat","Golbat","Crobat","Noibat","Turtonator","Metapod","Nidoking",
            "Torkoal","Carracosta","Bruxish","Hoopa","Seadra","Drednaw","Piplup","Ducklett",
            "Stoutland","Basculin","Solgaleo","Ferroseed","Vivillon"])

# ===== 10-02 Fri (mixed) : HARD (gap fill) =====
board("2026-10-02","mixed","Hard",[
  ("TANK",5,"stat:defense",["Shuckle","Aggron","Steelix"],"All three are famous defensive walls -- Shuckle in particular has the highest base Defense of any Pokemon."),
  ("LEVITATE",5,"connection:ability",["Rotom","Bronzong"],"Both share the Ability Levitate, which grants full immunity to Ground-type moves."),
  ("AXOLOTL",3,"arch:axolotl",["Wooper"],"Wooper is based on the axolotl, a salamander known for keeping its feathery gills into adulthood."),
  ("POUCH",2,"sprite:throat-pouch",["Wingull","Pelipper"],"Look for the huge throat pouch on Pelipper's sprite -- Wingull has the start of one too."),
  ("MIMIC",3,"trait:vocal-mimicry",["Chatot"],"Chatot is famous for mimicking sounds it hears, right down to its signature move Chatter."),
], exclude=["Sandslash","Torkoal","Bastiodon","Forretress","Skarmory","Donphan","Registeel",
            "Regirock","Metagross","Klefki","Magnezone","Dhelmise","Golurk",
            "Quagsire","Politoed","Swampert","Cradily","Taillow","Swellow",
            "Pelipper","Wingull","Chatot"])

# ===== 10-06 Tue (mixed) : MEDIUM (relocated from 09-28 -- QA rated the original Easy version
# "slightly hard"; re-leveled by merging the ROCK+ICE type clues into one shared MINERAL
# archetype clue (both Roggenrola and Bergmite share the mineral egg group) rather than adding
# a disguised-type word) =====
board("2026-10-06","mixed","Medium",[
  ("WATER",1,"type:water",["Buizel","Popplio","Binacle"]),
  ("GRASS",1,"type:grass",["Snivy","Chikorita","Snover"]),
  ("MINERAL",4,"arch:mineral",["Roggenrola","Bergmite"],"Both are Mineral egg-group Pokemon based on inert lumps of rock and ice -- a geode and an iceberg chunk."),
  ("GLARE",2,"sprite:blank-stare",["Espurr"],"Look for the wide, blank 'help me' stare on Espurr's sprite."),
], exclude=["Floatzel","Brionne","Primarina","Servine","Serperior","Bayleef","Meganium",
            "Boldore","Gigalith","Barbaracle","Abomasnow","Cubchoo","Meowstic"])

# ===== 10-09 Fri (mixed) : HARD -- owner-requested "FIRST" board linking three different
# senses of first: Bulbasaur (#001 in the Pokedex), Rhydon (the first Pokemon ever designed),
# and Arceus ("The Original One" that myth says created the universe). Placed here because
# Bulbasaur/Rhydon are blues on 09-27/09-28, so this is the first Hard/Challenging slot clear
# of the 10-day blue-repeat cap. =====
board("2026-10-09","mixed","Hard",[
  ("FIRST",5,"lore:first",["Bulbasaur","Rhydon","Arceus"],"Three different kinds of 'first': Bulbasaur is No. 001 in the National Pokedex, Rhydon was the very first Pokemon ever designed by Game Freak, and Arceus is 'The Original One' that legend says shaped the whole Pokemon universe."),
  ("FOSSIL",4,"lore:revived-fossil",["Tyrunt","Archen"],"Both are ancient Pokemon brought back to life from fossils -- Tyrunt from the Jaw Fossil and Archen from the Plume Fossil."),
  ("PENGUIN",3,"arch:penguin",["Piplup","Eiscue"],"Both are based on penguins -- Piplup the plucky chick and Eiscue a penguin hauling a block of ice for a head."),
  ("SERPENT",3,"arch:snake",["Seviper","Sandaconda"],"Both are based on real snakes -- Seviper a fanged viper and Sandaconda a coiled sand cobra."),
], exclude=[
  # FIRST look-alikes (other "original"/#1 legends)
  "Victini","Mew","Mewtwo","Dialga","Palkia","Giratina","Ivysaur","Venusaur","Rhyhorn","Rhyperior",
  # revived-fossil Pokemon (FOSSIL must fit only Tyrunt/Archen)
  "Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Lileep","Cradily","Anorith","Armaldo",
  "Cranidos","Rampardos","Shieldon","Bastiodon","Tirtouga","Carracosta","Amaura","Aurorus",
  "Tyrantrum","Archeops","Dracovish","Arctovish","Dracozolt","Arctozolt","Relicanth","Genesect",
  # ancient Paradox Pokemon (not fossils, but 'ancient' enough to be a FOSSIL red herring)
  "Great Tusk","Scream Tail","Brute Bonnet","Flutter Mane","Slither Wing","Sandy Shocks",
  "Roaring Moon","Walking Wake","Gouging Fire","Raging Bolt","Koraidon",
  # penguins (PENGUIN must fit only Piplup/Eiscue)
  "Prinplup","Empoleon","Delibird",
  # snakes (SERPENT must fit only Seviper/Silicobra)
  "Ekans","Arbok","Onix","Steelix","Dratini","Dragonair","Dragonite","Milotic","Feebas",
  "Serperior","Servine","Snivy","Silicobra","Huntail","Rayquaza","Gyarados","Eelektross",
  "Dunsparce","Dudunsparce","Silvally"])
