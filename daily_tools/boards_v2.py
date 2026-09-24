# Rescheduled boards 2026-08-22 .. 2026-09-06 (loaded by schedule_v2.py).
# Tier fixed by weekday: Mon Easy / Tue Medium / Wed Challenging / Thu Hard /
# Fri Hard / Sat Brutal / Sun Evil. Brutal/Evil pass the overlap gate
# (clue numbers sum >= 11, <= 1 single-tile clue).
#
# (2026-08-22 .. 2026-09-02 gen1/mixed boards removed here: long since live
# in Supabase and now outside the rolling anti-repetition window, so they
# were stale dead code that the verifier mistook for new, unverified boards.)

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
  ("FROST",4,"lore:ice-storm",["Articuno","Lapras","Dewgong"]),
  ("VOLCANO",3,"lore:volcano",["Moltres","Magmar"]),
], exclude=["Omanyte","Kabuto","Mewtwo","Mew","Jynx","Cloyster","Seel","Magby","Ponyta","Vulpix","Rhyhorn","Rhydon","Nidoking"])
# QA flourish (owner-approved): kept as Evil with 4 clues even though it misses
# the 3-distinct-cats / sum>=11 gates – Arctozolt folded into REVENANT (it's a
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

# ===== 10-06 Tue (gen1) : MEDIUM -- gap-fill (nightly maintainer) =====
board("2026-10-06","gen1","Medium",[
  ("PSYCHIC",1,"type:psychic",["Drowzee","Kadabra"],"Every one of these is a Psychic-type Pokemon."),
  ("FLYING",1,"type:flying",["Doduo","Golbat","Charizard"],"Every one of these is a Flying-type Pokemon."),
  ("PACHYDERM",4,"arch:pachyderm",["Rhyhorn","Nidoqueen"],"Both are designed as thick-hided, armoured beasts in the rhinoceros mould -- Rhyhorn is literally the Spikes Pokemon, and Nidoqueen's whole line is built around armoured hide."),
  ("POUCH",2,"sprite:pouch",["Kangaskhan"],"Look for the baby Cub peeking out of the pouch on Kangaskhan's belly."),
  ("TONGUE",2,"sprite:tongue",["Lickitung"],"Look for the extraordinarily long tongue on Lickitung's sprite -- as long as its whole body."),
], exclude=["Hypno","Abra","Alakazam","Dodrio","Zubat","Crobat","Charmander","Charmeleon",
            "Rhydon","Rhyperior","Nidoran♂","Nidorino","Nidoking","Nidoran♀","Nidorina"])

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

# ===== 10-03 Sat : BRUTAL (gap fill) =====
board("2026-10-03","gen1","Brutal",[
  ("KIND",3,"trait:gentle-giant",["Dragonite"],"Dragonite is famously gentle and kind despite its power -- Pokedex lore says it rescues drowning sailors and guides lost ships home."),
  ("TRADE",5,"connection:trade-evolution",["Alakazam","Golem","Gengar"],"All three only reach their final form when traded to another trainer -- Kadabra becomes Alakazam, Graveler becomes Golem, and Haunter becomes Gengar."),
  ("FOLKLORE",5,"myth:folklore-being",["Golem","Gengar","Hypno"],"Each is built on a folkloric being that blurs the line between animate and inanimate -- Golem the clay creature of Jewish legend, Gengar your own shadow come to life, and Hypno the baku, a dream-eating spirit of Japanese myth."),
  ("PREHISTORIC",4,"lore:fossil-revival",["Kabutops","Omastar"],"Both are ancient sea creatures revived from fossils -- Kabutops from the Dome Fossil (a horseshoe crab) and Omastar from the Helix Fossil (a giant ammonite)."),
  ("CONJOINED",2,"sprite:fused-body",["Magneton","Weezing"],"Look at the sprite and count the parts -- Magneton is three Magnemite fused together, and Weezing is twin gas-filled heads joined at the middle."),
], exclude=["Machoke","Graveler","Haunter","Kadabra","Poliwhirl","Geodude","Gastly","Drowzee",
            "Omanyte","Kabuto","Aerodactyl","Magnemite","Koffing","Exeggcute"])
board("2026-10-03","mixed","Brutal",[
  ("ANUBIS",5,"myth:anubis",["Lucario","Riolu"],"Both Lucario and its pre-evolution Riolu are based on Anubis, the jackal-headed Egyptian god who guided the dead -- fitting for Pokemon that read life energy through Aura."),
  ("STEEL",1,"type:steel",["Lucario","Metagross","Probopass","Magnezone"],"All four are Steel-type Pokemon."),
  ("SIX-HUNDRED",5,"stat:sixhundred",["Metagross","Salamence","Garchomp","Tyranitar"],"All four share the exact same base stat total of 600 -- the unofficial benchmark for a 'pseudo-legendary'."),
  ("DATA-BRAIN",4,"lore:supercomputer",["Metagross","Porygon-Z"],"Both are famous for computer-like minds -- Metagross's four fused brains are said to out-think a supercomputer, and Porygon-Z is an AI construct glitched by rogue software."),
], exclude=["Beldum","Metang","Bagon","Shelgon","Gible","Gabite","Larvitar","Pupitar",
            "Dragonite","Hydreigon","Goodra","Kommo-o","Dragapult","Baxcalibur",
            "Deino","Zweilous","Goomy","Sliggoo","Jangmo-o","Hakamo-o","Dreepy","Drakloak",
            "Frigibax","Arctibax","Porygon","Porygon2"])

# ===== 10-04 Sun : EVIL =====
board("2026-10-04","gen1","Evil",[
  ("ROCK-HEAD",5,"ability:rock-head",["Geodude","Onix","Marowak"],"All three share the Ability Rock Head, which stops them flinching from moves like Fake Out or Headbutt."),
  ("HUMAN-LIKE",5,"egg:human-like",["Mr. Mime","Jynx"],"Mr. Mime and Jynx are both in the Human-Like Egg Group, the category for Pokemon built to stand and move like people."),
  ("WATER-STONE",5,"connection:water-stone",["Starmie","Poliwrath"],"Both evolve on exposure to a Water Stone -- Staryu into Starmie, and Poliwhirl into Poliwrath."),
  ("SIMIAN",4,"arch:primate",["Machop","Primeape"],"Machop and Primeape are both modelled on real-world primates -- Machop a bodybuilding ape, Primeape an ill-tempered macaque."),
  ("CHUCK",3,"trainer:chuck",["Primeape","Poliwrath"],"Primeape and Poliwrath are both signature Pokemon of Johto Gym Leader Chuck at Cianwood Gym -- his ace team in Gold, Silver and Crystal."),
], exclude=["Cubone","Graveler","Golem","Abra","Kadabra","Alakazam","Machoke","Machamp",
            "Hitmonlee","Hitmonchan","Vaporeon","Cloyster","Mankey"])
board("2026-10-04","mixed","Evil",[
  ("OWN-TEMPO",5,"ability:own-tempo",["Slowpoke","Smeargle"],"Both have the Ability Own Tempo, which makes them immune to confusion."),
  ("REGENERATOR",5,"ability:regenerator",["Slowpoke","Tangela","Audino"],"All three can have Regenerator, healing a chunk of HP whenever they switch out of battle."),
  ("ARACHNID",4,"arch:arachnid",["Ariados","Galvantula"],"Both are explicitly spider Pokemon -- eight-legged arachnids with a web-spinning, venomous design."),
  ("COMPOUND-EYES",5,"ability:compound-eyes",["Yanma","Galvantula"],"Both can have Compound Eyes, an Ability modelled on a real insect's compound eye that boosts the accuracy of their moves."),
  ("AMPHIBIAN",3,"arch:frog",["Croagunk","Seismitoad"],"Both are built on real-world frogs and toads -- Croagunk a poison-secreting toad, Seismitoad a warty bullfrog."),
], exclude=["Slowbro","Slowking","Lickitung","Lotad","Lombre","Ludicolo","Corsola","Ho-Oh","Tangrowth",
            "Spinarak","Joltik","Araquanid","Dewpider","Spidops","Tarountula",
            "Dustox","Nincada","Scatterbug","Vivillon","Blipbug",
            "Toxicroak","Palpitoad","Tympole","Froakie","Frogadier","Greninja"])

# ===== 10-05 Mon : EASY =====
board("2026-10-05","gen1","Easy",[
  ("ELECTRIC",1,"type:electric",["Pikachu","Jolteon"],"Pikachu and Jolteon are both Electric-type Pokemon."),
  ("ICE",1,"type:ice",["Articuno","Dewgong"],"Articuno and Dewgong are both Ice-type Pokemon."),
  ("GHOST",1,"type:ghost",["Haunter"],"Haunter is a Ghost-type Pokemon, a shadowy spirit said to slip through walls at night."),
  ("BUG",1,"type:bug",["Pinsir","Scyther"],"Pinsir and Scyther are both Bug-type Pokemon."),
  ("CLAWS",2,"sprite:claws",["Krabby","Kabuto"],"Look at the sprites -- Krabby's oversized pincers and Kabuto's crab-like foreclaws are both a pair of prominent claws."),
], exclude=["Kingler","Kabutops","Sandshrew","Sandslash","Omastar","Machamp"])
board("2026-10-05","mixed","Easy",[
  ("GROUND",1,"type:ground",["Cubone","Donphan"],"Cubone and Donphan are both Ground-type Pokemon."),
  ("DRAGON",1,"type:dragon",["Jangmo-o","Goomy"],"Jangmo-o and Goomy are both Dragon-type Pokemon."),
  ("FAIRY",1,"type:fairy",["Sylveon","Comfey"],"Sylveon and Comfey are both Fairy-type Pokemon."),
  ("FIGHTING",1,"type:fighting",["Throh","Pancham"],"Throh and Pancham are both Fighting-type Pokemon."),
  ("GEARS",2,"sprite:gear-shape",["Klink"],"Klink's entire body is a pair of interlocking gears, spinning against each other."),
], exclude=["Klang","Klinklang","Bronzor","Bronzong","Magnemite","Magneton","Beldum","Metang","Ferroseed","Ferrothorn","Sawk"])

# ===== 10-07 Wed : CHALLENGING (gap fill) =====
board("2026-10-07","gen1","Challenging",[
  ("ROCK",1,"type:rock",["Graveler","Aerodactyl","Omanyte"],"Graveler, Aerodactyl and Omanyte are all Rock-type -- a walking boulder, a revived pterosaur, and a spiral ammonite shell."),
  ("LEEK",2,"lore:leek",["Farfetch'd"],"Farfetch'd always carries a stalk of leek -- a pun on the Japanese saying 'a duck that comes carrying its own leek', meaning a stroke of good luck."),
  ("STINGER",2,"sprite:tail-stinger",["Nidorina"],"Look at the sprite -- Nidorina carries a sharp poison barb on the tip of her tail, the feature her whole family is named for."),
  ("CLAM",3,"arch:clam",["Shellder"],"Shellder is modelled on a bivalve clam, its two-part shell snapping shut on its huge tongue."),
  ("BIPEDAL",3,"arch:humanoid",["Electabuzz","Magmar","Machoke"],"All three are built as upright, muscular humanoid figures -- Electabuzz and Magmar both drawing on Japanese oni demons, Machoke modelled on a professional wrestler."),
], exclude=["Nidoking","Nidoqueen","Nidoran♀","Nidoran♂","Nidorino","Cloyster",
            "Mr. Mime","Jynx","Hitmonlee","Hitmonchan","Primeape","Machamp","Machop",
            "Alakazam","Kadabra","Abra","Mewtwo","Elekid","Magby"])
board("2026-10-07","mixed","Challenging",[
  ("DARK",1,"type:dark",["Sneasel","Absol"],"Sneasel and Absol are both pure Dark-type Pokemon -- sharp-clawed hunters that prowl at night."),
  ("CATFISH",3,"arch:catfish",["Whiscash"],"Whiscash is based on a catfish -- specifically Japan's mythical namazu, said to thrash beneath the earth and cause earthquakes."),
  ("EEL",3,"arch:eel",["Gorebyss","Wugtrio"],"Gorebyss and Wugtrio are both based on eels -- Gorebyss a slender deep-sea snipe eel, Wugtrio three garden eels poking from the sand, echoing its Kanto look-alike Dugtrio."),
  ("BEETLE",3,"arch:beetle",["Heracross","Vikavolt"],"Heracross and Vikavolt are both modelled on real beetles -- Heracross a Hercules beetle, Vikavolt a stag beetle fused with a fighter jet."),
  ("BLADE",2,"sprite:blade-body",["Aegislash","Kartana"],"Look at the sprites -- Aegislash is a living sword and shield, and Kartana is a razor-edged sheet of steel-hard paper."),
], exclude=["Milotic","Eelektrik","Eelektross","Ledyba","Ledian","Pinsir","Scyther","Orbeetle","Honedge","Doublade","Bisharp","Kingambit","Drampa"])

# ===== 10-08 Thu : HARD =====
board("2026-10-08","gen1","Hard",[
  ("ANALYTIC",5,"ability:analytic",["Magnemite","Porygon","Staryu"],"Magnemite, Porygon and Staryu can all be born with the Ability Analytic, which boosts their move's power whenever they act after their opponent that turn."),
  ("SHELL-ARMOR",5,"ability:shell-armor",["Cloyster","Kingler","Lapras"],"Cloyster, Kingler and Lapras can all have the Ability Shell Armor, which flatly blocks any incoming attack from landing a critical hit."),
  ("MOLE",3,"arch:mole",["Diglett"],"Diglett is a mole through and through, spending its whole life burrowing just under the surface."),
  ("TRIPLE",2,"sprite:three-heads",["Dodrio"],"Dodrio's sprite gives it three separate heads growing from one long-legged body, an unmistakable silhouette."),
  ("FOX",3,"arch:fox",["Ninetales"],"Ninetales is a fox through and through, its nine flowing tails drawn straight from Japanese kitsune folklore."),
], exclude=["Magneton","Starmie","Shellder","Krabby","Omanyte","Omastar","Vulpix","Eevee","Doduo","Dugtrio"])
board("2026-10-08","mixed","Hard",[
  ("WEAK-ARMOR",5,"ability:weak-armor",["Garbodor","Cursola"],"Garbodor and Cursola can both have the Ability Weak Armor, which lowers their Defense but sharply raises their Speed every time they're struck by a move."),
  ("STURDY",5,"ability:sturdy",["Nosepass","Relicanth","Carbink","Togedemaru"],"Nosepass, Relicanth, Carbink and Togedemaru can all have the Ability Sturdy, guaranteeing they survive any hit that would otherwise knock them out from full HP."),
  ("BEAK",2,"sprite:cannon-beak",["Toucannon"],"Toucannon's whole design is built around one oversized, cannon-like beak, impossible to miss on its sprite."),
  ("TURTLE",3,"arch:turtle",["Torkoal"],"Torkoal is a tortoise fused with a coal-burning stove, complete with a smokestack shell that puffs out sooty smoke."),
  ("CRAB",3,"arch:crab",["Klawf"],"Klawf is a real crab through and through, ambushing prey sideways just like the rock crab that inspired it."),
], exclude=["Slugma","Magcargo","Skarmory","Boldore","Dwebble","Crustle","Vanillite","Vanillish","Vanilluxe","Vullaby","Mandibuzz","Sinistea","Polteageist","Armarouge","Ceruledge","Sudowoodo","Pineco","Forretress","Aron","Lairon","Regirock","Bastiodon","Bonsly","Sawk","Tirtouga","Carracosta","Avalugg","Cosmoem","Nacli","Naclstack","Garganacl","Archaludon","Probopass","Magnemite","Magnezone","Squirtle","Wartortle","Blastoise","Turtwig","Grotle","Torterra","Turtonator","Chewtle","Drednaw","Terapagos","Paras","Parasect","Krabby","Kingler","Corphish","Crawdaunt","Binacle","Barbaracle","Clauncher","Clawitzer","Crabrawler","Crabominable","Wimpod","Golisopod","Pidgey","Spearow","Fearow","Farfetch'd","Omastar","Wingull","Pikipek","Trumbeak","Donphan"])

# ===== 10-09 Fri : HARD =====
board("2026-10-09","gen1","Hard",[
  ("SERPENT",3,"arch:serpent",["Ekans","Gyarados","Dratini"],"All three are built on real snakes and Chinese dragon-serpent myth -- Ekans is a plain garden snake, Gyarados the carp-turned-dragon of the Dragon Gate legend, and Dratini a mystical river serpent said to shed its skin and ascend to the heavens."),
  ("CAT",3,"arch:feline",["Mew","Meowth","Vaporeon"],"Each blends in a real cat -- Mew's design mixes a housecat with a human fetus as the ancestor of all Pokemon, Meowth is explicitly a coin-clutching maneki-neko lucky cat, and Vaporeon's Pokedex flavour describes it as part mermaid, part cat that melted into water."),
  ("HOOK",2,"sprite:hook",["Weepinbell"],"Look at Weepinbell's sprite -- its pitcher-shaped body ends in a hooked lip, the same curled shape a real pitcher plant uses to trap insects."),
  ("SYNTHETIC",4,"based:genetic-engineering",["Mewtwo"],"Mewtwo isn't a natural species -- it was created through genetic engineering, spliced together from Mew's DNA in a lab on Cinnabar Island."),
  ("DOPPELGANGER",5,"myth:doppelganger",["Gengar"],"Gengar's Japanese name plays on 'doppelganger', and its Pokedex lore casts it as your own shadow, hiding in darkness to steal warmth from anyone it catches."),
], exclude=["Arbok","Onix","Dragonair","Dragonite","Seadra","Persian","Bellsprout","Victreebel","Porygon","Haunter","Gastly","Ditto"])

# ===== 10-10 Sat : BRUTAL (gap fill) =====
board("2026-10-10","gen1","Brutal",[
  ("NORMAL",1,"type:normal",["Tauros","Fearow","Chansey"],"Tauros, Fearow, and Chansey are all Normal-type Pokémon."),
  ("FLEET",5,"stat:speed",["Tauros","Dugtrio","Electrode","Fearow"],"Tauros, Dugtrio, Electrode, and Fearow are four of Kanto's fastest Pokémon, each built around a blistering base Speed stat."),
  ("GENIUS",5,"stat:special-attack",["Alakazam","Exeggutor","Moltres"],"Alakazam, Exeggutor, and Moltres are battle geniuses -- each carries one of the highest Special Attack stats among the original 151 Pokémon."),
  ("MEGATON",4,"lore:genus",["Golem"],"Golem's own Pokédex category is literally the 'Megaton Pokémon' -- official recognition of just how explosive and heavy its boulder body is."),
], exclude=["Abra","Aerodactyl","Charizard","Diglett","Dodrio","Electabuzz","Exeggcute","Gengar","Geodude",
            "Graveler","Jolteon","Kadabra","Magneton","Mew","Mewtwo","Ninetales","Persian","Pidgeot",
            "Raichu","Rapidash","Scyther","Spearow","Starmie","Tentacruel","Voltorb","Zapdos"])
board("2026-10-10","mixed","Brutal",[
  ("UNDERWORLD",4,"lore:underworld-guide",["Cofagrigus","Dusknoir"],"Both are guides to the realm of the dead -- Cofagrigus traps the greedy forever inside its gilded coffin body, while Dusknoir is modelled on a Shinigami said to drag lost souls into the afterlife."),
  ("BULWARK",5,"stat:defense",["Barbaracle","Suicune","Umbreon","Cofagrigus","Kingambit"],"Barbaracle, Suicune, Umbreon, Cofagrigus, and Kingambit are all built as defensive walls, each carrying one of the toughest bulk stats of its generation."),
  ("SLUGGER",5,"stat:attack",["Luxray","Passimian","Kingambit","Sharpedo"],"Luxray, Passimian, Kingambit, and Sharpedo are all hard hitters, each boasting one of the highest Attack stats of its generation."),
  ("SINNOH",3,"region:sinnoh",["Dusknoir","Luxray"],"Dusknoir and Luxray are both native to the Sinnoh region, first appearing in Pokémon Diamond and Pearl."),
], exclude=["Abomasnow","Ambipom","Archaludon","Archeops","Armaldo","Avalugg","Azelf","Barraskewda","Bastiodon",
            "Baxcalibur","Beartic","Bewear","Bibarel","Bidoof","Bisharp","Blacephalon","Blaziken","Bonsly",
            "Breloom","Bronzor","Brute Bonnet","Budew","Buneary","Burmy","Buzzwole","Carnivine","Carracosta",
            "Carvanha","Celebi","Ceruledge","Cherrim","Cherubi","Chien-Pao","Chimchar","Chingling","Coalossal",
            "Cobalion","Combee","Conkeldurr","Copperajah","Cosmoem","Crabominable","Cranidos","Crawdaunt",
            "Cresselia","Crustle","Dachsbun","Darkrai","Darmanitan","Deoxys","Dhelmise","Dialga","Diancie",
            "Dipplin","Dondozo","Doublade","Dragapult","Drifblim","Drifloon","Druddigon","Duraludon","Durant",
            "Dusclops","Duskull","Eevee","Electivire","Emboar","Empoleon","Escavalier","Espeon","Eternatus",
            "Excadrill","Ferrothorn","Finneon","Flareon","Floatzel","Forretress","Froslass","Gabite","Gallade",
            "Garganacl","Gastrodon","Genesect","Gible","Gigalith","Giratina","Glaceon","Glameow","Glastrier",
            "Gliscor","Golisopod","Golurk","Gouging Fire","Gourgeist","Granbull","Great Tusk","Grimmsnarl",
            "Grotle","Groudon","Happiny","Hariyama","Haxorus","Heatran","Hippopotas","Hippowdon","Ho-Oh",
            "Hydrapple","Iron Boulder","Iron Bundle","Iron Hands","Iron Leaves","Iron Thorns","Iron Treads",
            "Iron Valiant","Jirachi","Kleavor","Klinklang","Kommo-o","Koraidon","Kricketot","Kricketune",
            "Kyogre","Kyurem","Lairon","Leafeon","Lickilicky","Lopunny","Lugia","Lumineon","Lunala","Luxio",
            "Mabosstiff","Magcargo","Magearna","Magmortar","Mamoswine","Manaphy","Mandibuzz","Mantyke",
            "Marshadow","Melmetal","Meloetta","Mesprit","Mienshao","Mime Jr.","Miraidon","Mismagius",
            "Monferno","Mothim","Mudsdale","Munchlax","Musharna","Ogerpon","Okidogi","Orbeetle","Orthworm",
            "Pachirisu","Palkia","Palossand","Pawniard","Pecharunt","Pheromosa","Phione","Prinplup","Purugly",
            "Pyukumuku","Quaquaval","Raging Bolt","Rampardos","Rayquaza","Regigigas","Regirock","Registeel",
            "Reshiram","Rhyperior","Rillaboom","Roaring Moon","Roserade","Runerigus","Sawk","Scizor","Scrafty",
            "Scream Tail","Shaymin","Shellos","Shieldon","Shinx","Sirfetch'd","Skarmory","Skorupi","Skuntank",
            "Slaking","Slither Wing","Slowbro","Sneasler","Solgaleo","Spiritomb","Stakataka","Staraptor",
            "Staravia","Starly","Stonjourner","Stunfisk","Stunky","Sudowoodo","Swampert","Tangrowth",
            "Tapu Bulu","Tapu Fini","Terrakion","Ting-Lu","Togekiss","Torterra","Toxapex","Toxicroak",
            "Tsareena","Turtonator","Turtwig","Tyrantrum","Ursaluna","Ursaring","Urshifu","Uxie","Vespiquen",
            "Victini","Volcanion","Walrein","Weavile","Wormadam","Xerneas","Yamask","Yanmega","Yveltal",
            "Zacian","Zamazenta","Zarude","Zekrom","Zygarde"])

# ===== 10-13 Tue : MEDIUM (gap fill, +28d window) =====
board("2026-10-13","mixed","Medium",[
  ("STEEL",1,"type:steel",["Corviknight","Klefki","Mawile","Empoleon"],"Corviknight, Klefki, Mawile and Empoleon are all Steel-type Pokemon, each pairing it with a second type of Flying, Fairy, Fairy and Water."),
  ("GHOST",1,"type:ghost",["Mismagius","Hoopa","Chandelure"],"Mismagius, Hoopa and Chandelure are all Ghost-type Pokemon."),
  ("MOHAWK",2,"sprite:mohawk",["Toxtricity"],"Toxtricity's punk-rocker design is topped with a spiky mohawk crest, unmistakable on its sprite."),
  ("SHEER-FORCE",5,"ability:sheer-force",["Braviary","Mawile"],"Braviary and Mawile can both have the Ability Sheer Force, which strips a move of any secondary effect in exchange for a flat power boost."),
], exclude=["Bagon","Cetitan","Cetoddle","Conkeldurr","Copperajah","Cranidos","Croconaw","Cufant","Darmanitan","Druddigon","Feraligatr","Gurdurr","Hariyama","Kingler","Kleavor","Krabby","Landorus","Makuhita","Nidoking","Nidoqueen","Rampardos","Rufflet","Steelix","Tauros","Timburr","Totodile","Toucannon","Trapinch"])

# ===== 10-14 Wed : CHALLENGING (gap fill) =====
board("2026-10-14","gen1","Challenging",[
  ("WATER",1,"type:water",["Golduck","Seaking"],"Golduck and Seaking are both Water-type Pokemon."),
  ("PUPA",2,"sprite:cocoon",["Kakuna","Metapod"],"Kakuna and Metapod are both stationary cocoon-stage Pokemon from two different bug lines, each just a shell waiting to hatch."),
  ("HUMANOID",3,"arch:humanoid",["Hitmonchan","Jynx"],"Hitmonchan and Jynx are both built as upright, human-shaped fighters -- Hitmonchan a boxer forever throwing punches, Jynx a lipsticked figure said to mimic human dance."),
  ("ROCK-HEAD",5,"ability:rock-head",["Graveler","Marowak","Aerodactyl"],"Graveler, Marowak and Aerodactyl can all have the Ability Rock Head, which stops them taking any recoil damage from moves like Double-Edge or Head Smash."),
], exclude=["Cubone","Golem","Onix","Rhydon","Rhyhorn","Electabuzz","Hitmonlee","Machamp","Machoke","Machop","Magmar","Mewtwo","Mr. Mime"])
board("2026-10-14","mixed","Challenging",[
  ("GROUND",1,"type:ground",["Runerigus","Palossand","Golurk"],"Runerigus, Palossand and Golurk are all Ground-type Pokemon -- a cursed stone imprint, a vengeful sand spirit, and an ancient clay automaton animated by a ghost."),
  ("DEER",3,"arch:deer",["Stantler","Xerneas"],"Stantler and Xerneas are both deer through and through -- Stantler a stag whose antlers can conjure illusions, Xerneas a mythical deer said to grant eternal life."),
  ("SCYTHE",3,"arch:mantis",["Kleavor","Leavanny"],"Kleavor and Leavanny both carry scythe-like blade arms -- Kleavor's are living rock axes, Leavanny's are a pair of broad, curved leaves."),
  ("MULTISCALE",5,"ability:multiscale",["Dragonite","Lugia"],"Dragonite and Lugia are the only two Pokemon that can have the Ability Multiscale, which halves the damage they take from a hit while they're still at full HP."),
], exclude=["Deerling","Sawsbuck","Wyrdeer","Fomantis","Lurantis","Scizor","Scyther","Golett"])

# ===== 10-15 Thu : HARD (gap fill) =====
board("2026-10-15","gen1","Hard",[
  ("NIPPERS",3,"arch:crab",["Paras","Kingler"],"Paras and Kingler are both modelled on real crabs -- Paras a crab-like body sprouting parasitic mushrooms, Kingler a fiddler crab with one oversized, powerful nipper claw."),
  ("MOXIE",5,"ability:moxie",["Gyarados","Pinsir"],"Gyarados and Pinsir are the only two original Pokemon that can have the Ability Moxie, which raises their Attack every time they knock out an opposing Pokemon."),
  ("SIMIAN",4,"arch:primate",["Machamp","Primeape"],"Machamp and Primeape are both built as powerful primates -- Machamp a four-armed wrestler, Primeape a furious, ever-angry monkey."),
  ("SLURP",2,"sprite:tongue",["Lickitung"],"Lickitung's entire gimmick is its absurdly long, prehensile tongue, which it uses to lick and taste everything it touches."),
  ("FISH",3,"arch:fish",["Goldeen","Magikarp"],"Goldeen and Magikarp are both ordinary fish at heart -- a fantail goldfish and a nearly-useless carp, each destined to be outclassed by its own evolution."),
], exclude=["Krabby","Parasect","Machoke","Machop","Mankey","Horsea","Seadra","Seaking"])
board("2026-10-15","mixed","Hard",[
  ("HOOT",3,"arch:owl",["Noctowl","Rowlet"],"Noctowl and Rowlet are both owls through and through -- Noctowl a big-eyed nocturnal hunter, Rowlet a silent-winged archer owl most active after dark."),
  ("SOLID-ROCK",5,"ability:solid-rock",["Camerupt","Rhyperior"],"Camerupt and Rhyperior can both have the Ability Solid Rock, which shrinks the damage they take from any supereffective hit."),
  ("CEPHALOPOD",4,"arch:cephalopod",["Octillery","Inkay"],"Octillery and Inkay are both cephalopods -- Octillery a barrel-bodied octopus, Inkay a small squid that swims upside down and flashes bioluminescent light."),
  ("PIG",3,"arch:pig",["Emboar","Lechonk"],"Emboar and Lechonk are both modelled on real pigs -- Emboar a blazing fire-boar martial artist, Lechonk a stout, ever-hungry wild boar."),
  ("COINS",2,"sprite:coins",["Gholdengo"],"Gholdengo's entire body is formed from a thousand ancient coins fused together, according to its own Pokedex lore -- a callback to its coin-collecting pre-evolution, Gimmighoul."),
], exclude=["Dartrix","Decidueye","Hoothoot","Carracosta","Tirtouga","Clobbopus","Grapploct","Malamar","Oinkologne","Pignite","Tepig"])

# ===== 10-16 Fri : HARD (gap fill) =====
board("2026-10-16","gen1","Hard",[
  ("SNAKE",3,"arch:serpent",["Arbok","Dragonair"],"Arbok and Dragonair are both built on real-world and mythical serpents -- Arbok a hooded cobra, Dragonair a serene river dragon-snake said to control the weather."),
  ("STURDY",5,"ability:sturdy",["Golem","Magnemite"],"Golem and Magnemite can both have the Ability Sturdy, guaranteeing they survive any hit that would otherwise knock them out from full HP."),
  ("RAPTOR",4,"arch:raptor",["Fearow","Pidgeot"],"Fearow and Pidgeot are both modelled on real birds of prey -- Fearow a huge-beaked raptor, Pidgeot a hawk-like flier famed for its speed."),
  ("SHELL",2,"sprite:spiked-shell",["Cloyster"],"Cloyster's entire body is a pair of massive, spiked shells clamped shut around a soft core -- one of the hardest shells of any Pokemon."),
  ("RODENT",3,"arch:rodent",["Rattata","Nidorina"],"Rattata and Nidorina are both built like real rodents -- Rattata a common brown rat, Nidorina a spine-covered, cavy-sized creature."),
], exclude=["Dratini","Ekans","Gyarados","Onix","Geodude","Magneton","Aerodactyl","Pidgeotto","Shellder","Nidorino","Pikachu","Raichu"])
board("2026-10-16","mixed","Hard",[
  ("TUSKS",3,"arch:elephant",["Copperajah","Donphan"],"Copperajah and Donphan are both built on real elephants, complete with a pair of curved tusks -- Copperajah a rampaging bull elephant in copper armour, Donphan a rolling, armoured pachyderm."),
  ("HUGE-POWER",5,"ability:huge-power",["Azumarill","Bunnelby"],"Azumarill and Bunnelby can both have the Ability Huge Power, which doubles their Attack stat outright."),
  ("ARACHNID",4,"arch:scorpion",["Drapion","Gligar"],"Drapion and Gligar are both modelled on real scorpions -- Drapion a heavily armoured ogre scorpion, Gligar a flying scorpion-bat hybrid that glides on membrane wings."),
  ("SPOTS",2,"sprite:spots",["Ledian"],"Ledian is covered in small red spots across its wings and back, a nod to real ladybugs -- an easy tell on its sprite."),
  ("BOVINE",3,"arch:bovine",["Bouffalant","Miltank"],"Bouffalant and Miltank are both modelled on real cattle -- Bouffalant an American bison with an afro-like mane, Miltank a placid dairy cow."),
], exclude=["Cufant","Phanpy","Azurill","Diggersby","Marill","Skorupi","Gliscor","Tauros"])

# ===== 10-17 Sat : BRUTAL (gap fill) =====
board("2026-10-17","gen1","Brutal",[
  ("SPRINTER",5,"stat:speed",["Electrode","Jolteon","Dugtrio","Alakazam"],"Electrode, Jolteon, Dugtrio and Alakazam are among the fastest Pokemon from the original 151, each built around a blistering base Speed stat."),
  ("MASTERMIND",5,"stat:special-attack",["Alakazam","Gengar","Exeggutor","Jolteon"],"Alakazam, Gengar, Exeggutor and Jolteon all carry a formidable Special Attack stat, among the sharpest minds of the original 151."),
  ("FLASH-FIRE",4,"ability:flash-fire",["Growlithe","Ninetales","Ponyta"],"Growlithe, Ninetales and Ponyta can all have the Ability Flash Fire, which lets them shrug off a Fire-type hit completely and turn it into a power boost instead."),
  ("AMBER",1,"colour:yellow",["Ponyta","Exeggutor","Jolteon","Ninetales"],"Ponyta, Exeggutor, Jolteon and Ninetales are all predominantly yellow-coloured Pokemon."),
], exclude=["Flareon","Rapidash","Arcanine","Vulpix"])
board("2026-10-17","mixed","Brutal",[
  ("BLISTERING",5,"stat:speed",["Regieleki","Ninjask","Accelgor","Zeraora"],"Regieleki, Ninjask, Accelgor and Zeraora are among the fastest Pokemon ever recorded, each carrying an extraordinary base Speed stat."),
  ("SPECIAL",5,"stat:special-attack",["Xurkitree","Blacephalon","Zeraora"],"Xurkitree, Blacephalon and Zeraora all carry one of the highest Special Attack stats of their respective generations."),
  ("TOUGH-CLAWS",4,"ability:tough-claws",["Binacle","Perrserker"],"Binacle and Perrserker can both have the Ability Tough Claws, which boosts the power of any move that makes physical contact."),
  ("GOLDEN",1,"colour:yellow",["Regieleki","Ninjask","Zeraora","Raichu"],"Regieleki, Ninjask, Zeraora and Raichu are all predominantly yellow-coloured Pokemon."),
], exclude=["Barbaracle"])

# ===== 10-18 Sun : EVIL (gap fill) =====
board("2026-10-18","gen1","Evil",[
  ("VELOCITY",5,"stat:speed",["Mewtwo","Persian","Dodrio","Tauros"],"Mewtwo, Persian, Dodrio and Tauros are all built for speed, each carrying one of the sharpest base Speed stats among the original 151."),
  ("PRODIGY",5,"stat:special-attack",["Mewtwo","Zapdos","Moltres"],"Mewtwo, Zapdos and Moltres are three of the sharpest special attackers among the original 151, each carrying an exceptional Special Attack stat."),
  ("BASTION",4,"ability:sturdy",["Onix"],"Onix can have the Ability Sturdy, guaranteeing it survives any hit that would otherwise knock it out from full HP -- backed up by the single highest Defense stat of the original 151."),
  ("WATER-ABSORB",5,"ability:water-absorb",["Lapras","Vaporeon"],"Lapras and Vaporeon can both have the Ability Water Absorb, which heals them whenever they're struck by a Water-type move instead of taking damage."),
  ("FEATHERED",3,"arch:bird",["Dodrio","Zapdos","Moltres"],"Dodrio, Zapdos and Moltres are all birds at heart -- Dodrio a flightless three-headed ratite, Zapdos and Moltres legendary birds of thunder and flame."),
], exclude=["Geodude","Golem","Graveler","Magnemite","Magneton","Poliwag","Poliwhirl","Poliwrath","Articuno","Doduo","Farfetch'd","Fearow","Pidgeot","Pidgeotto","Pidgey","Spearow"])
board("2026-10-18","mixed","Evil",[
  ("SHADOW-TAG",5,"ability:shadow-tag",["Gothorita","Wobbuffet"],"Gothorita and Wobbuffet can both have the Ability Shadow Tag, which stops the opposing Pokemon from switching out or fleeing battle."),
  ("TRACE",5,"ability:trace",["Kirlia","Porygon2"],"Kirlia and Porygon2 can both have the Ability Trace, which lets them copy the Ability of the Pokemon they're facing."),
  ("GOOEY",4,"ability:gooey",["Wiglett","Wugtrio"],"Wiglett and Wugtrio can both have the Ability Gooey, which lowers the Speed of any attacker that makes physical contact with them."),
  ("GENIE",5,"myth:genie",["Landorus","Thundurus","Tornadus"],"Landorus, Thundurus and Tornadus are all genies from Unovan myth -- elemental spirits of the harvest, thunderstorms and violent winds respectively."),
  ("FIGURE",3,"arch:humanoid",["Gothorita","Kirlia"],"Gothorita and Kirlia are both built as upright, human-shaped figures -- Gothorita modelled on a gothic-lolita doll, Kirlia on a graceful ballet dancer."),
], exclude=["Gothita","Gothitelle","Wynaut","Gardevoir","Ralts","Goodra","Goomy","Sliggoo","Enamorus"])

# ===== 10-19 Mon : EASY (+28d window) =====
board("2026-10-19","gen1","Easy",[
  ("ELECTRIC",1,"type:electric",["Pikachu","Voltorb"],"Pikachu and Voltorb are both Electric-type Pokemon."),
  ("PSYCHIC",1,"type:psychic",["Drowzee","Mr. Mime"],"Drowzee and Mr. Mime are both Psychic-type Pokemon."),
  ("POISON",1,"type:poison",["Zubat","Ekans"],"Zubat and Ekans are both Poison-type Pokemon."),
  ("NORMAL",1,"type:normal",["Ditto","Kangaskhan"],"Ditto and Kangaskhan are both Normal-type Pokemon."),
  ("NOSE",2,"sprite:nose",["Diglett"],"Diglett's sprite is built entirely around its oversized, twitching pink nose poking up out of the ground."),
], exclude=["Pichu","Raichu","Electrode","Hypno","Golbat","Arbok","Dugtrio"])
board("2026-10-19","mixed","Easy",[
  ("GRASS",1,"type:grass",["Chikorita","Treecko"],"Chikorita and Treecko are both Grass-type Pokemon -- the grass starters of Johto and Hoenn."),
  ("FIGHTING",1,"type:fighting",["Machop","Riolu"],"Machop and Riolu are both Fighting-type Pokemon."),
  ("ICE",1,"type:ice",["Snorunt","Swinub"],"Snorunt and Swinub are both Ice-type Pokemon."),
  ("DARK",1,"type:dark",["Poochyena","Murkrow"],"Poochyena and Murkrow are both Dark-type Pokemon."),
  ("WEB",2,"sprite:web",["Spinarak"],"Spinarak's sprite carries a distinctive web-shaped pattern across its back and belly, matching its spider design."),
], exclude=["Bayleef","Meganium","Grovyle","Sceptile","Machoke","Machamp","Lucario","Glalie","Froslass","Piloswine","Mamoswine","Mightyena","Honchkrow","Ariados","Galvantula","Joltik"])

# ===== 10-20 Tue : MEDIUM (+28d window) =====
board("2026-10-20","gen1","Medium",[
  ("FIRE",1,"type:fire",["Magmar","Flareon","Charmeleon"],"Magmar, Flareon and Charmeleon are all Fire-type Pokémon."),
  ("BUG",1,"type:bug",["Caterpie","Weedle"],"Caterpie and Weedle are both Bug-type Pokémon."),
  ("BIRD",3,"arch:bird",["Farfetch'd","Spearow"],"Farfetch'd and Spearow are both birds at heart -- Farfetch'd a wild duck that carries a leek stalk everywhere it goes, Spearow a small, short-tempered bird of prey."),
  ("HORNS",2,"sprite:horn",["Nidoran♀","Nidoran♂"],"Nidoran♀ and Nidoran♂ both sport a small horn on their forehead in their sprite -- the poison barb that gives the entire Nidoran line its name."),
], exclude=["Doduo","Dodrio","Pidgey","Pidgeotto","Pidgeot","Fearow","Zapdos","Moltres","Articuno","Nidorina","Nidorino","Nidoking","Nidoqueen","Charmander","Charizard","Eevee","Vaporeon","Jolteon"])
board("2026-10-20","mixed","Medium",[
  ("ROCK",1,"type:rock",["Larvitar","Roggenrola"],"Larvitar and Roggenrola are both Rock-type Pokémon."),
  ("FLYING",1,"type:flying",["Rookidee","Noibat"],"Rookidee and Noibat are both Flying-type Pokémon."),
  ("FOX",3,"arch:fox",["Zorua","Nickit"],"Zorua and Nickit are both fox-based Pokémon -- Zorua a mischievous illusion-fox out of Unova, Nickit a sly, thieving fox styled after Galar's real red foxes."),
  ("HAMSTER",3,"arch:hamster",["Pawmi","Morpeko"],"Pawmi and Morpeko are both modelled on real hamsters -- small, round-cheeked rodents built for quick bursts of energy."),
  ("RUFF",2,"sprite:leaf-ruff",["Sprigatito"],"Sprigatito's sprite has a distinctive leafy ruff around its neck, one of its most recognisable details."),
], exclude=["Pupitar","Tyranitar","Roggenrola","Boldore","Gigalith","Bergmite","Corvisquire","Corviknight","Vullaby","Mandibuzz","Starly","Staravia","Staraptor","Zoroark","Thievul","Vulpix","Ninetales","Dedenne","Skwovet","Greedent","Bidoof","Bibarel","Floragato","Meowscarada"])

# ===== 10-21 Wed : CHALLENGING (+28d window) =====
board("2026-10-21","gen1","Challenging",[
  ("RED",1,"colour:red",["Charizard","Jynx","Magikarp"],"Charizard, Jynx and Magikarp are all predominantly red Pokémon."),
  ("WINGS",2,"sprite:wings",["Charizard","Venomoth"],"Look closely at the sprite and you'll spot it -- wings, on both Charizard and Venomoth."),
  ("BIPEDAL",3,"arch:humanoid",["Electabuzz","Hitmonlee","Jynx"],"Electabuzz, Hitmonlee and Jynx all stand and fight on two legs like a person, rather than moving like a typical animal."),
  ("SKULL",2,"sprite:skull-helmet",["Cubone"],"Cubone's entire design is built around the skull it wears as a helmet, mourning its lost parent."),
  ("PLANT",3,"arch:plant",["Tangela","Weepinbell"],"Tangela and Weepinbell are both modelled on plants -- Tangela a tangled mass of blue vines, Weepinbell a carnivorous pitcher plant."),
], exclude=["Seaking","Magmar","Gloom","Pidgeot","Machop","Vileplume","Oddish","Bellsprout","Exeggcute","Zubat","Golbat","Aerodactyl","Marowak","Scyther","Butterfree","Beedrill","Pidgeotto","Charmeleon","Ninetales","Golem","Zapdos","Moltres"])
board("2026-10-21","mixed","Challenging",[
  ("GHOST",1,"type:ghost",["Duskull","Drifloon","Spiritomb"],"Duskull, Drifloon and Spiritomb are all Ghost-type Pokémon."),
  ("BRANCHES",2,"sprite:coral-branches",["Corsola"],"Look closely at the sprite and you'll spot it -- Corsola's whole body is made of branching pink coral."),
  ("MUSTELID",4,"arch:mustelid",["Sneasel","Weavile"],"Sneasel and Weavile are both modelled on real mustelids -- sharp-clawed, weasel-like predators."),
  ("SQUIRREL",3,"arch:squirrel",["Pachirisu","Emolga"],"Pachirisu and Emolga are both modelled on real squirrels -- Pachirisu a chubby ground squirrel, Emolga a gliding flying squirrel."),
  ("FLYTRAP",3,"arch:flytrap",["Carnivine"],"Carnivine is modelled directly on a Venus flytrap, snapping its jaw-like leaves shut on prey."),
], exclude=["Chimecho","Yanmega","Misdreavus","Mismagius","Gastly","Haunter","Gengar","Rotom","Froslass","Sableye","Banette"])
