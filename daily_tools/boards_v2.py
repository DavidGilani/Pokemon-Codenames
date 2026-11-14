# Daily boards (loaded by schedule_v2.py).
# Tier fixed by weekday: Mon Easy / Tue Medium / Wed Challenging / Thu Hard /
# Fri Hard / Sat Brutal / Sun Evil. Brutal/Evil pass the overlap gate
# (clue numbers sum >= 11, <= 1 single-tile clue).
#
# Boards dated before 2026-10-24 were removed (nightly 2026-11-14): long since
# live in Supabase and outside the rolling anti-repetition window, so they were
# stale dead code the verifier mistook for new boards once live_boards.json
# was trimmed to [today-21, today+40].

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

# ===== 10-23 Fri : HARD =====

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
              extra=LEG+["Vanilish","Vanilluxe","Cubchoo","Beartic","Cryogonal","Beautifly","Butterfree","Venomoth","Mothim","Wormadam","Frosmoth","Ninjask","Masquerain","Vivillon","Sylveon","Glaceon","Crobat","Aipom","Sableye","Gastrodon","Trumbeak","Toucannon","Skuntank","Stunky","Spiritomb"]))

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
  # QA 2026-11-14: TRUNK (Munna's trunk too small to see) -> DREAMS.
  ("DREAMS",4,"genus:dream-eater",["Munna"],"Munna is the Dream Eater Pokémon: the Pokédex says it eats the dreams of people and Pokémon, and the mist it gives off shows what it has eaten. It is based on the baku, a dream-eating spirit from Japanese folklore."),
], exclude=ex("type:poison","type:dragon","sprite:shell","arch:tapir","arch:deer",
              extra=["Darkrai","Cresselia","Komala","Snorlax","Munchlax","Jigglypuff","Igglybuff","Wigglytuff","Slakoth","Slaking","Swablu","Wyrdeer","Deerling","Skiddo","Gogoat","Hypno","Drowzee","Musharna","Trumbeak","Toucannon","Skuntank","Toxel","Dwebble","Torkoal","Turtwig","Grotle","Torterra","Tirtouga","Carracosta","Chewtle","Drednaw","Shelmet","Cloyster","Shellder","Wartortle","Blastoise","Squirtle","Wimpod","Golisopod","Binacle","Barbaracle","Mudsdale","Kecleon","Gastrodon","Shellos","Zweilous","Hydreigon","Sliggoo","Goodra","Dratini","Dragonite","Salamence","Garchomp"]))


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
  ("WATER-VEIL",5,"ability:Water Veil",["Wailmer","Wailord"],"Wailmer and Wailord can both have the Ability Water Veil, which makes them immune to burns -- a nod to their water-soaked whale bodies."),
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


# ===== 4-week gap fill (nightly 2026-10-25): 11-20 Fri HARD =====
board("2026-11-20","gen1","Hard",[
  ("SHED-SKIN",5,"ability:Shed Skin",["Metapod","Kakuna","Dratini"],"Metapod, Kakuna and Dratini can all have the Ability Shed Skin, which gives them a one-in-three chance each turn of shaking off any status condition -- just like a cocoon or a snake sloughing its old skin."),
  ("SURGE",3,"trainer:Lt.",["Voltorb","Raichu"],"Voltorb and Raichu are on Vermilion Gym leader Lt. Surge's team in the Red and Blue games (alongside Pikachu) -- the American soldier whose Gym is wired with electric traps."),
  ("RODENT",3,"arch:rodent",["Raichu","Raticate"],"Raichu is a giant electric mouse and Raticate a big-fanged rat -- both are rodents, with the gnawing front teeth to prove it."),
  ("CHIROPTERAN",4,"arch:chiropteran",["Zubat"],"Zubat is a chiropteran -- the scientific order of bats -- a blind cave-dweller that finds its way by ultrasonic squeals."),
  ("PLANT",3,"arch:plant",["Oddish","Bellsprout"],"Oddish is a walking weed with a tuft of leaves for hair and Bellsprout a slender flower-stalk on legs -- both are plant Pokémon."),
], exclude=ex("ability:Shed Skin","trainer:Lt.","arch:rodent","arch:mouse","arch:rat","arch:chiropteran","arch:bat","arch:plant",
              extra=["Bulbasaur","Ivysaur","Venusaur","Golbat","Pikachu","Magneton","Magnemite","Electabuzz","Jolteon","Ekans","Arbok","Dragonair","Rattata","Gloom","Vileplume","Weepinbell","Victreebel","Exeggcute","Exeggutor","Tangela","Cloyster","Omanyte","Omastar","Slowbro","Paras","Parasect","Nidoran♂","Nidoran♀","Nidorina","Nidorino","Eevee","Articuno","Zapdos"]))
board("2026-11-20","mixed","Hard",[
  ("HEAVY-METAL",5,"ability:Heavy Metal",["Aron","Duraludon","Bronzong","Cufant"],"Aron, Duraludon, Bronzong and Cufant can all have the Ability Heavy Metal, which doubles their weight -- fitting for a gang of iron-plated bruisers."),
  ("FLANNERY",3,"trainer:Flannery",["Slugma","Camerupt"],"Slugma and Camerupt are on Lavaridge Gym leader Flannery's Fire-type team in Hoenn (alongside Numel and Torkoal)."),
  ("CRUSTACEAN",4,"arch:isopod",["Wimpod"],"Wimpod is based on a sea slater, an isopod -- a crustacean, the same group as crabs, lobsters and shrimp."),
  ("PANGOLIN",3,"arch:pangolin",["Sandslash"],"Sandslash is based on a pangolin -- the scaly, ant-eating mammal that rolls itself into an armoured ball."),
  ("ANGLER",3,"arch:anglerfish",["Chinchou"],"Chinchou is an anglerfish -- the deep-sea fish that dangles a glowing lure from its head, just like Chinchou's two glowing antennae."),
], exclude=ex("ability:Heavy Metal","trainer:Flannery","arch:crustacean","arch:crab","arch:pangolin","arch:armadillo","arch:anglerfish",
              extra=["Lairon","Aggron","Copperajah","Numel","Torkoal","Magcargo","Golisopod","Lanturn","Sandshrew","Clauncher","Clawitzer","Corphish","Crawdaunt","Binacle","Barbaracle","Dwebble","Crustle","Krabby","Kingler"]))

# ===== 11-21 Sat BRUTAL =====
board("2026-11-21","gen1","Brutal",[
  ("KEEN-EYE",5,"ability:Keen Eye",["Pidgeot","Fearow","Farfetch'd"],"Pidgeot, Fearow and Farfetch'd can all have the Ability Keen Eye, which stops other Pokémon lowering their accuracy -- sharp-eyed birds, one and all."),
  ("INNER-FOCUS",5,"ability:Inner Focus",["Farfetch'd","Golbat","Kangaskhan"],"Farfetch'd, Golbat and Kangaskhan can all have the Ability Inner Focus, which stops them from flinching, however hard they are hit."),
  ("RIVAL",3,"trainer:Blue",["Pidgeot","Rhydon","Arcanine","Gyarados"],"Pidgeot, Rhydon, Arcanine and Gyarados are all on the team of Blue, your rival and the Kanto Champion, in the Red/Blue/Yellow games (alongside Alakazam, Exeggutor and a starter)."),
  ("ECHINODERM",4,"arch:echinoderm",["Staryu"],"Staryu is an echinoderm -- the spiny-skinned sea-animal group that includes starfish, sea urchins and sea cucumbers."),
], exclude=ex("ability:Keen Eye","ability:Inner Focus","arch:echinoderm","trainer:Blue",
              extra=["Starmie","Alakazam","Exeggutor","Blastoise","Charizard","Venusaur","Jolteon","Vaporeon","Flareon","Ninetales","Dragonite","Kadabra","Abra","Zubat","Spearow","Pidgey","Pidgeotto","Hitmonchan","Drowzee","Hypno","Dodrio","Doduo"]))
board("2026-11-21","mixed","Brutal",[
  ("ROUGH-SKIN",5,"ability:Rough Skin",["Sharpedo","Garchomp","Druddigon"],"Sharpedo, Garchomp and Druddigon can all have the Ability Rough Skin, which hurts any Pokémon that makes contact with them -- three sandpaper-tough hides."),
  ("CYNTHIA",3,"trainer:Cynthia",["Garchomp","Gastrodon","Roserade"],"Garchomp, Gastrodon and Roserade are all on Sinnoh Champion Cynthia's team (alongside Spiritomb, Lucario and Milotic)."),
  ("DRASNA",4,"trainer:Drasna",["Druddigon","Noivern","Altaria"],"Druddigon, Noivern and Altaria are on Kalos Elite Four member Drasna's dragon team (alongside Dragalge)."),
  ("SUPER-LUCK",5,"ability:Super Luck",["Murkrow","Absol"],"Murkrow and Absol can both have the Ability Super Luck, which raises their critical-hit ratio -- two classic bad-luck omens that make their own luck."),
], exclude=ex("ability:Rough Skin","trainer:Cynthia","trainer:Drasna","ability:Super Luck",
              extra=["Dragalge","Honchkrow","Togetic","Togekiss","Pidove","Tranquill","Unfezant","Gabite","Gible","Carvanha","Swablu","Crobat","Zubat","Golbat","Noibat","Milotic","Lucario","Spiritomb","Glaceon","Eelektross","Roselia","Budew","Shellos"]))

# ===== 11-22 Sun EVIL =====
board("2026-11-22","gen1","Evil",[
  ("SWIFT-SWIM",5,"ability:Swift Swim",["Psyduck","Kabuto","Poliwrath"],"Psyduck, Kabuto and Poliwrath can all have the Ability Swift Swim, which doubles their Speed when it is raining."),
  ("WEAK-ARMOR",5,"ability:Weak Armor",["Kabuto","Onix"],"Kabuto and Onix can both have the Ability Weak Armor, which drops their Defense and raises their Speed when hit by a physical move -- hard shells that crack under the blow."),
  ("STURDY",5,"ability:Sturdy",["Onix","Geodude","Magnemite"],"Onix, Geodude and Magnemite can all have the Ability Sturdy, which stops a full-health Pokémon being knocked out in one hit -- they always cling on with 1 HP."),
  ("CNIDARIAN",4,"arch:cnidarian",["Tentacool"],"Tentacool is a cnidarian -- the group that includes jellyfish, sea anemones and corals -- with a glassy bell and stinging tentacles."),
  ("CANINE",3,"arch:canine",["Growlithe","Vulpix"],"Growlithe is a loyal puppy and Vulpix a six-tailed fox -- both belong to the canine family of dogs, wolves and foxes."),
], exclude=ex("ability:Swift Swim","ability:Weak Armor","ability:Sturdy","arch:cnidarian","arch:jellyfish","arch:canine","arch:dog","arch:fox",
              extra=["Golduck","Poliwhirl","Kabutops","Omanyte","Omastar","Goldeen","Poliwag","Seaking","Tentacruel","Arcanine","Ninetales","Eevee","Golem","Graveler","Magneton","Cubone","Marowak"]))
# QA 2026-11-14: "too ability heavy" -> rebuilt with one Ability clue (was POISON-TOUCH/DRY-SKIN/STORM-DRAIN/GASTROPOD/FROG).
board("2026-11-22","mixed","Evil",[
  ("POISON-TOUCH",5,"ability:Poison Touch",["Toxicroak","Grafaiai","Sneasler"],"Toxicroak, Grafaiai and Sneasler can all have the Ability Poison Touch, which gives their contact moves a 30% chance of poisoning the target: venom-filled knuckles, toxic paint-fingers and poison claws."),
  ("GASTROPOD",4,"arch:gastropod",["Shellos","Sliggoo"],"Shellos is a sea slug and Sliggoo a slimy, snail-like slug. Both are gastropods, the mollusc class of slugs and snails."),
  ("DANCER",4,"job:dancer",["Oricorio","Bellossom","Maractus"],"Oricorio is the Dancing Pokémon and changes style with the nectar it drinks. The Pokédex says Bellossom gather to dance in a ritual to summon the sun, and Maractus does an up-tempo song and dance to scare off birds."),
  ("SUN-STONE",5,"evo:sun-stone",["Bellossom","Heliolisk"],"Both are made with a Sun Stone: Gloom becomes Bellossom and Helioptile becomes Heliolisk when exposed to one."),
  ("DESERT",3,"place:desert",["Maractus","Heliolisk"],"The Pokédex puts both in dry country: Maractus lives in arid regions, and Heliolisk thrives in dry, sandy areas where it soaks up sunlight to make electricity."),
], exclude=ex("ability:Poison Touch","arch:gastropod","arch:slug","arch:snail","arch:mollusc","type:poison",
              extra=["Mr. Rime","Croagunk","Sneasel","Weavile","Shroodle","Grimer","Muk","Gastrodon","Goomy","Goodra","Slugma","Magcargo","Shelmet","Accelgor","Ludicolo","Lombre","Lilligant","Petilil","Hitmontop","Spinda","Flamigo","Kricketune","Jigglypuff","Sunflora","Sunkern","Whimsicott","Cottonee","Helioptile","Oddish","Gloom","Vileplume","Cacnea","Cacturne","Sandile","Krokorok","Krookodile","Trapinch","Vibrava","Flygon","Hippopotas","Hippowdon","Sandshrew","Sandslash","Silicobra","Sandaconda","Sigilyph","Yamask","Cofagrigus","Baltoy","Claydol","Numel","Camerupt","Maractus","Gible","Gabite","Garchomp","Orthworm","Larvesta","Volcarona","Scovillain","Sizzlipede","Rapidash","Ponyta"]))


# ===== 4-week gap fill (nightly 2026-10-26): 11-23 Mon EASY =====
board("2026-11-23","gen1","Easy",[
  ("GHOST",1,"type:ghost",["Gastly","Haunter"],"Gastly and Haunter are both Ghost-types -- a floating cloud of gas and its grinning, disembodied-hands evolution."),
  ("ICE",1,"type:ice",["Jynx","Articuno","Lapras"],"Jynx, Articuno and Lapras all have the Ice type -- an ice-queen, the legendary freezing bird and a gentle sea-ferry (Articuno and Lapras are dual-types)."),
  ("NORMAL",1,"type:normal",["Ditto","Tauros"],"Ditto and Tauros are both pure Normal-types -- the shapeless copycat and a charging wild bull."),
  ("FOSSIL",3,"lore:fossil",["Aerodactyl"],"Aerodactyl is a fossil Pokémon -- it is revived from ancient amber, and was a sky-hunter in prehistoric times."),
  ("BEETLE",3,"arch:beetle",["Pinsir"],"Pinsir is the Stag Beetle Pokémon, with a pair of huge pincer-horns like a stag beetle's jaws."),
], exclude=ex("type:ghost","type:ice","type:normal","lore:fossil","arch:beetle","arch:stag-beetle",
              extra=["Gengar","Dewgong","Cloyster","Seel","Kabuto","Kabutops","Omanyte","Omastar","Scyther","Heracross","Paras","Parasect","Venonat","Venomoth","Eevee","Kangaskhan","Chansey","Porygon","Moltres","Zapdos","Dragonite","Dragonair","Pidgeot","Zubat","Golbat"]))
board("2026-11-23","mixed","Easy",[
  ("STEEL",1,"type:steel",["Klink","Beldum","Skarmory"],"Klink, Beldum and Skarmory are all Steel-types -- a clockwork gear, a floating iron ball and an armour-winged bird."),
  ("GROUND",1,"type:ground",["Hippopotas","Phanpy"],"Hippopotas and Phanpy are both pure Ground-types -- a sand-spouting hippo and a little elephant."),
  ("BUG",1,"type:bug",["Wurmple","Grubbin"],"Wurmple and Grubbin are both pure Bug-types -- a spiky red caterpillar and a mandibled grub."),
  ("DOLPHIN",3,"arch:dolphin",["Finizen"],"Finizen is the Dolphin Pokémon -- it swims in playful circles and uses its tail like a propeller."),
  ("WOODPECKER",3,"arch:woodpecker",["Pikipek"],"Pikipek is the Woodpecker Pokémon -- it drills into trees with its beak, up to sixteen pecks a second."),
], exclude=ex("type:steel","type:ground","type:bug","arch:dolphin","arch:woodpecker","arch:cetacean",
              extra=["Metang","Metagross","Klang","Klinklang","Lairon","Aron","Aggron","Bronzor","Bronzong","Corviknight","Donphan","Hippowdon","Vigoroth","Slaking","Silcoon","Cascoon","Beautifly","Dustox","Charjabug","Vikavolt","Cubone","Marowak","Trapinch","Skiploom","Aipom","Ambipom","Kricketot","Munchlax","Snorlax","Palafin","Wailmer","Wailord","Lanturn","Trumbeak","Toucannon","Skuntank","Zigzagoon","Linoone","Obstagoon","Starly","Pidove"]))


# ===== 4-week gap fill (nightly 2026-10-27): 11-24 Tue MEDIUM =====
board("2026-11-24","gen1","Medium",[
  ("FIRE",1,"type:fire",["Charmeleon","Ponyta"],"Charmeleon and Ponyta are the board's only Fire-types -- a flame-tailed lizard and a fiery-maned pony."),
  ("WATER",1,"type:water",["Seadra","Krabby","Shellder"],"Seadra, Krabby and Shellder are the board's only Water-types -- a spiny seahorse, a pincer-clacking crab and a tongue-lolling bivalve."),
  ("EGG",2,"sprite:egg",["Chansey"],"Look at Chansey's sprite -- a big egg sits in the pouch on its belly, which it hands out to hurt or tired people and Pokémon."),
  ("SPRINGS",2,"sprite:springs",["Hitmonlee"],"Hitmonlee's legs stretch and recoil like coiled springs -- the Pokédex says they extend to deliver kicks from long range."),
  ("SABRINA",3,"trainer:sabrina",["Mr. Mime","Venomoth"],"Saffron City Gym Leader Sabrina trains Mr. Mime and Venomoth (alongside Kadabra and Alakazam) in the Kanto games -- a psychic team."),
], exclude=ex("type:fire","type:water","trainer:sabrina",
              extra=["Kadabra","Alakazam","Abra","Exeggcute","Exeggutor","Hitmonchan","Kangaskhan","Chansey","Cloyster","Vulpix","Ninetales","Growlithe","Arcanine","Magmar","Flareon","Charmander","Charizard","Rapidash","Moltres","Hypno","Drowzee","Mew","Mewtwo","Jynx","Slowbro","Slowpoke","Starmie","Staryu","Butterfree","Parasect","Venonat","Machamp","Machoke","Machop","Mankey","Primeape","Poliwrath"]))
board("2026-11-24","mixed","Medium",[
  ("FIRE",1,"type:fire",["Darumaka","Delphox"],"Darumaka and Delphox are the board's only Fire-types -- a round, snowman-like daruma doll and a fire-wielding fox mage (Delphox is Fire/Psychic)."),
  ("FAIRY",1,"type:fairy",["Swirlix","Spritzee"],"Swirlix and Spritzee are the board's only Fairy-types -- a cotton-candy puff and a perfume-scented little songbird."),
  ("CLOUD",2,"sprite:cloud",["Landorus","Thundurus"],"Look at the sprites -- Landorus and Thundurus both trail a billowing cloud in place of legs, like the other Forces of Nature."),
  ("PEARL",2,"sprite:pearl",["Clamperl"],"Clamperl is a blue bivalve with a pearl inside its shell -- it's said to sometimes form a rare Pink or White pearl."),
  ("CROC",3,"arch:crocodile",["Totodile","Sandile"],"Totodile is a big-jawed baby crocodile and Sandile a desert crocodile that hides under the sand with only its eyes showing -- both are crocodilians."),
], exclude=ex("type:fire","type:fairy","arch:crocodile","arch:alligator","sprite:pearl",
              extra=["Tornadus","Enamorus","Altaria","Swablu","Drifblim","Drifloon","Gorebyss","Huntail","Shellder","Cloyster","Krookodile","Krokorok","Feraligatr","Croconaw","Reuniclus","Vanilluxe","Vanillish","Cryogonal","Quilava","Typhlosion","Braixen","Fennekin","Emboar","Darmanitan","Torkoal","Cacturne","Hippowdon","Sandslash","Gastrodon","Mudkip","Sylveon","Kirlia","Togekiss","Togepi","Clefairy","Jigglypuff","Clefable","Wigglytuff","Gardevoir","Mimikyu","Whimsicott","Comfey","Cutiefly"]))


# ===== 4-week gap fill (nightly 2026-10-28): 11-25 Wed CHALLENGING =====
board("2026-11-25","gen1","Challenging",[
  ("PSYCHIC",1,"type:psychic",["Hypno","Mewtwo","Abra"],"Hypno, Mewtwo and Abra are the board's only Psychic-types -- a pendulum-swinging hypnotist, a genetically engineered powerhouse and a sleepy teleporter."),
  ("RHINO",3,"arch:rhino",["Rhyhorn"],"Rhyhorn is the Spikes Pokémon, based on a rhinoceros -- a heavily armoured charger with a drill-like horn on its nose."),
  ("BIRD",3,"arch:bird",["Pidgey","Spearow"],"Pidgey is a small tan songbird and Spearow a fierce little sparrow-like bird -- both are ordinary real-world-style birds."),
  ("SERPENT",3,"arch:serpent",["Ekans","Dragonair"],"Ekans is based on a cobra and Dragonair on a Chinese serpent-dragon -- both are long, scaled, limbless serpents."),
  ("BLADES",2,"sprite:scythe-arms",["Scyther"],"Look at the sprite -- Scyther's forearms are a pair of long, curved scythe blades, which it swings with lightning speed."),
], exclude=ex("type:psychic","arch:rhino","arch:serpent","arch:snake","arch:bird","sprite:scythe-arms",
              extra=["Rhydon","Arbok","Gyarados","Onix","Dratini","Dragonite","Pinsir","Kabutops","Mew","Kangaskhan","Seel","Gastly","Haunter","Gengar","Kadabra","Alakazam","Drowzee","Starmie","Slowbro","Slowpoke","Exeggutor","Exeggcute","Magneton","Electrode","Golem","Graveler","Snorlax","Farfetch'd","Doduo","Dodrio","Zapdos","Moltres","Articuno","Pidgeotto","Pidgeot","Fearow","Aerodactyl","Charizard","Butterfree"]))
board("2026-11-25","mixed","Challenging",[
  ("FIGHTING",1,"type:fighting",["Falinks","Kubfu"],"Falinks and Kubfu are the board's only Fighting-types -- a six-trooper phalanx and a kung-fu bear cub training for its Urshifu evolution."),
  ("SPIDER",3,"arch:spider",["Joltik","Tarountula","Araquanid"],"Joltik clings to bigger Pokémon to sap their static, Tarountula is a little yarn-ball tarantula and Araquanid a water-bubble-helmeted spider -- all three are spiders."),
  ("SHARK",3,"arch:shark",["Gible","Frigibax"],"Gible is the Land Shark Pokémon and Frigibax the Ice Fin Pokémon -- both are small dragons with shark fins and jaws."),
  ("LION",3,"arch:lion",["Pyroar"],"Pyroar is the Royal Pokémon, based on a lion -- the male's flaming mane is its pride."),
  ("DRUM",2,"sprite:log-drum",["Rillaboom"],"Look at the sprite -- Rillaboom is a gorilla drummer, carrying a big log drum whose beats it uses to command its forest."),
], exclude=ex("type:fighting","arch:spider","arch:arachnid","arch:shark","arch:lion","sprite:log-drum",
              extra=["Ariados","Spinarak","Galvantula","Dewpider","Spidops","Sharpedo","Carvanha","Garchomp","Baxcalibur","Gabite","Grookey","Thwackey","Litleo","Solgaleo","Urshifu","Dracovish","Arctovish","Surskit","Masquerain"]))


# ===== catch-up gap fill (nightly 2026-11-06): 11-26 Thu HARD =====
board("2026-11-26","gen1","Hard",[
  ("DAMP",5,"ability:damp",["Golduck","Poliwag","Poliwhirl"],"All three have the Ability Damp, which stops anyone on the field from using self-destructing moves like Explosion."),
  ("PACHYDERM",4,"arch:pachyderm",["Nidoking","Nidoqueen"],"Nidoking and Nidoqueen are the armoured, thick-skinned royals of the Nidoran line -- big, tough-hided beasts in the mould of the pachyderms (rhinos and elephants)."),
  ("TAPIR",3,"arch:tapir",["Drowzee"],"Drowzee is based on a tapir, and on the baku, the Japanese dream-eating tapir spirit -- hence its trunk-like snout and its taste for dreams."),
  ("CRAB",3,"arch:crab",["Kingler"],"Kingler is the Pincer Pokémon, a crab with one huge, crushing claw."),
  ("FOX",3,"arch:fox",["Eevee","Ninetales"],"Eevee has a fox's big ears, bushy tail and fluffy ruff, and Ninetales is the legendary nine-tailed fox -- inspired by the kitsune of Japanese folklore. Both are fox-based."),  # QA 2026-11-14: Kadabra-as-fox too much of a stretch -> Ninetales
], exclude=ex("ability:damp","arch:pachyderm","arch:tapir","arch:crab","arch:fox",
              extra=["Psyduck","Poliwrath","Parasect","Paras","Politoed","Raichu","Cubone","Rhyhorn","Rhydon","Goldeen","Nidoran♀","Nidorina","Nidoran♂","Nidorino","Hypno","Krabby","Abra","Kadabra","Alakazam","Vulpix","Jolteon","Flareon","Vaporeon","Growlithe","Arcanine","Pikachu","Electabuzz","Tauros","Mew","Mewtwo","Ponyta"]))
board("2026-11-26","mixed","Hard",[
  ("RAPTOR",4,"arch:raptor",["Staravia","Rufflet"],"Staravia (a starling-eagle hybrid) and Rufflet (the Eaglet Pokémon) are both birds of prey -- raptors."),
  ("TRACE",5,"ability:trace",["Porygon2","Ralts","Gardevoir"],"All three have the Ability Trace, which copies the Ability of the opposing Pokémon the moment they enter battle."),
  ("SCORPION",3,"arch:scorpion",["Gligar","Skorupi"],"Gligar is a flying scorpion with a stinging tail, and Skorupi the Scorpion Pokémon with its poison-tipped pincers -- both are scorpions."),
  ("PENGUIN",3,"arch:penguin",["Piplup"],"Piplup is the Penguin Pokémon, a proud little emperor penguin."),
  ("ZEBRA",3,"arch:zebra",["Blitzle"],"Blitzle is based on a zebra -- a black mane and a striped, lightning-charged coat."),
], exclude=ex("ability:trace","arch:raptor","arch:scorpion","arch:penguin","arch:zebra","arch:bird",
              extra=["Kirlia","Gallade","Porygon","Porygon-Z","Prinplup","Empoleon","Zebstrika","Staraptor","Starly","Braviary","Talonflame","Fletchinder","Fletchling","Skarmory","Gliscor","Drapion","Eiscue","Hawlucha","Pidgeot","Fearow","Honchkrow","Decidueye","Corviknight","Mandibuzz","Vullaby","Swellow","Unfezant","Xatu"]))

# ===== catch-up gap fill (nightly 2026-11-06): 11-27 Fri HARD =====
board("2026-11-27","gen1","Hard",[
  ("OWN-TEMPO",5,"ability:own-tempo",["Slowpoke","Lickitung"],"Both have the Ability Own Tempo, which makes them immune to confusion."),
  ("SIMIAN",4,"arch:primate",["Mankey","Machop"],"Simians are monkeys and apes -- Mankey is a pig-nosed monkey and Machop a strong, ape-like fighter."),
  ("GRUB",3,"arch:caterpillar",["Caterpie","Weedle"],"Caterpie and Weedle are the two bug-larva Pokémon of Kanto -- a green caterpillar and a hairy stinging one, both grubs."),
  ("FELINE",3,"arch:feline",["Meowth","Mew"],"Meowth is a house cat with a lucky-charm coin on its forehead, and Mew a playful, floating kitten -- both are cat-like."),
  ("ARMADILLO",3,"arch:armadillo",["Sandshrew"],"Sandshrew is based on a pangolin or armadillo, curling into a hard-shelled ball when threatened."),
], exclude=ex("ability:own-tempo","arch:primate","arch:caterpillar","arch:feline","arch:armadillo","arch:pangolin",
              extra=["Slowbro","Slowking","Primeape","Machoke","Machamp","Metapod","Kakuna","Butterfree","Beedrill","Persian","Sandslash","Mewtwo","Eevee","Jolteon","Flareon","Vaporeon","Cubone","Marowak","Golduck","Psyduck","Snorlax","Kangaskhan","Clefairy","Hitmonchan","Hitmonlee","Venonat","Paras","Parasect","Tauros","Vulpix","Ninetales","Growlithe","Arcanine"]))
board("2026-11-27","mixed","Hard",[
  ("TANGLED-FEET",5,"ability:tangled-feet",["Spinda","Chatot","Flamigo"],"All three have the Ability Tangled Feet, which raises their evasion while they are confused."),
  ("WOODLOUSE",4,"arch:isopod",["Golisopod"],"Golisopod is based on an isopod (a giant pill-bug/sea slater) -- the crustacean cousin of the woodlouse."),
  ("PARLIAMENT",3,"arch:owl",["Hoothoot","Rowlet"],"A group of owls is called a parliament -- Hoothoot is a classic owl standing on one foot, and Rowlet a round little owl chick."),
  ("BOAR",3,"arch:boar",["Swinub","Oinkologne"],"Swinub is a tiny wild-boar piglet and Oinkologne a bigger, scent-spraying pig -- both are swine/boar-based."),
  ("DROMEDARY",3,"arch:camelid",["Numel"],"Numel is based on a camel, and its hump holds volcanic magma instead of water."),
], exclude=ex("ability:tangled-feet","arch:isopod","arch:owl","arch:boar","arch:camelid","arch:pig",
              extra=["Mr. Rime","Mr. Mime","Noctowl","Dartrix","Decidueye","Mamoswine","Piloswine","Camerupt","Wimpod","Pignite","Emboar","Tepig","Bouffalant","Miltank","Tauros","Wooloo","Lechonk","Mudsdale","Stantler","Wyrdeer","Girafarig","Hoppip","Natu","Xatu","Delibird","Farigiraf","Dodrio","Swanna","Ducklett","Kricketune","Slither Wing"]))


# ===== gap fill (nightly 2026-11-14 run 3): 11-28 Sat BRUTAL =====
board("2026-11-28","gen1","Brutal",[
  ("TRADE",5,"evo:trade",["Kadabra","Machoke","Graveler"],"Kadabra, Machoke and Graveler only evolve when they're traded to another player -- into Alakazam, Machamp and Golem."),
  ("ERIKA",3,"trainer:erika",["Vileplume","Weepinbell","Tangela"],"Celadon City Gym Leader Erika, the nature-loving Grass specialist, uses Vileplume and Tangela in Red and Blue, and Weepinbell in Pokémon Yellow."),
  ("POISON",1,"type:poison",["Vileplume","Weepinbell","Gengar"],"Vileplume and Weepinbell are Grass/Poison and Gengar is Ghost/Poison -- the board's only Poison-types."),
  ("HYPNOSIS",4,"move:hypnosis",["Gengar","Poliwrath"],"Both learn the move Hypnosis as they level up: Gengar's family uses it to put prey to sleep before feeding on their dreams, and Poliwrath's swirl-bellied line is famous for it."),
  ("STONE",5,"evo:stone",["Vileplume","Poliwrath","Arcanine"],"Each was evolved with an evolution stone: Vileplume from Gloom with a Leaf Stone, Poliwrath from Poliwhirl with a Water Stone, and Arcanine from Growlithe with a Fire Stone."),
], exclude=["Gastly","Haunter","Drowzee","Hypno","Poliwag","Poliwhirl","Exeggcute","Exeggutor","Victreebel","Gloom","Golem","Alakazam","Machamp",
            "Ninetales","Clefable","Wigglytuff","Nidoqueen","Nidoking","Starmie","Cloyster","Raichu","Vaporeon","Jolteon","Flareon","Geodude","Onix","Growlithe","Seaking"],
  hints={"Kadabra":("SPOON",2,"Kadabra always grips a silver spoon, which amplifies the psychic alpha waves it gives off."),
         "Machoke":("MOVERS",3,"Machoke loves heavy work -- the Pokédex says it is often hired to help people move house."),
         "Graveler":("ROLLING",3,"Graveler is a living boulder with four stubby arms that rolls down mountain paths, eating rocks as it goes."),
         "Vileplume":("PETALS",2,"Vileplume carries some of the largest petals in the world, which scatter clouds of toxic pollen."),
         "Weepinbell":("HOOK",2,"Weepinbell hangs from branches by the hook on its head, with a wide mouth for swallowing bugs."),
         "Tangela":("BOOTS",2,"Tangela's body is hidden under a mass of blue vines -- only its eyes and little red boots poke out."),
         "Gengar":("GRIN",2,"Gengar's sprite is all wide, toothy grin and glowing red eyes."),
         "Poliwrath":("SWIRL",2,"Poliwrath has its family's tell-tale swirl on its belly -- now on a muscular, swimming-champion body."),
         "Arcanine":("MANE",2,"Arcanine's thick, flowing mane and tiger stripes make it look like a regal Chinese guardian lion.")})
board("2026-11-28","mixed","Brutal",[
  ("SHINOBI",4,"job:ninja",["Greninja","Ninjask","Accelgor"],"Shinobi is the Japanese word for a ninja, and all three are styled as ninja: Greninja is the Ninja Pokémon, hurling shuriken made of water; Ninjask moves so fast it seems to vanish; and Accelgor wears a ninja's mask and wraps."),
  ("KNIGHT",3,"job:knight",["Escavalier","Sirfetch'd","Gallade"],"Each is a knight: Escavalier is the Cavalry Pokémon, jousting with lance arms in borrowed armour; Sirfetch'd carries a leek lance and shield like a chivalrous warrior; and Gallade is the Blade Pokémon, a courteous swordsman sworn to protect."),
  ("SWAP",5,"evo:swap-trade",["Accelgor","Escavalier"],"These two evolve by being traded FOR EACH OTHER: Karrablast steals Shelmet's shell and becomes the armoured Escavalier, while the freed Shelmet sheds its shell and becomes the speedy Accelgor."),
  ("SHARPNESS",5,"ability:sharpness",["Gallade","Veluza","Kleavor"],"Gallade, Veluza and Kleavor can have the Ability Sharpness, which powers up their slicing moves (like Psycho Cut, Aqua Cutter and Stone Axe) by 50%."),
  ("TONGUE",2,"sprite:tongue",["Greninja","Heatmor"],"Look at the sprites: Greninja wears its long pink tongue wrapped round its neck like a scarf, and Heatmor's long tongue flicks out of its snout like a flame."),
], exclude=["Froakie","Frogadier","Nincada","Shedinja","Shelmet","Karrablast","Dragapult","Drakloak","Dreepy","Bisharp","Kingambit","Pawniard","Aegislash","Doublade","Honedge",
            "Corviknight","Corvisquire","Rookidee","Zacian","Zamazenta","Cobalion","Terrakion","Virizion","Keldeo","Samurott","Dewott","Oshawott","Ceruledge","Armarouge","Lucario",
            "Farfetch'd","Gardevoir","Kirlia","Ralts","Kartana","Lickitung","Lickilicky","Shellder","Haunter","Kecleon","Banette","Gengar","Alakazam","Machamp","Golem","Politoed","Slowking","Steelix","Scizor","Kingdra","Porygon2","Rhyperior","Electivire","Magmortar","Porygon-Z","Dusknoir","Milotic","Huntail","Gorebyss","Gigalith","Conkeldurr","Aromatisse","Slurpuff","Trevenant","Gourgeist","Hawlucha","Sneasel","Weavile","Zoroark","Bastiodon","Durant","Electrike","Trapinch","Klinklang","Corphish"],
  hints={"Greninja":("SHURIKEN",3,"Greninja hurls throwing stars made of compressed water -- its signature move is Water Shuriken."),
         "Ninjask":("FAST",3,"Ninjask is one of the fastest Pokémon of all -- it moves so quickly it seems invisible, and you can hear its cry but not see it."),
         "Accelgor":("WRAPS",2,"Accelgor's body is bound in mummy-like wraps to stop it drying out, with a mask like a ninja's."),
         "Escavalier":("LANCE",2,"Escavalier charges with two lance-shaped arms, wearing the shell it took from Shelmet as armour."),
         "Sirfetch'd":("LEEK",2,"Sirfetch'd wields a giant leek as a lance and a leek leaf as a shield."),
         "Gallade":("ELBOWS",2,"Gallade extends sharp swords from its elbows to fight."),
         "Veluza":("FISH",3,"Veluza is a sleek, sword-shaped fish that sheds its own flesh to sharpen its mind."),
         "Kleavor":("AXE",2,"Kleavor's arms are heavy stone axes, chipped from the rock it lives on."),
         "Heatmor":("CHIMNEY",2,"Heatmor's tail has a hole like a chimney, sucking in air to fuel the fire on its tongue.")})

# ===== 11-29 Sun : EVIL =====
board("2026-11-29","gen1","Evil",[
  ("FIRST",4,"lore:firsts",["Bulbasaur","Rhydon","Porygon"],"Three famous firsts: Bulbasaur is #001 in the National Pokédex, Rhydon was the very first Pokémon ever designed, and Porygon is the first man-made Pokémon, built from computer code."),
  ("TRI-ATTACK",4,"move:tri-attack",["Dodrio","Porygon"],"Both learn the move Tri Attack as they level up -- fitting for three-headed Dodrio, and for angular Porygon, which fires its triangle of fire, ice and electricity."),
  ("HP",5,"stat:hp",["Snorlax","Wigglytuff","Vaporeon"],"These three have the highest base HP on the board -- Snorlax 160, Wigglytuff 140 and Vaporeon 130 -- built to soak up hits."),
  ("BRUNO",4,"trainer:bruno",["Hitmonchan","Machamp"],"Bruno, the fighting master of the Kanto Elite Four, battles with Hitmonchan and Machamp (alongside two Onix and Hitmonlee)."),
  ("ASH",3,"trainer:ash",["Bulbasaur","Snorlax"],"Both joined Ash Ketchum's team in the anime: his loyal Bulbasaur from Cerulean's hidden village, and the big, sleepy Snorlax he caught in the Orange Islands."),
], exclude=["Chansey","Lapras","Jigglypuff","Doduo","Dugtrio","Magnemite","Magneton","Pikachu","Mew","Mewtwo","Charmander","Squirtle","Onix","Hitmonlee",
            "Charizard","Kingler","Krabby","Muk","Tauros","Butterfree","Pidgeotto","Pidgeot","Caterpie","Metapod","Primeape","Ivysaur","Venusaur","Kangaskhan","Machop","Machoke","Diglett","Mankey"],
  hints={"Bulbasaur":("SEED",2,"Bulbasaur carries a plant seed on its back from birth, and it grows bigger as Bulbasaur does."),
         "Rhydon":("HORN",2,"Rhydon has a drill-like horn on its snout, strong enough to shatter boulders."),
         "Porygon":("DIGITAL",3,"Porygon is made entirely of computer code, and can travel through cyberspace."),
         "Dodrio":("HEADS",2,"Dodrio has three heads -- the Pokédex says one feels joy, one sorrow and one anger."),
         "Snorlax":("SLEEPY",3,"Snorlax spends its days eating and sleeping, often blocking roads while it naps."),
         "Wigglytuff":("BALLOON",2,"Wigglytuff's body is so soft and stretchy that it can inflate like a balloon."),
         "Vaporeon":("FINS",2,"Vaporeon has a mermaid-like tail fin and frilled fins around its head."),
         "Hitmonchan":("BOXER",3,"Hitmonchan is a boxer, throwing punches faster than the eye can see."),
         "Machamp":("FOUR",2,"Machamp's four muscular arms can throw 500 punches a second.")})
board("2026-11-29","mixed","Evil",[
  ("MOMOTARO",4,"lore:momotaro",["Okidogi","Munkidori","Fezandipiti"],"In the Japanese folk tale of Momotarō, the peach boy is joined by a dog, a monkey and a pheasant -- the Loyal Three Okidogi, Munkidori and Fezandipiti are those companions, recast in Kitakami's legend as Ogerpon's foes."),
  ("FRISK",5,"ability:frisk",["Munkidori","Furret"],"Both can have the Ability Frisk, which lets them peek at the opposing Pokémon's held item the moment they enter battle."),
  ("TECHNICIAN",5,"ability:technician",["Fezandipiti","Cinccino","Kricketune"],"All three can have the Ability Technician, which powers up their weaker moves (60 power or less) by 50%."),
  ("MUSICIAN",3,"job:musician",["Kricketune","Meloetta","Primarina"],"All three are musicians: Kricketune plays its arms like a violin, Meloetta is the Melody Pokémon whose songs move people's hearts, and Primarina is a pop-diva soloist who sings to shape its water balloons."),
  ("GENDERLESS",5,"gender:genderless",["Meloetta","Golett"],"Neither has a gender -- Meloetta is a mythical Pokémon, and Golett is an ancient clay automaton built by a lost civilisation. Every other Pokémon here can be male or female."),
], exclude=sorted(set(["Ogerpon","Rillaboom","Grookey","Thwackey","Brionne","Popplio","Jigglypuff","Wigglytuff","Exploud","Loudred","Whismur","Kricketot",
            "Chatot","Chimecho","Chingling","Kommo-o","Toxel","Toxtricity","Maschiff","Mabosstiff","Meowth","Persian","Mr. Mime","Scyther","Scizor","Smeargle","Hitmontop","Breloom","Roserade","Ambipom",
            "Mime Jr.","Minccino","Marshadow","Clobbopus","Grapploct","Maushold","Aipom","Mankey","Primeape","Infernape","Chimchar","Monferno","Pansage","Pansear","Panpour",
            "Simisage","Simisear","Simipour","Passimian","Oranguru","Sentret","Yanma","Stantler","Shuppet","Banette","Duskull","Dusclops","Yanmega","Dusknoir","Gothita",
            "Gothorita","Gothitelle","Phantump","Trevenant","Pumpkaboo","Gourgeist","Noibat","Noivern","Orbeetle","Impidimp","Morgrem","Grimmsnarl","Wyrdeer","Flittle","Espathra",
            "Golurk","Kingler","Yamper","Boltund","Houndstone","Greavard","Rockruff","Lycanroc","Mightyena","Poochyena","Shiftry","Nuzleaf","Lillipup","Herdier","Stoutland","Growlithe","Arcanine","Snubbull","Granbull","Furfrou","Electrike","Manectric"]+[n for n,r in FACTS.items() if r["gender"]=="genderless"])-{"Meloetta","Golett"}),
  hints={"Okidogi":("COLLAR",2,"Okidogi wears a spiky, glowing toxic chain round its neck like a collar."),
         "Munkidori":("MONKEY",3,"Munkidori is a small, fluffy monkey that uses its toxic chain to fill foes with dread."),
         "Fezandipiti":("PHEASANT",3,"Fezandipiti is a gorgeous pheasant whose bright feathers and toxic chain charm everyone around it."),
         "Furret":("LONG",2,"Furret's body is so long and thin that it can slip into burrows other Pokémon can't follow it into."),
         "Cinccino":("SCARF",2,"Cinccino's white fur wraps round its body like a fluffy scarf, coated in an oil that repels dust."),
         "Kricketune":("VIOLIN",2,"Kricketune's arms are shaped like violin bows, and it plays its body to make melodies."),
         "Meloetta":("SONG",3,"Meloetta is the Melody Pokémon -- its singing can move hearts and even change its own form."),
         "Primarina":("SIREN",3,"Primarina is a sea-lion siren -- its singing controls the water balloons it uses in battle."),
         "Golett":("CLAY",2,"Golett is made of clay, an ancient automaton said to be built to protect people and Pokémon.")})

# ===== 11-30 Mon : EASY =====
board("2026-11-30","gen1","Easy",[
  ("GRASS",1,"type:grass",["Ivysaur","Bellsprout","Exeggcute"],"Ivysaur, Bellsprout and Exeggcute are the board's only Grass-types -- a budding seed-dinosaur, a bell-headed flycatcher plant and a clutch of six seeds."),
  ("ELECTRIC",1,"type:electric",["Pikachu","Jolteon"],"Pikachu and Jolteon are the board's only Electric-types -- the electric mouse mascot and Eevee's spiky, crackling Thunder Stone evolution."),
  ("ROCK",1,"type:rock",["Omanyte","Geodude"],"Omanyte (Rock/Water) and Geodude (Rock/Ground) are the board's only Rock-types -- a fossil ammonite and a living boulder."),
  ("GEM",2,"sprite:gem",["Starmie","Persian"],"Look at the sprites: Starmie has a glittering red jewel at its core, and Persian a red gem set in its forehead."),
], exclude=["Staryu","Meowth"],
  hints={"Ivysaur":("BUD",2,"Ivysaur has a big pink flower bud on its back that's about to bloom."),
         "Bellsprout":("THIN",2,"Bellsprout has a skinny, stalk-thin body topped by a bell-shaped head."),
         "Exeggcute":("SIX",2,"Exeggcute is a cluster of six egg-like seeds that talk to each other by telepathy."),
         "Pikachu":("CHEEKS",2,"Pikachu stores electricity in the red pouches on its cheeks."),
         "Jolteon":("NEEDLES",2,"Jolteon's fur bristles into sharp, needle-like spikes when it's charged up."),
         "Omanyte":("SPIRAL",2,"Omanyte hides its soft body in a spiral shell -- it's revived from a fossil."),
         "Geodude":("BOULDER",2,"Geodude is a round boulder with two strong arms and no legs."),
         "Starmie":("SPIN",3,"Starmie spins its star-shaped body like a propeller to swim through the sea."),
         "Persian":("ELEGANT",3,"Persian is a sleek, elegant cat -- proud, fussy and famously hard to tame.")})
board("2026-11-30","mixed","Easy",[
  ("DARK",1,"type:dark",["Sneasel","Nickit","Umbreon"],"Sneasel (Dark/Ice), Nickit and Umbreon are the board's only Dark-types -- a sly claw-thief, a sneaky fox cub and the moonlight eeveelution."),
  ("FLYING",1,"type:flying",["Hoppip","Swablu"],"Hoppip (Grass/Flying) and Swablu (Normal/Flying) are the board's only Flying-types -- a dandelion puff that drifts on the breeze and a little bird with cotton-cloud wings."),
  ("DRAGON",1,"type:dragon",["Axew","Dreepy"],"Axew and Dreepy (Dragon/Ghost) are the board's only Dragon-types -- a tusked little dragon and the ghost of an ancient one."),
  ("CANDLE",2,"object:candle",["Litwick"],"Litwick is a living candle -- its flame glows by burning the life energy of anyone it lures close."),
  ("ICE-CREAM",2,"food:ice-cream",["Vanillite"],"Vanillite is a scoop of soft-serve ice cream on an icicle cone, said to have formed from snow."),
], exclude=["Lampent","Chandelure","Vanillish","Vanilluxe","Alcremie","Milcery","Swirlix","Slurpuff","Sinistea","Polteageist"],
  hints={"Sneasel":("CLAWS",2,"Sneasel has long, hooked claws for climbing trees and snatching eggs from nests."),
         "Nickit":("TAIL",2,"Nickit sweeps away its own footprints with its big, bushy tail."),
         "Umbreon":("RINGS",2,"Umbreon's black fur is marked with yellow rings that glow in the dark."),
         "Hoppip":("LEAVES",2,"Hoppip floats on the wind using the three round leaves on its head."),
         "Swablu":("COTTON",2,"Swablu's wings are like fluffy tufts of cotton -- it loves to perch on people's heads."),
         "Axew":("TUSKS",2,"Axew's tusks grow back sharper and stronger every time they break."),
         "Dreepy":("SPIRIT",3,"Dreepy is the restless spirit of a dragon that lived in the sea long ago."),
         "Litwick":("FLAME",2,"Litwick's head flame burns brighter when it absorbs life energy."),
         "Vanillite":("SCOOP",2,"Vanillite looks like a little scoop of soft-serve on an icicle base.")})

# ===== 12-01 Tue : MEDIUM =====
board("2026-12-01","gen1","Medium",[
  ("GROUND",1,"type:ground",["Cubone","Diglett"],"Cubone and Diglett are the board's only Ground-types -- a lonely bone-wielder and a little mole that never leaves the soil."),
  ("ICE",1,"type:ice",["Dewgong","Articuno"],"Dewgong (Water/Ice) and Articuno (Ice/Flying) are the board's only Ice-types."),
  ("MISTY",3,"trainer:misty",["Psyduck","Goldeen","Horsea","Staryu"],"Misty, Cerulean City's Water-type Gym Leader, travelled with Psyduck, Goldeen, Horsea and Staryu in the anime -- and battles with Staryu in the games."),
  ("SINGER",3,"job:singer",["Jigglypuff"],"Jigglypuff is the board's singer -- its lullaby sends everyone to sleep, and in the anime it gets furious when its audience dozes off."),
  ("UNICORN",2,"sprite:single-horn",["Dewgong","Goldeen"],"Look at the sprites: like a unicorn, each has a single horn -- a small white one on Dewgong's forehead, and a long, sharp one on Goldeen's head."),
], exclude=["Starmie","Poliwag","Poliwhirl","Poliwrath","Gyarados","Seaking","Wigglytuff","Lapras","Clefairy","Clefable","Chansey","Jynx",
            "Rhyhorn","Rhydon","Nidoking","Nidorino","Nidoran♂","Rapidash","Ponyta","Tauros","Weedle","Marowak","Dugtrio","Seel"],
  hints={"Cubone":("SKULL",2,"Cubone wears the skull of its late mother as a helmet."),
         "Diglett":("SOIL",3,"Diglett lives underground and only ever pokes its head up out of the soil."),
         "Dewgong":("BLUBBER",3,"Dewgong's thick blubber keeps it warm in freezing seas."),
         "Articuno":("BIRD",3,"Articuno is a legendary bird of ice whose wing-beats chill the air and make it snow."),
         "Psyduck":("HEADACHE",3,"Psyduck always has a headache -- when it gets bad enough, it unleashes psychic powers."),
         "Goldeen":("FINS",2,"Goldeen's flowing fins look like a ball gown -- it's called the Water Queen."),
         "Horsea":("INK",3,"Horsea squirts ink from its snout to escape predators."),
         "Staryu":("CORE",2,"Staryu's red core glows -- it can regrow any lost limb as long as the core survives."),
         "Jigglypuff":("LULLABY",3,"Jigglypuff sings a soothing lullaby that sends anyone who hears it to sleep.")})
board("2026-12-01","mixed","Medium",[
  ("STEEL",1,"type:steel",["Tinkatink","Varoom","Klefki"],"Tinkatink (Fairy/Steel), Varoom (Steel/Poison) and Klefki (Steel/Fairy) are the board's only Steel-types."),
  ("BUG",1,"type:bug",["Nymble","Dewpider"],"Nymble and Dewpider (Water/Bug) are the board's only Bug-types -- a hopping grasshopper and a little diving spider."),
  ("NURSE",3,"job:nurse",["Audino","Blissey"],"Both are Pokémon Center nurses: Audino assists Nurse Joy in Unova, and Blissey (Chansey's evolution) works alongside her in Johto and beyond."),
  ("POKEBALL",2,"object:pokeball",["Foongus","Amoonguss"],"Look at their caps: Foongus and Amoonguss are mushrooms patterned like Poké Balls -- a disguise they use to lure Pokémon and trainers close."),
], exclude=["Voltorb","Electrode","Chansey","Happiny","Comfey","Alomomola","Indeedee","Tinkatuff","Tinkaton","Revavroom"],
  hints={"Tinkatink":("HAMMER",2,"Tinkatink swings a little hammer it forged itself from scrap metal."),
         "Varoom":("ENGINE",2,"Varoom is a living car engine -- it revs its exhaust pipes to scare off foes."),
         "Klefki":("KEYS",2,"Klefki is a little key ring that collects keys and never lets go of one it likes."),
         "Nymble":("HOPPER",3,"Nymble is a little grasshopper that springs on its prey with its powerful hind legs."),
         "Dewpider":("HELMET",2,"Dewpider wears a helmet-like bubble of water on its head so it can breathe when it comes up on land."),
         "Audino":("EARS",2,"Audino's curly ear-feelers can listen to a heartbeat to check how someone is feeling."),
         "Blissey":("EGG",2,"Blissey carries a precious egg in its belly pouch, which it shares with the sick."),
         "Foongus":("DECOY",3,"Foongus's Poké Ball-patterned cap is a decoy -- anyone who reaches for it gets a puff of poison spores."),
         "Amoonguss":("SPORES",3,"Amoonguss waves its Poké Ball-patterned arm-caps to lure prey, then blasts them with spores.")})

# ===== 12-02 Wed : CHALLENGING =====
board("2026-12-02","gen1","Challenging",[
  ("FAIRY",1,"type:fairy",["Clefable","Mr. Mime"],"Clefable and Mr. Mime (Psychic/Fairy) are the board's only Fairy-types."),
  ("SHELL",2,"sprite:shell",["Cloyster","Blastoise","Omastar","Kabuto"],"Look at the sprites: each lives in a hard shell -- Cloyster's spiky clam, Blastoise's cannon-fitted turtle shell, and the fossil shells of Omastar and Kabuto."),
  ("PUNCH",4,"move:elemental-punch",["Jynx","Electabuzz","Magmar"],"Each learns its own elemental punch as it levels up: Jynx gets Ice Punch, Electabuzz Thunder Punch and Magmar Fire Punch."),
], exclude=["Shellder","Slowbro","Slowpoke","Kabutops","Omanyte","Squirtle","Wartortle","Krabby","Kingler","Lapras","Metapod","Kakuna","Dewgong",
            "Hitmonchan","Hitmonlee","Machop","Machoke","Machamp","Primeape","Mankey","Poliwrath"],
  hints={"Clefable":("MOON",3,"Clefable lives on quiet mountains and is said to dance in the moonlight."),
         "Mr. Mime":("WALLS",3,"Mr. Mime mimes invisible walls so convincingly that they become real barriers."),
         "Cloyster":("SPIKES",2,"Cloyster's shell is covered in spikes and is said to be harder than diamond."),
         "Blastoise":("CANNONS",2,"Blastoise fires powerful jets of water from the cannons on its shell."),
         "Omastar":("FOSSIL",3,"Omastar is an ancient fossil Pokémon -- its shell grew so heavy that it could no longer hunt, and it died out."),
         "Kabuto":("EYES",2,"Kabuto peers out with glowing eyes from under its domed fossil shell."),
         "Jynx":("LIPS",2,"Jynx has big, pouting lips -- and sways as if dancing when it walks."),
         "Electabuzz":("STRIPES",2,"Electabuzz has tiger-like black stripes on its yellow body."),
         "Magmar":("FIREBALL",2,"Magmar's body is wreathed in flames, like a walking fireball.")})
board("2026-12-02","mixed","Challenging",[
  ("GHOST",1,"type:ghost",["Mimikyu","Phantump","Dhelmise"],"Mimikyu (Ghost/Fairy), Phantump (Ghost/Grass) and Dhelmise (Ghost/Grass) are the board's only Ghost-types."),
  ("TREE",2,"object:tree",["Phantump","Sudowoodo"],"Both look like trees: Phantump is a spirit living in an old tree stump, and Sudowoodo disguises itself as a tree to avoid being attacked."),
  ("FRUIT",3,"food:fruit",["Applin","Smoliv"],"Both are fruit: Applin is a tiny dragon living inside an apple, and Smoliv is an olive -- it even squirts bitter oil from its head."),
  ("COURIER",3,"job:delivery",["Pelipper","Delibird"],"Both make deliveries: Pelipper carries mail and small Pokémon in its huge bill (it runs the post in Pokémon Mystery Dungeon), and Delibird carries food in its tail to share, attacking with Present."),
  ("BREAD",3,"food:bread",["Dachsbun"],"Dachsbun's body smells of freshly baked bread -- its name blends dachshund and bun, and its fur is like a golden crust."),
], exclude=["Trevenant","Exeggutor","Tropius","Bonsly","Torterra","Grotle","Abomasnow","Snover","Brambleghast","Bramblin","Arboliva","Dolliv","Smoliv","Seedot","Nuzleaf","Shiftry",
            "Flapple","Appletun","Dipplin","Hydrapple","Cherubi","Cherrim","Bounsweet","Steenee","Tsareena","Exeggcute","Wingull","Corviknight","Corvisquire","Rookidee","Fidough","Sinistea","Polteageist","Gourgeist","Pumpkaboo"],
  hints={"Mimikyu":("SHEET",2,"Mimikyu hides under a homemade Pikachu-costume sheet -- no one has seen what's underneath."),
         "Phantump":("TWIGS",2,"Phantump is a lost spirit possessing an old tree stump, with little twigs for horns."),
         "Dhelmise":("ANCHOR",2,"Dhelmise is a ghostly seaweed clinging to a ship's anchor, which it swings at foes."),
         "Sudowoodo":("FAKE",3,"Sudowoodo pretends to be a tree -- but it's really a Rock-type that hates water."),
         "Applin":("WORM",3,"Applin is a tiny dragon living inside an apple, and it hardly ever comes out."),
         "Smoliv":("OIL",3,"Smoliv squirts a bitter-tasting oil from its head to drive off attackers."),
         "Pelipper":("BEAK",2,"Pelipper carries smaller Pokémon and eggs around in its huge, pouch-like beak."),
         "Delibird":("PRESENT",3,"Delibird carries food in its bag-like tail and shares it -- its signature move is Present."),
         "Dachsbun":("DOUGH",3,"Dachsbun's fur is the colour of a golden crust, and its body smells like freshly baked dough.")})

# ===== 12-03 Thu : HARD =====
board("2026-12-03","gen1","Hard",[
  ("GIOVANNI",3,"trainer:giovanni",["Kangaskhan","Dugtrio"],"Giovanni -- Viridian City's Gym Leader and secretly the boss of Team Rocket -- battles with Kangaskhan and Dugtrio (plus Persian, Rhyhorn, Rhydon and the Nido king and queen)."),
  ("MOTHER",4,"lore:mother",["Kangaskhan","Marowak"],"Both are famous mothers: Kangaskhan raises its baby in its belly pouch, and the ghost haunting Lavender Town's Pokémon Tower is a Marowak -- Cubone's mother, whose skull Cubone wears."),
  ("THREE",2,"sprite:three",["Dugtrio","Exeggutor","Magneton"],"Look at the sprites: Dugtrio is three Diglett, Exeggutor has three coconut heads, and Magneton is three Magnemite joined together."),
  ("ALOLA",4,"form:alola",["Dugtrio","Exeggutor","Marowak"],"All three have Alolan forms: Dugtrio grows golden metal hair, Exeggutor becomes a towering Grass/Dragon palm tree, and Marowak a Fire/Ghost fire-dancer."),
  ("BIRD",3,"arch:bird",["Pidgeotto","Fearow","Zapdos","Moltres"],"Pidgeotto, Fearow, Zapdos and Moltres are all birds -- a hawk-like hunter, a long-beaked brute, and two of Kanto's three legendary birds."),
], exclude=["Persian","Rhyhorn","Rhydon","Nidoking","Nidoqueen","Nidorino","Cubone","Chansey","Dodrio","Doduo","Magnemite","Weezing","Diglett",
            "Rattata","Raticate","Raichu","Sandshrew","Sandslash","Vulpix","Ninetales","Meowth","Geodude","Graveler","Golem","Grimer","Muk","Exeggcute",
            "Pidgey","Pidgeot","Spearow","Farfetch'd","Articuno","Aerodactyl","Zubat","Golbat"],
  hints={"Kangaskhan":("POUCH",2,"Kangaskhan raises its baby in a pouch on its belly."),
         "Marowak":("CLUB",2,"Marowak wields a thick bone like a club."),
         "Dugtrio":("TUNNELS",3,"Dugtrio digs tunnels as deep as 60 miles underground."),
         "Exeggutor":("PALM",2,"Exeggutor is a walking palm tree with three coconut-like heads."),
         "Magneton":("SCREWS",2,"Magneton is three Magnemite linked together, each with screws on its sides."),
         "Pidgeotto":("TALONS",2,"Pidgeotto grips its prey in sharp talons and carries it miles back to its nest."),
         "Fearow":("BEAK",2,"Fearow has a long, thin beak for plucking prey from water and soil."),
         "Zapdos":("THUNDER",3,"Zapdos is the legendary bird of thunder, said to grow stronger when struck by lightning."),
         "Moltres":("PHOENIX",3,"Moltres is the legendary bird of fire -- a phoenix whose wings blaze with flame.")})
board("2026-12-03","mixed","Hard",[
  ("SPACE",4,"lore:space",["Beheeyem","Minior","Solrock"],"All three come from outer space: Beheeyem is a 'grey alien' said to have arrived by UFO, Minior forms in the ozone layer and falls as a meteor, and Solrock is said to have fallen to Earth from space."),
  ("WITCH",3,"job:witch",["Mismagius","Hatterene"],"Both are witches: Mismagius is shaped like a witch's pointed hat and robe and chants curses, and Hatterene is the Silent Pokémon, a forest witch in a wide-brimmed hat."),
  ("LEVITATE",5,"ability:levitate",["Mismagius","Solrock"],"Mismagius and Solrock both have the Ability Levitate, which lets them float in the air and makes them immune to Ground-type moves."),
  ("CAKE",3,"food:cake",["Alcremie","Slurpuff"],"Both are desserts: Alcremie is a decorated cream cake, and Slurpuff a fluffy whipped-cream treat that works with pâtissiers thanks to its amazing nose."),
  ("CROWN",2,"sprite:crown",["Slowking","Kingambit"],"Look at the sprites: both wear a crown -- Slowking the spiral Shellder crown that made it a genius, and Kingambit the golden crown-blade of a general that commands an army of Bisharp."),
], exclude=sorted(set(["Deoxys","Elgyem","Clefairy","Clefable","Cleffa","Lunatone","Celesteela","Necrozma","Rayquaza","Jirachi","Cosmog","Cosmoem","Solgaleo","Lunala","Palkia","Dialga","Arceus","Hoopa",
            "Staryu","Starmie","Nihilego","Buzzwole","Pheromosa","Xurkitree","Kartana","Guzzlord","Poipole","Naganadel","Stakataka","Blacephalon",
            "Murkrow","Honchkrow","Misdreavus","Hattrem","Hatenna","Alakazam","Delphox","Braixen","Gothitelle",
            "Milcery","Swirlix","Vanillite","Vanillish","Vanilluxe","Dachsbun","Fidough","Sinistea","Polteageist",
            "Calyrex","Empoleon","Prinplup","Pyroar","Bisharp","Pawniard","Slowbro","Slowpoke","Nidoking","Kingdra"]+[n for n,r in FACTS.items() if "Levitate" in r["abilities"]])-{"Mismagius","Solrock"}),
  hints={"Beheeyem":("UFO",3,"Beheeyem looks like a classic grey alien and is said to have arrived in a UFO."),
         "Minior":("METEOR",3,"Minior forms in the ozone layer and falls as a meteor -- its shell cracks to reveal a coloured core."),
         "Solrock":("SUN",2,"Solrock is a sun-shaped rock that gains power from sunlight."),
         "Mismagius":("ROBE",2,"Mismagius's body looks like a witch's robe topped with a pointed hat, and it chants spells that cause headaches."),
         "Hatterene":("HAIR",2,"Hatterene lashes out with the long, claw-like tendril of hair on its head."),
         "Alcremie":("BERRY",2,"Alcremie decorates its whipped-cream body with berries and sweets."),
         "Slurpuff":("SNIFF",3,"Slurpuff's sense of smell is millions of times better than a human's -- pastry chefs use it to sniff out flavours."),
         "Slowking":("THINKER",3,"Ever since a Shellder bit its head, Slowking has become a genius thinker."),
         "Kingambit":("COMMANDER",3,"Kingambit is the general of a Bisharp army -- it only joins the fight when its troops are in trouble.")})

# ===== 12-04 Fri : HARD =====
board("2026-12-04","gen1","Hard",[
  ("AGATHA",4,"trainer:agatha",["Arbok","Haunter","Golbat"],"Agatha, the ghost-loving veteran of the Kanto Elite Four (and Professor Oak's old rival), battles with Arbok, Haunter and Golbat -- plus two Gengar."),
  ("SPEED",5,"stat:speed",["Electrode","Aerodactyl","Alakazam"],"These are the board's speed demons -- the only ones with base Speed of 120 or more: Electrode (150), Aerodactyl (130) and Alakazam (120)."),
  ("SPOON",2,"sprite:spoon",["Kadabra","Alakazam"],"Look at the sprites: Kadabra holds a silver spoon, and Alakazam one in each hand -- the spoons amplify their psychic power."),
  ("DELICACY",3,"food:delicacy",["Slowpoke","Farfetch'd"],"Both are said to be tasty: Slowpoke tails are sold as a delicacy (they grow back), and Farfetch'd was hunted close to extinction -- its Japanese name comes from a saying about a duck arriving with its own leek."),
], exclude=["Ekans","Meowth","Koffing","Weezing","Victreebel","Gastly","Gengar","Zubat","Snorlax","Jynx","Slowbro","Abra",
            "Mewtwo","Jolteon","Dugtrio","Starmie","Persian","Tauros","Raichu","Dodrio","Scyther","Rapidash","Electabuzz","Pidgeot","Zapdos","Voltorb","Tentacruel","Ninetales","Mew","Fearow","Charizard"],
  hints={"Arbok":("HOOD",2,"Arbok spreads a hood marked with a scary face pattern to frighten off foes."),
         "Golbat":("FANGS",2,"Golbat's huge mouth is lined with sharp fangs, and it can drain a lot of blood in one go."),
         "Haunter":("HANDS",2,"Haunter's floating, disembodied hands can pass through walls."),
         "Electrode":("BALL",2,"Electrode looks like a giant Poké Ball, and explodes at the slightest shock."),
         "Aerodactyl":("AMBER",3,"Aerodactyl was revived from ancient DNA preserved in a piece of old amber."),
         "Alakazam":("GENIUS",3,"Alakazam's huge brain gives it an IQ of around 5,000 -- it never forgets anything."),
         "Kadabra":("STAR",2,"Kadabra has a red star on its forehead and wavy lines across its belly."),
         "Slowpoke":("DOZY",3,"Slowpoke is so dozy it takes five seconds to notice it's been hurt."),
         "Farfetch'd":("LEEK",2,"Farfetch'd always carries a stalk of leek, which it uses as a sword.")})
board("2026-12-04","mixed","Hard",[
  ("YOKAI",5,"myth:yokai",["Froslass","Shiftry","Lombre"],"Each is based on a yōkai, a spirit of Japanese folklore: Froslass on the yuki-onna snow woman who freezes travellers, Shiftry on the long-nosed, fan-wielding tengu, and Lombre on the river-dwelling kappa."),
  ("CHLOROPHYLL",5,"ability:chlorophyll",["Shiftry","Whimsicott","Deerling"],"Shiftry, Whimsicott and Deerling can have the Ability Chlorophyll, which doubles their Speed in harsh sunlight."),
  ("SWORDSMAN",3,"job:swordsman",["Samurott","Ceruledge"],"Both are sword-fighters: Samurott draws the seamitar blades from its shell armour in a flash, and Ceruledge burns with the grudge of a fallen sword-wielder, its arms ending in blades of ghostly fire."),
  ("BELL",2,"object:bell",["Chimecho","Bronzong"],"Look at them: Chimecho is a wind chime, and Bronzong a great bronze temple bell."),
], exclude=sorted(set(["Ninetales","Vulpix","Golduck","Psyduck","Lotad","Ludicolo","Musharna","Munna","Drowzee","Hypno","Nuzleaf","Seedot","Zorua","Zoroark","Snorunt","Glalie",
            "Ogerpon","Spiritomb","Gallade","Aegislash","Doublade","Honedge","Kartana","Kingambit","Bisharp","Pawniard","Dewott","Oshawott","Escavalier","Sirfetch'd","Zacian",
            "Cobalion","Terrakion","Virizion","Keldeo","Farfetch'd","Scyther","Kleavor","Armarouge","Chingling","Bronzor","Weepinbell"]+[n for n,r in FACTS.items() if "Chlorophyll" in r["abilities"]])-{"Shiftry","Whimsicott","Deerling"}),
  hints={"Froslass":("KIMONO",2,"Froslass looks like a snow-white woman in a kimono, with an icy hair ornament."),
         "Shiftry":("FANS",2,"Shiftry's hands are big leaf fans that whip up gale-force winds."),
         "Lombre":("LILY",2,"Lombre wears a lily pad on its head like a hat."),
         "Whimsicott":("FLUFF",2,"Whimsicott's body is a big puff of fluff, which it uses to slip through gaps like the wind."),
         "Deerling":("SEASONS",3,"Deerling's coat changes colour and scent with the seasons."),
         "Samurott":("ARMOUR",2,"Samurott wears shell armour and draws its seamitar blades from it to fight."),
         "Ceruledge":("BLADES",2,"Ceruledge's arms end in blades of blue spirit-fire."),
         "Chimecho":("WIND",3,"Chimecho rides the wind like a wind chime, ringing out with cries."),
         "Bronzong":("RAIN",3,"Bronzong was once worshipped as a bringer of rain, and dug up from ancient tombs.")})

# ===== 12-05 Sat : BRUTAL =====
board("2026-12-05","gen1","Brutal",[
  ("ATTACK",5,"stat:attack",["Kingler","Machamp","Pinsir","Dragonite"],"These four hit hardest: Dragonite (134), Kingler and Machamp (130 each) and Pinsir (125) have the highest base Attack on the board."),
  ("LIFEGUARD",3,"job:lifeguard",["Dragonite","Lapras"],"Both rescue people at sea: Dragonite is said to guide shipwrecked sailors safely to land, and Lapras happily ferries people across the water on its back."),
  ("BAKU",5,"myth:baku",["Drowzee","Hypno"],"Drowzee and Hypno are based on the baku, a dream-eating spirit of Japanese folklore with a tapir's snout -- both feed on the dreams of sleeping people."),
  ("FRIENDSHIP",5,"evo:friendship",["Chansey","Eevee"],"Both evolve through friendship: a Chansey with a strong bond to its trainer becomes Blissey, and a devoted Eevee becomes Espeon by day or Umbreon by night."),
  ("WATER",1,"type:water",["Kingler","Lapras"],"Kingler and Lapras (Water/Ice) are the board's only Water-types."),
], exclude=["Rhydon","Flareon","Gyarados","Hitmonlee","Golem","Kabutops","Snorlax","Scyther","Mewtwo","Dodrio","Arcanine","Victreebel","Primeape","Muk","Krabby","Hitmonchan",
            "Golbat","Zubat","Pikachu","Raichu","Clefairy","Clefable","Jigglypuff","Wigglytuff","Machop","Machoke","Dratini","Dragonair","Tentacruel"],
  hints={"Kingler":("CLAW",2,"Kingler's one giant claw has 10,000 horsepower of crushing force."),
         "Machamp":("FOUR",2,"Machamp's four muscular arms can throw 500 punches a second."),
         "Pinsir":("HORNS",2,"Pinsir grips its foes between the two huge spiked horns on its head."),
         "Dragonite":("GENTLE",3,"Dragonite is a gentle, kind-hearted dragon that can circle the globe in just 16 hours."),
         "Lapras":("FERRY",3,"Lapras loves to ferry people across the sea on its back."),
         "Drowzee":("DREAMS",3,"Drowzee eats the dreams of sleeping people -- it especially likes fun ones."),
         "Hypno":("PENDULUM",2,"Hypno swings a pendulum to lull its targets into a hypnotic sleep."),
         "Chansey":("EGG",2,"Chansey carries a nutritious egg in its belly pouch, which it shares with the injured."),
         "Eevee":("EIGHT",3,"Eevee can evolve into eight different Pokémon -- more than any other.")})
board("2026-12-05","mixed","Brutal",[
  ("FEMALE",5,"gender:female",["Salazzle","Tsareena","Vespiquen","Mandibuzz"],"Every Salazzle, Tsareena, Vespiquen and Mandibuzz is female -- these species have no males at all."),
  ("KICK",3,"trait:kick",["Tsareena","Mienshao","Hitmontop"],"All three are famous kickers: Tsareena's signature move is Trop Kick, Mienshao lashes out with lightning-fast martial-arts kicks, and Hitmontop spins on its head like a top, kicking as it whirls."),
  ("BONES",2,"sprite:bones",["Mandibuzz","Houndoom"],"Look at the sprites: Mandibuzz wraps itself in bones like a harness, and Houndoom wears bone-like bands across its back and legs."),
  ("UNNERVE",5,"ability:unnerve",["Vespiquen","Houndoom"],"Vespiquen and Houndoom can have the Ability Unnerve, which makes the opposing Pokémon too nervous to eat their held Berries."),
  ("REGENERATOR",5,"ability:regenerator",["Mienshao","Toxapex","Tangrowth"],"Mienshao, Toxapex and Tangrowth can have the Ability Regenerator, which restores a third of their HP whenever they switch out."),
], exclude=sorted(set(["Hitmonlee","Hitmonchan","Tyrogue","Lopunny","Lokix","Nymble","Pheromosa","Blaziken","Combusken","Cinderace","Raboot","Scorbunny","Sawk","Mienfoo","Buneary","Hawlucha","Quaquaval","Medicham","Kubfu",
            "Cubone","Marowak","Houndour","Vullaby","Lucario"]
            +[n for n,r in FACTS.items() if r["gender"]=="female-only" or "Unnerve" in r["abilities"] or "Regenerator" in r["abilities"]])
            -{"Salazzle","Tsareena","Vespiquen","Mandibuzz","Mienshao","Toxapex","Tangrowth","Houndoom"}),
  hints={"Salazzle":("LIZARD",3,"Salazzle is a slinky poison lizard that lures foes with a sweet-smelling toxic gas."),
         "Tsareena":("LEGS",2,"Tsareena's long, elegant legs deliver its famous Trop Kick."),
         "Vespiquen":("HIVE",2,"Vespiquen's abdomen is a honeycomb hive where its grubs live."),
         "Mandibuzz":("VULTURE",3,"Mandibuzz is a vulture that dresses itself in bones it has collected."),
         "Mienshao":("WHIPS",2,"Mienshao's long arm fur works like whips in battle."),
         "Hitmontop":("WHIRL",3,"Hitmontop spins on the horn on its head like a top, lashing out with kicks as it whirls."),
         "Houndoom":("HORNS",2,"Houndoom has curved horns -- the bigger and backward-sweeping they are, the higher it ranks in its pack."),
         "Toxapex":("DOME",2,"Toxapex hides inside a dome made of its own poisonous, spiky legs."),
         "Tangrowth":("VINES",2,"Tangrowth is a huge tangle of vines that grow back as fast as they're torn off.")})

# ===== 12-06 Sun : EVIL =====
board("2026-12-06","gen1","Evil",[
  ("TRANSFORM",4,"move:transform",["Ditto","Mew"],"Both can use Transform to become an exact copy of their opponent -- it's the only move Ditto knows, and Mew learns it from the very start."),
  ("SPECIAL",5,"stat:special",["Mewtwo","Gengar"],"These two have the highest Special stat on the board (Mewtwo 154, Gengar 130) -- the Gen I stat that powered both special attack and special defence."),
  ("DEFENSE",5,"stat:defense",["Onix","Golem"],"Onix (160) and Golem (130) have the highest base Defense on the board -- living fortresses of solid rock."),
  ("MOON-STONE",5,"evo:moon-stone",["Nidorina","Nidorino","Clefairy"],"All three evolve when exposed to a Moon Stone: Nidorina into Nidoqueen, Nidorino into Nidoking, and Clefairy into Clefable."),
  ("PSYCHIC",1,"type:psychic",["Mew","Mewtwo"],"Mew and Mewtwo are the board's only Psychic-types."),
], exclude=["Alakazam","Exeggutor","Zapdos","Moltres","Articuno","Cloyster","Omastar","Graveler","Rhydon","Slowbro","Sandslash","Kabutops","Geodude",
            "Jigglypuff","Wigglytuff","Nidoqueen","Nidoking","Clefable","Nidoran♀","Nidoran♂"],
  hints={"Ditto":("BLOB",2,"Ditto is a pink blob that can rearrange its cells to copy anything it sees."),
         "Mew":("ANCESTOR",3,"Mew is said to carry the DNA of every Pokémon -- the ancestor of them all."),
         "Mewtwo":("CLONE",3,"Mewtwo was created by scientists from Mew's DNA."),
         "Gengar":("SHADOW",3,"Gengar lurks in the shadows and steals the warmth from anyone nearby."),
         "Onix":("SNAKE",3,"Onix is a giant snake of boulders that tunnels underground at high speed."),
         "Golem":("BOULDER",2,"Golem is a huge living boulder that sheds its shell once a year."),
         "Nidorina":("SPINES",2,"Nidorina folds down its poison spines when it relaxes with its friends."),
         "Nidorino":("HORN",2,"Nidorino's horn is harder than diamond and full of venom."),
         "Clefairy":("METRONOME",3,"Clefairy wags its finger to use Metronome -- a move that could be anything.")})
board("2026-12-06","mixed","Evil",[
  ("PUPPY",4,"genus:puppy",["Rockruff","Yamper","Fidough"],"All three are listed in the Pokédex as the Puppy Pokémon."),
  ("SUN",4,"genus:sun",["Espeon","Volcarona"],"Espeon and Volcarona are both the Sun Pokémon in the Pokédex -- Espeon draws power from sunlight, and Volcarona was worshipped as a stand-in for the sun when volcanic ash blotted it out."),
  ("FLAME-BODY",5,"ability:flame-body",["Volcarona","Coalossal"],"Volcarona and Coalossal can have the Ability Flame Body, which may burn any Pokémon that touches them."),
  ("FUTURE",4,"lore:future",["Xatu","Espeon","Delphox"],"All three can see what's coming: Xatu is said to watch the past with one eye and the future with the other, Espeon predicts its foe's moves from shifts in the air, and Delphox gazes into the flame on its stick to see the future."),
  ("GALAR",3,"region:galar",["Yamper","Coalossal","Cramorant"],"Yamper, Coalossal and Cramorant all debuted in the Galar region, in Pokémon Sword and Shield."),
], exclude=sorted(set(["Growlithe","Lillipup","Maschiff","Snubbull","Houndour","Poochyena","Electrike","Sunflora","Sunkern","Solrock","Solgaleo","Helioptile","Heliolisk","Castform",
            "Natu","Absol","Braixen","Fennekin","Gardevoir","Kirlia","Ralts","Celebi","Dialga","Jirachi","Arrokuda","Barraskewda",
            "Meowth","Ponyta","Rapidash","Slowpoke","Slowbro","Farfetch'd","Weezing","Mr. Mime","Corsola","Zigzagoon","Darumaka","Yamask","Stunfisk","Articuno","Zapdos","Moltres"]
            +[n for n,r in FACTS.items() if "Flame Body" in r["abilities"] or r["gen"]==8])-{"Volcarona","Coalossal","Yamper","Cramorant"}),
  hints={"Rockruff":("COLLAR",2,"Rockruff has a collar of rocks round its neck, which it rubs against others to show affection."),
         "Yamper":("CORGI",3,"Yamper is a corgi-like puppy that makes electricity in its tail when it runs."),
         "Fidough":("YEAST",3,"Fidough's body is made of dough, and the yeast in its breath helps make bread."),
         "Espeon":("GEM",2,"Espeon has a red gem on its forehead that glows when it uses its psychic power."),
         "Volcarona":("MOTH",3,"Volcarona is a great fiery moth whose wings scatter burning scales."),
         "Coalossal":("FURNACE",3,"Coalossal's body is a furnace of burning coal, hot enough to melt rock."),
         "Xatu":("TOTEM",3,"Xatu stands as still as a totem pole all day, gazing at the sun."),
         "Delphox":("WAND",2,"Delphox carries a burning twig like a wizard's wand."),
         "Cramorant":("GULP",3,"Cramorant gulps down whole fish -- and sometimes a surprised Pikachu -- without noticing.")})

# ===== 12-07 Mon : EASY =====
board("2026-12-07","gen1","Easy",[
  ("FIRE",1,"type:fire",["Charmander","Vulpix","Growlithe"],"Charmander, Vulpix and Growlithe are the board's only Fire-types."),
  ("POISON",1,"type:poison",["Ekans","Zubat","Bulbasaur"],"Ekans, Zubat (Poison/Flying) and Bulbasaur (Grass/Poison) are the board's only Poison-types."),
  ("PINK",1,"colour:pink",["Jigglypuff","Lickitung"],"Jigglypuff and Lickitung are the board's pink Pokémon -- a balloon-like singer and a long-tongued licker."),
  ("STARTER",1,"role:starter",["Charmander","Bulbasaur"],"Charmander and Bulbasaur are both Kanto starters, chosen in Professor Oak's lab at the start of Pokémon Red and Blue."),
  ("HORSESHOE",2,"sprite:horseshoe",["Magnemite"],"Magnemite floats along with a horseshoe magnet on each side of its round metal body."),
], exclude=["Squirtle","Wartortle","Blastoise","Ivysaur","Venusaur","Charmeleon","Charizard","Slowpoke","Slowbro","Chansey","Lickitung","Porygon","Exeggcute","Mew","Ditto",
            "Wigglytuff","Clefable","Clefairy","Mr. Mime","Jynx","Butterfree","Magneton","Pikachu","Eevee"],
  hints={"Charmander":("FLAME",2,"Charmander's tail flame shows how it's feeling -- it blazes when it's angry."),
         "Vulpix":("TAILS",2,"Vulpix is born with one white tail that splits into six curly red tails as it grows."),
         "Growlithe":("PUPPY",3,"Growlithe is the Puppy Pokémon -- loyal and brave, it barks to protect its territory."),
         "Ekans":("BACKWARDS",4,"Ekans is 'snake' spelt backwards."),
         "Zubat":("EYELESS",2,"Zubat has no eyes -- it finds its way using ultrasonic waves."),
         "Bulbasaur":("SEED",2,"Bulbasaur carries a plant seed on its back from the day it's born."),
         "Lickitung":("TONGUE",2,"Lickitung's tongue is twice as long as its body."),
         "Jigglypuff":("LULLABY",3,"Jigglypuff sings a soothing lullaby that sends anyone who hears it to sleep."),
         "Magnemite":("SCREWS",2,"Magnemite has a screw on each side of its body and floats using electromagnetism.")})
board("2026-12-07","mixed","Easy",[
  ("NORMAL",1,"type:normal",["Teddiursa","Skwovet","Zigzagoon"],"Teddiursa, Skwovet and Zigzagoon are the board's only Normal-types."),
  ("FIGHTING",1,"type:fighting",["Crabrawler","Hawlucha"],"Crabrawler and Hawlucha (Fighting/Flying) are the board's only Fighting-types."),
  ("LEGENDARY",1,"role:legendary",["Lugia","Ho-Oh"],"Lugia and Ho-Oh are legendary Pokémon -- the guardians of the sea and the sky, and the cover stars of Pokémon Silver and Gold."),
  ("AXOLOTL",3,"arch:axolotl",["Wooper"],"Wooper is based on an axolotl -- a pink Mexican salamander with feathery gills on its head."),
  ("SUSHI",3,"food:sushi",["Tatsugiri"],"Tatsugiri looks just like a piece of sushi -- its three forms mimic different toppings."),
], exclude=sorted(set(["Mudkip","Quagsire","Clodsire","Dondozo"]+[n for n,r in FACTS.items() if r["legendary"] or r["mythical"]])-{"Lugia","Ho-Oh"}),
  hints={"Teddiursa":("HONEY",3,"Teddiursa licks the honey that soaks into its paws -- the crescent on its forehead glows like the moon."),
         "Skwovet":("CHEEKS",2,"Skwovet stuffs berries into its huge cheeks so it always has a snack."),
         "Zigzagoon":("STRIPES",2,"Zigzagoon has zigzag stripes on its fur -- and walks in zigzags too."),
         "Crabrawler":("BOXER",3,"Crabrawler is a crab that punches like a boxer, aiming for the top of the tree it climbs."),
         "Hawlucha":("MASK",2,"Hawlucha wears a wrestler's mask and loves to show off its high-flying moves."),
         "Lugia":("SEA",3,"Lugia sleeps in a deep-sea trench -- a flap of its wings could cause a 40-day storm."),
         "Ho-Oh":("RAINBOW",3,"Ho-Oh's feathers shine in seven colours, leaving a rainbow wherever it flies."),
         "Wooper":("GILLS",2,"Wooper has feathery gills on its head."),
         "Tatsugiri":("SMALL",2,"Tatsugiri is a small, clever dragon that rides in Dondozo's mouth.")})

# ===== 12-08 Tue : MEDIUM =====
board("2026-12-08","gen1","Medium",[
  ("ELECTRIC",1,"type:electric",["Raichu","Jolteon"],"Raichu and Jolteon are the board's only Electric-types."),
  ("ROCK",1,"type:rock",["Rhyhorn","Geodude"],"Rhyhorn and Geodude (both Rock/Ground) are the board's only Rock-types."),
  ("LORELEI",3,"trainer:lorelei",["Dewgong","Cloyster","Slowbro"],"Lorelei, the Kanto Elite Four's Ice expert, battles with Dewgong, Cloyster and Slowbro (alongside Jynx and Lapras)."),
  ("BALLOON",4,"genus:balloon",["Wigglytuff"],"Wigglytuff is the Balloon Pokémon -- it can puff its soft, stretchy body up to a huge size."),
  ("MOLE",3,"arch:mole",["Diglett"],"Diglett is based on a mole -- it lives underground and only ever pokes its head out of the soil."),
], exclude=["Jynx","Lapras","Dugtrio","Jigglypuff","Koffing","Weezing","Shellder","Slowpoke"],
  hints={"Raichu":("TAIL",2,"Raichu's long, thin tail ends in a lightning-bolt tip and grounds its electricity."),
         "Jolteon":("NEEDLES",2,"Jolteon's fur bristles into sharp, needle-like spikes when it's charged up."),
         "Rhyhorn":("CHARGE",3,"Rhyhorn charges in a straight line, smashing through anything in its way."),
         "Geodude":("ARMS",2,"Geodude is a round rock with two strong arms -- and no legs."),
         "Dewgong":("BLUBBER",3,"Dewgong's thick blubber keeps it warm in freezing seas."),
         "Cloyster":("SPIKES",2,"Cloyster's shell is covered in spikes and is said to be harder than diamond."),
         "Slowbro":("SHELLDER",2,"Slowbro has a Shellder clamped onto its tail -- if it ever lets go, Slowbro turns back into Slowpoke."),
         "Wigglytuff":("PLUSH",2,"Wigglytuff's fur is so soft and fine that it feels like plush velvet."),
         "Diglett":("SOIL",3,"Diglett lives underground and only ever pokes its head up out of the soil.")})
board("2026-12-08","mixed","Medium",[
  ("DARK",1,"type:dark",["Zorua","Impidimp","Sableye"],"Zorua, Impidimp (Dark/Fairy) and Sableye (Dark/Ghost) are the board's only Dark-types."),
  ("DRAGON",1,"type:dragon",["Gible","Turtonator"],"Gible (Dragon/Ground) and Turtonator (Fire/Dragon) are the board's only Dragon-types."),
  ("PAINTER",3,"job:painter",["Smeargle"],"Smeargle is the Painter Pokémon -- it marks its territory by painting with the fluid from the brush-tip of its tail."),
  ("TAILOR",3,"job:tailor",["Leavanny"],"Leavanny is a tailor: it sews leaves together with sticky silk to make clothes for little Sewaddle."),
  ("MOUSTACHE",2,"sprite:moustache",["Whiscash","Stoutland"],"Look at the sprites: Whiscash has long catfish whiskers like a drooping moustache, and Stoutland a big, shaggy moustache of fur."),
], exclude=["Kricketune","Mr. Rime","Alakazam","Kadabra","Barboach","Mienshao","Mienfoo","Herdier","Lillipup","Emboar","Gumshoos","Grafaiai","Sewaddle","Swadloon"],
  hints={"Zorua":("ILLUSION",3,"Zorua tricks people by taking on the form of others with its illusions."),
         "Impidimp":("PRANK",3,"Impidimp loves mischief -- it sneaks into homes to steal people's energy."),
         "Sableye":("GEMS",2,"Sableye's eyes are sparkling gemstones -- it eats gems it digs up in caves."),
         "Gible":("JAWS",2,"Gible's huge jaws make up most of its body -- it ambushes prey from its cave."),
         "Turtonator":("SPIKES",2,"Turtonator's shell is covered in spikes that explode when touched."),
         "Smeargle":("BRUSH",2,"Smeargle's tail ends in a brush dripping with paint."),
         "Leavanny":("SEWING",3,"Leavanny is a master of sewing -- it stitches leaves together using the sharp cutters on its arms."),
         "Whiscash":("QUAKE",3,"Whiscash can sense earthquakes coming -- and is said to cause them when it thrashes."),
         "Stoutland":("CAPE",2,"Stoutland's thick fur drapes over its back like a warm cape.")})

# ===== 12-09 Wed : CHALLENGING =====
board("2026-12-09","gen1","Challenging",[
  ("GRASS",1,"type:grass",["Tangela","Exeggcute","Ivysaur"],"Tangela, Exeggcute (Grass/Psychic) and Ivysaur (Grass/Poison) are the board's only Grass-types."),
  ("KOGA",3,"trainer:koga",["Venomoth","Muk"],"Koga, the ninja master of Fuchsia City's Gym (and later the Elite Four), battles with poisonous Venomoth and Muk."),
  ("JELLYFISH",3,"arch:jellyfish",["Tentacool","Tentacruel"],"Tentacool and Tentacruel are the Jellyfish Pokémon -- they drift through the sea and sting with venomous tentacles."),
  ("ROADBLOCK",4,"lore:roadblock",["Snorlax"],"Snorlax famously blocks the road in Kanto -- you need the Poké Flute to wake it before you can get past on Routes 12 and 16."),
  ("SKULL",2,"sprite:skull",["Cubone"],"Look at the sprite: Cubone wears a skull as a helmet -- said to be the skull of its late mother."),
], exclude=["Koffing","Weezing","Venonat","Golbat","Zubat","Grimer","Marowak","Parasect"],
  hints={"Exeggcute":("SIX",2,"Exeggcute is a cluster of six egg-like seeds that talk to each other by telepathy."),
         "Ivysaur":("BUD",2,"Ivysaur has a big pink flower bud on its back that's about to bloom."),
         "Tangela":("VINES",2,"Tangela's whole body is hidden under a tangle of blue vines."),
         "Venomoth":("POWDER",3,"Venomoth's wings shed a powder that can paralyse or poison anyone it touches."),
         "Muk":("SLUDGE",2,"Muk is a heap of toxic sludge -- even its footprints are poisonous."),
         "Tentacool":("ORBS",2,"Tentacool's clear body has two red, crystal-like orbs that absorb sunlight."),
         "Tentacruel":("EIGHTY",3,"Tentacruel has 80 tentacles that it can stretch and shrink at will."),
         "Snorlax":("SLEEPY",3,"Snorlax spends its days eating and sleeping."),
         "Cubone":("CLUB",2,"Cubone wields a bone like a club.")})
board("2026-12-09","mixed","Challenging",[
  ("FLYING",1,"type:flying",["Wattrel","Starly","Rookidee"],"Wattrel (Electric/Flying), Starly (Normal/Flying) and Rookidee are the board's only Flying-types."),
  ("SHOVEL",2,"object:shovel",["Sandygast","Palossand"],"Look at the sprites: both have a toy shovel stuck in them -- Sandygast and Palossand are haunted sandcastles that drain the life from anyone who touches them."),
  ("SWEETS",3,"food:candy",["Swirlix"],"Swirlix is a ball of cotton candy -- it eats nothing but sweets, so its fur is sugary and sticky."),
  ("BUTLER",3,"job:butler",["Indeedee"],"Indeedee is the Emotion Pokémon and serves its trainer like a butler, sensing their feelings and seeing to their every need."),
  ("RIVALS",4,"lore:rivals",["Zangoose","Seviper"],"Zangoose and Seviper are famous rivals -- the Pokédex says they have been bitter enemies since ancient times and fight on sight."),
], exclude=["Slurpuff","Alcremie","Milcery","Vanillite","Vanillish","Vanilluxe","Mr. Mime","Mime Jr.","Mr. Rime",
            "Heatmor","Durant","Electabuzz","Magmar","Electivire","Magmortar","Throh","Sawk","Tornadus","Thundurus","Groudon","Kyogre","Dialga","Palkia","Xerneas","Yveltal","Scyther","Pinsir"],
  hints={"Wattrel":("SEABIRD",3,"Wattrel is a seabird that stores electricity in its wings and rides storm winds."),
         "Starly":("FLOCK",3,"Starly gather in huge flocks -- alone they're weak, but together their wingbeats are fierce."),
         "Rookidee":("BOLD",3,"Rookidee is a tiny bird that bravely picks fights with much bigger foes."),
         "Sandygast":("MOUND",2,"Sandygast is a little mound of haunted sand that grows by draining the life of anyone who touches it."),
         "Palossand":("TOWER",2,"Palossand is a towering sand castle that pulls in people who play nearby."),
         "Swirlix":("SUGAR",3,"Swirlix eats so many sweets that its fur is like sticky spun sugar."),
         "Indeedee":("HORNS",2,"Indeedee senses people's emotions through the horns on its head."),
         "Zangoose":("CLAWS",2,"Zangoose's razor-sharp claws are its main weapon against Seviper."),
         "Seviper":("BLADE",2,"Seviper's tail ends in a poisonous blade, which it sharpens on rocks.")})
