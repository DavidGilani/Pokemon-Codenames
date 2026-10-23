# Rescheduled boards 2026-08-22 .. 2026-09-06 (loaded by schedule_v2.py).
# Tier fixed by weekday: Mon Easy / Tue Medium / Wed Challenging / Thu Hard /
# Fri Hard / Sat Brutal / Sun Evil. Brutal/Evil pass the overlap gate
# (clue numbers sum >= 11, <= 1 single-tile clue).
#
# (2026-08-22 .. 2026-09-06 gen1/mixed boards removed here: long since live
# in Supabase and now outside the rolling anti-repetition window, so they
# were stale dead code that the verifier mistook for new, unverified boards.)

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

# ===== 10-12 Mon : EASY (rebuilt from QA -- old purple/pink colour board had
# clashing, ambiguous colour clues; replaced with a clean colour+type+sprite set) =====
board("2026-10-12","mixed","Easy",[
  ("GREEN",1,"colour:green",["Cacnea","Axew","Cradily"],"Cacnea, Axew and Cradily are all predominantly green -- a spiny green cactus, a green tusked dragon, and a green sea-lily fossil."),
  ("GRAY",1,"colour:gray",["Excadrill","Glalie"],"Excadrill and Glalie are both mainly grey -- Excadrill a steel-clawed mole, Glalie a floating grey ice-mask with a gaping jaw."),
  ("FIRE",1,"type:fire",["Delphox","Darumaka"],"Delphox and Darumaka are both Fire-types -- Delphox a fox mage wreathed in flame, Darumaka a fiery daruma doll."),
  ("PINCERS",2,"sprite:pincers",["Crawdaunt","Clauncher"],"Look closely at the sprites for the big pincer claws -- Crawdaunt's heavy crayfish claws and Clauncher's single oversized pistol-shrimp claw."),
], exclude=["Kingler","Krabby","Corphish","Clawitzer","Crabrawler","Crabominable","Klawf","Pinsir","Heracross","Crustle","Dwebble","Durant","Escavalier","Scyther","Scizor","Kabutops","Kabuto","Anorith","Armaldo","Gligar","Gliscor","Drapion","Skorupi","Mawile","Barbaracle","Binacle","Golisopod","Wimpod","Parasect","Paras","Fraxure","Haxorus","Cacturne","Lileep","Drilbur","Snorunt","Froslass","Fennekin","Braixen","Darmanitan","Corphish"])

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
  ("NIPPERS",3,"trait:pincers",["Paras","Kingler","Pinsir"],"Paras, Kingler and Pinsir all wield big pincer claws -- Paras a crab's little nippers, Kingler one oversized fiddler-crab claw, and Pinsir a pair of gripping horn-pincers."),
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
  ("YELLOW",1,"colour:yellow",["Ponyta","Exeggutor","Jolteon","Ninetales"],"Ponyta, Exeggutor, Jolteon and Ninetales are all predominantly yellow-coloured Pokemon."),
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
  ("MASTER-BALL",4,"lore:master-ball",["Mewtwo","Zapdos","Moltres"],"Mewtwo, Zapdos and Moltres are the prize legendaries of Kanto -- the Pokemon you'd save your single, never-fail Master Ball for."),
  ("STURDY",4,"ability:sturdy",["Onix"],"Onix can have the Ability Sturdy, guaranteeing it survives any hit that would otherwise knock it out from full HP -- backed up by the single highest Defense stat of the original 151."),
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
  ("WINGS",2,"sprite:wings",["Charizard","Venomoth","Venonat","Pinsir"],"Look closely at the sprite and you'll spot it -- wings, on both Charizard and Venomoth."),
  ("BIPEDAL",3,"arch:humanoid",["Electabuzz","Hitmonlee","Jynx"],"Electabuzz, Hitmonlee and Jynx all stand and fight on two legs like a person, rather than moving like a typical animal."),
  ("SKULL",2,"sprite:skull-helmet",["Cubone"],"Cubone's entire design is built around the skull it wears as a helmet, mourning its lost parent."),
  ("PLANT",3,"arch:plant",["Tangela","Weepinbell"],"Tangela and Weepinbell are both modelled on plants -- Tangela a tangled mass of blue vines, Weepinbell a carnivorous pitcher plant."),
], exclude=["Seaking","Magmar","Gloom","Pidgeot","Machop","Vileplume","Oddish","Bellsprout","Exeggcute","Zubat","Golbat","Aerodactyl","Marowak","Scyther","Butterfree","Beedrill","Pidgeotto","Charmeleon","Ninetales","Golem","Zapdos","Moltres"])
board("2026-10-21","mixed","Challenging",[
  ("FAIRY",1,"type:fairy",["Spritzee","Swirlix"],"Spritzee and Swirlix are the board's only Fairy-types -- a sweet-scented perfume bird and a cotton-candy pup."),
  ("RABBIT",3,"arch:rabbit",["Buneary","Lopunny"],"Buneary and its evolution Lopunny are rabbits -- Buneary with its tightly rolled ears, Lopunny with the long elegant ones it unrolls to fight."),
  ("TURTLE",3,"arch:turtle",["Torkoal","Tirtouga"],"Torkoal and Tirtouga are both turtles -- Torkoal a coal-burning tortoise, Tirtouga a prehistoric sea turtle revived from a fossil."),
  ("HORSE",3,"arch:horse",["Rapidash","Mudsdale"],"Rapidash and Mudsdale are both horses -- Rapidash a blazing unicorn-steed, Mudsdale a powerful heavy draft horse."),
  ("COGS",2,"sprite:gears",["Klink"],"Look closely at the sprite -- Klink is a pair of interlocking cogs that spin against each other to generate energy."),
], exclude=["Cutiefly","Ribombee","Comfey","Flabébé","Floette","Florges","Bunnelby","Diggersby","Azumarill","Audino","Nidoran♀","Nidoran♂","Nidorina","Nidorino","Raboot","Scorbunny","Cinderace","Wigglytuff","Whismur","Squirtle","Wartortle","Blastoise","Turtwig","Grotle","Torterra","Chewtle","Drednaw","Carracosta","Turtonator","Shuckle","Ponyta","Blitzle","Zebstrika","Mudbray","Keldeo","Glastrier","Spectrier","Klang","Klinklang"])

# ===== 10-22 Thu : HARD (mustelid board moved here from 10-21 per QA feedback) =====
board("2026-10-22","mixed","Hard",[
  ("MUSTELID",4,"arch:mustelid",["Sneasel","Weavile"],"Sneasel and its evolution Weavile are the board's two mustelids -- sleek, sharp-clawed members of the weasel family (Weavile even hunts in coordinated packs)."),
  ("CRUSTACEAN",4,"arch:crustacean",["Klawf","Clawitzer"],"Klawf and Clawitzer are crustaceans from different branches -- Klawf an ambush crab, Clawitzer a pistol shrimp whose oversized claw fires a blast of water."),
  ("BEETLE",3,"arch:beetle",["Heracross","Vikavolt"],"Heracross and Vikavolt are both beetles -- Heracross a horned Hercules beetle, Vikavolt a stag beetle whose jaws fire an electric railgun."),
  ("GATOR",3,"arch:crocodile",["Sandile","Fuecoco"],"Sandile and Fuecoco are both crocodiles -- Sandile a desert croc that ambushes from under the sand, Fuecoco a laid-back fire croc."),
  ("BLADE",2,"sprite:blade",["Aegislash"],"Look closely at the sprite -- Aegislash is a living sword, its body the blade and one arm a shield."),
], exclude=["Buizel","Dewott","Floatzel","Furret","Mienfoo","Mienshao","Oshawott","Samurott","Sentret","Sneasler","Zangoose","Barbaracle","Binacle","Clauncher","Corphish","Crabominable","Crabrawler","Crawdaunt","Crustle","Dwebble","Golisopod","Kabuto","Kabutops","Kingler","Krabby","Paras","Parasect","Remoraid","Shuckle","Wimpod","Grubbin","Karrablast","Ledian","Ledyba","Orbeetle","Pinsir","Rabsca","Rellor","Crocalor","Croconaw","Feraligatr","Krokorok","Krookodile","Skeledirge","Totodile","Baxcalibur","Bisharp","Ceruledge","Chien-Pao","Dartrix","Doublade","Gallade","Grovyle","Honedge","Kartana","Kingambit","Lurantis","Pawniard","Sceptile","Seviper","Skarmory","Virizion","Zacian"])

# ===== 10-31 Sat : BRUTAL (Halloween holiday board, holiday_boards.md) =====
board("2026-10-31","gen1","Brutal",[
  ("POISON",1,"type:poison",["Gengar","Zubat","Weezing","Arbok"],"Gengar, Zubat, Weezing and Arbok are every Poison-type Pokemon on this board -- a fittingly toxic, unsettling crew for Halloween night."),
  ("MYTH",5,"myth:legend",["Gengar","Drowzee","Jynx","Cubone","Marowak"],"Each carries a specific folklore or legend: Gengar's own name means 'doppelganger', a shadow-double said to bring death; Drowzee is based on the baku, a Japanese dream-eating spirit; Jynx blends an opera diva with the Yuki-onna snow spirit; and Cubone and Marowak both trace back to Lavender Town's grieving ghost-mother legend from the original games."),
  ("DECEPTION",4,"lore:mimicry",["Mr. Mime","Arbok"],"Both survive by faking something they're not -- Mr. Mime (the Barrier Pokemon) mimes invisible walls into being, while Arbok's hood bears a menacing false-face pattern that bluffs predators into backing off."),
  ("HUMAN-LIKE",5,"egg:humanlike",["Drowzee","Jynx","Mr. Mime"],"Drowzee, Jynx and Mr. Mime all belong to the Human-Like Egg Group -- the games' own classification for Pokemon built on a human or human-like silhouette."),
], exclude=["Haunter","Gastly","Golbat","Koffing","Ekans","Hypno","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Hitmonlee","Hitmonchan","Electabuzz","Magmar","Ditto","Voltorb","Electrode","Arcanine","Clefable","Clefairy","Dragonair","Golduck","Golem","Grimer","Gyarados","Lapras","Magikarp","Meowth","Moltres","Ninetales","Paras","Parasect","Vulpix","Zapdos"])
board("2026-10-31","mixed","Brutal",[  # QA 2026-10-09: reworked around a DECORATION clue (Pumpkaboo, Zubat, Chandelure, Ariados)
  ("GHOST",1,"type:ghost",["Banette","Pumpkaboo","Chandelure","Froslass","Mimikyu"],"Happy Halloween! Banette (a cursed doll), Pumpkaboo (a haunted pumpkin), Chandelure (a spirit-eating chandelier), Froslass (a snow-ghost) and Mimikyu (a lonely ghost in a Pikachu costume) are all Ghost-types."),
  ("DECORATION",4,"lore:decoration",["Pumpkaboo","Zubat","Chandelure","Ariados"],"Happy Halloween! Classic party decorations: Pumpkaboo is a carved pumpkin, Zubat a hanging bat, Chandelure a spooky candelabra and Ariados a spider spinning cobwebs."),
  ("OMEN",4,"lore:omen",["Absol","Murkrow"],"Both are explicitly tied to bad luck in their Pokedex lore: Absol is the 'Disaster Pokemon', wrongly blamed for the earthquakes and storms it merely senses coming, while Murkrow's crow-like look and cunning nature have long made trainers see it as a bird of ill omen."),
  ("INSOMNIA",5,"ability:insomnia",["Banette","Murkrow","Ariados"],"Banette, Murkrow and Ariados all share the Ability Insomnia, which stops them from ever falling asleep -- fitting, since Banette is too busy plotting revenge, Murkrow too mischievous, and Ariados too busy guarding its web."),
], exclude=["Yamask","Runerigus","Shuppet","Snorunt","Glalie","Phantump","Spinarak","Honchkrow","Capsakid","Delibird","Drowzee","Gourgeist","Hoothoot","Hypno","Noctowl","Pumpkaboo","Scovillain","Spidops","Tarountula","Terapagos","Venusaur","Charizard","Blastoise","Beedrill","Pidgeot","Alakazam","Slowbro","Gengar","Kangaskhan","Pinsir","Gyarados","Aerodactyl","Mewtwo","Ampharos","Steelix","Scizor","Heracross","Houndoom","Tyranitar","Sceptile","Blaziken","Swampert","Gardevoir","Sableye","Mawile","Aggron","Medicham","Manectric","Sharpedo","Camerupt","Altaria","Salamence","Metagross","Latias","Latios","Rayquaza","Lopunny","Gallade","Audino","Diancie","Garchomp","Lucario","Abomasnow"])

# ===== 4-week gap fill (nightly 2026-09-30): 10-22 .. 10-28 =====
def ex(*tags, extra=()):
    """Neutral-exclusion list: every species whose fact-bank record matches any tag (kind:value)."""
    out = set(extra)
    for nm, r in FACTS.items():
        for t in tags:
            k, _, v = t.partition(":")
            if (k == "arch" and v in r["arch"]) or (k == "sprite" and v in r["sprite"]) or \
               (k == "ability" and v in r["abilities"]) or (k == "role" and v in r.get("role", [])) or \
               (k == "type" and v in r["types"]) or (k == "trainer" and any(x.startswith(v) for x in r["trainer"])):
                out.add(nm)
    return sorted(out)

# ===== 10-22 Thu : HARD (gen1; mixed board already live) =====
board("2026-10-22","gen1","Hard",[
  ("SWIFT-SWIM",5,"ability:Swift Swim",["Omanyte","Goldeen","Psyduck","Poliwag"],"Omanyte, Goldeen, Psyduck and Poliwag all have the Ability Swift Swim, which doubles their Speed when it's raining."),
  ("INTIMIDATE",5,"ability:Intimidate",["Arcanine","Gyarados","Arbok"],"Arcanine, Gyarados and Arbok all have the Ability Intimidate, which lowers the Attack of every opposing Pokémon the moment they enter battle."),
  ("CLAM",3,"arch:clam",["Shellder"],"Shellder is a clam -- a bivalve whose two shells snap shut around a soft, tongue-like body."),
  ("PENDULUM",2,"sprite:pendulum",["Hypno"],"Hypno swings a pendulum in one hand to hypnotise foes -- look for it in the sprite."),
], exclude=ex("ability:Swift Swim","ability:Intimidate","arch:clam","arch:bivalve","arch:mollusc","arch:tapir","sprite:pendulum"))

# ===== 10-23 Fri : HARD =====
board("2026-10-23","gen1","Hard",[
  ("BRUNO",3,"trainer:Bruno",["Machamp","Hitmonchan"],"Machamp and Hitmonchan are on Elite Four member Bruno's fighting team (alongside Onix and Hitmonlee)."),
  ("MEGA",5,"role:mega",["Beedrill","Pinsir","Blastoise","Alakazam"],"Beedrill, Pinsir, Blastoise and Alakazam all have a Mega Evolution -- Mega Beedrill gains huge stingers, Mega Pinsir wings, Mega Blastoise a double cannon and Mega Alakazam a third spoon."),
  ("ERIKA",3,"trainer:Erika",["Victreebel","Vileplume"],"Victreebel and Vileplume are on Celadon Gym leader Erika's grass team (with Tangela, Gloom and Weepinbell)."),
  ("CNIDARIAN",4,"arch:cnidarian",["Tentacool"],"Tentacool is a cnidarian -- the group that includes jellyfish, sea anemones and corals -- with a glassy bell and stinging tentacles."),
], exclude=ex("trainer:Bruno","role:mega","trainer:Erika","arch:cnidarian","arch:jellyfish"))

# ===== 10-24 Sat : BRUTAL =====
board("2026-10-24","gen1","Brutal",[
  ("OBLIVIOUS",5,"ability:Oblivious",["Slowbro","Lickitung"],"Slowbro and Lickitung both have the Ability Oblivious -- they're so dopey and distracted that they're immune to Attract and Taunt."),
  ("LORELEI",3,"trainer:Lorelei",["Slowbro","Cloyster","Lapras"],"Lorelei, the Kanto Elite Four's ice specialist, sends out Slowbro, Cloyster and Lapras (plus Dewgong and Jynx)."),
  ("SHELL-ARMOR",5,"ability:Shell Armor",["Cloyster","Lapras","Omastar","Krabby"],"Cloyster, Lapras, Omastar and Krabby all have the Ability Shell Armor, whose hard shell makes them immune to critical hits."),
  ("RAPTOR",4,"arch:raptor",["Pidgeotto","Fearow"],"Pidgeotto and Fearow are raptors -- birds of prey built on the hawk and eagle, with sharp talons and a hunter's eye."),
  ("DOG",3,"arch:dog",["Growlithe"],"Growlithe is a loyal puppy, based on a real dog (with a hint of the Chinese guardian lion)."),
], exclude=ex("ability:Oblivious","trainer:Lorelei","ability:Shell Armor","arch:raptor","arch:dog","arch:canine","arch:fox",extra=["Slowpoke","Kingler","Shellder"]))

# ===== 10-25 Sun : EVIL =====
board("2026-10-25","gen1","Evil",[
  ("UNNERVE",5,"ability:Unnerve",["Aerodactyl","Mewtwo","Meowth"],"Aerodactyl, Mewtwo and Meowth all have the Ability Unnerve, which spooks the opposing side so much they can't eat their held Berries."),
  ("PRESSURE",5,"ability:Pressure",["Aerodactyl","Mewtwo","Articuno"],"Aerodactyl, Mewtwo and Articuno all have the Ability Pressure, which makes foes burn extra PP every time they attack."),
  ("INNER-FOCUS",5,"ability:Inner Focus",["Dragonite","Abra"],"Dragonite and Abra both have the Ability Inner Focus, which stops them from flinching, however hard they're hit."),
  ("ROYALTY",4,"lore:royalty",["Nidoking","Nidoqueen"],"Their names are royal titles -- Nidoking and Nidoqueen are the king and queen forms of the male and female Nidoran lines."),
  ("MOLE",3,"arch:mole",["Diglett"],"Diglett is a mole -- it lives underground and only ever pokes its head out of the soil."),
], exclude=ex("ability:Unnerve","ability:Pressure","ability:Inner Focus","arch:mole"))

# ===== 10-26 Mon : EASY =====
board("2026-10-26","gen1","Easy",[
  ("WATER",1,"type:water",["Squirtle","Seaking","Kingler","Vaporeon"],"Squirtle, Seaking, Kingler and Vaporeon are all Water-type Pokémon."),
  ("GROUND",1,"type:ground",["Sandshrew","Rhydon"],"Sandshrew and Rhydon are both Ground-type Pokémon."),
  ("STEEL",1,"type:steel",["Magnemite"],"Magnemite is a Steel-type Pokémon (Electric/Steel)."),
  ("MOUSE",3,"arch:mouse",["Raichu"],"Raichu is an electric mouse -- the evolved form of Pikachu."),
  ("MANTIS",3,"arch:mantis",["Scyther"],"Scyther is a praying mantis, with a pair of razor-sharp scythes for arms."),
], exclude=ex("arch:mouse","arch:mantis","arch:rat","arch:rodent"))

# ===== 10-27 Tue : MEDIUM =====
board("2026-10-27","gen1","Medium",[
  ("FIGHTING",1,"type:fighting",["Mankey","Machoke","Hitmonlee"],"Mankey, Machoke and Hitmonlee are all Fighting-type Pokémon."),
  ("PSYCHIC",1,"type:psychic",["Kadabra","Slowpoke","Starmie"],"Kadabra, Slowpoke and Starmie are all Psychic-type Pokémon (Slowpoke and Starmie pair it with Water)."),
  ("BULL",3,"arch:bull",["Tauros"],"Tauros is a bull -- it lowers its horned head and charges, lashing itself with its three tails."),
  ("PLATYPUS",4,"arch:platypus",["Golduck"],"Golduck is partly modelled on the platypus (with a dash of the Japanese water-spirit kappa) -- webbed limbs and a duck-bill face."),
  ("CAT",3,"arch:cat",["Persian"],"Persian is a cat -- a sleek, Siamese-style feline with a jewel on its forehead."),
], exclude=ex("arch:bull","arch:bovine","arch:platypus","arch:cat","arch:feline",extra=["Psyduck","Kingler","Miltank","Meowth"]))

# ===== 10-28 Wed : CHALLENGING =====
board("2026-10-28","gen1","Challenging",[
  ("FIRE",1,"type:fire",["Vulpix","Ponyta","Moltres"],"Vulpix, Ponyta and Moltres are all Fire-type Pokémon."),
  ("HEADS",2,"sprite:many-heads",["Dugtrio","Dodrio","Exeggutor"],"Dugtrio, Dodrio and Exeggutor are each a cluster of several heads -- count them on the sprites."),
  ("ARMADILLO",4,"arch:armadillo",["Sandslash"],"Sandslash is armadillo- and pangolin-like -- it rolls into a spiny ball of armour when threatened."),
  ("SNAKE",3,"arch:snake",["Ekans"],"Ekans is a snake -- its name is 'snake' spelled backwards."),
  ("FROG",3,"arch:frog",["Poliwhirl"],"Poliwhirl is a tadpole-turned-frog -- the swirl on its belly is its coiled intestines showing through its skin."),
], exclude=ex("sprite:three-heads","sprite:two-heads","arch:armadillo","arch:pangolin","arch:snake","arch:serpent","arch:tadpole","arch:frog",extra=["Doduo","Magneton","Weezing","Diglett","Sandshrew"]))

# ===== MIXED (all-gens) boards 10-23 .. 10-28 =====
# ===== 10-23 Fri : HARD =====
board("2026-10-23","mixed","Hard",[
  ("SHARK",3,"arch:shark",["Garchomp","Baxcalibur"],"Garchomp and Baxcalibur are sharks on land and ice -- Garchomp a 'land shark' with a dorsal fin it uses to fly at jet speed, Baxcalibur a frozen shark-dragon whose fin doubles as a blade."),
  ("CEPHALOPOD",4,"arch:cephalopod",["Malamar","Grapploct"],"Malamar and Grapploct are cephalopods -- the squid-and-octopus family. Malamar is an inverted-squid hypnotist, Grapploct an eight-armed octopus wrestler."),
  ("UNAWARE",5,"ability:Unaware",["Bidoof","Woobat","Pyukumuku"],"Bidoof, Woobat and Pyukumuku all have the Ability Unaware, which makes them ignore the opponent's stat boosts and drops when attacking or defending."),
  ("LION",3,"arch:lion",["Litleo","Solgaleo"],"Litleo and Solgaleo are lions -- Litleo a lion cub with a flame-red mane, Solgaleo a radiant, sun-powered lion of legend."),
], exclude=ex("arch:shark","arch:cephalopod","ability:Unaware","arch:lion",extra=["Inkay","Clobbopus","Octillery","Pyroar"]))

# ===== 10-24 Sat : BRUTAL =====
board("2026-10-24","mixed","Brutal",[
  ("HEALER",5,"ability:Healer",["Hatenna","Audino","Bellossom"],"Hatenna, Audino and Bellossom all have the Ability Healer, which gives them a chance to cure an ally's status condition every turn."),
  ("MAGIC-BOUNCE",5,"ability:Magic Bounce",["Hatenna","Natu","Espeon"],"Hatenna, Natu and Espeon all have the Ability Magic Bounce, which reflects most status moves straight back at whoever used them."),
  ("FELINE",3,"arch:feline",["Espeon","Shinx"],"Espeon and Shinx are both cats -- Espeon a sleek, sun-worshipping cat, Shinx a lion-cub-like kitten crackling with static."),
  ("MOLLUSC",4,"arch:mollusc",["Clamperl","Shellos","Shelmet"],"Clamperl, Shellos and Shelmet are all molluscs -- Clamperl a pearl-making clam, Shellos a sea slug, Shelmet a snail wearing a helmet-like shell."),
], exclude=ex("ability:Healer","ability:Magic Bounce","arch:feline","arch:cat","arch:mollusc",extra=["Slowking","Slowpoke","Slowbro","Shuckle","Gastrodon","Umbreon","Luxio","Luxray","Alomomola","Chansey","Blissey","Aromatisse","Hattrem","Hatterene","Xatu"]))

# ===== 10-25 Sun : EVIL =====
board("2026-10-25","mixed","Evil",[
  ("MUSKETEERS",4,"lore:musketeers",["Cobalion","Terrakion","Virizion"],"Cobalion, Terrakion and Virizion are three of the four Swords of Justice, the legendary musketeers of Unova (Keldeo is the fourth)."),
  ("JUSTIFIED",5,"ability:Justified",["Cobalion","Lucario","Gallade"],"Cobalion, Lucario and Gallade all have the Ability Justified, which raises their Attack whenever they're hit by a Dark-type move."),
  ("STEADFAST",5,"ability:Steadfast",["Lucario","Gallade","Rockruff"],"Lucario, Gallade and Rockruff all have the Ability Steadfast, which boosts their Speed every time they flinch."),
  ("WOLF",3,"arch:wolf",["Zacian","Zamazenta"],"Zacian and Zamazenta are the legendary wolves of Galar -- one wields a sword, the other a shield."),
  ("CETACEAN",4,"arch:cetacean",["Wailord"],"Wailord is a cetacean -- the whale family -- and the largest Pokémon ever found."),
], exclude=ex("lore:musketeers","ability:Justified","ability:Steadfast","arch:wolf","arch:cetacean",extra=["Keldeo","Lycanroc","Wailmer","Kyogre","Arcanine","Tyrogue","Hitmontop","Dubwool","Sirfetch'd","Finizen","Palafin"]))

# ===== 10-26 Mon : EASY =====
board("2026-10-26","mixed","Easy",[
  ("WATER",1,"type:water",["Froakie","Buizel","Popplio"],"Froakie, Buizel and Popplio are all Water-type Pokémon."),
  ("GROUND",1,"type:ground",["Trapinch","Drilbur"],"Trapinch and Drilbur are both Ground-type Pokémon."),
  ("STEEL",1,"type:steel",["Bronzor"],"Bronzor is a Steel-type Pokémon (Steel/Psychic)."),
  ("BEAR",3,"arch:bear",["Cubchoo","Teddiursa"],"Cubchoo and Teddiursa are both bear cubs -- Cubchoo a snotty polar-bear cub, Teddiursa a honey-loving teddy bear."),
  ("SHEEP",3,"arch:sheep",["Wooloo"],"Wooloo is a sheep -- a round bundle of wool that bounces about the Galar fields."),
], exclude=ex("arch:bear","arch:sheep",extra=["Ursaring","Beartic","Stufful","Bewear","Snorlax","Munchlax","Kubfu","Mareep","Flaaffy","Ampharos","Dubwool","Gogoat"]))

# ===== 10-27 Tue : MEDIUM =====
board("2026-10-27","mixed","Medium",[
  ("FIGHTING",1,"type:fighting",["Timburr","Pancham"],"Timburr and Pancham are both Fighting-type Pokémon."),
  ("PSYCHIC",1,"type:psychic",["Munna","Elgyem","Solosis"],"Munna, Elgyem and Solosis are all Psychic-type Pokémon."),
  ("MONKEY",3,"arch:monkey",["Aipom","Pansage"],"Aipom and Pansage are both monkeys -- Aipom a long-tailed monkey that grabs things with its hand-shaped tail, Pansage a leafy-crowned grass monkey."),
  ("ARACHNID",4,"arch:arachnid",["Joltik","Dewpider"],"Joltik and Dewpider are both arachnids -- eight-legged spider relatives (Joltik a tiny electric tick-spider, Dewpider a water spider in an air bubble)."),
], exclude=ex("arch:monkey","arch:primate","arch:arachnid","arch:spider"))

# ===== 10-28 Wed : CHALLENGING =====
board("2026-10-28","mixed","Challenging",[
  ("FIRE",1,"type:fire",["Litwick","Scorbunny"],"Litwick and Scorbunny are both Fire-type Pokémon."),
  ("UDDER",2,"sprite:udder",["Miltank"],"Look closely at the sprite -- Miltank, the Milk Cow Pokémon, has a pink udder."),
  ("DEER",3,"arch:deer",["Stantler","Sawsbuck"],"Stantler and Sawsbuck are both deer -- Stantler a stag whose twisting antlers warp the space around it, Sawsbuck a seasonal deer with a tree growing from its antlers."),
  ("HOOT",3,"arch:owl",["Hoothoot","Dartrix"],"Hoothoot and Dartrix are both owls -- Hoothoot a wide-eyed owl that keeps time, Dartrix a dapper archer-owl."),
  ("CHIROPTERAN",4,"arch:chiropteran",["Noivern","Crobat"],"Noivern and Crobat are chiropterans -- bats, the only mammals capable of true flight (Noivern a dragon-bat, Crobat a four-winged one)."),
], exclude=ex("arch:deer","arch:owl","arch:chiropteran","arch:bat","sprite:udder",extra=["Tauros","Bouffalant","Wooloo","Noibat","Zubat","Golbat","Woobat","Swoobat","Deerling","Wyrdeer","Xerneas"]))

# ===== 4-week gap fill (nightly 2026-10-01): 10-29 Thu HARD + 11-05 Thu HARD (Bonfire Night) =====
board("2026-10-29","gen1","Hard",[
  ("ARTHROPOD",4,"arch:arthropod",["Kabuto","Parasect","Venonat"],"Kabuto, Parasect and Venonat are all arthropods -- Kabuto a horseshoe-crab/trilobite fossil, Parasect a crab-like bug carrying a fungus, Venonat a fuzzy moth-and-fly bug."),
  ("MOON",4,"lore:moon",["Clefairy"],"Clefairy is the Moon Pokémon -- it evolves with a Moon Stone, is found on Mt. Moon, and its Pokédex entries say it dances in the light of a full moon."),
  ("AVIAN",3,"arch:bird",["Pidgey","Doduo"],"Pidgey and Doduo are both birds -- Pidgey a plain pigeon-sparrow, Doduo a two-headed ostrich-like runner."),
  ("HORN",2,"sprite:horn",["Nidorino","Dewgong","Rapidash"],"Nidorino has a sharp horn on its head, Dewgong a horn on its forehead, and Rapidash a single unicorn-like horn."),
], exclude=ex("arch:arthropod","arch:insect","arch:crab","arch:bird","arch:ratite","arch:trilobite","arch:fairy","sprite:horn","sprite:head-horn","sprite:nose-horn","sprite:horns",
              extra=["Clefable","Jigglypuff","Wigglytuff","Ponyta","Nidoking","Nidoqueen","Nidorina","Rhydon","Rhyhorn","Seaking","Goldeen","Pinsir","Tauros","Kangaskhan","Scyther","Butterfree",
                     "Fearow","Spearow","Pidgeotto","Pidgeot","Dodrio","Farfetch'd","Articuno","Zapdos","Moltres","Golbat","Beedrill","Weedle","Kakuna","Venomoth","Paras","Kingler","Krabby","Seel","Onix","Charmeleon","Electabuzz","Aerodactyl"]))
board("2026-10-29","mixed","Hard",[
  ("ECHINODERM",4,"arch:echinoderm",["Mareanie"],"Mareanie is based on a brittle star -- an echinoderm, the spiny-skinned sea group that also includes starfish and sea urchins."),
  ("SUCTION-CUPS",5,"ability:Suction Cups",["Inkay","Lileep","Cradily"],"Inkay, Lileep and Cradily all have the Ability Suction Cups, which stops them being forced out of battle by moves like Roar or Whirlwind."),
  ("PENGUIN",3,"arch:penguin",["Piplup","Eiscue"],"Piplup and Eiscue are both penguins -- Piplup a proud little emperor-penguin chick, Eiscue a penguin wearing a block of ice on its head."),
  ("MUSTACHE",2,"sprite:mustache",["Stoutland","Whiscash","Kricketune"],"Look at the sprites -- Kricketune has curling antennae like a handlebar moustache, Stoutland has a long, white, moustache-like fringe of fur, and Whiscash has long barbels that hang like a catfish's whiskers."),
], exclude=ex("arch:echinoderm","arch:penguin","arch:cephalopod","arch:octopus","ability:Suction Cups","sprite:mustache","sprite:mustache-fur",
              extra=["Pincurchin","Staryu","Starmie","Toxapex","Empoleon","Prinplup","Malamar","Octillery","Clobbopus","Grapploct","Barboach","Remoraid","Alakazam","Conkeldurr","Gurdurr","Kricketor","Gumshoos","Mabosstiff","Herdier","Lairon"]))

board("2026-11-05","gen1","Hard",[
  ("EXPLOSION",4,"move:explosion",["Electrode","Golem","Voltorb"],"Happy Bonfire Night! Voltorb, Electrode and Golem all go out with a bang -- they can learn Self-Destruct and Explosion, the biggest blasts in the game."),  # QA 2026-10-09: POKEBALL clue dropped (too easy)
  ("BIRD",3,"arch:bird",["Zapdos","Moltres","Articuno"],"The three legendary birds of Kanto -- Zapdos (lightning), Moltres (flame) and Articuno (frost) -- are all based on real-world birds."),
  ("STRIPES",2,"sprite:stripes",["Electabuzz","Arcanine"],"Look at the sprites -- Electabuzz has black tiger stripes across its body and arms, and Arcanine has bold black stripes on its orange coat."),
  ("CATTLE",3,"arch:bull",["Tauros"],"Tauros is a bull -- a charging wild bull that whips itself with its three tails."),
], exclude=ex("arch:bird","sprite:stripes","arch:bovine","arch:bull","sprite:ball-shape","sprite:three-tails",
              extra=["Cloyster","Weezing","Koffing","Exeggutor","Exeggcute","Geodude","Graveler","Magnemite","Magneton","Growlithe","Beedrill","Weedle","Pikachu","Raichu","Jolteon","Zubat","Persian","Meowth","Mankey","Primeape","Ponyta","Rapidash","Kangaskhan","Miltank","Charmander","Charmeleon","Charizard","Magmar","Flareon","Ninetales","Vulpix","Onix","Rhydon","Rhyhorn"]))
board("2026-11-05","mixed","Hard",[
  ("WHITE-SMOKE",5,"ability:White Smoke",["Centiskorch","Heatmor","Sizzlipede"],"Happy Bonfire Night! Centiskorch, Heatmor and Sizzlipede all have the Ability White Smoke, which stops other Pokémon lowering their stats -- named for the smoke that billows off a bonfire."),
  ("FIREFLY",4,"arch:firefly",["Volbeat","Illumise"],"Happy Bonfire Night! Volbeat and Illumise are both based on fireflies -- they glow and trace shapes in the night sky like sparklers."),
  ("SWINE",3,"arch:pig",["Tepig","Lechonk"],"Tepig and Lechonk are both pigs -- Tepig a fire-snorting piglet that sneezes embers, Lechonk a round, hungry hog."),
  ("TONGUE",2,"sprite:tongue",["Haunter","Shellder","Heatmor"],"Look at the sprites -- Haunter lolls a long tongue out of its grinning mouth, Shellder's big pink tongue pokes out between its shells, and Heatmor (an anteater) has a long tongue of flame."),  # QA 2026-10-09: Heatmor also ticks TONGUE
], exclude=ex("ability:White Smoke","arch:firefly","arch:pig","arch:boar","sprite:tongue",
              extra=["Pignite","Emboar","Oinkologne","Piloswine","Swinub","Mamoswine","Lickitung","Lickilicky","Gastly","Gengar","Chewtle","Drednaw","Cloyster","Croagunk","Toxicroak","Gulpin","Swalot","Frogadier","Carkol","Coalossal","Rolycoly","Torkoal","Litwick","Lampent","Chandelure","Lanturn","Chinchou","Sizzlipede","Magcargo","Slugma","Camerupt","Numel"]))

# ===== 4-week gap fill (nightly 2026-10-02): 10-30 Fri HARD =====
board("2026-10-30","gen1","Hard",[
  ("JELLYFISH",4,"arch:jellyfish",["Tentacool"],"Tentacool is based on a jellyfish -- a drifting, translucent sea jelly with long stinging tentacles."),
  ("AMMONITE",4,"arch:ammonite",["Omanyte"],"Omanyte is based on an ammonite -- an extinct spiral-shelled sea mollusc; it is revived from the Helix Fossil."),
  ("DRAGON-ISH",3,"arch:dragon",["Charizard","Gyarados"],"Charizard and Gyarados are both dragon-ish -- Charizard a fire-breathing winged dragon (but not a Dragon-type), Gyarados a rampaging sea dragon that evolves from a Magikarp."),  # QA 2026-10-09: owner asked DRAGON -> DRAGON-ISH
  ("FISH",3,"arch:fish",["Magikarp","Goldeen","Horsea"],"Magikarp, Goldeen and Horsea are all based on real-world fish -- Magikarp a flopping carp, Goldeen a graceful goldfish, Horsea a seahorse (a fish despite its looks)."),
  ("BEAK",2,"sprite:beak",["Spearow","Farfetch'd"],"Look at the sprites -- Spearow and Farfetch'd both have a prominent pointed beak."),
], exclude=ex("arch:jellyfish","arch:ammonite","arch:dragon","arch:fish","sprite:beak",
              extra=["Seadra","Seaking","Omastar","Kabuto","Kabutops","Dratini","Dragonair","Dragonite","Charmander","Charmeleon","Pidgeotto","Pidgeot","Fearow","Doduo","Dodrio","Lapras","Articuno","Zapdos","Moltres",
                     "Aerodactyl","Cloyster","Shellder","Staryu","Starmie","Tentacruel","Pidgey","Seadra","Psyduck","Golduck","Poliwag","Squirtle","Blastoise","Wartortle","Vaporeon","Slowpoke","Slowbro","Seel","Dewgong"]))
board("2026-10-30","mixed","Hard",[
  ("SCORPION",4,"arch:scorpion",["Skorupi","Gligar"],"Skorupi and Gligar are both based on scorpions -- Skorupi a buried scorpion with a poisonous tail, Gligar a flying scorpion that glides silently down to sting."),
  ("SAND-STREAM",5,"ability:Sand Stream",["Tyranitar","Hippowdon","Gigalith"],"Tyranitar, Hippowdon and Gigalith all have the Ability Sand Stream, which whips up a sandstorm the moment they enter battle."),
  ("GOAT",3,"arch:goat",["Skiddo"],"Skiddo is a goat -- a mountain goat with a leafy back that lets it grow plants."),
  ("ZEBRA",3,"arch:zebra",["Blitzle"],"Blitzle is a zebra -- a striped black-and-white zebra foal with a flickering electric mane."),
  ("HEADBAND",2,"sprite:headband",["Cinderace","Kubfu"],"Look at the sprites -- Cinderace wears a white bandage-like band across its face and Kubfu a white headband, like martial artists."),
], exclude=ex("arch:scorpion","ability:Sand Stream","arch:goat","arch:zebra","sprite:headband",
              extra=["Scorbunny","Raboot","Urshifu","Drapion","Gliscor","Gogoat","Zebstrika","Hippopotas","Pupitar","Larvitar","Talonflame","Combusken","Torchic","Rufflet","Staraptor","Fletchinder","Sandile","Sandshrew","Sandslash","Krokorok","Krookodile","Sandaconda","Silicobra","Palossand","Sandygast","Excadrill","Garchomp","Mudbray","Mudsdale","Stantler","Pidove","Unfezant","Honchkrow"]))

# ===== 4-week gap fill (nightly 2026-10-04): 11-01 Sun EVIL + 11-08 Sun EVIL (Diwali) =====
board("2026-11-01","gen1","Evil",[
  ("WEAK-ARMOR",5,"ability:Weak Armor",["Omastar","Kabutops","Onix"],"Omastar, Kabutops and Onix all have the Ability Weak Armor, which lowers their Defense but raises their Speed every time a physical move hits them."),
  ("CHLOROPHYLL",5,"ability:Chlorophyll",["Vileplume","Tangela","Exeggcute"],"Vileplume, Tangela and Exeggcute all have the Ability Chlorophyll, which doubles their Speed in harsh sunlight."),
  ("EFFECT-SPORE",5,"ability:Effect Spore",["Vileplume","Paras"],"Vileplume and Paras both have the Ability Effect Spore, which can poison, paralyse or put to sleep anything that makes contact with them."),
  ("MOLLUSC",4,"arch:mollusc",["Omastar","Cloyster"],"Omastar and Cloyster are both molluscs -- Omastar an extinct spiral-shelled ammonite revived from a fossil, Cloyster a spiked bivalve like a clam or oyster."),
  ("BEETLE",3,"arch:beetle",["Pinsir"],"Pinsir is a stag beetle -- its huge pincers are modelled on a stag beetle's jaws."),
], exclude=ex("ability:Weak Armor","ability:Chlorophyll","ability:Effect Spore","arch:mollusc","arch:beetle",
              extra=["Kabuto","Omanyte","Shellder","Parasect","Oddish","Gloom","Bellsprout","Weepinbell","Victreebel","Exeggutor","Venusaur","Bulbasaur","Ivysaur","Venonat","Scyther","Slowbro","Slowpoke","Krabby","Kingler","Aerodactyl","Geodude","Graveler","Golem","Rhyhorn","Rhydon"]))
board("2026-11-01","mixed","Evil",[
  ("FLOWER-VEIL",5,"ability:Flower Veil",["Flabébé","Comfey"],"Flabébé and Comfey both have the Ability Flower Veil, which protects Grass-type Pokémon on their side from having their stats lowered."),
  ("POISON-POINT",5,"ability:Poison Point",["Scolipede","Roserade","Qwilfish"],"Scolipede, Roserade and Qwilfish all have the Ability Poison Point, which can poison any Pokémon that touches them."),
  ("NATURAL-CURE",5,"ability:Natural Cure",["Roserade","Comfey","Pawmo"],"Roserade, Comfey and Pawmo all have the Ability Natural Cure, which heals any status condition the moment they switch out."),
  ("SIMIAN",4,"arch:primate",["Primeape","Slaking"],"Primeape and Slaking are both simians (apes and monkeys) -- Primeape a furious pig-monkey, Slaking a lazy gorilla-sloth that does nothing every other turn."),
  ("DUCK",3,"arch:duck",["Quaxly"],"Quaxly is a duck -- a cheerful duckling that practises its splashy dance moves."),
], exclude=ex("ability:Flower Veil","ability:Poison Point","ability:Natural Cure","arch:primate","arch:monkey","arch:duck",
              extra=["Floette","Florges","Quaxwell","Quaquaval","Venipede","Whirlipede","Budew","Roselia","Chansey","Blissey","Corsola","Mankey","Ambipom","Aipom","Simisage","Simisear","Simipour","Pansage","Pansear","Panpour","Oranguru","Passimian","Monferno","Infernape","Chimchar","Psyduck","Golduck","Ducklett","Swanna","Farfetch'd","Sirfetch'd","Slakoth","Vigoroth","Overqwil"]))

# ===== 4-week gap fill (nightly 2026-10-05): 11-02 Mon EASY =====
# ===== 4-week gap fill (nightly 2026-10-06): 11-03 Tue MEDIUM =====
board("2026-11-03","gen1","Medium",[
  ("WATER",1,"type:water",["Seel","Krabby","Lapras"],"Seel, Krabby and Lapras are all Water-types (Lapras pairs it with Ice) -- a seal, a crab and a gentle sea-plesiosaur."),
  ("PINK",1,"colour:pink",["Lickitung","Chansey","Ditto"],"Lickitung, Chansey and Ditto are all pink Pokémon -- a long-tongued lump, a nurse with an egg pouch and a blob that copies anything."),
  ("WINGS",2,"sprite:wings",["Golbat","Aerodactyl"],"Look closely at the sprites -- Golbat has broad bat wings and Aerodactyl has leathery pterosaur wings."),
  ("RHINO",3,"arch:rhino",["Rhyhorn"],"Rhyhorn is a rhinoceros -- a heavily armoured, horned charger that bulldozes through anything in its path."),
], exclude=ex("sprite:wings","arch:rhino","arch:pachyderm",extra=["Zubat","Rhydon","Pidgey","Pidgeotto","Pidgeot","Spearow","Fearow","Zapdos","Moltres","Articuno","Dragonite","Charizard","Butterfree","Beedrill","Venomoth","Scyther","Clefairy","Clefable","Dragonair","Gyarados","Mew","Jigglypuff","Wigglytuff","Slowpoke","Slowbro","Porygon","Mr. Mime","Jynx"]))
board("2026-11-03","mixed","Medium",[
  ("STEEL",1,"type:steel",["Aron","Pawniard"],"Aron and Pawniard are both Steel-types (Aron pairs it with Rock, Pawniard with Dark)."),
  ("STARTER",1,"group:starter",["Grookey","Fuecoco","Snivy"],"Grookey (Galar), Fuecoco (Paldea) and Snivy (Unova) are all starter Pokémon -- the first partners offered at the start of their games."),
  ("BELL",2,"sprite:bell",["Chimecho"],"Look closely at the sprite -- Chimecho is a little wind-chime bell, ringing a soft, soothing tone as it drifts about."),
  ("MAMMOTH",3,"arch:boar",["Piloswine"],"Piloswine is a woolly mammoth crossed with a boar -- a shaggy, tusked beast that hunts for food buried under the snow."),
  ("RAPTOR",4,"arch:raptor",["Talonflame","Braviary"],"Talonflame and Braviary are both raptors -- birds of prey, Talonflame a swift falcon that dive-bombs, Braviary a bold eagle that fights fearlessly."),
], exclude=ex("type:steel","role:starter","arch:raptor","arch:eagle","arch:falcon","arch:pig","arch:boar",extra=["Phanpy","Donphan","Cufant","Copperajah","Swinub","Lechonk","Oinkologne","Mamoswine","Rhydon","Rhyhorn","Rhyperior","Swablu","Altaria","Fletchling","Fletchinder","Staravia","Staraptor","Rufflet","Hawlucha","Pidgeot","Skarmory","Corviknight","Pelipper","Wingull","Hoothoot","Noctowl","Wooper","Xatu","Natu","Rotom","Jynx"]))

# ===== 4-week gap fill (nightly 2026-10-07): 11-04 Wed CHALLENGING =====
board("2026-11-04","gen1","Challenging",[
  ("GROUND",1,"type:ground",["Dugtrio","Sandslash"],"Dugtrio and Sandslash are both pure Ground-types -- a trio of burrowing moles and a spiny, clawed pangolin-armadillo."),
  ("WHISKERS",2,"sprite:whiskers",["Meowth","Nidoran♀","Raticate"],"Look closely at the sprites -- Meowth, Nidoran♀ and Raticate all sport prominent whiskers on their faces."),
  ("LARVA",3,"arch:caterpillar",["Caterpie","Weedle"],"Caterpie and Weedle are both bug larvae -- a green caterpillar that will become a butterfly and a hairy, stinger-tailed grub."),
  ("MERMAID",3,"arch:mermaid",["Vaporeon"],"Vaporeon is based on a mermaid -- its fin-tail, frilled collar and water-like body let it melt into the sea, as the Pokédex notes mermaid legends."),
  ("TAPIR",3,"arch:tapir",["Hypno"],"Hypno is based on the baku, the dream-eating tapir of Japanese folklore -- hence its long, trunk-like snout and its hypnotist's pendulum."),
], exclude=["Rattata","Persian","Nidorina","Nidorino","Nidoran♂","Magikarp","Kadabra","Alakazam","Raichu","Pikachu","Metapod","Butterfree","Kakuna","Beedrill","Weezing","Eevee","Jolteon","Flareon","Drowzee","Vaporeon","Seadra","Horsea","Lapras","Dewgong","Poliwhirl","Poliwrath","Sandshrew","Diglett","Rhydon","Rhyhorn","Geodude","Graveler","Golem","Onix","Cubone","Marowak","Nidoqueen","Nidoking","Slowpoke","Slowbro","Snorlax"])
board("2026-11-04","mixed","Challenging",[
  ("FIGHTING",1,"type:fighting",["Mienfoo","Sawk","Hitmontop","Makuhita"],"Mienfoo, Sawk, Hitmontop and Makuhita are all pure Fighting-types -- a martial-arts weasel, a karate-gi brawler, a spinning kicker and a sumo-style wrestler."),
  ("SLUG",3,"arch:slug",["Sliggoo","Shellos"],"Sliggoo and Shellos are both based on sea slugs -- Sliggoo a slimy, shell-antennaed dragon, Shellos a frilly nudibranch."),
  ("TIGER",3,"arch:tiger",["Incineroar"],"Incineroar is a tiger crossed with a heel pro-wrestler, with a flaming championship belt."),
  ("CICADA",4,"arch:cicada",["Ninjask"],"Ninjask is modelled on an adult cicada (crossed with a ninja) -- a buzzing insect that clings to trees and moves with blinding speed."),
  ("DONKEY",3,"arch:donkey",["Mudbray"],"Mudbray is a donkey -- a stubborn, hard-working beast that can haul loads many times its own weight."),
], exclude=["Goomy","Goodra","Slugma","Magcargo","Gastrodon","Litten","Torracat","Nincada","Shedinja","Mudsdale","Blitzle","Zebstrika","Ponyta","Rapidash","Hitmonlee","Hitmonchan","Machop","Machoke","Machamp","Timburr","Gurdurr","Conkeldurr","Throh","Pangoro","Riolu","Lucario","Meditite","Medicham","Hawlucha","Hariyama","Pancham","Tyrogue","Cranidos","Combusken","Blaziken","Mankey","Primeape","Scrafty","Scraggy","Passimian","Falinks","Kubfu","Urshifu","Obstagoon","Luxray","Shinx","Luxio","Liepard","Purrloin","Pyroar","Sprigatito","Raikou","Entei"])

# ===== 4-week gap fill (nightly 2026-10-09): 11-06 Fri HARD =====
board("2026-11-06","gen1","Hard",[
  ("GIOVANNI",3,"trainer:Giovanni",["Persian","Nidoking","Nidoqueen","Rhydon"],"Persian, Nidoking, Nidoqueen and Rhydon are all Pokémon used by Giovanni, the Team Rocket boss and Viridian City Gym leader."),  # QA 2026-10-09: LIMBER removed (no abilities in Gen I); Hitmonlee tile -> Nidoqueen
  ("TRILOBITE",4,"arch:trilobite",["Kabuto"],"Kabuto is based on a trilobite (with a touch of horseshoe crab) -- an extinct armoured sea arthropod, revived from the Dome Fossil."),
  ("HORN",2,"sprite:horn",["Nidoking","Rhydon","Rapidash"],"Look at the sprites -- Nidoking has a sharp horn on its head, Rhydon a drill-like horn on its snout, and Rapidash a single unicorn-like horn."),
  ("PLANT",3,"arch:plant",["Weepinbell","Exeggutor"],"Weepinbell and Exeggutor are both based on plants -- Weepinbell on a pitcher plant, Exeggutor on a tall palm tree."),
  ("LIZARD",3,"arch:lizard",["Charmander"],"Charmander is a lizard -- the Lizard Pokémon, a salamander-like reptile whose tail flame shows its health."),
], exclude=ex("arch:plant","arch:lizard","arch:trilobite","arch:arthropod","sprite:horn","sprite:head-horn","sprite:nose-horn","sprite:horns","ability:Limber","arch:cat","arch:feline",
              extra=["Charmeleon","Charizard","Slowpoke","Slowbro","Gyarados","Dragonair","Machop","Machoke","Machamp","Primeape","Meowth","Kabutops","Omanyte","Omastar","Tauros","Pinsir","Nidorino","Nidorina","Nidoqueen","Rhyhorn","Seaking","Dewgong","Ponyta","Exeggcute","Tangela","Oddish","Bellsprout","Victreebel","Gloom","Vileplume","Bulbasaur","Ivysaur","Venusaur","Ditto","Hitmonchan","Scyther","Ninetales","Vulpix","Growlithe","Arcanine","Lickitung","Snorlax"]))
board("2026-11-06","mixed","Hard",[
  ("SOLID-ROCK",5,"ability:Solid Rock",["Camerupt","Rhyperior","Carracosta"],"Camerupt, Rhyperior and Carracosta all have the Ability Solid Rock, which cuts the damage they take from super-effective moves."),
  ("PROBOSCIDEAN",4,"arch:elephant",["Donphan","Copperajah"],"Donphan and Copperajah are proboscideans -- the elephant order: Donphan an armoured Indian elephant that rolls like a tyre, Copperajah a big rusty working elephant."),
  ("RAVEN",3,"arch:corvid",["Honchkrow","Corviknight"],"Honchkrow and Corviknight are corvids -- Honchkrow a boss-like crow/raven, Corviknight an armoured raven."),
  ("SPIDER",3,"arch:spider",["Galvantula","Araquanid"],"Galvantula and Araquanid are spiders -- Galvantula an electrified spinner, Araquanid a water spider carrying an air bubble like a diving bell."),
], exclude=ex("arch:corvid","arch:elephant","arch:spider","arch:arachnid","arch:crow","arch:mammoth","ability:Solid Rock",
              extra=["Corvisquire","Rookidee","Murkrow","Phanpy","Cufant","Joltik","Ariados","Spinarak","Tarountula","Spidops","Dewpider","Tirtouga","Numel","Rhyhorn","Rhydon","Mamoswine","Piloswine","Swinub","Mudsdale","Hippowdon","Hippopotas","Skarmory","Talonflame","Braviary","Aegislash"]))

# ===== NIGHTLY 2026-10-11: QA rework (11-02 variety, 11-08 Diwali) + gap fill (11-07) + Friday-13th (11-13) =====
LEG=[n for n,r in FACTS.items() if r.get("legendary") or r.get("mythical") or any("Paradox" in x or "Ultra Beast" in x or "Treasures" in x or "Tapu" in x or "guardian" in x or "beast trio" in x for x in (r.get("nickname") or [])+(r.get("mythology") or []))]

# 11-02 Mon EASY -- QA: "needs more variety, can't be all types" -> types + a colour + real animals
board("2026-11-02","gen1","Easy",[
  ("ELECTRIC",1,"type:electric",["Magnemite","Jolteon"],"Magnemite and Jolteon are both Electric-types -- a floating magnet-ball and the sparkiest Eevee evolution."),
  ("PURPLE",1,"colour:purple",["Rattata","Gastly"],"Rattata and Gastly are both purple Pokémon -- a pushy little rat and a floating cloud of gas."),
  ("GRASS",1,"type:grass",["Oddish","Bellsprout","Ivysaur"],"Oddish, Bellsprout and Ivysaur are all Grass-types -- a weed, a sapling and a flower-budded dino-toad."),
  ("MARSUPIAL",3,"arch:marsupial",["Kangaskhan"],"Kangaskhan is a marsupial (a kangaroo), carrying its baby in a belly pouch."),
  ("WASP",3,"arch:wasp",["Beedrill"],"Beedrill is a wasp, with a stinger on each forearm and one on its tail."),
], exclude=ex("type:electric","type:grass","arch:marsupial","arch:wasp",
              extra=["Pikachu","Raichu","Eevee","Magneton","Voltorb","Electrode","Electabuzz","Zapdos","Vaporeon","Flareon","Gloom","Vileplume","Weepinbell","Victreebel","Tangela","Exeggcute","Exeggutor","Parasect","Ekans","Arbok","Haunter","Gengar","Koffing","Weezing","Grimer","Muk","Zubat","Golbat","Raticate","Nidoran♂","Nidorino","Nidoking","Tentacool","Tentacruel","Ditto","Venonat","Venomoth","Kakuna","Weedle","Metapod","Caterpie","Butterfree","Scyther","Pinsir"]))
board("2026-11-02","mixed","Easy",[
  ("PURPLE",1,"colour:purple",["Drapion","Mismagius","Toxtricity"],"Drapion, Mismagius and Toxtricity are all purple Pokémon -- a scorpion-ogre, a witchy ghost and a punk-rock lizard."),
  ("LEGENDARY",1,"group:legendary",["Lugia","Groudon"],"Lugia and Groudon are both legendary Pokémon -- the guardian of the seas and the continent-shaping titan."),
  ("ICE",1,"type:ice",["Vanillite","Bergmite"],"Vanillite and Bergmite are both pure Ice-types -- an ice-cream cone and a block of ice."),
  ("MOTH",3,"arch:moth",["Volcarona","Dustox"],"Volcarona and Dustox are both moths -- a fiery sun-moth and a poisonous night-moth."),
], exclude=ex("type:ice","arch:moth",
              extra=LEG+["Vanilish","Vanilluxe","Cubchoo","Beartic","Cryogonal","Beautifly","Butterfree","Venomoth","Mothim","Wormadam","Frosmoth","Ninjask","Masquerain","Vivillon","Sylveon","Glaceon","Crobat","Aipom","Sableye","Gastrodon","Skuntank","Stunky","Spiritomb"]))

# 11-07 Sat BRUTAL -- gap fill (Brutal: sum>=11, <=1 single, exactly 3 Cat4-5)
board("2026-11-07","gen1","Brutal",[
  ("SAFFRON",4,"trainer:Sabrina",["Kadabra","Mr. Mime","Venomoth"],"Kadabra, Mr. Mime and Venomoth are all on Saffron City Gym leader Sabrina's psychic team (Alakazam completes it, but isn't here)."),
  ("PSYCHIC",1,"type:psychic",["Kadabra","Mr. Mime","Jynx"],"Kadabra, Mr. Mime and Jynx are all Psychic-types -- a spoon-bender, a pantomime and an ice-queen opera singer."),
  ("DEFENSE",5,"stat:defense",["Cloyster","Onix","Omastar"],"Cloyster (180), Onix (160) and Omastar (125) have some of the highest base Defense stats in Gen I -- only Golem (130) joins them, and it isn't here."),
  ("BLAINE",4,"trainer:Blaine",["Growlithe","Magmar"],"Growlithe and Magmar both fight for Cinnabar Island Gym leader Blaine's fire team (with Ponyta, Rapidash and Arcanine)."),
], exclude=ex("trainer:Sabrina","trainer:Blaine","type:psychic",
              extra=["Alakazam","Abra","Golem","Graveler","Geodude","Rhydon","Kingler","Marowak","Sandslash","Slowbro","Slowpoke","Weezing","Tangela","Kabutops","Kabuto","Omanyte","Shellder","Steelix","Ponyta","Rapidash","Arcanine","Vulpix","Ninetales","Flareon","Charmander","Charmeleon","Charizard","Moltres","Magikarp","Exeggcute","Exeggutor","Venonat","Mewtwo","Mew","Hypno","Drowzee"]))
board("2026-11-07","mixed","Brutal",[
  ("CYNTHIA",4,"trainer:Cynthia",["Spiritomb","Lucario","Milotic"],"Spiritomb, Lucario and Milotic are all on Sinnoh Champion Cynthia's team (with Garchomp, Roserade and Gastrodon)."),
  ("DARK",1,"type:dark",["Spiritomb","Houndoom"],"Spiritomb (Ghost/Dark) and Houndoom (Dark/Fire) are both part Dark-type."),
  ("FIRE",1,"type:fire",["Houndoom","Torkoal"],"Houndoom (Dark/Fire) and Torkoal (pure Fire) are both Fire-types -- a hellhound and a coal-burning tortoise."),
  ("MOLD-BREAKER",5,"ability:Mold Breaker",["Excadrill","Fraxure"],"Excadrill and Fraxure both have the Ability Mold Breaker, which lets their moves ignore abilities like Levitate or Sturdy."),
  ("CRUSTACEAN",4,"arch:crustacean",["Dwebble","Clauncher"],"Dwebble and Clauncher are both crustaceans -- a rock-lugging hermit-style crab and a snapping-shrimp."),
], exclude=ex("trainer:Cynthia","type:dark","type:fire","ability:Mold Breaker","arch:crustacean","arch:crab","arch:lobster",
              extra=["Garchomp","Roserade","Gastrodon","Riolu","Haxorus","Axew","Drilbur","Crustle","Clawitzer","Houndour","Milotic","Feebas","Tyranitar","Anorith","Armaldo","Kabuto","Kabutops","Omanyte","Omastar","Lileep","Cradily","Shuckle","Dwebble","Binacle","Barbaracle","Skrelp","Dragalge"]))

# 11-08 Sun EVIL -- QA: Diwali theme (no Moxie/Swarm); wealth, cleanliness, lights, Ganesh
board("2026-11-08","gen1","Evil",[
  ("RAMAYANA",5,"myth:ramayana",["Mankey"],"Happy Diwali! Mankey is a monkey -- like Hanuman and his Vanara army in the Ramayana, who helped Rama rescue Sita, the epic Diwali celebrates (Rama's return home). Primeape, its evolution, isn't here."),
  ("FLYING",1,"type:flying",["Pidgeot","Fearow","Gyarados","Charizard"],"Pidgeot, Fearow, Gyarados and Charizard are all part Flying-type -- two soaring birds, a sea serpent that takes to the air and a fire-breathing dragon."),
  ("NAGA",5,"myth:naga",["Arbok","Dragonair","Gyarados"],"Arbok, Dragonair and Gyarados are all serpent beings in the vein of the Nagas of Hindu myth -- divine cobras and snake-spirits, like Shesha, the serpent Vishnu rests upon."),
  ("FORTUNE",4,"lore:koi",["Magikarp","Goldeen"],"Happy Diwali! A carp and a goldfish -- koi-style fish are symbols of wealth, good fortune and perseverance, the blessings of Lakshmi that Diwali invites in."),
  ("LANCE",4,"trainer:Lance",["Dragonair","Gyarados","Charizard"],"Dragonair, Gyarados and Charizard are all on Lance's team, the Dragon-master Elite Four member and Champion (Dragonite and Aerodactyl join them, but aren't here)."),
], exclude=ex("type:flying","trainer:Lance","arch:monkey","arch:primate","arch:cobra","arch:fish","arch:carp","arch:serpent",
              extra=["Primeape","Dragonite","Dratini","Seaking","Horsea","Seadra","Machop","Machoke","Machamp","Ekans","Onix","Zubat","Golbat","Doduo","Dodrio","Farfetch'd","Aerodactyl","Spearow","Pidgey","Pidgeotto","Scyther","Butterfree","Moltres","Zapdos","Articuno","Gengar","Hitmonlee","Hitmonchan","Poliwag","Poliwrath"]))
board("2026-11-08","mixed","Evil",[
  ("ILLUMINATE",5,"ability:Illuminate",["Staryu","Chinchou","Watchog"],"Happy Diwali, the festival of lights! Staryu, Chinchou and Watchog all have the Ability Illuminate, which makes them glow and raises the chance of meeting wild Pokémon."),
  ("JEWELS",4,"arch:gem",["Staryu","Carbink","Sableye"],"Wealth and treasure are part of Diwali's Lakshmi blessings -- Staryu's glowing core-gem, Carbink's jewel body and Sableye's gem eyes (it feeds on gems) are all precious stones."),
  ("LAUNDRY",4,"lore:appliance",["Rotom"],"Cleanliness is a Diwali tradition -- homes are spring-cleaned before the festival. Rotom possesses household appliances -- Wash Rotom takes over a washing machine."),
  ("GANESH",5,"myth:ganesh",["Phanpy","Cufant"],"Ganesh, the elephant-headed god, is honoured alongside Lakshmi at Diwali. Phanpy and Cufant are both elephants."),
  ("NORMAL",1,"type:normal",["Watchog","Cinccino"],"Watchog and Cinccino are both pure Normal-types -- a meerkat lookout and a chinchilla with a fur stole."),
], exclude=ex("ability:Illuminate","arch:gem","type:normal","arch:pachyderm","arch:elephant",
              extra=["Starmie","Lanturn","Volbeat","Illumise","Morelull","Shiinotic","Diancie","Minior","Terapagos","Nihilego","Gimmighoul","Gholdengo","Minccino","Donphan","Copperajah","Mamoswine","Swinub","Piloswine","Mimikyu","Jynx","Mr. Mime","Mr. Rime","Corsola","Shuckle","Dwebble","Crustle","Rolycoly","Carkol","Coalossal","Stonjourner","Probopass","Nosepass"]))

# 11-13 Fri HARD -- Friday the 13th (superstition)
board("2026-11-13","gen1","Hard",[  # QA 2026-10-11: THIRTEEN (dex numbers) too hard -> reworked
  ("GROUND",1,"type:ground",["Diglett","Sandshrew","Cubone"],"Diglett, Sandshrew and Cubone are the only Ground-types on the board -- a mole, an armadillo and an orphan wearing its mother's skull, all at home in the dirt."),
  ("RABBIT",3,"arch:rabbit",["Nidoran♀","Nidorino"],"Nidoran♀ and Nidorino are rabbit-like -- long ears and a hop; a rabbit's foot is a classic lucky charm."),
  ("PINK",2,"colour:pink",["Chansey","Porygon"],"Look at the sprites -- Chansey is a round pink blob and Porygon is built from pink and blue polygons; nothing else on this board is pink."),
  ("LARVA",4,"arch:caterpillar",["Weedle"],"Weedle is the Hairy Bug Pokémon -- a larva (a caterpillar) that spends its days munching leaves before spinning a cocoon as Kakuna."),
  ("PLESIOSAUR",4,"arch:plesiosaur",["Lapras"],"Lapras's long neck, flippers and shell echo a plesiosaur -- the prehistoric sea reptile behind the Loch Ness Monster legend that inspired it."),
], exclude=ex("arch:rabbit","arch:mole","arch:armadillo","arch:pangolin",
              extra=["Gyarados","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Omanyte","Omastar","Marowak","Kakuna","Beedrill","Nidorina","Nidoran♂","Nidoqueen","Nidoking","Dugtrio","Sandslash","Haunter","Gengar","Gastly"]))
board("2026-11-13","mixed","Hard",[
  ("BLACK-CAT",3,"arch:cat",["Purrloin","Liepard"],"Happy Friday the 13th! Purrloin and Liepard are sleek, mischievous black-and-purple cats -- the classic unlucky omen when one crosses your path."),
  ("SALT",5,"myth:salt",["Garganacl"],"Spilling salt is bad luck, so you throw a pinch over your shoulder. Garganacl is the Salt Pokémon, a rock-salt giant (Nacli and Naclstack, its pre-evolutions, aren't here)."),
  ("MIRROR",4,"lore:mirror",["Bronzor","Wobbuffet"],"Breaking a mirror means seven years' bad luck. Bronzor is modelled on an ancient bronze mirror, and Wobbuffet's signature move is Mirror Coat, reflecting special attacks back."),
  ("LUCKY",3,"group:lucky",["Togepi"],"Togepi is the Spike Ball Pokémon said to bring happiness and good luck to those who are kind to it -- the opposite of Friday the 13th."),
  ("RABBIT",3,"arch:rabbit",["Scorbunny","Bunnelby","Lopunny"],"Scorbunny, Bunnelby and Lopunny are all rabbits -- and a rabbit's foot is a classic lucky charm."),
], exclude=ex("arch:cat","arch:feline","arch:rabbit","arch:hare",
              extra=["Meowth","Persian","Espurr","Meowstic","Skitty","Delcatty","Litten","Torracat","Incineroar","Nacli","Naclstack","Bronzong","Mime Jr.","Mr. Mime","Ledyba","Ledian","Buneary","Raboot","Cinderace","Diggersby","Umbreon","Absol","Murkrow","Honchkrow","Sneasel","Weavile","Shuppet","Banette","Yamask","Cofagrigus","Wynaut","Sudowoodo","Lunatone","Solrock","Chansey","Blissey","Togetic","Togekiss","Happiny","Cleffa","Pichu","Jirachi","Manaphy","Shaymin"]))

# ===== 4-week gap fill (nightly 2026-10-12): 11-09 Mon EASY =====
board("2026-11-09","gen1","Easy",[
  ("BUG",1,"type:bug",["Butterfree","Scyther"],"Butterfree and Scyther are both Bug-types -- a big-winged butterfly and a razor-armed mantis."),
  ("ROCK",1,"type:rock",["Geodude","Aerodactyl"],"Geodude and Aerodactyl are both Rock-types -- a floating boulder with arms and a fossil sky-hunter."),
  ("POISON",1,"type:poison",["Ekans","Tentacool","Nidoran♂"],"Ekans, Tentacool and Nidoran♂ are every Poison-type on the board -- a venomous snake, a stinging jellyfish and a spiky little poison-barb."),
  ("OSTRICH",3,"arch:ratite",["Doduo"],"Doduo is an ostrich (or emu) -- a two-headed flightless bird that sprints across the plains on powerful legs."),
  ("SEAL",3,"arch:pinniped",["Seel"],"Seel is a seal -- a sleek, white-furred pinniped with a little horn that dives into icy seas."),
], exclude=ex("type:bug","type:rock","type:poison","arch:ratite","arch:pinniped","arch:bird",
              extra=["Dodrio","Dewgong","Seaking","Psyduck","Slowbro","Cloyster","Omanyte","Omastar","Kabuto","Kabutops","Caterpie","Metapod","Kakuna","Beedrill","Pinsir","Paras","Parasect","Venonat","Venomoth","Onix","Nidoking","Nidoqueen","Arbok","Tentacruel","Grimer","Muk","Koffing","Weezing","Zubat","Golbat"]))
board("2026-11-09","mixed","Easy",[
  ("DRAGON",1,"type:dragon",["Axew","Gible"],"Axew and Gible are both Dragon-types -- a tusk-sharpening hatchling and a land-shark that nests in caves."),
  ("FAIRY",1,"type:fairy",["Mawile","Togekiss"],"Mawile and Togekiss are both Fairy-types -- a deceiver with a hidden jaw and the Jubilee Pokémon that brings peace."),
  ("POISON",1,"type:poison",["Gulpin","Skrelp","Croagunk"],"Gulpin, Skrelp and Croagunk are every Poison-type on the board -- a stomach with legs, a sludgy seaweed seahorse and a croaking poison-frog."),
  ("FOX",3,"arch:fox",["Fennekin"],"Fennekin is a fox -- a fire-fox starter with big ears that it uses to vent heat."),
  ("LION",3,"arch:lion",["Litleo"],"Litleo is a lion cub -- a small fire-lion with a fluffy flaming mane that grows into Pyroar."),
], exclude=ex("type:dragon","type:fairy","type:poison","arch:dragon","arch:fox","arch:lion","arch:canine",
              extra=["Sylveon","Clefairy","Clefable","Togepi","Togetic","Mimikyu","Wooper","Quagsire","Carvanha","Sharpedo","Dratini","Dragonair","Dragonite","Fraxure","Haxorus","Garchomp","Gabite","Krookodile","Pyroar","Braixen","Delphox","Vulpix","Ninetales","Zorua","Zoroark","Shinx","Luxio","Luxray","Meowth","Persian","Skitty"]))

# ===== 4-week gap fill (nightly 2026-10-13): 11-10 Tue MEDIUM =====
board("2026-11-10","gen1","Medium",[
  ("ELECTRIC",1,"type:electric",["Pikachu","Magnemite"],"Pikachu and Magnemite are the only Electric-types among the blues -- the famous mouse and a floating magnet-ball."),
  ("GRASS",1,"type:grass",["Bulbasaur","Tangela","Exeggcute","Oddish"],"Bulbasaur, Tangela, Exeggcute and Oddish are all Grass-types (some paired with Poison or Psychic) -- a seed-bulb starter, a tangle of blue vines, a clutch of six eggs and a weed-bulb."),
  ("COCOON",2,"sprite:cocoon",["Metapod"],"Look at the sprite -- Metapod is a hard green cocoon, a caterpillar mid-way through turning into a butterfly."),
  ("VAMPIRE",3,"lore:vampire",["Golbat"],"Golbat drinks the blood of sleeping people and animals, and is a bat -- just like the vampire of legend."),
  ("TURTLE",3,"arch:turtle",["Blastoise"],"Blastoise is a giant turtle -- a heavy shell with water cannons poking out of it."),
], exclude=ex("type:electric","type:grass","arch:dog","sprite:cocoon","arch:bat","arch:turtle",
              extra=["Squirtle","Wartortle","Weepinbell","Exeggutor","Raichu","Magneton","Voltorb","Electrode","Electabuzz","Jolteon","Zapdos","Ivysaur","Venusaur","Gloom","Vileplume","Bellsprout","Victreebel","Exeggcute","Tangela","Paras","Parasect","Kakuna","Caterpie","Butterfree","Pinsir","Zubat","Arcanine","Vulpix","Ninetales","Eevee","Meowth","Persian","Pidgeot","Dragonite","Charizard","Aerodactyl","Venomoth","Weedle","Beedrill","Flareon","Vaporeon"]))
board("2026-11-10","mixed","Medium",[
  ("GHOST",1,"type:ghost",["Yamask","Drifloon","Sinistea"],"Yamask, Drifloon and Sinistea are all Ghost-types (Drifloon pairs it with Flying) -- a mask-clutching spirit, a balloon of souls and a haunted teacup."),
  ("ICE",1,"type:ice",["Cryogonal","Snorunt","Delibird"],"Cryogonal, Snorunt and Delibird are all Ice-types -- a drifting snowflake crystal, a snow-cone-hatted spirit and a gift-carrying penguin-like bird."),
  ("BEAVER",3,"arch:beaver",["Bidoof"],"Bidoof is a beaver -- a plump, buck-toothed gnawer that fells trees with its sturdy incisors."),
  ("SQUIRREL",3,"arch:squirrel",["Pachirisu"],"Pachirisu is a squirrel -- a chubby, bushy-tailed Electric-type that stores berries in its fluffy tail."),
  ("FLIPPERS",2,"sprite:flippers",["Palafin"],"Look at the sprite -- Palafin's Zero Form has two broad flippers on its sides, like a dolphin's."),
], exclude=ex("type:ghost","type:ice","arch:beaver","arch:squirrel","arch:dolphin","sprite:flippers",
              extra=["Piplup","Prinplup","Empoleon","Seel","Dewgong","Lapras","Spheal","Sealeo","Walrein","Popplio","Brionne","Primarina","Finneon","Lumineon","Wailord","Kingdra","Shuppet","Banette","Misdreavus","Mismagius","Phantump","Trevenant","Pumpkaboo","Gourgeist","Mimikyu","Litwick","Lampent","Chandelure","Froslass","Dusclops","Dusknoir","Duskull","Cofagrigus","Frillish","Drifblim","Spiritomb","Sandygast","Palossand","Polteageist","Greavard","Houndstone","Dreepy","Vanillite","Vanillish","Vanilluxe","Bergmite","Avalugg","Eiscue","Glalie","Cubchoo","Beartic","Swinub","Jynx","Regice","Abomasnow","Snover","Emolga","Dedenne","Bibarel","Buizel","Zigzagoon","Linoone","Furret","Sentret","Marill","Azumarill","Finizen","Wailmer","Lanturn","Mantyke","Mantine","Castform","Cetoddle","Cetitan","Skwovet","Greedent"]))

# ===== 4-week gap fill (nightly 2026-10-14): 11-11 Wed CHALLENGING =====
board("2026-11-11","gen1","Challenging",[  # QA 2026-10-19: FANGS dropped (other blues show teeth too) -> split into two sprite clues
  ("WATER",1,"type:water",["Wartortle","Poliwrath","Seadra"],"Wartortle, Poliwrath and Seadra are the board's only Water-types -- a fluffy-eared turtle, a muscular frog (Water/Fighting) and a spiny seahorse."),
  ("SYNCHRONIZE",5,"ability:Synchronize",["Mew","Alakazam"],"Mew and Alakazam both have the Ability Synchronize, which passes a burn, poison or paralysis they catch straight back to the Pokémon that inflicted it."),
  ("EYELESS",2,"sprite:no-eyes",["Zubat"],"Look closely at Zubat's sprite -- it has no eyes at all. The Pokédex says it finds its way around pitch-dark caves by sending out ultrasonic waves from its mouth."),
  ("FLOWER",2,"sprite:back-flower",["Venusaur"],"Look at Venusaur's sprite -- a huge flower blooms on its back. The Pokédex says the flower catches the sun's rays, and the sunlight is absorbed and turned into energy."),
  ("RODENT",3,"arch:rodent",["Rattata","Raichu"],"Rattata is a rat and Raichu is a mouse -- both members of the rodent family."),
], exclude=ex("type:water","ability:Synchronize","sprite:no-eyes","sprite:back-flower","arch:rodent","arch:rat","arch:mouse","arch:plant",
              extra=["Kadabra","Abra","Mewtwo","Squirtle","Tentacruel","Horsea","Poliwhirl","Poliwag","Blastoise","Ivysaur","Bulbasaur","Golbat","Crobat","Arbok","Ekans","Raticate","Pikachu","Nidorina","Nidorino","Nidoran♂","Nidoran♀","Nidoqueen","Nidoking","Gyarados","Dragonite","Dragonair","Dratini","Sandshrew","Sandslash","Meowth","Persian","Hypno","Drowzee","Mr. Mime","Jynx","Slowpoke","Slowbro","Starmie","Exeggutor","Exeggcute","Clefairy","Clefable","Jigglypuff","Wigglytuff","Eevee","Pinsir","Weedle","Beedrill","Oddish","Gloom","Vileplume","Bellsprout","Weepinbell","Victreebel","Tangela","Paras","Parasect","Cubone","Marowak","Hitmonlee","Hitmonchan"]))
board("2026-11-11","mixed","Challenging",[
  ("STEEL",1,"type:steel",["Skarmory","Bastiodon"],"Skarmory and Bastiodon are the board's only Steel-types -- a steel-feathered armoured bird and a shield-faced, armour-plated dinosaur (Rock/Steel)."),
  ("SNAKE",3,"arch:snake",["Seviper","Silicobra"],"Seviper is a fanged viper locked in a feud with Zangoose, and Silicobra is a sand cobra that hoods and burrows -- both are real-world snakes."),
  ("FLEECE",2,"sprite:wool",["Mareep","Dubwool"],"Look closely at the sprites -- Mareep's body is a fleecy ball of wool that stores static electricity, and Dubwool is a sheep wrapped in thick, springy wool."),
  ("DRIZZLE",5,"ability:Drizzle",["Politoed","Pelipper","Kyogre"],"Politoed, Pelipper and Kyogre all have the Ability Drizzle, which makes it rain the moment they enter battle."),
], exclude=ex("type:steel","arch:snake","arch:serpent","arch:cobra","sprite:wool","arch:sheep","ability:Drizzle","arch:raptor",
              extra=["Sandaconda","Ekans","Arbok","Dratini","Dragonair","Rayquaza","Onix","Steelix","Gyarados","Milotic","Zangoose","Flaaffy","Ampharos","Wooloo","Whimsicott","Cottonee","Eldegoss","Gossifleur","Gogoat","Skiddo","Bouffalant","Rampardos","Registeel","Jirachi","Aggron","Lairon","Aron","Poliwag","Poliwhirl","Poliwrath","Wingull","Groudon","Rayquaza","Salandit","Salazzle","Anorith","Armaldo","Tyrunt","Tyrantrum","Cranidos","Shieldon","Archen","Archeops","Rufflet","Braviary","Corviknight","Staraptor","Staravia","Talonflame","Kyurem","Palkia"]))

# ===== 4-week gap fill (nightly 2026-10-15): 11-12 Thu HARD =====
board("2026-11-12","gen1","Hard",[
  ("RUN-AWAY",5,"ability:Run Away",["Venonat","Ponyta","Eevee"],"Venonat, Ponyta and Eevee all have the Ability Run Away, which lets them flee guaranteed from any wild Pokémon battle."),
  ("ECHINODERM",4,"arch:echinoderm",["Starmie"],"Starmie is an echinoderm -- the spiny-skinned sea group of starfish, urchins and sea cucumbers -- its two-star body is a starfish with a glowing core."),
  ("WATERFOWL",3,"arch:duck",["Psyduck","Farfetch'd"],"Psyduck is a clumsy duckling with a permanent headache, and Farfetch'd is a wild duck that carries a leek -- from the Japanese saying that a duck arrives carrying its own onions. Both are waterfowl."),
  ("POUCH",2,"sprite:belly-pouch",["Kangaskhan"],"Look at the sprite -- Kangaskhan carries a baby joey in the pouch on its belly, just like a kangaroo."),
  ("HUMANOID",3,"arch:humanoid",["Hitmonlee","Mewtwo"],"Hitmonlee is a kicking martial artist and Mewtwo a tall, cloned psychic -- both stand and move on two legs like a person."),
], exclude=ex("ability:Run Away","arch:echinoderm","arch:starfish","arch:duck","arch:kangaroo","arch:marsupial","arch:humanoid","sprite:belly-egg-pouch",
              extra=["Chansey","Kadabra","Alakazam","Abra","Drowzee","Hypno","Staryu","Golduck","Rapidash","Dodrio","Caterpie","Raticate","Machop","Machoke","Machamp","Mr. Mime","Jynx","Hitmonchan","Electabuzz","Mew","Doduo","Pidgey","Spearow","Fearow","Pidgeotto","Pidgeot","Jolteon","Flareon","Vaporeon","Venomoth","Parasect","Paras"]))
board("2026-11-12","mixed","Hard",[  # QA 2026-10-19: CHIROPTERAN -> ECHOLOCATION; SKILL-LINK (too obscure) -> INTIMIDATE (Mightyena/Staraptor/Scrafty)
  ("ECHOLOCATION",4,"trait:echolocation",["Woobat","Noibat"],"Woobat and Noibat are bat Pokémon that find their way with sound -- like real bats' echolocation, they use ultrasonic waves to sense their surroundings in the dark."),
  ("INTIMIDATE",5,"ability:Intimidate",["Mightyena","Staraptor","Scrafty"],"Mightyena, Staraptor and Scrafty all have the Ability Intimidate, which lowers the opposing Pokémon's Attack stat as soon as they enter battle."),
  ("MANTIS",3,"arch:mantis",["Scizor","Leavanny"],"Scizor is a steel-red praying mantis with a pincer pair for forelegs, and Leavanny is a leafy mantis that stitches clothes for its young."),
  ("PENGUIN",3,"arch:penguin",["Empoleon","Eiscue"],"Empoleon is an emperor penguin with steel flippers and a trident crest, and Eiscue is an Antarctic penguin that wears a block of ice on its head like a hat."),
], exclude=ex("ability:Intimidate","arch:chiropteran","arch:bat","arch:mantis","arch:penguin","arch:scorpion","arch:arachnid",
              extra=["Zubat","Golbat","Crobat","Swoobat","Noivern","Gliscor","Scyther","Kleavor","Fomantis","Lurantis","Piplup","Prinplup","Heracross","Skorupi","Gligar","Wailmer","Wailord","Finizen","Palafin","Cetoddle","Cetitan","Lunala","Gyarados","Arcanine","Incineroar","Hitmontop","Landorus","Salamence","Sneasel","Weavile"]))
# ===== 4-week gap fill (nightly 2026-10-17): 11-14 Sat BRUTAL =====
board("2026-11-14","gen1","Brutal",[
  ("AGATHA",4,"trainer:Agatha",["Gengar","Haunter","Arbok"],"Gengar, Haunter and Arbok are all on Kanto Elite Four member Agatha's team (with Golbat, which isn't here) -- the ghost-and-poison specialist."),
  ("HEAVYWEIGHT",5,"stat:weight",["Snorlax","Golem","Onix","Gyarados"],"Snorlax (460 kg), Golem (300 kg), Gyarados (235 kg) and Onix (210 kg) all weigh over 200 kg -- only Lapras and Dragonite join them in Gen I, and neither is here."),
  ("SERPENT",3,"arch:serpent",["Arbok","Onix","Gyarados"],"Arbok is a cobra, Gyarados a sea serpent, and Onix is literally the Rock Snake Pokémon -- a chain of boulders shaped like a giant snake."),
  ("NIMBLE",5,"stat:speed",["Gengar","Dugtrio","Electrode"],"Gengar (110), Dugtrio (120) and Electrode (150) all have a base Speed of 110 or more -- among the fastest Pokémon in Gen I."),
], exclude=ex("trainer:Agatha","arch:serpent","arch:cobra","arch:snake",
              extra=["Golbat","Lapras","Dragonite","Ekans","Dragonair","Dratini","Seadra","Raichu","Persian","Alakazam","Dodrio","Starmie","Tauros","Jolteon","Aerodactyl","Mewtwo","Mew","Gastly","Marowak","Cubone","Rhydon","Kangaskhan","Charizard","Dewgong","Slowbro","Blastoise","Venusaur","Machamp"]))
board("2026-11-14","mixed","Brutal",[  # QA 2026-10-19: BAKU dropped; Metagross added to STEVEN (x4); new CEPHALOPOD clue
  ("STEVEN",4,"trainer:Steven",["Claydol","Aggron","Cradily","Metagross"],"Claydol, Aggron, Cradily and Metagross are all on Hoenn Champion Steven Stone's team (with Skarmory and Armaldo) -- a rock-and-steel collector whose ace is Metagross."),
  ("PRANKSTER",5,"ability:Prankster",["Klefki","Whimsicott","Tornadus"],"Klefki, Whimsicott and Tornadus all have the Ability Prankster, which gives their status moves priority so they strike first."),
  ("GRAY",1,"colour:gray",["Klefki","Aggron"],"Look at the sprites -- Klefki's ring of keys and Aggron's iron armour are both gray, and nothing else on this board is."),
  ("CEPHALOPOD",4,"arch:cephalopod",["Octillery","Malamar"],"Octillery is an octopus and Malamar is a squid -- both are cephalopods, the tentacled mollusc class that also includes cuttlefish and nautiluses."),
  ("WIND",3,"lore:wind",["Tornadus"],"Tornadus is the Cyclone Pokémon -- a storm genie that whips up violent winds from its tail, and Wind is its signature theme."),
], exclude=ex("trainer:Steven","ability:Prankster","arch:cephalopod","arch:octopus","arch:squid",
              extra=["Skarmory","Lileep","Armaldo","Anorith","Beldum","Metang","Aron","Lairon","Hypno","Sableye","Murkrow","Volbeat","Illumise","Riolu","Purrloin","Liepard","Cottonee","Thundurus","Meowstic","Impidimp","Morgrem","Grimmsnarl","Shroodle","Grafaiai","Baltoy","Bronzong","Bronzor","Lucario","Garchomp","Remoraid","Clobbopus","Grapploct","Dhelmise","Kraken"]))
# ===== 4-week gap fill (nightly 2026-10-18): 11-15 Sun EVIL =====
def _gen1_where(pred): return [n for n,r in FACTS.items() if r["gen"]==1 and pred(r)]
_atk120 = _gen1_where(lambda r: r["base"]["attack"]>=120)
_arthro = _gen1_where(lambda r: "bug" in r["types"] or any(a in r["arch"] for a in ("insect","crustacean","crab","arthropod","trilobite","spider","arachnid")))
board("2026-11-15","gen1","Evil",[
  ("KAPPA",3,"myth:kappa",["Golduck"],"Golduck is the Duck Pokémon, but its webbed hands and feet, beak-like snout and the gem on its forehead come straight from the kappa -- a mischievous Japanese river spirit."),
  ("ARTHROPOD",4,"arch:arthropod",["Kingler","Pinsir","Kabutops"],"Kingler (a crab), Pinsir (a stag beetle) and Kabutops (a fossil horseshoe crab/trilobite) are all arthropods -- the jointed-legged, hard-shelled animal group that includes crabs, insects and trilobites."),
  ("BRAWN",5,"stat:attack",["Machamp","Kingler","Pinsir"],"Machamp (130), Kingler (130) and Pinsir (125) all have a base Attack stat of 120 or more -- among the hardest hitters in Gen I (Golem, Rhydon, Dragonite and a few others share it, but aren't on this board)."),
  ("MOON-STONE",5,"evo:moon-stone",["Clefable","Wigglytuff"],"Clefable and Wigglytuff are both reached by evolving with a Moon Stone: Clefairy becomes Clefable and Jigglypuff becomes Wigglytuff."),
  ("OBLIVIOUS",5,"ability:Oblivious",["Lickitung","Jynx"],"Lickitung and Jynx can both have the Ability Oblivious, which makes them immune to infatuation (and, in later games, to Taunt) -- too absent-minded to be charmed or goaded."),
], exclude=ex("ability:Oblivious","myth:kappa","arch:platypus",
              extra=_atk120+_arthro+["Kabuto","Krabby","Psyduck","Squirtle","Wartortle","Blastoise","Poliwhirl","Poliwag","Poliwrath","Farfetch'd","Slowpoke","Slowbro","Clefairy","Jigglypuff","Nidorina","Nidorino","Nidoqueen","Nidoking","Golem","Rhydon","Hitmonlee","Hitmonchan","Dragonite","Flareon","Gyarados","Machoke","Machop","Mr. Mime","Chansey","Snorlax","Kangaskhan"]))
board("2026-11-15","mixed","Evil",[
  ("STARTER",1,"group:starter",["Greninja","Meowscarada","Popplio"],"Greninja, Meowscarada and Popplio are all starter Pokémon -- the Water-type pick of Kalos, the Grass-type pick of Paldea and the Water-type pick of Alola."),
  ("PROTEAN",5,"ability:Protean",["Greninja","Kecleon","Meowscarada"],"Greninja, Kecleon and Meowscarada can all have the Ability Protean, which changes their type to match the move they are about to use."),
  ("THICK-FAT",5,"ability:Thick Fat",["Walrein","Dewgong","Miltank"],"Walrein, Dewgong and Miltank all have the Ability Thick Fat, which halves the damage they take from Fire- and Ice-type moves -- blubber and milk-cow bulk in action."),
  ("PINNIPED",4,"arch:pinniped",["Walrein","Popplio","Dewgong"],"Walrein (a walrus), Popplio and Dewgong (both billed as the Sea Lion Pokémon) are pinnipeds -- the flippered marine mammals that include seals, sea lions and walruses."),
  ("FOSSIL",4,"role:fossil",["Archeops","Tyrantrum"],"Archeops and Tyrantrum are both revived from fossils -- the Plume Fossil (Archen, the First Bird) and the Jaw Fossil (Tyrunt, the Despot Pokémon) -- so each is a prehistoric creature brought back by science."),
], exclude=ex("role:starter","role:fossil","ability:Protean","ability:Thick Fat","arch:pinniped",
              extra=["Libero","Cinderace","Rillaboom","Primarina","Brionne","Sealeo","Spheal","Seel","Aurorus","Amaura","Dracozolt","Arctozolt","Dracovish","Arctovish","Aerodactyl","Kabuto","Kabutops","Omanyte","Omastar","Lileep","Cradily","Anorith","Armaldo","Cranidos","Rampardos","Shieldon","Bastiodon","Tirtouga","Carracosta","Archen","Tyrunt","Wailord","Kangaskhan","Tauros","Bouffalant","Gogoat","Camerupt","Numel","Chameleon","Castform","Zoroark","Zorua","Staraptor","Rufflet","Braviary","Corviknight","Pidgeot","Fearow","Dodrio","Doduo"]))


# ===== 4-week gap fill (nightly 2026-10-19): 11-16 Mon EASY =====
board("2026-11-16","gen1","Easy",[
  ("FIRE",1,"type:fire",["Charmander","Magmar","Flareon"],"Charmander, Magmar and Flareon are the board's only Fire-types -- a flame-tailed lizard, a living fireball and the Flame Pokémon."),
  ("PSYCHIC",1,"type:psychic",["Abra","Hypno"],"Abra and Hypno are the board's only Psychic-types -- a sleepy teleporter and a pendulum-swinging hypnotist."),
  ("FISTS",2,"sprite:fists",["Mankey","Hitmonchan"],"Look at the sprites -- Mankey shakes both fists in a permanent rage and Hitmonchan's are boxing gloves. They are the only two on this board throwing punches."),  # QA 2026-10-20: type clue swapped for FISTS; Electabuzz->Seel, Geodude->Diglett neutrals
  ("BIRD",3,"arch:bird",["Spearow","Doduo"],"Spearow is a tiny, fierce sparrow-like bird and Doduo is a two-headed flightless bird -- both are birds, and neither is a Fire-, Psychic- or Fighting-type."),
], exclude=ex("type:fire","type:psychic","sprite:fists","arch:bird",
              extra=["Farfetch'd","Aerodactyl","Articuno","Zapdos","Moltres","Pidgey","Pidgeotto","Pidgeot","Fearow","Dodrio","Kadabra","Alakazam","Mewtwo","Mew","Machop","Machoke","Machamp","Hitmonlee","Primeape","Drowzee","Jynx","Mr. Mime"]))
board("2026-11-16","mixed","Easy",[
  ("FIRE",1,"type:fire",["Cyndaquil","Torchic","Litten"],"Cyndaquil, Torchic and Litten are the board's only Fire-types -- three fire starters from Johto, Hoenn and Alola."),
  ("FIGHTING",1,"type:fighting",["Riolu","Timburr"],"Riolu and Timburr are the board's only Fighting-types -- an aura-sensing jackal cub and a log-carrying muscle-builder."),
  ("DARK",1,"type:dark",["Poochyena","Zorua"],"Poochyena and Zorua are the board's only Dark-types -- a snapping hyena pup and an illusion-casting fox cub."),
  ("BEAR",3,"arch:bear",["Teddiursa","Cubchoo"],"Teddiursa is a honey-loving teddy bear cub and Cubchoo is a polar bear cub with a runny nose -- both are bears."),
], exclude=ex("type:fire","type:fighting","type:dark","arch:bear",
              extra=["Ursaring","Ursaluna","Beartic","Munchlax","Stufful","Bewear","Kubfu","Urshifu","Lucario","Gallade","Mienfoo","Mienshao","Conkeldurr","Gurdurr","Zoroark","Mightyena","Houndour","Houndoom","Sneasel","Weavile","Absol","Umbreon","Murkrow","Honchkrow"]))


# ===== 4-week gap fill (nightly 2026-10-20): 11-17 Tue MEDIUM =====
board("2026-11-17","gen1","Medium",[
  ("ROCK",1,"type:rock",["Rhyhorn","Omanyte","Graveler"],"Rhyhorn (Ground/Rock), Omanyte (Rock/Water) and Graveler (Rock/Ground) are the board's only Rock-types -- an armoured rhino, a spiral-shelled fossil and a boulder with arms."),
  ("FLYING",1,"type:flying",["Pidgeotto","Dodrio"],"Pidgeotto and Dodrio (both Normal/Flying) are the board's only Flying-types -- a crested hawk and a three-headed ostrich."),
  ("CURLY",2,"sprite:curl",["Clefairy","Jigglypuff"],"Look at the sprites -- Clefairy and Jigglypuff both have a single curly tuft of hair on their foreheads, and nothing else on this board does."),
  ("MUSHROOM",2,"sprite:mushrooms",["Paras"],"Look at Paras's back -- two big mushrooms grow out of it, feeding off the little bug that carries them."),
  ("WASP",3,"arch:wasp",["Beedrill"],"Beedrill is a giant wasp-like bug with a stinger on each forearm and another on its tail -- built like a hornet, despite its 'Poison Bee' title."),
], exclude=ex("type:rock","type:flying","arch:wasp","arch:bee",
              extra=["Wigglytuff","Clefable","Mr. Mime","Poliwag","Poliwhirl","Poliwrath","Jynx","Magnemite","Pidgey","Pidgeot","Spearow","Fearow","Doduo","Farfetch'd","Aerodactyl","Zapdos","Articuno","Moltres","Parasect","Weedle","Kakuna","Tangela","Vileplume","Gloom","Oddish","Venonat","Venomoth","Scyther","Pinsir","Butterfree","Geodude","Golem","Onix","Kabuto","Kabutops","Omastar","Rhydon","Mew"]))
board("2026-11-17","mixed","Medium",[
  ("POISON",1,"type:poison",["Stunky","Salandit"],"Stunky (Poison/Dark) and Salandit (Poison/Fire) are the board's only Poison-types -- a spraying skunk and a toxic-gas lizard."),
  ("DRAGON",1,"type:dragon",["Goomy","Deino"],"Goomy and Deino (Dark/Dragon) are the board's only Dragon-types -- a slimy soft-bodied dragon and a blind, biting hatchling."),
  ("DEER",3,"arch:deer",["Stantler","Sawsbuck"],"Stantler is a stag with twisting, hypnotic antlers and Sawsbuck is a deer whose tree-like antlers change with the seasons -- both are deer."),
  ("SHELL",2,"sprite:shell",["Shuckle","Crustle"],"Shuckle hides inside a holed shell where it ferments berry juice, and Crustle hauls a boulder-slab shell on its back -- the only shelled Pokémon here."),
  ("DREAMS",3,"lore:dreams",["Munna"],"Munna feeds on the dreams of sleeping people and floats pink dream smoke -- its Pokédex entry is all about eating dreams (Dream Eater)."),
], exclude=ex("type:poison","type:dragon","sprite:shell","arch:tapir","arch:deer",
              extra=["Wyrdeer","Deerling","Skiddo","Gogoat","Hypno","Drowzee","Musharna","Skuntank","Toxel","Dwebble","Torkoal","Turtwig","Grotle","Torterra","Tirtouga","Carracosta","Chewtle","Drednaw","Shelmet","Cloyster","Shellder","Wartortle","Blastoise","Squirtle","Wimpod","Golisopod","Binacle","Barbaracle","Mudsdale","Kecleon","Gastrodon","Shellos","Zweilous","Hydreigon","Sliggoo","Goodra","Dratini","Dragonite","Salamence","Garchomp"]))


# ===== 4-week gap fill (nightly 2026-10-21): 11-18 Wed CHALLENGING =====
board("2026-11-18","gen1","Challenging",[
  ("GRASS",1,"type:grass",["Gloom","Victreebel","Tangela","Exeggutor"],"Gloom, Victreebel, Tangela and Exeggutor are the board's only Grass-types -- a drooling weed, a pitcher-plant trap, a mop of blue vines and a walking palm grove (Grass/Psychic)."),
  ("HORSE",3,"arch:horse",["Ponyta","Rapidash"],"Ponyta is a fire-maned foal and Rapidash its full-grown, unicorn-horned racehorse -- both are horses."),
  ("BICEPS",2,"sprite:muscles",["Machop"],"Look at the sprite -- Machop is a small but impossibly ripped fighter, flexing a body that's all muscle."),
  ("KITSUNE",5,"myth:kitsune",["Ninetales"],"Ninetales is based on the kitsune, the Japanese fox spirit that gains an extra tail for every century it lives, up to nine -- the Pokédex says it can live 1,000 years."),
  ("RUBIES",2,"sprite:red-jewels",["Tentacruel"],"Look at the sprite -- Tentacruel has two big red ruby-like jewels on its head, above its trailing tentacles; no other Pokémon on this board wears them."),
], exclude=ex("type:grass","arch:horse","arch:equine","sprite:muscles","sprite:red-jewels","arch:jellyfish","arch:cnidarian","arch:fox","arch:primate",
              extra=["Vulpix","Eevee","Machoke","Machamp","Hitmonlee","Hitmonchan","Primeape","Mankey","Tentacool","Seadra","Horsea","Dewgong","Cloyster","Doduo","Dodrio","Zebstrika","Parasect","Paras","Bulbasaur","Ivysaur","Venusaur","Oddish","Bellsprout","Weepinbell","Exeggcute","Vileplume","Charizard","Arcanine","Growlithe","Rhydon","Golem","Kangaskhan"]))
board("2026-11-18","mixed","Challenging",[
  ("ELECTRIC",1,"type:electric",["Emolga","Dedenne","Togedemaru"],"Emolga, Dedenne and Togedemaru are the board's only Electric-types -- three cheek-sparking, static-charged little rodents (Emolga is a flying squirrel)."),
  ("BELT",2,"sprite:belt",["Hariyama","Throh"],"Look at the sprites -- Hariyama wears a heavy sumo mawashi belt and Throh a black judo belt tied round its waist, and no other Pokémon here wears one."),
  ("HOOT",3,"arch:owl",["Noctowl","Decidueye"],"Noctowl is a tall, wise owl that sees in the dark and Decidueye is an archer owl with an arrow quill -- both are real-world owls."),
  ("CETACEAN",4,"arch:cetacean",["Wailmer","Wailord"],"Wailmer and Wailord are both cetaceans -- the order of whales, dolphins and porpoises; Wailord is the largest Pokémon ever recorded by height."),
], exclude=ex("type:electric","sprite:belt","arch:owl","arch:whale","arch:cetacean","arch:rodent",
              extra=["Rowlet","Dartrix","Hoothoot","Plusle","Minun","Emolga","Pikachu","Raichu","Pawmi","Pawmot","Pachirisu","Marill","Azumarill","Sandslash","Dewgong","Lanturn","Chinchou","Primarina","Wishiwashi","Dondozo","Tatsugiri","Wailord","Machamp","Conkeldurr","Gurdurr","Timburr","Sawk","Hitmontop","Makuhita","Spinda","Rufflet","Hawlucha","Falinks","Sumo","Hoothoot","Ursaring","Bewear","Zeraora","Rotom","Morpeko","Mimikyu","Luxray","Shinx","Luxio","Stoutland","Loudred"]))


# ===== 4-week gap fill (nightly 2026-10-22): 11-19 Fri HARD =====
board("2026-11-19","gen1","Hard",[
  ("SHELL-ARMOR",5,"ability:Shell Armor",["Cloyster","Omastar"],"Cloyster and Omastar can both have the Ability Shell Armor, which blocks critical hits against them -- their hard shells are why."),
  ("SIMIAN",4,"arch:simian",["Primeape"],"Primeape is the Pig Monkey Pokémon -- a simian (monkey/ape), famously so furious it never stops being angry."),
  ("SPOONS",2,"sprite:spoons",["Alakazam"],"Look at the sprite -- Alakazam holds a silver spoon in each hand, the tools it uses to focus its psychic power."),
  ("FISH",3,"arch:fish",["Magikarp","Goldeen","Horsea"],"Magikarp, Goldeen and Horsea are all fish -- a flopping carp, a goldfish-like swimmer and a seahorse (which is a fish too)."),
  ("SNAKE",3,"arch:snake",["Ekans","Dragonair"],"Ekans is a coiling venomous snake and Dragonair a long, serpentine dragon with no legs -- both are snake-bodied."),
], exclude=ex("ability:Shell Armor","arch:simian","sprite:spoons","arch:fish","arch:snake",
              extra=["Dewgong","Lapras","Articuno","Seel","Kadabra","Abra","Machop","Machoke","Machamp","Mankey","Gyarados","Seaking","Seadra","Staryu","Starmie","Shellder","Omanyte","Kabuto","Kabutops","Kingler","Krabby","Blastoise","Squirtle","Wartortle","Hitmonlee","Hitmonchan","Mew","Mewtwo","Poliwag","Poliwhirl","Poliwrath","Raticate","Pikachu","Nidoran♀","Nidoran♂","Nidorina","Nidorino","Arbok","Dratini","Dragonite","Gyarados","Onix","Persian","Meowth"]))
board("2026-11-19","mixed","Hard",[
  ("DRONE",3,"arch:bee",["Combee","Cutiefly"],"Combee is a tiny honeycomb-shaped bee (a drone is a male honeybee) and Cutiefly the Bee Fly Pokémon -- both are based on bees."),
  ("MOLE",3,"arch:mole",["Drilbur"],"Drilbur is the Mole Pokémon -- a mole that tunnels with its steel claws, which is why it spins like a drill."),
  ("TUSKS",2,"sprite:tusks",["Mamoswine","Haxorus"],"Look at the sprites -- Mamoswine's huge ivory tusks and Haxorus's axe-like tusks jut from their faces; nothing else on this board has them."),
  ("LEPIDOPTERAN",4,"arch:butterfly",["Beautifly","Vivillon"],"Beautifly and Vivillon are butterflies -- lepidopterans, the scaly-winged insect order of moths and butterflies."),
  ("SPEED-BOOST",5,"ability:Speed Boost",["Blaziken","Yanmega"],"Blaziken and Yanmega can both have the Ability Speed Boost, which raises their Speed at the end of every turn they stay in battle."),
], exclude=ex("arch:bee","arch:mole","sprite:tusks","arch:butterfly","ability:Speed Boost",
              extra=["Beedrill","Vespiquen","Ribombee","Excadrill","Diglett","Dugtrio","Sandshrew","Sandslash","Wiglett","Wugtrio","Cubone","Marowak","Teddiursa","Ursaring","Ursaluna","Piloswine","Swinub","Fraxure","Axew","Donphan","Phanpy","Copperajah","Cufant","Walrein","Butterfree","Dustox","Volcarona","Mothim","Wormadam","Ledian","Ledyba","Torchic","Combusken","Ninjask","Nincada","Shedinja","Yanma","Accelgor","Zeraora","Regieleki","Sceptile","Hawlucha","Heracross","Pinsir"]))
