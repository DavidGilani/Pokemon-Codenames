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
board("2026-09-06","gen1","Evil",[
  ("RELIC",5,"lore:fossil",["Aerodactyl","Omastar","Kabutops"]),
  ("LEGEND",5,"lore:legendary",["Articuno","Zapdos","Moltres"]),
  ("FROST",4,"lore:ice-storm",["Articuno","Lapras"]),
  ("VOLCANO",4,"lore:volcano",["Moltres","Magmar"]),
  ("SEAL",3,"arch:pinniped",["Dewgong"]),
], exclude=["Omanyte","Kabuto","Mewtwo","Mew","Jynx","Cloyster","Seel","Magby","Ponyta","Vulpix"])
board("2026-09-06","mixed","Evil",[
  ("REVENANT",5,"lore:fossil",["Tirtouga","Archen","Dracovish"]),
  ("FUSION",4,"arch:chimera",["Dracovish","Arctozolt"]),
  ("FROZEN",4,"lore:ice-storm",["Arctozolt","Eiscue"]),
  ("POSSESSED",5,"lore:haunted-object",["Polteageist","Sinistcha"]),
  ("ROBIN-HOOD",3,"arch:fox",["Thievul","Zoroark"]),
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
