#!/usr/bin/env python3
"""
Hand-curated overlay for the daily fact bank — the SUBJECTIVE columns that can't
be pulled from data: real-world inspiration (based_on), distinctive sprite
features (sprite), signature move, Pokedex flavour / puns (lore), folklore origin
(mythology), distinctive location, popular trainer/character (trainer), fandom
nickname/meme (nickname), secondary colour, animal archetype (arch), and role.

Authored generation by generation. Fields are left EMPTY where a mon genuinely
has no famous trainer / meme / mythology — blank is correct, not fabricated.
Run this to (re)write curated_overlay.json, then run build_facts.py.
"""
import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
DATA={}
def E(name, arch=None, based=None, sprite=None, sig="", lore=None, myth=None,
      loc=None, trn=None, nick=None, c2="", role=None, wk=1):
    DATA[name]=dict(arch=arch or [], based_on=based or [], sprite=sprite or [],
        signature_move=sig, lore=lore or [], mythology=myth or [], location=loc or [],
        trainer=trn or [], nickname=nick or [], color_secondary=c2, role=role or [], wk=wk)

# ============================== GEN 1 (Kanto) ==============================
E("Bulbasaur", arch=["toad","dinosaur"], based=["frog","plant bulb","seed"], sprite=["back-bulb","fangs"], lore=["starter"], trn=["Ash"], role=["starter"], c2="teal")
E("Ivysaur", arch=["toad","dinosaur"], based=["frog","flower bud"], sprite=["back-bud","fangs"], c2="pink")
E("Venusaur", arch=["toad","dinosaur"], based=["frog","toad","rafflesia flower"], sprite=["back-flower","fangs"], sig="Frenzy Plant", role=["starter","mega","gmax"], c2="pink")
E("Charmander", arch=["lizard","salamander"], based=["salamander","fire lizard"], sprite=["flame-tail","claws"], lore=["starter","tail flame = life"], trn=["Ash"], role=["starter"], c2="cream")
E("Charmeleon", arch=["lizard","salamander"], based=["salamander"], sprite=["flame-tail","head-horn","claws"], c2="cream")
E("Charizard", arch=["dragon","lizard"], based=["dragon","winged fire lizard"], sprite=["wings","flame-tail","fangs"], sig="Blast Burn", lore=["not a Dragon type despite looks"], trn=["Ash"], role=["starter","mega","gmax"], nick=["fan favourite"], c2="cream")
E("Squirtle", arch=["turtle"], based=["turtle"], sprite=["shell","curl-tail"], lore=["starter"], trn=["Ash","Squirtle Squad"], role=["starter"], c2="brown")
E("Wartortle", arch=["turtle"], based=["turtle"], sprite=["shell","furry-ears","fluffy-tail"], c2="white")
E("Blastoise", arch=["turtle"], based=["tortoise","water cannons"], sprite=["shell","back-cannons"], sig="Hydro Cannon", role=["starter","mega","gmax"], c2="brown")
E("Caterpie", arch=["insect","caterpillar"], based=["caterpillar","swallowtail larva"], sprite=["antenna","osmeterium"], trn=["Ash"], c2="yellow")
E("Metapod", arch=["insect","pupa"], based=["chrysalis"], sprite=["hard-shell"], lore=["only knows Harden"])
E("Butterfree", arch=["insect","butterfly"], based=["butterfly","moth"], sprite=["wings","big-eyes"], trn=["Ash (released it)"], role=["gmax"], nick=["Ash's goodbye episode"], c2="blue")
E("Weedle", arch=["insect","caterpillar"], based=["hairy caterpillar","larva"], sprite=["nose-horn","tail-stinger"], c2="brown")
E("Kakuna", arch=["insect","pupa"], based=["cocoon"], sprite=["hard-shell"])
E("Beedrill", arch=["insect","wasp"], based=["wasp","hornet"], sprite=["arm-stingers","wings","tail-stinger"], role=["mega"], c2="black")
E("Pidgey", arch=["bird"], based=["pigeon","sparrow"], sprite=["beak","crest"], trn=["Ash"], c2="cream")
E("Pidgeotto", arch=["bird","raptor"], based=["hawk","falcon"], sprite=["crest","talons"], c2="cream")
E("Pidgeot", arch=["bird","raptor"], based=["eagle","hawk"], sprite=["long-crest","wings"], role=["mega"], c2="cream")
E("Rattata", arch=["rodent","rat"], based=["rat"], sprite=["buck-teeth","whiskers"], nick=["FEAR strategy"], c2="cream")
E("Raticate", arch=["rodent","rat"], based=["rat"], sprite=["buck-teeth","whiskers"], nick=["Ash's Raticate (trade myth)"], c2="cream")
E("Spearow", arch=["bird"], based=["sparrow"], sprite=["beak","short-wings"], trn=["attacked Ash ep.1"], c2="pink")
E("Fearow", arch=["bird","raptor"], based=["eagle"], sprite=["long-beak","long-neck"], c2="pink")
E("Ekans", arch=["serpent","snake"], based=["cobra","snake"], sprite=["rattle-tail","fangs"], lore=["name = snake backwards"], trn=["Jessie (Team Rocket)"], c2="yellow")
E("Arbok", arch=["serpent","snake","cobra"], based=["cobra"], sprite=["hood-pattern","fangs"], lore=["name = kobra backwards"], trn=["Jessie (Team Rocket)"], c2="yellow")
E("Pikachu", arch=["rodent","mouse"], based=["mouse","pika"], sprite=["cheek-pouches","lightning-tail"], sig="Volt Tackle", loc=["Viridian Forest"], trn=["Ash","Pikachu"], role=["mascot","gmax"], nick=["franchise mascot"], c2="brown")
E("Raichu", arch=["rodent","mouse"], based=["mouse"], sprite=["cheeks","thin-tail"], c2="brown")
E("Sandshrew", arch=["pangolin","armadillo"], based=["pangolin","armadillo"], sprite=["curl","claws"], loc=["desert routes"], c2="cream")
E("Sandslash", arch=["pangolin","armadillo"], based=["pangolin","echidna"], sprite=["back-spikes","claws"], c2="brown")
E("Nidoran♀", arch=["rodent","rabbit"], based=["rabbit","poison rodent"], sprite=["small-spines","whiskers"], lore=["one of few gendered species"], c2="red")
E("Nidorina", arch=["rodent","rabbit"], based=["rabbit"], sprite=["spines","ears"], c2="cream")
E("Nidoqueen", arch=["pachyderm"], based=["rhino/armoured beast (queen)"], sprite=["scales","spikes","tail"], lore=["royalty (queen)"], role=[], c2="cream")
E("Nidoran♂", arch=["rodent","rabbit"], based=["rabbit","poison rodent"], sprite=["large-ears","forehead-horn"], c2="red")
E("Nidorino", arch=["rodent","rabbit"], based=["rabbit"], sprite=["horn","spines"], c2="red")
E("Nidoking", arch=["pachyderm"], based=["rhino/armoured beast (king)"], sprite=["head-horn","tail","scales"], sig="", lore=["royalty (king)"], c2="cream")
E("Clefairy", arch=["fairy"], based=["fairy","moon sprite"], sprite=["curl-forehead","small-wings"], myth=["arrived from space / moon"], loc=["Mt. Moon"], c2="pink")
E("Clefable", arch=["fairy"], based=["fairy","moon sprite"], sprite=["wings","pointed-ears"], myth=["moonlight folklore"], loc=["Mt. Moon"], c2="pink")
E("Vulpix", arch=["fox","canine"], based=["fox"], sprite=["curled-tails","curls"], myth=["kitsune (six-tailed fox)"], c2="orange")
E("Ninetales", arch=["fox","canine"], based=["nine-tailed fox"], sprite=["nine-tails","mane"], myth=["kitsune / kyubi (1000-year fox)"], nick=["curse lore"], c2="cream")
E("Jigglypuff", arch=["fairy"], based=["balloon","fairy"], sprite=["round-body","big-eyes","curl"], sig="Sing", lore=["draws on faces when you sleep"], trn=["anime singer"], role=["mascot"], c2="")
E("Wigglytuff", arch=["fairy"], based=["balloon","rabbit"], sprite=["round-body","rabbit-ears"], c2="")
E("Zubat", arch=["chiropteran","bat"], based=["bat"], sprite=["no-eyes","wings","fangs"], loc=["caves (everywhere)"], nick=["cave nuisance / Supersonic"], c2="purple")
E("Golbat", arch=["chiropteran","bat"], based=["bat"], sprite=["huge-mouth","fangs","wings"], c2="purple")
E("Oddish", arch=["plant"], based=["mandrake","nazuna weed"], sprite=["leaf-head","blue-body"], loc=["grass at night"], c2="green")
E("Gloom", arch=["plant"], based=["mandrake","corpse flower"], sprite=["drool","flower-head"], c2="orange")
E("Vileplume", arch=["plant"], based=["rafflesia (corpse flower)"], sprite=["giant-petals"], c2="red")
E("Paras", arch=["insect","crab"], based=["cicada nymph","cordyceps fungus"], sprite=["mushrooms","claws"], myth=["zombie fungus lore"], c2="orange")
E("Parasect", arch=["insect","crab"], based=["cicada + cordyceps"], sprite=["big-mushroom","dead-eyes"], lore=["the fungus controls the host"], myth=["cordyceps zombie"], c2="orange")
E("Venonat", arch=["insect"], based=["moth larva","fly"], sprite=["big-red-eyes","fur"], c2="red")
E("Venomoth", arch=["insect","moth"], based=["moth"], sprite=["wings","dust-scales"], c2="blue")
E("Diglett", arch=["mole"], based=["mole"], sprite=["nose","underground-body"], loc=["Diglett's Cave"], nick=["what's under Diglett?"], c2="brown")
E("Dugtrio", arch=["mole"], based=["moles (triplet)"], sprite=["three-heads"], loc=["Diglett's Cave"], c2="brown")
E("Meowth", arch=["feline","cat"], based=["cat","maneki-neko lucky cat"], sprite=["coin-charm","whiskers"], sig="Pay Day", myth=["maneki-neko (beckoning cat)"], trn=["Team Rocket (talking Meowth)"], role=["gmax"], nick=["Team Rocket's Meowth"], c2="")
E("Persian", arch=["feline","cat"], based=["cat","siamese"], sprite=["forehead-gem","whiskers"], trn=["Giovanni"], c2="")
E("Psyduck", arch=["duck","platypus"], based=["duck","platypus"], sprite=["blank-stare","headache-hands"], lore=["psychic when headache peaks"], trn=["Misty"], nick=["perpetual headache"], c2="cream")
E("Golduck", arch=["platypus"], based=["kappa","platypus"], sprite=["forehead-gem","webbed"], myth=["kappa (water sprite)"], c2="")
E("Mankey", arch=["primate","monkey"], based=["monkey","macaque"], sprite=["angry-face","fists"], lore=["always furious"], trn=["Ash (Primeape)"], c2="brown")
E("Primeape", arch=["primate","monkey"], based=["monkey"], sprite=["angry","fists","bound-hands"], sig="Rage Fist (via Annihilape)", c2="brown")
E("Growlithe", arch=["canine","dog"], based=["dog","shisa lion-dog"], sprite=["stripes","fluffy-mane"], trn=["Officer Jenny (Growlithe/Arcanine)"], c2="cream")
E("Arcanine", arch=["canine","dog"], based=["Chinese guardian lion (shisa)","kirin"], sprite=["stripes","mane"], lore=["'Legendary Pokemon' in the Pokedex"], myth=["shisa / komainu"], c2="cream")
E("Poliwag", arch=["frog","tadpole"], based=["tadpole"], sprite=["belly-swirl","tail"], lore=["swirl = visible guts"], c2="white")
E("Poliwhirl", arch=["frog"], based=["tadpole"], sprite=["belly-swirl","gloved-hands"], c2="white")
E("Poliwrath", arch=["frog"], based=["frog","boxer"], sprite=["muscles","belly-swirl"], c2="white")
E("Abra", arch=["psychic"], based=["psychic / yogi","fennec fox"], sprite=["sleeps-18h","fox-ears"], sig="Teleport", lore=["always asleep"], c2="brown")
E("Kadabra", arch=["psychic"], based=["Uri Geller (spoon-bender)","fox"], sprite=["spoon","forehead-star","whiskers"], lore=["Uri Geller lawsuit → absent for 20 years"], nick=["Uri Geller"], c2="yellow")
E("Alakazam", arch=["psychic"], based=["Uri Geller","psychic sage"], sprite=["twin-spoons","mustache","armour"], sig="", lore=["IQ 5000; huge brain"], role=["mega"], c2="yellow")
E("Machop", arch=["primate","humanoid"], based=["bodybuilder","superpower human"], sprite=["muscles","tail"], c2="")
E("Machoke", arch=["primate","humanoid"], based=["wrestler"], sprite=["muscles","power-save-belt"], c2="")
E("Machamp", arch=["primate","humanoid"], based=["four-armed wrestler","Asura"], sprite=["four-arms","belt"], sig="Dynamic Punch", role=["gmax"], c2="")
E("Bellsprout", arch=["plant"], based=["pitcher plant","bellflower"], sprite=["bell-head","stem-body"], c2="brown")
E("Weepinbell", arch=["plant"], based=["pitcher plant"], sprite=["pitcher-body","hook"], c2="")
E("Victreebel", arch=["plant"], based=["pitcher plant","venus flytrap"], sprite=["pitcher-mouth","vine"], trn=["James (Team Rocket)"], c2="yellow")
E("Tentacool", arch=["cnidarian","jellyfish"], based=["jellyfish"], sprite=["red-orbs","tentacles"], loc=["surfing on the sea"], c2="red")
E("Tentacruel", arch=["cnidarian","jellyfish"], based=["portuguese man o' war"], sprite=["red-jewels","tentacles"], c2="red")
E("Geodude", arch=["golem"], based=["rock","boulder"], sprite=["muscled-arms","rocky-body"], loc=["caves / Rock Tunnel"], nick=["Rock-throwing meme"], c2="")
E("Graveler", arch=["golem"], based=["boulder"], sprite=["four-arms","rocky-body"], c2="")
E("Golem", arch=["golem"], based=["boulder","golem"], sprite=["shell-plates","stubby-limbs"], sig="", myth=["golem"], c2="green")
E("Ponyta", arch=["equine","horse"], based=["horse"], sprite=["fire-mane","hooves"], c2="cream")
E("Rapidash", arch=["equine","horse","unicorn"], based=["unicorn","horse"], sprite=["fire-mane","horn"], c2="cream")
E("Slowpoke", arch=["hippo","salamander"], based=["axolotl","hippo"], sprite=["dopey-face","pink-tail"], lore=["takes 5s to feel pain"], nick=["derpy / slow"], c2="")
E("Slowbro", arch=["hippo"], based=["hermit + shellfish symbiosis"], sprite=["shell-on-tail"], lore=["Shellder bites its tail"], role=["mega"], c2="")
E("Magnemite", arch=["mineral"], based=["magnet","UFO"], sprite=["magnets","screws","single-eye"], c2="gray")
E("Magneton", arch=["mineral"], based=["magnets (three fused)","UFO"], sprite=["three-fused"], c2="gray")
E("Farfetch'd", arch=["bird","duck"], based=["wild duck with leek (kamo negi idiom)"], sprite=["leek-stalk","beak"], lore=["Japanese idiom 'duck comes with spring onions'"], c2="")
E("Doduo", arch=["bird","ratite"], based=["ostrich","emu"], sprite=["two-heads","long-legs"], c2="cream")
E("Dodrio", arch=["bird","ratite"], based=["ostrich (three heads)"], sprite=["three-heads","long-legs"], c2="cream")
E("Seel", arch=["pinniped","seal"], based=["sea lion","seal"], sprite=["horn","tusk"], c2="")
E("Dewgong", arch=["pinniped"], based=["dugong","sea lion"], sprite=["sleek-body","horn"], c2="")
E("Grimer", arch=["amorphous"], based=["sludge","pollution"], sprite=["ooze-body","grin"], myth=["born from polluted sludge"], c2="")
E("Muk", arch=["amorphous"], based=["toxic sludge","pollution"], sprite=["oozing-body"], role=["gmax"], c2="")
E("Shellder", arch=["mollusc","clam"], based=["clam","bivalve"], sprite=["tongue","clam-shell"], lore=["bites Slowpoke's tail"], c2="")
E("Cloyster", arch=["mollusc","bivalve"], based=["oyster (pearl)"], sprite=["spiked-shell","face-inside"], sig="", c2="purple")
E("Gastly", arch=["ghost"], based=["will-o'-wisp","poison gas","onibi"], sprite=["gas-cloud","eyes"], myth=["onibi / ghost gas"], loc=["Pokemon Tower"], c2="black")
E("Haunter", arch=["ghost"], based=["ghost","boogeyman"], sprite=["floating-hands","tongue"], loc=["Pokemon Tower"], c2="black")
E("Gengar", arch=["ghost"], based=["shadow / doppelganger (gengar = 'doppelganger')"], sprite=["wide-grin","spikes"], sig="", myth=["your shadow come alive"], trn=["Agatha"], role=["mega","gmax"], nick=["Clefable's shadow theory"], c2="")
E("Onix", arch=["serpent"], based=["rock snake","tunnelling serpent"], sprite=["boulder-body","head-horn"], loc=["Rock Tunnel"], trn=["Brock"], c2="")
E("Drowzee", arch=["tapir"], based=["tapir (baku dream-eater)"], sprite=["pendulum-hands","trunk"], myth=["baku (eats dreams)"], c2="yellow")
E("Hypno", arch=["tapir"], based=["hypnotist","baku"], sprite=["pendulum","collar-ruff"], sig="", myth=["baku dream-eater"], nick=["creepy dex entries"], c2="")
E("Krabby", arch=["crustacean","crab"], based=["crab"], sprite=["pincers","claws"], c2="white")
E("Kingler", arch=["crustacean","crab"], based=["crab (giant claw)"], sprite=["huge-claw"], trn=["Ash"], role=["gmax"], c2="")
E("Voltorb", arch=["mineral"], based=["Poke Ball"], sprite=["ball-shape","face"], lore=["disguised as a Poke Ball"], nick=["Self-Destruct troll"], c2="white")
E("Electrode", arch=["mineral"], based=["Poke Ball (upside down)"], sprite=["ball-shape","grin"], nick=["Explosion / suicide bomber"], c2="white")
E("Exeggcute", arch=["plant"], based=["eggs / seeds (coconut)"], sprite=["six-eggs","cracks"], lore=["actually seeds, not eggs"], c2="pink")
E("Exeggutor", arch=["plant"], based=["coconut palm tree"], sprite=["three-heads","palm-trunk"], nick=["Alolan long-neck meme"], c2="brown")
E("Cubone", arch=["mammal"], based=["orphaned dinosaur wearing a skull"], sprite=["skull-helmet","bone-club"], lore=["wears its dead mother's skull; cries"], myth=["Marowak ghost (Lavender Town)"], nick=["saddest backstory"], c2="brown")
E("Marowak", arch=["mammal"], based=["skull-wearing beast"], sprite=["skull-helmet","bone-club"], loc=["Pokemon Tower ghost"], myth=["vengeful ghost of its mother"], c2="brown")
E("Hitmonlee", arch=["humanoid"], based=["Bruce Lee (kickboxer)"], sprite=["spring-legs","no-head-neck"], sig="High Jump Kick", lore=["name from Bruce Lee"], nick=["Bruce Lee"], c2="")
E("Hitmonchan", arch=["humanoid"], based=["Jackie Chan (boxer)"], sprite=["boxing-gloves"], sig="", lore=["name from Jackie Chan"], nick=["Jackie Chan"], c2="")
E("Lickitung", arch=["mammal"], based=["licking beast","namekuji"], sprite=["long-tongue"], c2="cream")
E("Koffing", arch=["amorphous"], based=["poison gas balloon","sea mine"], sprite=["skull-and-crossbones","gas"], trn=["James (Team Rocket)"], c2="purple")
E("Weezing", arch=["amorphous"], based=["twin gas balloons","smog"], sprite=["twin-heads","gas"], trn=["James (Team Rocket)"], role=[], c2="purple")
E("Rhyhorn", arch=["pachyderm","rhino"], based=["rhinoceros","dinosaur"], sprite=["nose-horn","armour-hide"], trn=["Ash's mum races them"], c2="gray")
E("Rhydon", arch=["pachyderm","rhino"], based=["rhino","Godzilla-style kaiju"], sprite=["drill-horn","tail"], lore=["first Pokemon ever designed"], c2="gray")
E("Chansey", arch=["mammal"], based=["egg-bearing fairy","luck"], sprite=["belly-egg-pouch"], lore=["hard to catch; gives lots of XP"], trn=["Nurse Joy"], nick=["EXP grind / low catch rate"], c2="white")
E("Tangela", arch=["plant"], based=["mass of vines","seaweed"], sprite=["blue-vines","red-boots"], c2="blue")
E("Kangaskhan", arch=["marsupial","kangaroo"], based=["kangaroo (with joey)"], sprite=["belly-pouch","baby"], lore=["Genghis Khan pun"], role=["mega"], c2="")
E("Horsea", arch=["fish","seahorse"], based=["seahorse"], sprite=["snout","dorsal-fin"], c2="")
E("Seadra", arch=["fish","seahorse"], based=["seahorse","dragon"], sprite=["spines","fins"], c2="")
E("Goldeen", arch=["fish"], based=["goldfish"], sprite=["head-horn","flowing-fins"], nick=["only knows Splash/Peck meme"], c2="white")
E("Seaking", arch=["fish"], based=["goldfish","koi"], sprite=["head-horn","koi-fins"], c2="white")
E("Staryu", arch=["echinoderm","starfish"], based=["starfish"], sprite=["core-gem","star-shape"], trn=["Misty"], c2="brown")
E("Starmie", arch=["echinoderm","starfish"], based=["starfish (two stars)"], sprite=["core-gem","spinning"], trn=["Misty"], nick=["'it's a UFO'"], c2="purple")
E("Mr. Mime", arch=["humanoid"], based=["mime / clown"], sprite=["mime-gloves","invisible-walls"], sig="", lore=["makes invisible barriers"], trn=["Ash's mum's Mr. Mime (Mimey)"], c2="red")
E("Scyther", arch=["insect","mantis"], based=["praying mantis"], sprite=["scythe-arms","wings"], c2="cream")
E("Jynx", arch=["humanoid"], based=["opera singer","Yuki-onna / ganguro"], sprite=["gown","lips"], myth=["Yuki-onna (snow woman)"], nick=["design controversy"], c2="red")
E("Electabuzz", arch=["humanoid"], based=["oni (demon)"], sprite=["stripes","horns"], lore=["rival to Magmar"], c2="black")
E("Magmar", arch=["humanoid"], based=["oni","duck-billed fire beast"], sprite=["duck-bill","flame-body"], lore=["rival to Electabuzz"], c2="yellow")
E("Pinsir", arch=["insect","beetle"], based=["stag beetle"], sprite=["horn-pincers"], role=["mega"], c2="")
E("Tauros", arch=["bovine","bull"], based=["bull"], sprite=["three-tails","head-horns"], loc=["Safari Zone"], c2="cream")
E("Magikarp", arch=["fish","carp"], based=["carp (Chinese dragon-gate legend)"], sprite=["whiskers","floppy"], sig="Splash", myth=["carp leaping the dragon gate → becomes dragon"], nick=["most useless Pokemon"], c2="white")
E("Gyarados", arch=["serpent","dragon"], based=["Chinese dragon (carp that became a dragon)"], sprite=["serpent-body","fangs","barbels"], sig="", myth=["carp → dragon transformation"], role=["mega"], nick=["red Gyarados (Lake of Rage)"], c2="")
E("Lapras", arch=["plesiosaur"], based=["plesiosaur / Loch Ness Monster"], sprite=["shell-back","long-neck"], myth=["Nessie"], role=["gmax"], nick=["gentle ferry; near-extinct lore"], c2="gray")
E("Ditto", arch=["amorphous"], based=["amoeba / blob"], sprite=["pink-blob","dot-eyes"], sig="Transform", lore=["copies anything; breeding partner"], nick=["failed transformations (keeps its face)"], c2="")
E("Eevee", arch=["mammal","fox"], based=["fox / dog (evolution: 'eevee'='evolution')"], sprite=["fluffy-collar","bushy-tail"], lore=["unstable DNA; many evolutions"], role=["gmax","starter (Let's Go)"], nick=["Eeveelutions"], c2="cream")
E("Vaporeon", arch=["mermaid"], based=["mermaid / fish-cat"], sprite=["fins","frilled-collar"], lore=["Water Stone eeveelution"], nick=["copypasta"], role=["eeveelution"], c2="")
E("Jolteon", arch=["mammal"], based=["spiky electric fox"], sprite=["spiky-fur"], role=["eeveelution"], c2="white")
E("Flareon", arch=["mammal"], based=["fire fox/dog"], sprite=["fluffy-mane","fluffy-tail"], role=["eeveelution"], nick=["bad movepool discourse"], c2="yellow")
E("Porygon", arch=["mineral"], based=["polygon / 3D CGI / digital"], sprite=["blocky-body"], lore=["first man-made Pokemon"], nick=["banned seizure episode (blamed on Pikachu)"], c2="blue")
E("Omanyte", arch=["mollusc","ammonite"], based=["ammonite"], sprite=["spiral-shell","tentacles"], role=["fossil"], c2="blue")
E("Omastar", arch=["mollusc","ammonite"], based=["ammonite (giant)"], sprite=["spiral-shell","beak","spikes"], role=["fossil"], c2="blue")
E("Kabuto", arch=["arthropod","trilobite"], based=["horseshoe crab / trilobite"], sprite=["dome-shell","red-eyes"], role=["fossil"], c2="brown")
E("Kabutops", arch=["arthropod","trilobite"], based=["horseshoe crab (raptor form)"], sprite=["scythe-arms","shell"], role=["fossil"], c2="brown")
E("Aerodactyl", arch=["pterosaur","raptor"], based=["pterodactyl","dragon"], sprite=["wings","fangs"], role=["fossil","mega"], c2="gray")
E("Snorlax", arch=["bear"], based=["sleeping glutton (designer's friend)"], sprite=["big-belly","sleepy"], sig="", lore=["blocks roads; always sleeping/eating"], role=["gmax"], nick=["road blocker"], c2="cream")
E("Articuno", arch=["bird"], based=["ice bird / phoenix (freeze)"], sprite=["ice-wings","crest","tail"], loc=["Seafoam Islands"], role=["legendary"], nick=["legendary bird trio"], c2="")
E("Zapdos", arch=["bird"], based=["thunderbird (Native American myth)"], sprite=["spiky-wings","spiky-crest"], myth=["thunderbird"], loc=["Power Plant"], role=["legendary"], nick=["legendary bird trio"], c2="")
E("Moltres", arch=["bird","phoenix"], based=["phoenix / firebird"], sprite=["flame-wings","flame-crest"], myth=["phoenix"], loc=["Victory Road / Mt. Ember"], role=["legendary"], nick=["legendary bird trio"], c2="")
E("Dratini", arch=["serpent","dragon"], based=["Chinese dragon / mizuchi serpent"], sprite=["serpent-body","forehead-orb"], loc=["Safari Zone / Dragon's Den"], nick=["fishing rarity"], c2="white")
E("Dragonair", arch=["serpent","dragon"], based=["Chinese dragon / mystical serpent"], sprite=["neck-orbs","wing-crest"], myth=["dragon that controls weather"], c2="white")
E("Dragonite", arch=["dragon"], based=["Western dragon (but friendly/kind)"], sprite=["antennae","small-wings"], sig="", lore=["rescues sailors; gentle"], role=["pseudo"], nick=["fat dragon; carries mail"], c2="cream")
E("Mewtwo", arch=["humanoid"], based=["genetically-engineered clone of Mew"], sprite=["tube-neck","tail"], sig="Psystrike", lore=["cloned in Cinnabar Mansion; movie antagonist"], loc=["Cerulean Cave"], role=["legendary","mega"], nick=["first movie villain"], c2="purple")
E("Mew", arch=["mammal"], based=["cat / fetus (ancestor of all Pokemon)"], sprite=["small","long-tail"], sig="", lore=["contains all Pokemon DNA; ancestor of all"], role=["mythical"], nick=["truck myth (Mew under the truck)"], c2="")

# ---- bulk tables applied on top of the per-mon entries ----
SIG={}      # name -> best-known move
TEAMS={}    # "Trainer (role)" -> [mons on their notable team]

def _ensure(name):
    return DATA.setdefault(name, dict(arch=[],based_on=[],sprite=[],signature_move="",
        lore=[],mythology=[],location=[],trainer=[],nickname=[],color_secondary="",role=[],wk=1))

# === Gen 1 best-known moves ===
SIG.update({
 "Bulbasaur":"Vine Whip","Ivysaur":"Razor Leaf","Venusaur":"Solar Beam","Charmander":"Ember",
 "Charmeleon":"Flamethrower","Charizard":"Flamethrower","Squirtle":"Water Gun","Wartortle":"Water Pulse",
 "Blastoise":"Hydro Pump","Caterpie":"String Shot","Metapod":"Harden","Butterfree":"Sleep Powder",
 "Weedle":"Poison Sting","Kakuna":"Harden","Beedrill":"Twineedle","Pidgey":"Gust","Pidgeotto":"Wing Attack",
 "Pidgeot":"Hurricane","Rattata":"Quick Attack","Raticate":"Super Fang","Spearow":"Peck","Fearow":"Drill Peck",
 "Ekans":"Wrap","Arbok":"Glare","Pikachu":"Thunderbolt","Raichu":"Thunderbolt","Sandshrew":"Dig",
 "Sandslash":"Earthquake","Nidoran♀":"Scratch","Nidorina":"Bite","Nidoqueen":"Earthquake","Nidoran♂":"Horn Attack",
 "Nidorino":"Horn Attack","Nidoking":"Earthquake","Clefairy":"Metronome","Clefable":"Moonblast","Vulpix":"Ember",
 "Ninetales":"Flamethrower","Jigglypuff":"Sing","Wigglytuff":"Double-Edge","Zubat":"Leech Life","Golbat":"Wing Attack",
 "Oddish":"Absorb","Gloom":"Acid","Vileplume":"Petal Dance","Paras":"Spore","Parasect":"Spore","Venonat":"Confusion",
 "Venomoth":"Psychic","Diglett":"Dig","Dugtrio":"Earthquake","Meowth":"Pay Day","Persian":"Slash","Psyduck":"Confusion",
 "Golduck":"Hydro Pump","Mankey":"Karate Chop","Primeape":"Cross Chop","Growlithe":"Flamethrower","Arcanine":"Extreme Speed",
 "Poliwag":"Water Gun","Poliwhirl":"Body Slam","Poliwrath":"Submission","Abra":"Teleport","Kadabra":"Psybeam",
 "Alakazam":"Psychic","Machop":"Karate Chop","Machoke":"Submission","Machamp":"Dynamic Punch","Bellsprout":"Vine Whip",
 "Weepinbell":"Razor Leaf","Victreebel":"Razor Leaf","Tentacool":"Acid","Tentacruel":"Hydro Pump","Geodude":"Rock Throw",
 "Graveler":"Rock Slide","Golem":"Explosion","Ponyta":"Flame Wheel","Rapidash":"Fire Blast","Slowpoke":"Confusion",
 "Slowbro":"Psychic","Magnemite":"Thunder Shock","Magneton":"Thunderbolt","Farfetch'd":"Slash","Doduo":"Peck",
 "Dodrio":"Tri Attack","Seel":"Aurora Beam","Dewgong":"Ice Beam","Grimer":"Sludge","Muk":"Sludge Bomb","Shellder":"Clamp",
 "Cloyster":"Ice Beam","Gastly":"Lick","Haunter":"Night Shade","Gengar":"Shadow Ball","Onix":"Rock Throw","Drowzee":"Hypnosis",
 "Hypno":"Psychic","Krabby":"Crabhammer","Kingler":"Crabhammer","Voltorb":"Self-Destruct","Electrode":"Explosion",
 "Exeggcute":"Barrage","Exeggutor":"Psychic","Cubone":"Bone Club","Marowak":"Bonemerang","Hitmonlee":"High Jump Kick",
 "Hitmonchan":"Sky Uppercut","Lickitung":"Lick","Koffing":"Smog","Weezing":"Sludge Bomb","Rhyhorn":"Horn Attack",
 "Rhydon":"Earthquake","Chansey":"Soft-Boiled","Tangela":"Vine Whip","Kangaskhan":"Dizzy Punch","Horsea":"Smokescreen",
 "Seadra":"Hydro Pump","Goldeen":"Horn Attack","Seaking":"Megahorn","Staryu":"Swift","Starmie":"Psychic","Mr. Mime":"Barrier",
 "Scyther":"X-Scissor","Jynx":"Lovely Kiss","Electabuzz":"Thunder Punch","Magmar":"Fire Punch","Pinsir":"Guillotine",
 "Tauros":"Body Slam","Magikarp":"Splash","Gyarados":"Hydro Pump","Lapras":"Ice Beam","Ditto":"Transform","Eevee":"Quick Attack",
 "Vaporeon":"Hydro Pump","Jolteon":"Thunderbolt","Flareon":"Flamethrower","Porygon":"Tri Attack","Omanyte":"Water Gun",
 "Omastar":"Hydro Pump","Kabuto":"Scratch","Kabutops":"Slash","Aerodactyl":"Rock Slide","Snorlax":"Body Slam",
 "Articuno":"Ice Beam","Zapdos":"Thunder","Moltres":"Fire Blast","Dratini":"Wrap","Dragonair":"Dragon Rage",
 "Dragonite":"Hyper Beam","Mewtwo":"Psystrike","Mew":"Psychic",
})
# === Kanto gym leaders / Elite Four / Champion ===
TEAMS.update({
 "Brock (gym)":["Geodude","Onix"],
 "Misty (gym)":["Staryu","Starmie"],
 "Lt. Surge (gym)":["Voltorb","Pikachu","Raichu"],
 "Erika (gym)":["Victreebel","Tangela","Vileplume","Weepinbell","Gloom"],
 "Koga (gym)":["Koffing","Muk","Weezing","Golbat","Grimer","Venonat"],
 "Sabrina (gym)":["Kadabra","Mr. Mime","Venomoth","Alakazam"],
 "Blaine (gym)":["Growlithe","Ponyta","Rapidash","Arcanine","Magmar"],
 "Giovanni (gym)":["Rhyhorn","Dugtrio","Nidoqueen","Nidoking","Rhydon","Persian","Kangaskhan"],
 "Lorelei (E4)":["Dewgong","Cloyster","Slowbro","Jynx","Lapras"],
 "Bruno (E4)":["Onix","Hitmonlee","Hitmonchan","Machamp"],
 "Agatha (E4)":["Gengar","Golbat","Haunter","Arbok"],
 "Lance (E4/champion)":["Gyarados","Dragonair","Aerodactyl","Dragonite","Charizard","Kingdra"],
 "Blue (champion)":["Pidgeot","Alakazam","Rhydon","Exeggutor","Arcanine","Gyarados","Charizard","Blastoise","Venusaur"],
})

# ============================== GEN 2 (Johto) ==============================
E("Chikorita", arch=["dinosaur"], based=["sauropod","leaf"], sprite=["head-leaf"], lore=["starter"], role=["starter"], c2="green")
E("Bayleef", arch=["dinosaur"], based=["sauropod","laurel"], sprite=["leaf-buds-neck"], c2="green")
E("Meganium", arch=["dinosaur"], based=["sauropod","flower"], sprite=["neck-petals","antennae"], role=["starter"], c2="pink")
E("Cyndaquil", arch=["mammal"], based=["echidna","shrew"], sprite=["back-flames"], lore=["starter"], role=["starter"], c2="cream")
E("Quilava", arch=["mammal"], based=["echidna","badger"], sprite=["flame-vents"], c2="cream")
E("Typhlosion", arch=["mammal"], based=["honey badger","volcano"], sprite=["flame-collar"], role=["starter"], c2="cream")
E("Totodile", arch=["reptile","crocodile"], based=["crocodile"], sprite=["jaws","spikes"], lore=["starter"], role=["starter"], c2="yellow")
E("Croconaw", arch=["reptile","crocodile"], based=["crocodile"], sprite=["jaws","spikes"], c2="yellow")
E("Feraligatr", arch=["reptile","crocodile"], based=["crocodile","gharial"], sprite=["jaws","fangs","spikes"], role=["starter"], c2="red")
E("Sentret", arch=["rodent"], based=["ferret","meerkat"], sprite=["scout-tail"], c2="cream")
E("Furret", arch=["mustelid"], based=["ferret"], sprite=["long-body","stripes"], c2="cream")
E("Hoothoot", arch=["bird","owl"], based=["owl"], sprite=["one-foot","clock-eyes"], lore=["stands on one foot; internal clock"], c2="cream")
E("Noctowl", arch=["bird","owl"], based=["owl"], sprite=["horns","triangle-brows"], trn=["Ash"], c2="cream")
E("Ledyba", arch=["insect","beetle"], based=["ladybug"], sprite=["spots"], c2="black")
E("Ledian", arch=["insect","beetle"], based=["ladybug"], sprite=["star-spots","arms"], lore=["draws power from starlight"], myth=["star folklore"], c2="black")
E("Spinarak", arch=["arachnid","spider"], based=["spider"], sprite=["face-pattern","web"], c2="yellow")
E("Ariados", arch=["arachnid","spider"], based=["spider"], sprite=["face-pattern","legs"], c2="yellow")
E("Crobat", arch=["chiropteran","bat"], based=["bat (four wings)"], sprite=["four-wings","fangs"], lore=["evolves via friendship; silent flight"], c2="purple")
E("Chinchou", arch=["fish"], based=["anglerfish","frogfish"], sprite=["antennae-lights"], c2="yellow")
E("Lanturn", arch=["fish"], based=["anglerfish"], sprite=["lure-light"], lore=["'the deep-sea star' (glows)"], c2="yellow")
E("Pichu", arch=["rodent","mouse"], based=["baby mouse"], sprite=["cheeks","big-ears"], lore=["baby Pikachu; shocks itself"], role=["baby"], nick=["Spiky-eared Pichu"], c2="black")
E("Cleffa", arch=["fairy"], based=["star sprite"], sprite=["star-shape","curl"], role=["baby"], c2="pink")
E("Igglybuff", arch=["fairy"], based=["balloon"], sprite=["round","curl"], role=["baby"], c2="")
E("Togepi", arch=["fairy"], based=["egg (Fabergé)"], sprite=["eggshell","spikes"], lore=["hatched by Misty; symbol of luck"], trn=["Misty (anime)"], role=["baby"], nick=["Misty's Togepi"], c2="cream")
E("Togetic", arch=["fairy"], based=["egg fairy","angel"], sprite=["wings","belly-spikes"], c2="white")
E("Natu", arch=["bird"], based=["totem pole","quail chick"], sprite=["big-eyes","wings-pattern"], c2="green")
E("Xatu", arch=["bird"], based=["totem pole","Native American shaman"], sprite=["eye-wings"], lore=["stares at the sun; sees past & future"], myth=["mystic seer"], c2="green")
E("Mareep", arch=["mammal"], based=["sheep"], sprite=["wool","tail-orb"], nick=["Electric Sheep (Do Androids Dream)"], c2="blue")
E("Flaaffy", arch=["mammal"], based=["sheep"], sprite=["bare-patches","wool"], c2="pink")
E("Ampharos", arch=["mammal"], based=["sheep","lighthouse beacon"], sprite=["tail-orb","glow"], lore=["light seen from space (Olivine lighthouse 'Amphy')"], trn=["Jasmine (gym)"], role=["mega"], c2="cream")
E("Bellossom", arch=["plant"], based=["hula dancer","flower"], sprite=["skirt-petals"], c2="red")
E("Marill", arch=["mammal"], based=["blue mouse","water rat"], sprite=["ball-tail","round-ears"], nick=["'Pikablu' (pre-release mix-up)"], c2="white")
E("Azumarill", arch=["mammal"], based=["rabbit","water rat"], sprite=["ball-tail","belly-pattern"], c2="white")
E("Sudowoodo", arch=["plant-mimic"], based=["fake tree (bonsai)"], sprite=["tree-arms"], lore=["Rock-type that mimics a tree; hates water"], loc=["blocks Route 36 (needs Squirtbottle)"], nick=["not a tree"], c2="green")
E("Politoed", arch=["frog"], based=["frog (king)"], sprite=["curl-head","throat"], lore=["evolves from Poliwhirl via King's Rock"], c2="yellow")
E("Hoppip", arch=["plant"], based=["dandelion","cottonweed"], sprite=["leaf","float"], c2="green")
E("Skiploom", arch=["plant"], based=["dandelion"], sprite=["flower-head"], c2="green")
E("Jumpluff", arch=["plant"], based=["dandelion seed head"], sprite=["cotton-puffs"], c2="blue")
E("Aipom", arch=["primate","monkey"], based=["monkey (tail-hand)"], sprite=["hand-tail"], c2="purple")
E("Sunkern", arch=["plant"], based=["seed"], sprite=["seed-body"], lore=["one of the weakest/lightest Pokemon"], c2="brown")
E("Sunflora", arch=["plant"], based=["sunflower"], sprite=["petal-head"], c2="green")
E("Yanma", arch=["insect"], based=["dragonfly"], sprite=["big-eyes","wings"], c2="red")
E("Wooper", arch=["amphibian"], based=["axolotl","salamander"], sprite=["gills","flat-face"], nick=["derpy smile"], c2="")
E("Quagsire", arch=["amphibian"], based=["giant salamander (ōsanshōuo)"], sprite=["flat-face","fins"], c2="")
E("Slowking", arch=["hippo"], based=["hermit + Shellder crown"], sprite=["shellder-crown"], lore=["intelligent king; Movie 2000"], role=[], c2="pink")
E("Espeon", arch=["feline","fox"], based=["cat / fox (psychic sun)"], sprite=["forehead-gem","forked-tail"], lore=["Sun eeveelution (evolves by day + friendship)"], role=["eeveelution"], c2="purple")
E("Umbreon", arch=["feline","fox"], based=["cat / black rabbit (moonlight)"], sprite=["yellow-rings","glow"], lore=["Moon eeveelution (evolves by night + friendship); rings glow"], trn=["Karen (E4)","Gary (anime)"], role=["eeveelution"], c2="yellow")
E("Murkrow", arch=["bird","corvid"], based=["crow / witch's familiar"], sprite=["witch-hat-crest","tail"], myth=["bird of ill omen"], trn=["Karen (E4)"], c2="")
E("Misdreavus", arch=["ghost"], based=["banshee","screech spirit"], sprite=["red-orbs","hair"], myth=["banshee"], c2="")
E("Unown", arch=["symbol"], based=["alphabet / hieroglyphs / crop circles"], sprite=["single-eye","letter-shape"], lore=["28 forms (A-Z, ! ?)"], myth=["ancient writing; summons power in Movie 3"], loc=["Ruins of Alph"], nick=["alphabet Pokemon; worst stats"], c2="")
E("Wobbuffet", arch=["patience"], based=["Nihonjin gag / patience balloon"], sprite=["black-body","tail-face"], lore=["only counterattacks; hides its real body"], trn=["Team Rocket (Jessie, anime)"], nick=["Team Rocket's Wobbuffet"], c2="black")
E("Girafarig", arch=["mammal"], based=["giraffe / okapi (palindrome name)"], sprite=["tail-head"], lore=["name is a palindrome; tail has a brain"], c2="cream")
E("Pineco", arch=["insect"], based=["bagworm","pinecone"], sprite=["pinecone-shell"], c2="")
E("Forretress", arch=["insect"], based=["bagworm","fortress"], sprite=["steel-shell","spikes"], c2="red")
E("Dunsparce", arch=["serpent"], based=["Tsuchinoko (mythical snake)","land snake"], sprite=["tiny-wings","drill-tail"], myth=["Tsuchinoko"], nick=["elusive; fan-beloved underdog"], c2="blue")
E("Gligar", arch=["scorpion"], based=["scorpion + bat"], sprite=["pincers","wings","stinger-tail"], c2="purple")
E("Steelix", arch=["serpent"], based=["iron snake"], sprite=["metal-body","jaw"], trn=["Jasmine (gym)"], role=["mega"], c2="gray")
E("Snubbull", arch=["canine"], based=["bulldog"], sprite=["underbite","pink-body"], c2="black")
E("Granbull", arch=["canine"], based=["bulldog"], sprite=["huge-jaw","fangs"], c2="black")
E("Qwilfish", arch=["fish"], based=["pufferfish"], sprite=["spikes","balloon-body"], c2="gray")
E("Scizor", arch=["insect","mantis"], based=["mantis (steel pincers)"], sprite=["pincer-claws","wings"], trn=["Ariana? no"], role=["mega"], c2="red")
E("Shuckle", arch=["mollusc"], based=["barnacle / snail (makes berry juice)"], sprite=["holed-shell","stubby-limbs"], lore=["highest Defense; can hit hardest theoretical damage"], nick=["mold juice; wall"], c2="red")
E("Heracross", arch=["insect","beetle"], based=["Hercules beetle"], sprite=["horn"], role=["mega"], c2="")
E("Sneasel", arch=["feline","mustelid"], based=["weasel + Japanese kamaitachi"], sprite=["claws","ear-feathers"], myth=["kamaitachi (sickle weasel)"], c2="red")
E("Teddiursa", arch=["bear"], based=["bear cub"], sprite=["crescent-brow","honey-paw"], c2="")
E("Ursaring", arch=["bear"], based=["bear"], sprite=["chest-ring","claws"], c2="")
E("Slugma", arch=["amorphous"], based=["lava slug","magma"], sprite=["molten-body"], c2="")
E("Magcargo", arch=["amorphous"], based=["lava snail"], sprite=["rock-shell","molten"], lore=["dex says hotter than the sun (13,000°F)"], nick=["hotter than the sun meme"], c2="gray")
E("Swinub", arch=["boar"], based=["pig / boar"], sprite=["snout","fur"], c2="brown")
E("Piloswine", arch=["boar"], based=["mammoth / boar"], sprite=["tusks","shaggy-fur"], c2="brown")
E("Corsola", arch=["coral"], based=["coral"], sprite=["coral-branches"], nick=["Galarian Corsola (dead coral ghost)"], c2="pink")
E("Remoraid", arch=["fish"], based=["remora / pistol shrimp"], sprite=["fins"], lore=["evolves into an octopus (odd)"], c2="gray")
E("Octillery", arch=["cephalopod","octopus"], based=["octopus (+ tank turret)"], sprite=["suckers","cannon-mouth"], sig="Octazooka", c2="")
E("Delibird", arch=["bird"], based=["Santa Claus / penguin"], sprite=["sack-tail"], sig="Present", lore=["carries food in its tail-sack"], myth=["Santa Claus"], c2="white")
E("Mantine", arch=["fish"], based=["manta ray"], sprite=["wings","remora-passenger"], c2="")
E("Skarmory", arch=["bird","raptor"], based=["armoured bird / steel raptor"], sprite=["steel-wings","blades"], c2="red")
E("Houndour", arch=["canine"], based=["Doberman / hellhound"], sprite=["skull-markings","horns"], c2="white")
E("Houndoom", arch=["canine"], based=["hellhound / Cerberus"], sprite=["horns","rib-bands","tail-arrow"], myth=["hellhound"], trn=["Karen (E4)"], role=["mega"], c2="white")
E("Kingdra", arch=["fish","seahorse"], based=["seahorse dragon"], sprite=["snout","fins"], trn=["Clair (gym)"], c2="")
E("Phanpy", arch=["pachyderm","elephant"], based=["elephant calf"], sprite=["big-ears","trunk"], trn=["Ash"], c2="blue")
E("Donphan", arch=["pachyderm","elephant"], based=["elephant"], sprite=["tusks","tyre-tread"], c2="gray")
E("Porygon2", arch=["mineral"], based=["upgraded 3D model"], sprite=["rounded-blocks"], c2="pink")
E("Stantler", arch=["deer"], based=["reindeer / deer"], sprite=["hypnotic-antlers"], lore=["antler orbs hypnotise"], c2="")
E("Smeargle", arch=["canine"], based=["beagle / painter"], sprite=["paintbrush-tail"], sig="Sketch", lore=["tail oozes paint; can copy any move"], nick=["can learn every move"], c2="brown")
E("Tyrogue", arch=["humanoid"], based=["young boxer"], sprite=["tiny-fighter"], role=["baby"], c2="purple")
E("Hitmontop", arch=["humanoid"], based=["capoeira / breakdancer / spinning top"], sprite=["spins-on-head"], sig="Triple Kick", c2="brown")
E("Smoochum", arch=["humanoid"], based=["baby / infant"], sprite=["big-lips"], role=["baby"], c2="")
E("Elekid", arch=["humanoid"], based=["baby / power plug"], sprite=["plug-horns","stripes"], role=["baby"], c2="black")
E("Magby", arch=["humanoid"], based=["baby fire duck"], sprite=["flame-nose"], role=["baby"], c2="yellow")
E("Miltank", arch=["bovine"], based=["dairy cow"], sprite=["udder","pink-hide"], lore=["Milk Drink heals"], trn=["Whitney (gym)"], nick=["Whitney's Miltank (Rollout terror)"], c2="black")
E("Blissey", arch=["mammal"], based=["egg nurse / happiness"], sprite=["egg-pouch","apron"], lore=["huge HP; nurse"], trn=["Nurse Joy (anime)"], c2="white")
E("Raikou", arch=["feline"], based=["saber-tooth tiger / thunder"], sprite=["storm-cloud-back","mane"], myth=["revived by Ho-Oh; roaming legend"], role=["legendary"], nick=["roaming beast trio"], c2="black")
E("Entei", arch=["canine"], based=["Chinese guardian lion / volcano"], sprite=["cape-smoke","mane"], myth=["revived by Ho-Oh; Movie 3 'Unown/Entei'"], role=["legendary"], nick=["roaming beast trio"], c2="gray")
E("Suicune", arch=["canine"], based=["cheetah / north wind"], sprite=["crystal-crest","ribbon-mane"], myth=["revived by Ho-Oh; purifies water; Crystal mascot"], role=["legendary"], nick=["roaming beast trio"], c2="white")
E("Larvitar", arch=["reptile"], based=["larva / rock"], sprite=["belly-plate","horn"], trn=["Ash (anime)"], c2="")
E("Pupitar", arch=["reptile"], based=["cocoon / chrysalis"], sprite=["hard-shell","horn"], c2="")
E("Tyranitar", arch=["dinosaur"], based=["Godzilla / T-rex"], sprite=["armour-plates","horn"], lore=["pseudo; kicks up sandstorms"], role=["pseudo","mega"], c2="")
E("Lugia", arch=["dragon","plesiosaur"], based=["silver bird / plesiosaur / guardian of the sea"], sprite=["back-plates","fingered-wings"], sig="Aeroblast", myth=["guardian of the seas; calms the bird trio; Movie 2000"], loc=["Whirl Islands"], role=["legendary"], nick=["box legend (Silver/SoulSilver)"], c2="white")
E("Ho-Oh", arch=["bird","phoenix"], based=["phoenix / Fenghuang / rainbow bird"], sprite=["rainbow-wings","gold-body"], sig="Sacred Fire", myth=["phoenix; revives the beast trio; rainbow over Tin Tower; Ash saw it in ep.1"], loc=["Tin Tower"], role=["legendary"], nick=["box legend (Gold/HeartGold)"], c2="red")
E("Celebi", arch=["fairy"], based=["fairy / onion sprout (time travel)"], sprite=["antennae","wings"], myth=["voice of the forest; time-travel guardian; Movie 4"], role=["mythical"], c2="green")

# === Gen 2 best-known moves ===
SIG.update({
 "Chikorita":"Razor Leaf","Bayleef":"Body Slam","Meganium":"Petal Dance","Cyndaquil":"Ember","Quilava":"Flame Wheel",
 "Typhlosion":"Eruption","Totodile":"Water Gun","Croconaw":"Crunch","Feraligatr":"Crunch","Sentret":"Quick Attack",
 "Furret":"Double-Edge","Hoothoot":"Hypnosis","Noctowl":"Psychic","Ledyba":"Tackle","Ledian":"Comet Punch",
 "Spinarak":"Poison Sting","Ariados":"Spider Web","Crobat":"Cross Poison","Chinchou":"Spark","Lanturn":"Surf",
 "Pichu":"Thunder Shock","Cleffa":"Pound","Igglybuff":"Sing","Togepi":"Metronome","Togetic":"Metronome","Natu":"Peck",
 "Xatu":"Future Sight","Mareep":"Thunder Shock","Flaaffy":"Thunderbolt","Ampharos":"Discharge","Bellossom":"Petal Dance",
 "Marill":"Water Gun","Azumarill":"Play Rough","Sudowoodo":"Rock Slide","Politoed":"Perish Song","Hoppip":"Leech Seed",
 "Skiploom":"Bullet Seed","Jumpluff":"Cotton Spore","Aipom":"Double Hit","Sunkern":"Mega Drain","Sunflora":"Solar Beam",
 "Yanma":"Bug Buzz","Wooper":"Water Gun","Quagsire":"Earthquake","Slowking":"Psychic","Misdreavus":"Perish Song",
 "Unown":"Hidden Power","Wobbuffet":"Counter","Girafarig":"Psychic","Pineco":"Spikes","Forretress":"Explosion",
 "Dunsparce":"Glare","Gligar":"Slash","Steelix":"Iron Tail","Snubbull":"Bite","Granbull":"Play Rough","Qwilfish":"Pin Missile",
 "Scizor":"Bullet Punch","Shuckle":"Toxic","Heracross":"Megahorn","Sneasel":"Ice Punch","Teddiursa":"Fury Swipes",
 "Ursaring":"Hammer Arm","Slugma":"Ember","Magcargo":"Lava Plume","Swinub":"Powder Snow","Piloswine":"Earthquake",
 "Corsola":"Recover","Remoraid":"Water Gun","Delibird":"Present","Mantine":"Surf","Skarmory":"Steel Wing",
 "Houndour":"Ember","Houndoom":"Flamethrower","Kingdra":"Dragon Pulse","Phanpy":"Rollout","Donphan":"Earthquake",
 "Porygon2":"Tri Attack","Stantler":"Hypnosis","Tyrogue":"Tackle","Smoochum":"Sweet Kiss","Elekid":"Thunder Punch",
 "Magby":"Fire Punch","Miltank":"Rollout","Blissey":"Soft-Boiled","Raikou":"Thunder","Entei":"Sacred Fire",
 "Suicune":"Aurora Beam","Larvitar":"Bite","Pupitar":"Rock Slide","Tyranitar":"Crunch","Lugia":"Aeroblast",
 "Ho-Oh":"Sacred Fire","Celebi":"Future Sight",
})
# === Johto gym leaders / Elite Four / Champion ===
TEAMS.update({
 "Falkner (gym)":["Pidgey","Pidgeotto","Hoothoot"],
 "Bugsy (gym)":["Metapod","Kakuna","Scyther","Spinarak"],
 "Whitney (gym)":["Clefairy","Miltank"],
 "Morty (gym)":["Gastly","Haunter","Gengar","Misdreavus"],
 "Chuck (gym)":["Primeape","Poliwrath"],
 "Jasmine (gym)":["Magnemite","Magneton","Steelix"],
 "Pryce (gym)":["Seel","Dewgong","Piloswine"],
 "Clair (gym)":["Dragonair","Gyarados","Kingdra","Dragonite"],
 "Will (E4)":["Xatu","Jynx","Slowbro","Exeggutor"],
 "Koga (E4)":["Ariados","Venomoth","Forretress","Muk","Crobat"],
 "Karen (E4)":["Umbreon","Murkrow","Vileplume","Gengar","Houndoom"],
 "Red (champion)":["Pikachu","Espeon","Snorlax","Lapras","Venusaur","Charizard","Blastoise"],
})

# ============================== GEN 3 (Hoenn) ==============================
E("Treecko", arch=["reptile","gecko"], based=["gecko / wood lizard"], sprite=["tail","belly"], lore=["starter"], role=["starter"], c2="red")
E("Grovyle", arch=["reptile","gecko"], based=["gecko / theropod"], sprite=["leaf-blades","tail-leaves"], c2="red")
E("Sceptile", arch=["reptile","gecko"], based=["monitor lizard / forest guardian"], sprite=["leaf-blades","tail","seed-back"], trn=["Ash"], role=["starter","mega"], c2="red")
E("Torchic", arch=["bird"], based=["chick"], sprite=["fluffy","head-feathers"], lore=["starter"], trn=["May (anime)"], role=["starter"], c2="orange")
E("Combusken", arch=["bird"], based=["young fighting fowl"], sprite=["leg-spurs","crest"], c2="orange")
E("Blaziken", arch=["bird"], based=["fighting cockerel / kickboxer"], sprite=["wrist-flames","talons"], sig="Blaze Kick", role=["starter","mega"], c2="cream")
E("Mudkip", arch=["amphibian","mudfish"], based=["mudskipper / axolotl"], sprite=["head-fin","cheek-fins"], lore=["starter"], nick=["'so i herd u liek mudkipz'"], role=["starter"], c2="orange")
E("Marshtomp", arch=["amphibian","mudfish"], based=["mudskipper"], sprite=["head-fin","belly-pattern"], c2="")
E("Swampert", arch=["amphibian","mudfish"], based=["mudskipper / axolotl"], sprite=["head-fins","gill-cheeks"], role=["starter","mega"], c2="orange")
E("Poochyena", arch=["canine"], based=["hyena / dog pup"], sprite=["bushy-tail","fangs"], c2="gray")
E("Mightyena", arch=["canine"], based=["hyena"], sprite=["mane","fangs"], trn=["Sidney (E4)"], c2="gray")
E("Zigzagoon", arch=["mammal"], based=["raccoon / tanuki"], sprite=["zigzag-pattern"], lore=["Pickup ability; zigzags"], c2="brown")
E("Linoone", arch=["mammal"], based=["badger / raccoon"], sprite=["stripes","pointed-face"], c2="white")
E("Wurmple", arch=["insect","caterpillar"], based=["caterpillar"], sprite=["spikes","suction-feet"], c2="red")
E("Silcoon", arch=["insect","pupa"], based=["cocoon"], sprite=["silk-shell"], c2="")
E("Beautifly", arch=["insect","butterfly"], based=["butterfly"], sprite=["wings","proboscis"], c2="black")
E("Cascoon", arch=["insect","pupa"], based=["cocoon"], sprite=["spiky-silk"], c2="")
E("Dustox", arch=["insect","moth"], based=["moth"], sprite=["wings","antennae"], c2="green")
E("Lotad", arch=["plant"], based=["lily pad / duckweed"], sprite=["leaf-hat"], c2="green")
E("Lombre", arch=["plant"], based=["kappa / lily pad"], sprite=["leaf-hat","frills"], myth=["kappa"], c2="white")
E("Ludicolo", arch=["plant"], based=["Mexican dancer / pineapple / kappa"], sprite=["sombrero-leaf","poncho-pattern"], lore=["dances to festive rhythms"], c2="yellow")
E("Seedot", arch=["plant"], based=["acorn"], sprite=["acorn-body","stalk"], c2="brown")
E("Nuzleaf", arch=["plant"], based=["tengu / trickster"], sprite=["leaf-nose","mask-pattern"], myth=["tengu"], c2="brown")
E("Shiftry", arch=["plant"], based=["tengu (long-nosed goblin)"], sprite=["leaf-fans","nose","hair"], myth=["tengu (wind demon)"], c2="brown")
E("Taillow", arch=["bird"], based=["swallow"], sprite=["forked-tail"], trn=["Ash"], c2="blue")
E("Swellow", arch=["bird"], based=["swallow / swift"], sprite=["forked-tail","crest"], c2="blue")
E("Wingull", arch=["bird"], based=["seagull"], sprite=["long-wings","beak"], c2="white")
E("Pelipper", arch=["bird"], based=["pelican"], sprite=["huge-bill-pouch"], c2="yellow")
E("Ralts", arch=["humanoid"], based=["psychic embryo / fairy"], sprite=["horns","hair-bowl"], c2="green")
E("Kirlia", arch=["humanoid"], based=["ballet dancer"], sprite=["tutu-flare","horns"], c2="green")
E("Gardevoir", arch=["humanoid"], based=["elegant dancer / knight's guardian"], sprite=["gown","chest-horn"], lore=["will protect its trainer with its life"], role=["mega"], c2="white")
E("Surskit", arch=["insect"], based=["pond skater / water strider"], sprite=["antenna","thin-legs"], c2="blue")
E("Masquerain", arch=["insect"], based=["moth / mask"], sprite=["eye-pattern-wings"], c2="black")
E("Shroomish", arch=["plant"], based=["mushroom (button)"], sprite=["cap","spots"], c2="green")
E("Breloom", arch=["plant"], based=["mushroom + kangaroo boxer"], sprite=["cap","spring-arms"], sig="Mach Punch", c2="green")
E("Slakoth", arch=["mammal"], based=["sloth"], sprite=["lazy-face","claws"], lore=["Truant; barely moves"], c2="brown")
E("Vigoroth", arch=["primate"], based=["hyperactive sloth / ape"], sprite=["wild-mane","claws"], c2="white")
E("Slaking", arch=["primate"], based=["gorilla / sloth (lazy king)"], sprite=["big-belly","collar-fur"], lore=["highest raw stats but Truant halves output"], c2="brown")
E("Nincada", arch=["insect"], based=["cicada nymph (underground)"], sprite=["claws","dull-eyes"], c2="gray")
E("Ninjask", arch=["insect","cicada"], based=["cicada (adult) / ninja"], sprite=["wings","speed-lines"], lore=["fastest first-stage-related; Speed Boost"], c2="black")
E("Shedinja", arch=["ghost"], based=["cicada husk / empty shell"], sprite=["hollow-back","halo"], lore=["appears from Nincada's shed shell; always 1 HP; Wonder Guard"], myth=["steals souls through its back"], nick=["1 HP; Wonder Guard"], c2="gray")
E("Whismur", arch=["mammal"], based=["earplug / rabbit"], sprite=["big-ears","round"], c2="pink")
E("Loudred", arch=["mammal"], based=["speaker / delinquent"], sprite=["speaker-ears","big-mouth"], c2="")
E("Exploud", arch=["mammal"], based=["subwoofer / sound tubes"], sprite=["sound-tubes","big-mouth"], sig="Boomburst", c2="green")
E("Makuhita", arch=["humanoid"], based=["sumo wrestler"], sprite=["big-fists","tubby"], c2="yellow")
E("Hariyama", arch=["humanoid"], based=["sumo wrestler"], sprite=["huge-palms","belt"], trn=["Brawly (gym)"], c2="")
E("Azurill", arch=["mammal"], based=["baby (ball tail)"], sprite=["ball-tail","big-ears"], role=["baby"], c2="")
E("Nosepass", arch=["mineral"], based=["Easter Island moai statue (compass)"], sprite=["magnet-nose"], lore=["nose always points north (magnetic)"], myth=["moai"], c2="")
E("Skitty", arch=["feline","cat"], based=["kitten"], sprite=["curl-tail","big-ears"], trn=["May (anime)"], c2="pink")
E("Delcatty", arch=["feline","cat"], based=["cat (fancy)"], sprite=["collar-fur"], c2="")
E("Sableye", arch=["gremlin"], based=["gremlin / gem-hoarder"], sprite=["gem-eyes","gem-body"], lore=["feeds on gems; first Dark/Ghost"], role=["mega"], c2="blue")
E("Mawile", arch=["deceiver"], based=["futakuchi-onna (two-mouthed woman) / trap"], sprite=["jaw-horns","innocent-face"], myth=["futakuchi-onna"], role=["mega"], c2="black")
E("Aron", arch=["dinosaur"], based=["armoured dinosaur / iron"], sprite=["steel-armour","eyes"], lore=["eats iron ore"], c2="gray")
E("Lairon", arch=["dinosaur"], based=["armoured beast"], sprite=["armour-bands"], c2="gray")
E("Aggron", arch=["dinosaur"], based=["armoured dinosaur / territory guardian"], sprite=["horns","armour-plates"], role=["mega"], c2="")
E("Meditite", arch=["humanoid"], based=["yogi (meditation)"], sprite=["lotus-pose"], c2="red")
E("Medicham", arch=["humanoid"], based=["yoga master / Indian dancer"], sprite=["floaty-limbs","turban-head"], role=["mega"], c2="red")
E("Electrike", arch=["canine"], based=["dog / lightning"], sprite=["spiky-fur"], c2="yellow")
E("Manectric", arch=["canine"], based=["lightning wolf / jackal"], sprite=["mane","bolt-body"], trn=["Wattson (gym)"], role=["mega"], c2="yellow")
E("Plusle", arch=["rodent"], based=["cheerleader mouse (plus)"], sprite=["plus-cheeks","pom-tail"], c2="red")
E("Minun", arch=["rodent"], based=["cheerleader mouse (minus)"], sprite=["minus-cheeks","pom-tail"], c2="blue")
E("Volbeat", arch=["insect"], based=["firefly (male)"], sprite=["light-tail"], c2="")
E("Illumise", arch=["insect"], based=["firefly (female)"], sprite=["antennae","light"], c2="purple")
E("Roselia", arch=["plant"], based=["rose (thorns)"], sprite=["rose-hands"], c2="green")
E("Gulpin", arch=["amorphous"], based=["stomach / sac"], sprite=["big-mouth","tuft"], c2="")
E("Swalot", arch=["amorphous"], based=["stomach / glutton"], sprite=["huge-mouth","whiskers"], lore=["swallows anything whole"], c2="")
E("Carvanha", arch=["fish"], based=["piranha"], sprite=["fangs","fins"], c2="red")
E("Sharpedo", arch=["shark"], based=["bull shark / torpedo submarine"], sprite=["torpedo-body","teeth","star-scar"], trn=["Archie (Team Aqua)"], role=["mega"], c2="yellow")
E("Wailmer", arch=["cetacean","whale"], based=["whale (ball)"], sprite=["round","blue-body"], c2="")
E("Wailord", arch=["cetacean","whale"], based=["blue whale (largest Pokemon)"], sprite=["huge-body","spots"], lore=["largest Pokemon by size"], c2="")
E("Numel", arch=["camelid"], based=["camel / volcano"], sprite=["back-hump","dopey"], c2="green")
E("Camerupt", arch=["camelid"], based=["camel + volcano"], sprite=["back-volcanoes","humps"], trn=["Maxie (Team Magma)"], role=["mega"], c2="")
E("Torkoal", arch=["turtle"], based=["tortoise + coal/boiler"], sprite=["smokestack-shell"], c2="black")
E("Spoink", arch=["mammal"], based=["pig (bouncing) + pearl"], sprite=["spring-tail","head-pearl"], lore=["bounces on its tail to keep its heart beating; stops = dies"], nick=["dies if it stops bouncing"], c2="black")
E("Grumpig", arch=["mammal"], based=["pig / manipulator"], sprite=["black-pearls","curl-ears"], c2="black")
E("Spinda", arch=["mammal"], based=["panda / drunkard"], sprite=["spiral-eyes","wobble"], lore=["staggers dizzily; every Spinda's spots differ (4 billion patterns)"], nick=["unique spot pattern each"], c2="brown")
E("Trapinch", arch=["insect"], based=["antlion / trapdoor"], sprite=["huge-jaws","big-head"], c2="brown")
E("Vibrava", arch=["insect"], based=["antlion (adult) / dragonfly"], sprite=["rhombus-wings"], c2="green")
E("Flygon", arch=["insect","dragon"], based=["dragonfly / desert spirit"], sprite=["goggle-eyes","green-wings"], lore=["'the desert spirit'; hums in sandstorms"], c2="red")
E("Cacnea", arch=["plant"], based=["cactus"], sprite=["spikes","arms"], trn=["James (anime)"], c2="")
E("Cacturne", arch=["plant"], based=["cactus + scarecrow / bandit"], sprite=["diamond-eyes","spiky-arms"], lore=["stalks travellers in the desert at night"], c2="green")
E("Swablu", arch=["bird"], based=["cotton bird / bluebird"], sprite=["cotton-wings"], c2="blue")
E("Altaria", arch=["bird","dragon"], based=["cloud bird / phoenix / bluebird"], sprite=["cotton-cloud-wings"], trn=["Winona (gym)"], role=["mega"], c2="blue")
E("Zangoose", arch=["mammal","mustelid"], based=["mongoose / cat-weasel"], sprite=["claws","scars"], lore=["sworn enemy of Seviper"], c2="red")
E("Seviper", arch=["serpent","snake"], based=["viper (sword-tail)"], sprite=["blade-tail","fangs"], lore=["feuds with Zangoose"], trn=["Jessie (anime)"], c2="purple")
E("Lunatone", arch=["mineral"], based=["moon / meteorite"], sprite=["crescent","red-eye"], myth=["moon rock"], c2="yellow")
E("Solrock", arch=["mineral"], based=["sun / meteorite"], sprite=["sun-rays","face"], myth=["sun rock"], c2="")
E("Barboach", arch=["fish"], based=["loach / catfish"], sprite=["whiskers","slimy"], c2="")
E("Whiscash", arch=["fish"], based=["catfish (namazu — earthquake myth)"], sprite=["whiskers","mustache"], myth=["namazu (earthquake catfish)"], c2="blue")
E("Corphish", arch=["crustacean","crayfish"], based=["crayfish"], sprite=["pincers"], trn=["Ash"], c2="red")
E("Crawdaunt", arch=["crustacean","crayfish"], based=["lobster / crayfish rogue"], sprite=["big-claws","star-head"], trn=["Sidney (E4)"], c2="")
E("Baltoy", arch=["mineral"], based=["dogu clay figurine (spinning top)"], sprite=["single-eye","spins"], myth=["dogu"], c2="brown")
E("Claydol", arch=["mineral"], based=["dogu / ancient clay doll"], sprite=["many-eyes","arms-float"], myth=["ancient dogu automaton"], c2="black")
E("Lileep", arch=["plant"], based=["sea lily / crinoid (fossil)"], sprite=["petals","stalk"], role=["fossil"], c2="purple")
E("Cradily", arch=["plant"], based=["sea lily / anemone (fossil)"], sprite=["neck-frill","tentacle-petals"], role=["fossil"], c2="green")
E("Anorith", arch=["arthropod"], based=["Anomalocaris (fossil)"], sprite=["plate-armour","claws"], role=["fossil"], c2="blue")
E("Armaldo", arch=["arthropod"], based=["Anomalocaris (armoured)"], sprite=["plate-armour","claws"], role=["fossil"], c2="")
E("Feebas", arch=["fish"], based=["ugly fish (Chinese ugly carp)"], sprite=["ragged-fins","dull"], lore=["extremely rare; ugly duckling"], nick=["ugly → Milotic"], c2="brown")
E("Milotic", arch=["fish","serpent"], based=["eel / Chinese dragon / mermaid (beauty)"], sprite=["ribbon-fins","scales"], lore=["'most beautiful Pokemon'; calms hostility"], trn=["Wallace (gym/champion)"], c2="cream")
E("Castform", arch=["weather"], based=["cloud / weather forecast"], sprite=["changes-with-weather"], c2="")
E("Kecleon", arch=["reptile","chameleon"], based=["chameleon"], sprite=["zigzag-belly","curl-tail"], c2="red")
E("Shuppet", arch=["ghost"], based=["cloth puppet / teru teru bozu"], sprite=["horn","wispy-body"], myth=["grudge doll"], c2="")
E("Banette", arch=["ghost"], based=["abandoned marionette doll (voodoo)"], sprite=["zipper-mouth","pins"], lore=["a discarded doll seeking the child who threw it away"], myth=["cursed doll / voodoo"], role=["mega"], c2="")
E("Duskull", arch=["ghost"], based=["grim reaper / Yamawaro"], sprite=["skull-mask","single-eye"], c2="")
E("Dusclops", arch=["ghost"], based=["mummy / reaper (hollow body)"], sprite=["cyclops-eye","bandages"], c2="")
E("Tropius", arch=["dinosaur"], based=["sauropod + banana + palm"], sprite=["neck-fruit","leaf-wings"], c2="brown")
E("Chimecho", arch=["ghost"], based=["wind chime (fūrin)"], sprite=["chime-body","tail"], c2="")
E("Absol", arch=["feline","canine"], based=["disaster beast / kirin / barghest"], sprite=["scythe-horn","mane"], lore=["appears before disasters; wrongly blamed"], myth=["harbinger of calamity"], trn=["Sidney (E4)"], role=["mega"], c2="white")
E("Wynaut", arch=["patience"], based=["baby (patience)"], sprite=["ears-hands","big-mouth"], role=["baby"], c2="")
E("Snorunt", arch=["yokai"], based=["Yuki-warashi (snow child)"], sprite=["hood-body"], myth=["yuki-warashi"], c2="")
E("Glalie", arch=["yokai"], based=["floating ice head / oni mask"], sprite=["ice-mask","horns"], role=["mega"], c2="")
E("Froslass", arch=["yokai"], based=["Yuki-onna (snow woman)"], sprite=["kimono-body","hollow"], myth=["yuki-onna"], c2="purple")
E("Spheal", arch=["pinniped"], based=["seal pup (ball)"], sprite=["round","clap"], nick=["rolls like a ball"], c2="")
E("Sealeo", arch=["pinniped"], based=["sea lion"], sprite=["tusks","whiskers"], c2="")
E("Walrein", arch=["pinniped"], based=["walrus"], sprite=["tusks","blubber"], trn=["Glacia (E4)"], c2="")
E("Clamperl", arch=["mollusc"], based=["clam (pearl)"], sprite=["shell","pearl"], c2="blue")
E("Huntail", arch=["fish"], based=["deep-sea anglerfish / eel"], sprite=["tail-lure","fangs"], c2="")
E("Gorebyss", arch=["fish"], based=["deep-sea fish / eel"], sprite=["thin-snout"], c2="pink")
E("Relicanth", arch=["fish"], based=["coelacanth (living fossil)"], sprite=["rock-scales"], lore=["unchanged for 100 million years"], c2="")
E("Luvdisc", arch=["fish"], based=["heart-shaped fish"], sprite=["heart-body"], c2="pink")
E("Bagon", arch=["dragon"], based=["dragon (headbutts, dreams of flying)"], sprite=["rock-head"], lore=["dreams of flying; headbutts rocks"], c2="blue")
E("Shelgon", arch=["dragon"], based=["dragon in a shell / cocoon"], sprite=["shell-armour"], c2="white")
E("Salamence", arch=["dragon"], based=["Western dragon (grew wings from wishing to fly)"], sprite=["red-wings","crescent-head"], lore=["pseudo; its cells awakened wings"], role=["pseudo","mega"], c2="red")
E("Beldum", arch=["mineral"], based=["magnet / steel claw"], sprite=["single-eye","claw"], c2="blue")
E("Metang", arch=["mineral"], based=["two Beldum fused / robot arms"], sprite=["claws","cross-face"], c2="blue")
E("Metagross", arch=["mineral"], based=["four Beldum / supercomputer spider"], sprite=["four-legs","x-face"], lore=["pseudo; brain like a supercomputer"], trn=["Steven (champion)"], role=["pseudo","mega"], c2="")
E("Regirock", arch=["golem"], based=["rock golem (titan)"], sprite=["rock-body","dot-face"], myth=["ancient golem titan"], role=["legendary"], c2="")
E("Regice", arch=["golem"], based=["ice golem (titan)"], sprite=["ice-body","dot-face"], myth=["ancient golem titan"], role=["legendary"], c2="")
E("Registeel", arch=["golem"], based=["steel golem (titan)"], sprite=["metal-body","dot-face"], myth=["ancient golem titan"], role=["legendary"], c2="")
E("Latias", arch=["dragon"], based=["jet plane dragon (eon)"], sprite=["glider-wings"], myth=["Eon duo; Movie 5 (Heroes)"], role=["legendary"], c2="white")
E("Latios", arch=["dragon"], based=["jet plane dragon (eon)"], sprite=["glider-wings"], myth=["Eon duo; Movie 5 (Heroes)"], role=["legendary"], c2="white")
E("Kyogre", arch=["cetacean"], based=["orca / whale / Leviathan (the sea)"], sprite=["fins","markings"], sig="Origin Pulse", myth=["expanded the seas; primal weather trio"], role=["legendary"], nick=["box legend (Sapphire)"], c2="white")
E("Groudon", arch=["dinosaur"], based=["Behemoth / dinosaur (the land)"], sprite=["claws","plates"], sig="Precipice Blades", myth=["raised the continents; primal weather trio"], role=["legendary"], nick=["box legend (Ruby)"], c2="white")
E("Rayquaza", arch=["serpent","dragon"], based=["sky serpent / ozone dragon / quetzalcoatl"], sprite=["serpent-body","fins"], sig="Dragon Ascent", myth=["calms Kyogre & Groudon; lives in the ozone layer"], loc=["Sky Pillar"], role=["legendary","mega"], nick=["box legend (Emerald)"], c2="yellow")
E("Jirachi", arch=["fairy"], based=["wish star / tanabata"], sprite=["tags","third-eye"], myth=["grants wishes; wakes 7 days every 1000 years; Movie 6"], role=["mythical"], c2="")
E("Deoxys", arch=["alien"], based=["DNA / virus from space"], sprite=["crystal-chest","tentacle-arms"], myth=["mutated from a space virus; forme changer; Movie 7"], role=["mythical"], c2="")

# === Gen 3 best-known moves ===
SIG.update({
 "Treecko":"Pound","Grovyle":"Leaf Blade","Sceptile":"Leaf Blade","Torchic":"Ember","Combusken":"Double Kick",
 "Blaziken":"Blaze Kick","Mudkip":"Water Gun","Marshtomp":"Mud Shot","Swampert":"Muddy Water","Poochyena":"Bite",
 "Mightyena":"Crunch","Zigzagoon":"Tackle","Linoone":"Belly Drum","Wurmple":"Poison Sting","Silcoon":"Harden",
 "Beautifly":"Silver Wind","Cascoon":"Harden","Dustox":"Psybeam","Lotad":"Absorb","Lombre":"Fake Out","Ludicolo":"Hydro Pump",
 "Seedot":"Bide","Nuzleaf":"Razor Leaf","Shiftry":"Leaf Storm","Taillow":"Wing Attack","Swellow":"Aerial Ace",
 "Wingull":"Water Gun","Pelipper":"Hurricane","Ralts":"Confusion","Kirlia":"Psybeam","Gardevoir":"Psychic",
 "Surskit":"Bubble","Masquerain":"Air Slash","Shroomish":"Absorb","Breloom":"Mach Punch","Slakoth":"Slack Off",
 "Vigoroth":"Slash","Slaking":"Hammer Arm","Nincada":"Fury Swipes","Ninjask":"Fury Cutter","Shedinja":"Shadow Sneak",
 "Whismur":"Uproar","Loudred":"Screech","Exploud":"Boomburst","Makuhita":"Arm Thrust","Hariyama":"Close Combat",
 "Azurill":"Water Gun","Nosepass":"Rock Slide","Skitty":"Assist","Delcatty":"Double-Edge","Sableye":"Shadow Ball",
 "Mawile":"Iron Head","Aron":"Metal Claw","Lairon":"Iron Head","Aggron":"Heavy Slam","Meditite":"Confusion",
 "Medicham":"Hi Jump Kick","Electrike":"Spark","Manectric":"Thunderbolt","Plusle":"Helping Hand","Minun":"Helping Hand",
 "Volbeat":"Tail Glow","Illumise":"Covet","Roselia":"Petal Dance","Gulpin":"Sludge","Swalot":"Sludge Bomb",
 "Carvanha":"Bite","Sharpedo":"Crunch","Wailmer":"Water Pulse","Wailord":"Water Spout","Numel":"Ember","Camerupt":"Eruption",
 "Torkoal":"Lava Plume","Spoink":"Psychic","Grumpig":"Psychic","Spinda":"Teeter Dance","Trapinch":"Bite",
 "Vibrava":"Dragon Breath","Flygon":"Earthquake","Cacnea":"Needle Arm","Cacturne":"Needle Arm","Swablu":"Peck",
 "Altaria":"Dragon Pulse","Zangoose":"Crush Claw","Seviper":"Poison Fang","Lunatone":"Psychic","Solrock":"Solar Beam",
 "Barboach":"Mud Slap","Whiscash":"Earthquake","Corphish":"Crabhammer","Crawdaunt":"Crabhammer","Baltoy":"Rapid Spin",
 "Claydol":"Earthquake","Lileep":"Ingrain","Cradily":"Ancient Power","Anorith":"Fury Cutter","Armaldo":"X-Scissor",
 "Feebas":"Splash","Milotic":"Recover","Castform":"Weather Ball","Kecleon":"Sucker Punch","Shuppet":"Shadow Sneak",
 "Banette":"Shadow Claw","Duskull":"Night Shade","Dusclops":"Will-O-Wisp","Tropius":"Magical Leaf","Chimecho":"Psywave",
 "Absol":"Night Slash","Wynaut":"Counter","Snorunt":"Powder Snow","Glalie":"Ice Beam","Froslass":"Ice Shard",
 "Spheal":"Rollout","Sealeo":"Aurora Beam","Walrein":"Ice Beam","Clamperl":"Clamp","Huntail":"Crunch","Gorebyss":"Psychic",
 "Relicanth":"Head Smash","Luvdisc":"Sweet Kiss","Bagon":"Ember","Shelgon":"Dragon Breath","Salamence":"Dragon Claw",
 "Beldum":"Take Down","Metang":"Metal Claw","Metagross":"Meteor Mash","Regirock":"Stone Edge","Regice":"Ice Beam",
 "Registeel":"Flash Cannon","Latias":"Mist Ball","Latios":"Luster Purge","Kyogre":"Origin Pulse","Groudon":"Precipice Blades",
 "Rayquaza":"Dragon Ascent","Jirachi":"Doom Desire","Deoxys":"Psycho Boost",
})
# === Hoenn gym leaders / Elite Four / Champions ===
TEAMS.update({
 "Roxanne (gym)":["Geodude","Nosepass"],
 "Brawly (gym)":["Machop","Makuhita","Hariyama"],
 "Wattson (gym)":["Magnemite","Voltorb","Magneton","Electrike","Manectric"],
 "Flannery (gym)":["Slugma","Numel","Torkoal","Camerupt"],
 "Norman (gym)":["Slaking","Vigoroth","Spinda","Linoone"],
 "Winona (gym)":["Swellow","Pelipper","Skarmory","Altaria","Tropius"],
 "Tate & Liza (gym)":["Solrock","Lunatone","Xatu","Claydol"],
 "Wallace (gym/champion)":["Milotic","Whiscash","Sealeo","Seaking","Ludicolo","Tentacruel","Gyarados"],
 "Sidney (E4)":["Mightyena","Shiftry","Cacturne","Crawdaunt","Absol"],
 "Phoebe (E4)":["Dusclops","Banette","Sableye"],
 "Glacia (E4)":["Glalie","Sealeo","Walrein"],
 "Drake (E4)":["Salamence","Flygon","Altaria","Kingdra","Shelgon"],
 "Steven (champion)":["Metagross","Skarmory","Aggron","Cradily","Armaldo","Claydol"],
})

# ============================== GEN 4 (Sinnoh) ==============================
E("Turtwig", arch=["turtle"], based=["turtle + sapling"], sprite=["head-sprout","shell"], lore=["starter"], role=["starter"], c2="brown")
E("Grotle", arch=["turtle"], based=["tortoise + shrubs"], sprite=["back-bushes"], c2="brown")
E("Torterra", arch=["turtle"], based=["World Turtle (tree on its back)"], sprite=["tree-back","shell"], myth=["world turtle (Akupara)"], role=["starter"], c2="brown")
E("Chimchar", arch=["primate","monkey"], based=["chimpanzee / Sun Wukong"], sprite=["tail-flame"], lore=["starter"], trn=["Ash"], role=["starter"], c2="red")
E("Monferno", arch=["primate","monkey"], based=["monkey (Journey to the West)"], sprite=["tail-flame","mask"], c2="red")
E("Infernape", arch=["primate","monkey"], based=["Sun Wukong (Monkey King)"], sprite=["head-flame","cape-fur"], myth=["Sun Wukong"], trn=["Ash"], role=["starter"], c2="")
E("Piplup", arch=["bird","penguin"], based=["penguin chick"], sprite=["cape-collar","crest"], lore=["starter; proud"], trn=["Dawn (anime)"], role=["starter"], nick=["Dawn's Piplup"], c2="white")
E("Prinplup", arch=["bird","penguin"], based=["penguin (prince)"], sprite=["crown-crest","cape"], c2="white")
E("Empoleon", arch=["bird","penguin"], based=["emperor penguin (Napoleon / trident)"], sprite=["trident-face","crown"], role=["starter"], c2="yellow")
E("Starly", arch=["bird"], based=["starling"], sprite=["white-face-patch"], trn=["Ash"], c2="brown")
E("Staravia", arch=["bird","raptor"], based=["starling"], sprite=["head-crest"], c2="brown")
E("Staraptor", arch=["bird","raptor"], based=["hawk / eagle (bold raptor)"], sprite=["crest","white-mane"], c2="brown")
E("Bidoof", arch=["rodent"], based=["beaver / plateau pika"], sprite=["buck-teeth","flat-tail"], lore=["HM user (Cut/Surf/Strength)"], nick=["'HM slave'; God Bidoof meme"], c2="cream")
E("Bibarel", arch=["rodent"], based=["beaver"], sprite=["flat-tail","buck-teeth"], c2="cream")
E("Kricketot", arch=["insect"], based=["cricket (xylophone)"], sprite=["antennae"], c2="black")
E("Kricketune", arch=["insect"], based=["cricket + violinist / mustache man"], sprite=["mustache","violin-arms"], c2="red")
E("Shinx", arch=["feline"], based=["lion cub / lynx"], sprite=["star-tail","tuft"], c2="black")
E("Luxio", arch=["feline"], based=["lynx"], sprite=["star-tail","mane"], c2="black")
E("Luxray", arch=["feline"], based=["lion / lynx (X-ray vision)"], sprite=["mane","star-tail"], lore=["can see through walls (X-ray)"], role=[], c2="black")
E("Budew", arch=["plant"], based=["rosebud"], sprite=["bud-head"], role=["baby"], c2="green")
E("Roserade", arch=["plant"], based=["rose + masquerade dancer"], sprite=["bouquet-hands","cape"], c2="white")
E("Cranidos", arch=["dinosaur"], based=["Pachycephalosaurus (fossil)"], sprite=["dome-skull"], trn=["Roark (gym)"], role=["fossil"], c2="blue")
E("Rampardos", arch=["dinosaur"], based=["Pachycephalosaurus (fossil)"], sprite=["skull-dome","spikes"], role=["fossil"], c2="blue")
E("Shieldon", arch=["dinosaur"], based=["Styracosaurus / shield (fossil)"], sprite=["face-shield"], role=["fossil"], c2="brown")
E("Bastiodon", arch=["dinosaur"], based=["Styracosaurus + castle rampart (fossil)"], sprite=["shield-face","armour"], trn=["Byron (gym)"], role=["fossil"], c2="gray")
E("Burmy", arch=["insect"], based=["bagworm (cloak of debris)"], sprite=["cloak"], c2="")
E("Wormadam", arch=["insect"], based=["bagworm (mino-mushi)"], sprite=["cloak-dress"], c2="")
E("Mothim", arch=["insect","moth"], based=["moth"], sprite=["wings"], c2="yellow")
E("Combee", arch=["insect"], based=["honeycomb (three bees)"], sprite=["three-faces"], c2="black")
E("Vespiquen", arch=["insect"], based=["queen bee"], sprite=["honeycomb-skirt","crown"], trn=["Aaron (E4)"], c2="black")
E("Pachirisu", arch=["rodent"], based=["squirrel / chipmunk"], sprite=["curl-tail","cheeks"], nick=["'Sejun Park' 2014 Worlds"], c2="white")
E("Buizel", arch=["mustelid"], based=["weasel / otter (flotation collar)"], sprite=["float-collar","twin-tails"], trn=["Ash"], c2="")
E("Floatzel", arch=["mustelid"], based=["sea otter / weasel"], sprite=["float-ring","fins"], c2="")
E("Cherubi", arch=["plant"], based=["cherries"], sprite=["twin-cherry"], c2="red")
E("Cherrim", arch=["plant"], based=["cherry blossom (sunshine forme)"], sprite=["petal-bloom"], c2="green")
E("Shellos", arch=["mollusc"], based=["sea slug / nudibranch"], sprite=["frills"], nick=["east vs west sea"], c2="")
E("Gastrodon", arch=["mollusc"], based=["sea slug / sea hare"], sprite=["mantle-frills"], trn=["Cynthia (champion)"], c2="")
E("Ambipom", arch=["primate","monkey"], based=["monkey (two tail-hands)"], sprite=["twin-hand-tails"], c2="")
E("Drifloon", arch=["ghost"], based=["hot-air balloon / lost soul (yokai)"], sprite=["balloon-body","cross-eyes"], lore=["said to snatch children; appears Fridays at Valley Windworks"], myth=["soul-stealing balloon"], nick=["creepy dex entries"], c2="")
E("Drifblim", arch=["ghost"], based=["blimp / will-o-wisp"], sprite=["big-balloon","tassels"], c2="")
E("Buneary", arch=["mammal"], based=["rabbit (rolled ears)"], sprite=["curled-ears","fluff"], trn=["Dawn (anime)"], c2="cream")
E("Lopunny", arch=["mammal"], based=["rabbit / Playboy bunny"], sprite=["ear-fluff","leg-fluff"], role=["mega"], c2="brown")
E("Mismagius", arch=["ghost"], based=["witch / magician (hex)"], sprite=["witch-hat","hex-orbs"], trn=["Fantina (gym)"], c2="red")
E("Honchkrow", arch=["bird","corvid"], based=["crow mob boss (Godfather)"], sprite=["fedora-crest"], c2="")
E("Glameow", arch=["feline","cat"], based=["cat"], sprite=["curl-tail"], c2="")
E("Purugly", arch=["feline","cat"], based=["fat alley cat"], sprite=["tail-ring","scowl"], trn=["Mars (Team Galactic)"], c2="")
E("Chingling", arch=["ghost"], based=["bell / suzu"], sprite=["bell-body"], role=["baby"], c2="yellow")
E("Stunky", arch=["mammal"], based=["skunk"], sprite=["stripe","tail-spray"], c2="")
E("Skuntank", arch=["mammal"], based=["skunk"], sprite=["tail-plume"], trn=["Team Galactic"], c2="")
E("Bronzor", arch=["mineral"], based=["bronze mirror (dogu artifact)"], sprite=["mirror-body","runes"], myth=["ancient artifact"], c2="")
E("Bronzong", arch=["mineral"], based=["temple bell (dotaku) / rain-caller"], sprite=["bell-body","cross-eyes"], myth=["summons rain; ancient bell"], trn=["Lucian (E4)"], c2="green")
E("Bonsly", arch=["plant-mimic"], based=["bonsai sapling"], sprite=["rock-orbs"], role=["baby"], c2="")
E("Mime Jr.", arch=["humanoid"], based=["baby mime / harlequin"], sprite=["bowtie","curl"], role=["baby"], c2="red")
E("Happiny", arch=["mammal"], based=["baby (egg pouch)"], sprite=["belly-pouch-stone"], role=["baby"], c2="")
E("Chatot", arch=["bird"], based=["parrot / musical note"], sprite=["note-head","baton-tail"], lore=["mimics speech (Chatter)"], c2="black")
E("Spiritomb", arch=["ghost"], based=["108 bound spirits (Odd Keystone)"], sprite=["keystone","swirl-face"], lore=["108 spirits bound to a keystone; caught only with 32 people via underground"], myth=["108 earthly desires (Buddhist)"], nick=["no weaknesses (pre-Fairy)"], c2="green")
E("Gible", arch=["shark","dragon"], based=["land shark pup"], sprite=["fin-hood","jaws"], trn=["Ash"], c2="red")
E("Gabite", arch=["shark","dragon"], based=["land shark"], sprite=["fins","jaws"], c2="blue")
E("Garchomp", arch=["shark","dragon"], based=["land shark / jet fighter"], sprite=["jet-fins","jaws"], lore=["pseudo; flies at jet speed"], trn=["Cynthia (champion)"], role=["pseudo","mega"], nick=["Cynthia's ace"], c2="red")
E("Munchlax", arch=["bear"], based=["baby glutton"], sprite=["big-belly","bib"], trn=["Ash"], role=["baby"], c2="cream")
E("Riolu", arch=["canine","jackal"], based=["jackal pup (aura)"], sprite=["face-mask","aura-bumps"], lore=["reads emotions via aura"], role=["baby"], c2="black")
E("Lucario", arch=["canine","jackal"], based=["Anubis / jackal (aura knight)"], sprite=["aura-sensors","chest-spike"], lore=["senses aura; Movie 8 (Sir Aaron)"], trn=["Korrina","Maylene (gym)"], role=["mega"], nick=["fan-favourite; Smash rep"], c2="black")
E("Hippopotas", arch=["hippo"], based=["hippo (sand)"], sprite=["sand-body","nostrils"], c2="brown")
E("Hippowdon", arch=["hippo"], based=["hippopotamus"], sprite=["huge-jaws","sand-vents"], trn=["Bertha (E4)"], c2="brown")
E("Skorupi", arch=["scorpion"], based=["scorpion"], sprite=["claws","tail-stinger"], c2="purple")
E("Drapion", arch=["scorpion"], based=["scorpion / ogre"], sprite=["head-claws","armour"], trn=["Aaron (E4)"], c2="purple")
E("Croagunk", arch=["frog"], based=["poison dart frog / con-artist"], sprite=["cheek-sacs","fingers"], trn=["Brock (anime)"], nick=["Poison Jab comic relief"], c2="red")
E("Toxicroak", arch=["frog"], based=["poison frog boxer"], sprite=["throat-sac","knuckle-claws"], trn=["Saturn (Team Galactic)"], c2="red")
E("Carnivine", arch=["plant"], based=["Venus flytrap"], sprite=["jaw-trap","tendrils"], trn=["James (anime)"], c2="yellow")
E("Finneon", arch=["fish"], based=["neon tetra / butterflyfish"], sprite=["tail-fins","glow-marks"], c2="blue")
E("Lumineon", arch=["fish"], based=["neon deep-sea fish"], sprite=["wing-fins","lights"], c2="blue")
E("Mantyke", arch=["fish"], based=["baby manta ray"], sprite=["wings"], role=["baby"], c2="")
E("Snover", arch=["plant"], based=["snowy fir tree"], sprite=["berry-belly","fluff"], c2="white")
E("Abomasnow", arch=["plant"], based=["Yeti / Abominable Snowman"], sprite=["shaggy-ice","spikes"], myth=["yeti"], trn=["Candice (gym)"], role=["mega"], c2="white")
E("Weavile", arch=["mustelid"], based=["weasel + kamaitachi / trickster"], sprite=["ear-feathers","claws"], myth=["kamaitachi"], trn=["Candice? no"], c2="red")
E("Magnezone", arch=["mineral"], based=["UFO / magnet (evolves in a magnetic field)"], sprite=["disc-body","magnets"], c2="red")
E("Lickilicky", arch=["mammal"], based=["licking beast / mochi"], sprite=["curl-tuft","long-tongue"], c2="cream")
E("Rhyperior", arch=["pachyderm","rhino"], based=["rhino + rock drill mecha"], sprite=["drill-hands","armour"], trn=["Bertha (E4)"], c2="")
E("Tangrowth", arch=["plant"], based=["vine mass"], sprite=["vine-arms"], c2="blue")
E("Electivire", arch=["humanoid"], based=["oni + power cables"], sprite=["tail-plugs","stripes"], trn=["Volkner (gym)"], c2="black")
E("Magmortar", arch=["humanoid"], based=["oni + cannon arms"], sprite=["cannon-arms","flame-crown"], trn=["Flint (E4)"], c2="yellow")
E("Togekiss", arch=["bird"], based=["jubilee bird / dove of peace"], sprite=["egg-markings","wings"], lore=["appears in peaceful places"], c2="white")
E("Yanmega", arch=["insect"], based=["Meganeura (giant prehistoric dragonfly)"], sprite=["big-wings","tail-fins"], c2="black")
E("Leafeon", arch=["mammal","fox"], based=["fox / plant (Moss Rock)"], sprite=["leaf-tail","sprout-ears"], role=["eeveelution"], c2="brown")
E("Glaceon", arch=["mammal","fox"], based=["fox / ice (Ice Rock)"], sprite=["ice-crystals"], role=["eeveelution"], c2="blue")
E("Gliscor", arch=["scorpion","bat"], based=["vampire bat + scorpion"], sprite=["fang-grin","wings","tail-pincer"], trn=["Ash"], c2="purple")
E("Mamoswine", arch=["proboscidean"], based=["woolly mammoth"], sprite=["tusks","shaggy-fur"], trn=["Dawn (anime)"], c2="brown")
E("Porygon-Z", arch=["mineral"], based=["hacked 3D model (glitchy)"], sprite=["dislocated-parts"], lore=["a faulty upgrade; acts erratically"], nick=["glitchy hax"], c2="")
E("Gallade", arch=["humanoid"], based=["knight / blade duellist"], sprite=["elbow-blades","chest-fin"], lore=["chivalrous blade master"], role=["mega"], c2="white")
E("Probopass", arch=["mineral"], based=["moai + magnet (mustache)"], sprite=["magnet-mustache","mini-noses"], c2="black")
E("Dusknoir", arch=["ghost"], based=["grim reaper / spirit sender"], sprite=["antenna-mouth","belly-mouth"], c2="")
E("Rotom", arch=["ghost"], based=["ghost in the machine (poltergeist / plasma)"], sprite=["plasma-body","possesses-appliances"], lore=["possesses appliances for extra Formes; Rotom Dex (SM anime)"], myth=["poltergeist"], c2="orange")
E("Uxie", arch=["fairy"], based=["Knowledge (Being of Knowledge)"], sprite=["closed-eyes","tails"], myth=["Lake trio; gave humanity knowledge; Lake Acuity"], role=["legendary"], nick=["Lake guardian trio"], c2="")
E("Mesprit", arch=["fairy"], based=["Emotion (Being of Emotion)"], sprite=["tails","gem-forehead"], myth=["Lake trio; gave humanity emotion; Lake Verity"], role=["legendary"], nick=["Lake guardian trio"], c2="")
E("Azelf", arch=["fairy"], based=["Willpower (Being of Willpower)"], sprite=["tails","gem-forehead"], myth=["Lake trio; gave humanity willpower; Lake Valor"], role=["legendary"], nick=["Lake guardian trio"], c2="")
E("Dialga", arch=["dinosaur","dragon"], based=["Time / diamond (steel dragon)"], sprite=["chest-diamond","fins"], sig="Roar of Time", myth=["controls time; creation trio; Movie 10-11"], role=["legendary"], nick=["box legend (Diamond)"], c2="white")
E("Palkia", arch=["dinosaur","dragon"], based=["Space / pearl (dragon)"], sprite=["shoulder-pearls","fins"], sig="Spacial Rend", myth=["controls space; creation trio; Movie 10-11"], role=["legendary"], nick=["box legend (Pearl)"], c2="purple")
E("Heatran", arch=["mineral"], based=["lava tortoise / magma golem"], sprite=["cross-face","molten-body"], myth=["dwells in volcanic caves"], role=["legendary"], c2="")
E("Regigigas", arch=["golem"], based=["colossus / titan master (moved continents)"], sprite=["stone-body","dot-face"], myth=["towed the continents; master of the Regis"], role=["legendary"], c2="white")
E("Giratina", arch=["dragon","serpent"], based=["antimatter dragon / banished god (Distortion World)"], sprite=["six-wings","ghost-halves"], sig="Shadow Force", myth=["banished for violence; rules the Distortion World; Movie 11"], role=["legendary"], nick=["renegade Pokemon"], c2="black")
E("Cresselia", arch=["fairy"], based=["crescent moon / swan (lunar)"], sprite=["ring-wings","crescents"], sig="Lunar Dance", myth=["brings good dreams; opposes Darkrai; Movie 10"], role=["legendary"], c2="yellow")
E("Phione", arch=["fairy"], based=["sea drifter"], sprite=["antenna","float"], myth=["drifts warm seas"], role=["mythical"], c2="")
E("Manaphy", arch=["fairy"], based=["sea prince / water sprite"], sprite=["antennae","gem-chest"], myth=["Prince of the Sea; Movie 9"], role=["mythical"], c2="yellow")
E("Darkrai", arch=["ghost"], based=["nightmare / boogeyman (New Moon)"], sprite=["shadow-body","red-collar","one-eye"], sig="Dark Void", myth=["causes nightmares; New Moon Island; Movie 10"], role=["mythical"], nick=["gives nightmares"], c2="red")
E("Shaymin", arch=["mammal"], based=["hedgehog + gratitude flowers"], sprite=["flower-collar","sky-forme-wings"], sig="Seed Flare", myth=["Gratitude Pokemon; blooms Gracidea; Movie 11"], role=["mythical"], c2="pink")
E("Arceus", arch=["deity"], based=["creator god (the original one / horse-qilin)"], sprite=["gold-wheel","cross-eyes"], sig="Judgment", myth=["created the Sinnoh universe; 'the original one'; Movie 12"], role=["mythical"], nick=["the God Pokemon"], c2="gray")

SIG.update({
 "Turtwig":"Razor Leaf","Grotle":"Bite","Torterra":"Wood Hammer","Chimchar":"Ember","Monferno":"Mach Punch",
 "Infernape":"Close Combat","Piplup":"Bubble","Prinplup":"Metal Claw","Empoleon":"Hydro Pump","Starly":"Wing Attack",
 "Staravia":"Aerial Ace","Staraptor":"Brave Bird","Bidoof":"Tackle","Bibarel":"Super Fang","Kricketot":"Bide",
 "Kricketune":"Bug Buzz","Shinx":"Spark","Luxio":"Bite","Luxray":"Wild Charge","Budew":"Absorb","Roserade":"Sludge Bomb",
 "Cranidos":"Head Smash","Rampardos":"Head Smash","Shieldon":"Metal Burst","Bastiodon":"Iron Defense","Burmy":"Protect",
 "Wormadam":"Quiver Dance","Mothim":"Bug Buzz","Combee":"Gust","Vespiquen":"Attack Order","Pachirisu":"Nuzzle",
 "Buizel":"Water Gun","Floatzel":"Aqua Jet","Cherubi":"Growth","Cherrim":"Petal Dance","Shellos":"Mud Bomb",
 "Gastrodon":"Muddy Water","Ambipom":"Double Hit","Drifloon":"Ominous Wind","Drifblim":"Shadow Ball","Buneary":"Bounce",
 "Lopunny":"High Jump Kick","Mismagius":"Shadow Ball","Honchkrow":"Sucker Punch","Glameow":"Fake Out","Purugly":"Body Slam",
 "Chingling":"Uproar","Stunky":"Poison Gas","Skuntank":"Sucker Punch","Bronzor":"Confusion","Bronzong":"Gyro Ball",
 "Bonsly":"Rock Throw","Mime Jr.":"Mimic","Happiny":"Pound","Chatot":"Chatter","Spiritomb":"Dark Pulse","Gible":"Dragon Rage",
 "Gabite":"Dragon Claw","Garchomp":"Dragon Rush","Munchlax":"Metronome","Riolu":"Force Palm","Lucario":"Aura Sphere",
 "Hippopotas":"Sand Tomb","Hippowdon":"Earthquake","Skorupi":"Poison Sting","Drapion":"Cross Poison","Croagunk":"Poison Jab",
 "Toxicroak":"Poison Jab","Carnivine":"Vine Whip","Finneon":"Water Pulse","Lumineon":"Silver Wind","Mantyke":"Bubble Beam",
 "Snover":"Ice Shard","Abomasnow":"Blizzard","Weavile":"Ice Punch","Magnezone":"Zap Cannon","Lickilicky":"Wring Out",
 "Rhyperior":"Rock Wrecker","Tangrowth":"Power Whip","Electivire":"Thunder Punch","Magmortar":"Fire Blast","Togekiss":"Air Slash",
 "Yanmega":"Bug Buzz","Leafeon":"Leaf Blade","Glaceon":"Ice Beam","Gliscor":"Earthquake","Mamoswine":"Earthquake",
 "Porygon-Z":"Tri Attack","Gallade":"Psycho Cut","Probopass":"Power Gem","Dusknoir":"Shadow Punch","Froslass":"Ice Beam",
 "Rotom":"Thunderbolt","Uxie":"Future Sight","Mesprit":"Future Sight","Azelf":"Psychic","Dialga":"Roar of Time",
 "Palkia":"Spacial Rend","Heatran":"Magma Storm","Regigigas":"Crush Grip","Giratina":"Shadow Force","Cresselia":"Lunar Dance",
 "Phione":"Water Pulse","Manaphy":"Heart Swap","Darkrai":"Dark Void","Shaymin":"Seed Flare","Arceus":"Judgment",
})
TEAMS.update({
 "Roark (gym)":["Geodude","Onix","Cranidos"],
 "Gardenia (gym)":["Turtwig","Cherrim","Roserade"],
 "Maylene (gym)":["Meditite","Machoke","Lucario"],
 "Crasher Wake (gym)":["Gyarados","Quagsire","Floatzel"],
 "Fantina (gym)":["Duskull","Haunter","Mismagius","Gengar"],
 "Byron (gym)":["Bronzor","Steelix","Bastiodon"],
 "Candice (gym)":["Sneasel","Piloswine","Abomasnow","Froslass","Medicham"],
 "Volkner (gym)":["Raichu","Octillery","Luxray","Electivire","Ambipom"],
 "Aaron (E4)":["Dustox","Beautifly","Vespiquen","Heracross","Drapion"],
 "Bertha (E4)":["Whiscash","Gliscor","Hippowdon","Golem","Rhyperior"],
 "Flint (E4)":["Rapidash","Steelix","Drifblim","Lopunny","Infernape","Magmortar"],
 "Lucian (E4)":["Mr. Mime","Girafarig","Medicham","Alakazam","Bronzong"],
 "Cynthia (champion)":["Spiritomb","Roserade","Gastrodon","Lucario","Milotic","Garchomp"],
})

# ============================== GEN 5 (Unova) ==============================
E("Victini", arch=["fairy"], based=["rabbit / fox + victory (V-shape)"], sprite=["V-ears","big-eyes"], sig="V-create", lore=["brings victory to its trainer"], myth=["Victory Pokemon; Movie 14 (Black/White)"], role=["mythical"], c2="cream")
E("Snivy", arch=["reptile","serpent"], based=["grass snake / gecko"], sprite=["leaf-collar","regal-look"], lore=["starter"], role=["starter"], c2="cream")
E("Servine", arch=["reptile","serpent"], based=["vine snake"], sprite=["leaf-arms"], c2="cream")
E("Serperior", arch=["reptile","serpent"], based=["royal cobra / regal serpent"], sprite=["collar-frill","regal-glare"], lore=["intimidates with a regal gaze"], role=["starter"], c2="cream")
E("Tepig", arch=["boar","pig"], based=["piglet"], sprite=["snout","curl-tail"], lore=["starter"], trn=["Ash"], role=["starter"], c2="black")
E("Pignite", arch=["boar","pig"], based=["fire pig / wrestler"], sprite=["flame-belt"], c2="black")
E("Emboar", arch=["boar","pig"], based=["boar + flaming beard (Zhu Bajie)"], sprite=["beard-flames","chest"], role=["starter"], c2="red")
E("Oshawott", arch=["mustelid","otter"], based=["sea otter (samurai)"], sprite=["belly-scalchop","whiskers"], lore=["starter; scalchop shell weapon"], trn=["Ash"], role=["starter"], nick=["Ash's Oshawott"], c2="white")
E("Dewott", arch=["mustelid","otter"], based=["otter (dual scalchops)"], sprite=["twin-scalchops"], c2="")
E("Samurott", arch=["mustelid","otter"], based=["sea otter samurai / seamitar"], sprite=["seamitar-armour","whiskers"], role=["starter"], c2="")
E("Patrat", arch=["rodent"], based=["prairie dog / meerkat sentry"], sprite=["scout-eyes","tail"], c2="brown")
E("Watchog", arch=["rodent"], based=["meerkat lookout"], sprite=["glowing-stripes","eyes"], trn=["Lenora (gym)"], c2="yellow")
E("Lillipup", arch=["canine"], based=["Yorkshire terrier puppy"], sprite=["face-fur"], c2="cream")
E("Herdier", arch=["canine"], based=["terrier / sheepdog"], sprite=["cloak-fur"], c2="black")
E("Stoutland", arch=["canine"], based=["Scottish terrier / mustached gentleman"], sprite=["mustache","beard-fur"], c2="")
E("Purrloin", arch=["feline","cat"], based=["burglar cat"], sprite=["mask","curl-tail"], c2="")
E("Liepard", arch=["feline","leopard"], based=["leopard / thief"], sprite=["sleek-body","spots"], trn=["Grimsley (E4)"], c2="")
E("Pansage", arch=["primate","monkey"], based=["monkey + broccoli"], sprite=["leaf-crown"], c2="")
E("Simisage", arch=["primate","monkey"], based=["monkey (grass)"], sprite=["thorn-tail"], c2="")
E("Pansear", arch=["primate","monkey"], based=["monkey + fire tuft"], sprite=["flame-crown"], c2="")
E("Simisear", arch=["primate","monkey"], based=["monkey (fire)"], sprite=["flame-brows"], c2="")
E("Panpour", arch=["primate","monkey"], based=["monkey + water tuft"], sprite=["water-crown"], c2="")
E("Simipour", arch=["primate","monkey"], based=["monkey (water)"], sprite=["water-plume"], c2="")
E("Munna", arch=["tapir"], based=["tapir (baku dream-eater)"], sprite=["flower-pattern"], myth=["baku (dream eater)"], c2="pink")
E("Musharna", arch=["tapir"], based=["tapir + dream smoke"], sprite=["dream-mist","forehead"], trn=["Caitlin (E4)"], c2="")
E("Pidove", arch=["bird"], based=["city pigeon"], sprite=["heart-nose"], c2="gray")
E("Tranquill", arch=["bird"], based=["dove"], sprite=["wing-bands"], c2="gray")
E("Unfezant", arch=["bird"], based=["pheasant"], sprite=["face-plumes (male)"], trn=["Skyla (gym)"], c2="")
E("Blitzle", arch=["equine","zebra"], based=["zebra foal"], sprite=["lightning-mane"], c2="white")
E("Zebstrika", arch=["equine","zebra"], based=["zebra"], sprite=["bolt-mane","stripes"], trn=["Elesa (gym)"], c2="white")
E("Roggenrola", arch=["mineral"], based=["geode / ore"], sprite=["hexagon-ear","crystal-core"], c2="blue")
E("Boldore", arch=["mineral"], based=["ore cluster"], sprite=["orange-crystals"], c2="blue")
E("Gigalith", arch=["mineral"], based=["compressed rock (solar cannon)"], sprite=["core-crystals","spikes"], trn=["Clay (gym)"], c2="red")
E("Woobat", arch=["chiropteran","bat"], based=["bat (heart nose)"], sprite=["heart-nose","fluffy"], c2="")
E("Swoobat", arch=["chiropteran","bat"], based=["fruit bat"], sprite=["heart-nose","ears"], trn=["Skyla (gym)"], c2="")
E("Drilbur", arch=["mole"], based=["mole (drill)"], sprite=["claws","spin"], c2="")
E("Excadrill", arch=["mole"], based=["mole + drill machine"], sprite=["drill-head","claws"], trn=["Clay (gym)","Iris (champion)"], c2="")
E("Audino", arch=["mammal"], based=["nurse / rabbit (stethoscope ears)"], sprite=["feeler-ears"], lore=["hears heartbeats; EXP grinder"], role=["mega"], c2="pink")
E("Timburr", arch=["humanoid"], based=["construction worker (carries beam)"], sprite=["wooden-beam"], c2="gray")
E("Gurdurr", arch=["humanoid"], based=["builder (girder)"], sprite=["steel-girder","muscles"], c2="gray")
E("Conkeldurr", arch=["humanoid"], based=["builder (concrete pillars)"], sprite=["concrete-pillars","mustache"], trn=["Marshal (E4)"], c2="brown")
E("Tympole", arch=["frog","tadpole"], based=["tadpole (sound waves)"], sprite=["cheek-vibrations"], c2="")
E("Palpitoad", arch=["frog"], based=["toad / tadpole"], sprite=["bumps","big-eyes"], c2="")
E("Seismitoad", arch=["frog"], based=["toad (bufo / vibrations)"], sprite=["warty-bumps"], c2="")
E("Throh", arch=["humanoid"], based=["judoka (red gi)"], sprite=["red-body","belt"], lore=["always found with Sawk; judo"], trn=["Marshal (E4)"], c2="white")
E("Sawk", arch=["humanoid"], based=["karateka (blue gi)"], sprite=["blue-body","belt"], lore=["karate rival to Throh"], trn=["Marshal (E4)"], c2="white")
E("Sewaddle", arch=["insect"], based=["caterpillar + leaf hood (tailor)"], sprite=["leaf-hood"], c2="green")
E("Swadloon", arch=["insect"], based=["leaf-wrapped larva"], sprite=["leaf-cloak"], c2="green")
E("Leavanny", arch=["insect","mantis"], based=["mantis + tailor / seamstress"], sprite=["leaf-arms","sewing"], lore=["sews clothes of leaves for others"], trn=["Ash","Burgh (gym)"], c2="green")
E("Venipede", arch=["insect"], based=["centipede"], sprite=["antennae","segments"], c2="red")
E("Whirlipede", arch=["insect","pupa"], based=["cocoon / wheel"], sprite=["wheel-shell","horns"], c2="")
E("Scolipede", arch=["insect"], based=["centipede (megarian)"], sprite=["horn-mandibles","legs"], c2="")
E("Cottonee", arch=["plant","fairy"], based=["cotton boll / dandelion"], sprite=["cotton-puff"], c2="green")
E("Whimsicott", arch=["plant","fairy"], based=["sheep + cotton sprite (trickster)"], sprite=["cotton-mane","curls"], lore=["prankster; slips through gaps"], c2="brown")
E("Petilil", arch=["plant"], based=["bulb / seedling"], sprite=["leaf-head"], c2="green")
E("Lilligant", arch=["plant"], based=["lily / garden flower (dancer)"], sprite=["flower-crown"], c2="green")
E("Basculin", arch=["fish"], based=["bass (red/blue stripe rivalry)"], sprite=["stripe","fangs"], lore=["red-striped and blue-striped forms fight"], c2="")
E("Sandile", arch=["reptile","crocodile"], based=["crocodile in sand (shades)"], sprite=["eye-stripe","sandy"], c2="black")
E("Krokorok", arch=["reptile","crocodile"], based=["crocodile (desert goggles)"], sprite=["eye-mask","stripes"], trn=["Ash"], c2="black")
E("Krookodile", arch=["reptile","crocodile"], based=["crocodile + sunglasses gangster"], sprite=["eye-shades","red-hide"], trn=["Ash","Grimsley (E4)"], c2="black")
E("Darumaka", arch=["mammal"], based=["Daruma doll (roly-poly)"], sprite=["round","eyebrows"], myth=["Daruma doll"], c2="")
E("Darmanitan", arch=["primate"], based=["Daruma doll + baboon (Zen Mode)"], sprite=["flame-brows","Zen-statue"], lore=["switches to a stone Zen Mode at low HP"], myth=["Daruma / Bodhidharma"], c2="")
E("Maractus", arch=["plant"], based=["cactus (maracas dancer)"], sprite=["maraca-arms","flowers"], c2="green")
E("Dwebble", arch=["crustacean"], based=["hermit crab (rock shell)"], sprite=["rock-shell","pincers"], c2="red")
E("Crustle", arch=["crustacean"], based=["hermit crab (rock slab)"], sprite=["boulder-shell","legs"], trn=["Ash"], c2="red")
E("Scraggy", arch=["reptile","lizard"], based=["lizard + saggy trousers (delinquent)"], sprite=["pants-skin","crest"], trn=["Ash"], c2="yellow")
E("Scrafty", arch=["reptile","lizard"], based=["lizard hoodie thug (mohawk)"], sprite=["hood-skin","crest"], trn=["Grimsley (E4)"], c2="red")
E("Sigilyph", arch=["bird"], based=["Nazca Lines / psychic guardian"], sprite=["geometric-body","eye-wings"], myth=["Nazca geoglyphs; guards ruins"], c2="")
E("Yamask", arch=["ghost"], based=["mummy / spirit carrying its human face-mask"], sprite=["mask-hands","tail"], lore=["carries a mask of its face from when it was human"], myth=["Egyptian mummy"], nick=["saddest dex entry"], c2="")
E("Cofagrigus", arch=["ghost"], based=["sarcophagus / Egyptian coffin"], sprite=["gold-coffin","shadow-hands"], myth=["cursed tomb; eats grave robbers"], trn=["Shauntal (E4)"], c2="yellow")
E("Tirtouga", arch=["turtle"], based=["Archelon (fossil sea turtle)"], sprite=["shell","flippers"], role=["fossil"], c2="blue")
E("Carracosta", arch=["turtle"], based=["prehistoric sea turtle"], sprite=["shell-armour","tusks"], role=["fossil"], c2="blue")
E("Archen", arch=["bird"], based=["Archaeopteryx (fossil)"], sprite=["feathered-arms"], role=["fossil"], c2="yellow")
E("Archeops", arch=["bird","raptor"], based=["Archaeopteryx (first bird)"], sprite=["feathered-wings","head-plumes"], trn=["Iris (champion)"], role=["fossil"], c2="red")
E("Trubbish", arch=["amorphous"], based=["rubbish bag"], sprite=["trash-bag-body"], c2="")
E("Garbodor", arch=["amorphous"], based=["pile of garbage"], sprite=["trash-body","arm-pipe"], role=["gmax"], nick=["'trash bag' derided design"], c2="")
E("Zorua", arch=["canine","fox"], based=["fox kit (illusion)"], sprite=["scruff-tuft"], lore=["Illusion; Movie 13"], myth=["kitsune"], c2="black")
E("Zoroark", arch=["canine","fox"], based=["nine-tailed fox trickster"], sprite=["ponytail-mane"], lore=["master of illusions; Movie 13"], myth=["kitsune / bakemono"], role=[], c2="red")
E("Minccino", arch=["rodent"], based=["chinchilla"], sprite=["scarf-fur","broom-tail"], c2="")
E("Cinccino", arch=["rodent"], based=["chinchilla (fur scarf)"], sprite=["fur-stole"], c2="")
E("Gothita", arch=["humanoid"], based=["gothic lolita (ribbons)"], sprite=["bow-hair","big-eyes"], c2="")
E("Gothorita", arch=["humanoid"], based=["gothic lolita"], sprite=["star-hair"], myth=["said to control stars"], c2="")
E("Gothitelle", arch=["humanoid"], based=["gothic lolita astrologer"], sprite=["gown","star-hair"], lore=["reads the future in the stars"], trn=["Caitlin (E4)"], c2="")
E("Solosis", arch=["cell"], based=["cell / embryo in fluid"], sprite=["gel-membrane"], c2="")
E("Duosion", arch=["cell"], based=["dividing cell (split brain)"], sprite=["split-core"], c2="")
E("Reuniclus", arch=["cell"], based=["homunculus / cell colony"], sprite=["gel-arms","core"], trn=["Caitlin (E4)"], c2="green")
E("Ducklett", arch=["bird"], based=["duckling / cygnet"], sprite=["round-body"], c2="blue")
E("Swanna", arch=["bird"], based=["swan (ballet)"], sprite=["long-neck","crest"], trn=["Skyla (gym)"], c2="white")
E("Vanillite", arch=["mineral"], based=["soft-serve ice cream / icicle"], sprite=["ice-cream-swirl"], nick=["'it's ice cream' derided design"], c2="")
E("Vanillish", arch=["mineral"], based=["ice cream"], sprite=["icy-body"], c2="")
E("Vanilluxe", arch=["mineral"], based=["twin soft-serve ice cream"], sprite=["two-heads-swirl"], nick=["ice cream meme"], c2="")
E("Deerling", arch=["deer"], based=["fawn (seasonal coat)"], sprite=["flower-ears","seasonal-colour"], c2="pink")
E("Sawsbuck", arch=["deer"], based=["deer (antlers change with seasons)"], sprite=["tree-antlers"], c2="brown")
E("Emolga", arch=["rodent"], based=["flying squirrel / sugar glider"], sprite=["cape-membrane","cheeks"], trn=["Elesa (gym)","Iris (anime)"], c2="yellow")
E("Karrablast", arch=["insect"], based=["beetle larva / knight"], sprite=["horn","claws"], c2="blue")
E("Escavalier", arch=["insect"], based=["cavalier knight (lance & armour)"], sprite=["lance-arms","helmet"], lore=["wears Shelmet's shell; trade evolution"], c2="")
E("Foongus", arch=["fungus"], based=["mushroom disguised as a Poke Ball"], sprite=["poke-ball-cap"], lore=["lures with its Poke Ball pattern"], nick=["Poke Ball troll"], c2="white")
E("Amoonguss", arch=["fungus"], based=["mushroom (Poke Ball caps)"], sprite=["poke-ball-arms"], c2="white")
E("Frillish", arch=["cnidarian","jellyfish"], based=["jellyfish (male/female)"], sprite=["frill-veil"], c2="")
E("Jellicent", arch=["cnidarian","jellyfish"], based=["jellyfish gentleman/lady (mustache/crown)"], sprite=["mustache-frills"], trn=["Shauntal (E4)"], c2="")
E("Alomomola", arch=["fish"], based=["ocean sunfish / mola (caretaker)"], sprite=["heart-shape","fins"], lore=["heals injured Pokemon at sea"], c2="pink")
E("Joltik", arch=["arachnid","spider"], based=["tick / spider (static)"], sprite=["tiny","four-eyes"], lore=["smallest Pokemon (0.1 m)"], c2="yellow")
E("Galvantula", arch=["arachnid","spider"], based=["tarantula (electric web)"], sprite=["fuzzy","fangs"], sig="Electroweb", c2="yellow")
E("Ferroseed", arch=["plant"], based=["durian / spiky seed / caltrop"], sprite=["spikes","ore-body"], c2="")
E("Ferrothorn", arch=["plant"], based=["durian on a vine / mine"], sprite=["thorn-vines","spikes"], c2="")
E("Klink", arch=["mineral"], based=["interlocking gears"], sprite=["twin-gears"], c2="")
E("Klang", arch=["mineral"], based=["gears (minigear + gear)"], sprite=["gear-ring"], c2="")
E("Klinklang", arch=["mineral"], based=["gear system (crown gear)"], sprite=["spinning-gears","spike"], c2="red")
E("Tynamo", arch=["fish"], based=["lamprey / eel larva"], sprite=["glowing-nub"], c2="white")
E("Eelektrik", arch=["fish"], based=["electric eel / lamprey"], sprite=["sucker-mouth","spots"], c2="blue")
E("Eelektross", arch=["fish"], based=["electric eel (lamprey jaws)"], sprite=["sucker-mouth","fangs"], lore=["no type weaknesses (Levitate)"], c2="red")
E("Elgyem", arch=["alien"], based=["grey alien (Roswell)"], sprite=["big-head","finger-lights"], myth=["Roswell UFO / grey alien"], c2="blue")
E("Beheeyem", arch=["alien"], based=["grey alien (communicates with lights)"], sprite=["finger-lights","brown-body"], myth=["extraterrestrial"], c2="brown")
E("Litwick", arch=["ghost"], based=["candle / will-o-wisp (soul thief)"], sprite=["candle-body","flame"], lore=["lures with its flame then drains life"], myth=["will-o-wisp / hitodama"], c2="yellow")
E("Lampent", arch=["ghost"], based=["street lamp (grim escort)"], sprite=["lamp-body","flame"], lore=["appears near the dying to take their spirit"], c2="")
E("Chandelure", arch=["ghost"], based=["chandelier (soul-burning)"], sprite=["candelabra-arms","flames"], lore=["its flames burn the spirit, not the body"], myth=["will-o-wisp"], trn=["Shauntal (E4)"], c2="black")
E("Axew", arch=["dragon"], based=["dragon (tusk axe)"], sprite=["tusks"], trn=["Iris (anime)"], c2="green")
E("Fraxure", arch=["dragon"], based=["dragon (axe tusks)"], sprite=["axe-tusks"], trn=["Drayden (gym)"], c2="green")
E("Haxorus", arch=["dragon"], based=["dragon / armoured tusk-axe"], sprite=["axe-jaw-tusks","armour"], trn=["Iris (champion)","Drayden (gym)"], c2="yellow")
E("Cubchoo", arch=["bear"], based=["polar bear cub (runny nose)"], sprite=["snot-nose"], nick=["snotty nose"], c2="white")
E("Beartic", arch=["bear"], based=["polar bear (ice beard)"], sprite=["ice-beard","claws"], trn=["Brycen (gym)"], c2="white")
E("Cryogonal", arch=["mineral"], based=["snowflake / ice crystal (chains)"], sprite=["crystal-face","ice-chains"], trn=["Brycen (gym)"], c2="")
E("Shelmet", arch=["mollusc"], based=["snail (helmet)"], sprite=["shell-helmet"], c2="red")
E("Accelgor", arch=["mollusc"], based=["slug ninja"], sprite=["scarf-cape","ninja-wrap"], lore=["trade evo with Karrablast; ninja-fast"], c2="")
E("Stunfisk", arch=["fish"], based=["flounder / stargazer (electric mud)"], sprite=["flat-body","lips"], nick=["derpy flatfish meme"], c2="brown")
E("Mienfoo", arch=["mustelid"], based=["weasel martial artist"], sprite=["sleeve-arms"], c2="yellow")
E("Mienshao", arch=["mustelid"], based=["weasel kung-fu master (sleeve whips)"], sprite=["long-fur-sleeves"], trn=["Marshal (E4)"], c2="purple")
E("Druddigon", arch=["dragon"], based=["gargoyle dragon"], sprite=["red-face","claws"], trn=["Iris (champion)"], c2="blue")
E("Golett", arch=["automaton"], based=["ancient clay golem (automaton)"], sprite=["glow-core","seal-body"], myth=["ancient automaton"], c2="")
E("Golurk", arch=["automaton"], based=["golem / mecha (rocket flight)"], sprite=["seal-chest","fists"], myth=["built to protect people; sealed"], c2="")
E("Pawniard", arch=["blade"], based=["pawn (chess) / blade"], sprite=["blade-body","helmet"], c2="red")
E("Bisharp", arch=["blade"], based=["bishop (chess) warlord"], sprite=["axe-head","blade-arms"], trn=["Grimsley (E4)"], c2="red")
E("Bouffalant", arch=["bovine"], based=["buffalo / bison (afro)"], sprite=["afro","horns"], trn=["Alder (champion)"], c2="black")
E("Rufflet", arch=["bird","raptor"], based=["eaglet"], sprite=["headwing-plumes"], trn=["Ash"], c2="white")
E("Braviary", arch=["bird","raptor","eagle"], based=["bald eagle (valour)"], sprite=["head-plumes","talons"], lore=["symbol of valour; fights for friends"], c2="red")
E("Vullaby", arch=["bird"], based=["vulture chick (bone diaper)"], sprite=["bone-skirt"], c2="")
E("Mandibuzz", arch=["bird"], based=["vulture matriarch (bone jewellery)"], sprite=["bone-skirt","hair-plumes"], trn=["Grimsley? no"], c2="brown")
E("Heatmor", arch=["mammal"], based=["anteater + furnace"], sprite=["flame-tongue","chimney"], c2="red")
E("Durant", arch=["insect"], based=["armoured ant"], sprite=["steel-armour","mandibles"], c2="gray")
E("Deino", arch=["dragon"], based=["hydra head (blind)"], sprite=["fur-mane","fangs"], myth=["hydra / Yamata-no-Orochi"], c2="blue")
E("Zweilous", arch=["dragon"], based=["two-headed hydra"], sprite=["two-heads","mane"], myth=["hydra"], c2="blue")
E("Hydreigon", arch=["dragon"], based=["three-headed hydra / Cerberus (arms as heads)"], sprite=["three-heads","wings"], lore=["pseudo; heads on its arms"], myth=["hydra / Yamata-no-Orochi"], trn=["Iris (champion)"], role=["pseudo"], c2="black")
E("Larvesta", arch=["insect"], based=["larva / sun moth caterpillar"], sprite=["horn-flames","fuzzy"], c2="white")
E("Volcarona", arch=["insect","moth"], based=["sun moth / Mothra (giver of warmth)"], sprite=["sun-wings","fluff"], lore=["revered as a substitute for the sun"], myth=["sun deity / Mothra"], trn=["Alder (champion)"], c2="")
E("Cobalion", arch=["mammal"], based=["Musketeer (Athos) / ibex (steel)"], sprite=["horns","mane"], myth=["Swords of Justice; protected Pokemon from war"], role=["legendary"], nick=["Musketeer quartet"], c2="")
E("Terrakion", arch=["mammal"], based=["Musketeer (Porthos) / bison (rock)"], sprite=["horns","bulk"], myth=["Swords of Justice"], role=["legendary"], nick=["Musketeer quartet"], c2="")
E("Virizion", arch=["mammal"], based=["Musketeer (Aramis) / antelope (grass)"], sprite=["horn-blades","mane"], myth=["Swords of Justice"], role=["legendary"], nick=["Musketeer quartet"], c2="")
E("Keldeo", arch=["equine"], based=["Musketeer (d'Artagnan) / colt (water)"], sprite=["horn","mane"], sig="Secret Sword", myth=["Sword of Justice trainee; Movie 15"], role=["mythical"], c2="white")
E("Tornadus", arch=["genie"], based=["Fujin (wind kami) / genie"], sprite=["cloud-tail","spikes"], myth=["Forces of Nature (kami trio)"], role=["legendary"], c2="")
E("Thundurus", arch=["genie"], based=["Raijin (thunder kami) / genie"], sprite=["cloud-tail","spikes"], myth=["Forces of Nature (kami trio)"], role=["legendary"], c2="blue")
E("Reshiram", arch=["dragon"], based=["white dragon of Truth (yin) / feathered serpent"], sprite=["turbine-tail","feathers"], sig="Fusion Flare", myth=["Tao trio (Truth); Original Dragon"], role=["legendary"], nick=["box legend (Black)"], c2="")
E("Zekrom", arch=["dragon"], based=["black dragon of Ideals (yang) / electric serpent"], sprite=["turbine-tail","scales"], sig="Fusion Bolt", myth=["Tao trio (Ideals); Original Dragon"], role=["legendary"], nick=["box legend (White)"], c2="")
E("Landorus", arch=["genie"], based=["Inari (harvest kami) / genie"], sprite=["cloud-tail","tusks"], myth=["Forces of Nature; brings fertile soil"], role=["legendary"], nick=["kami trio 'Landorus-T' VGC king"], c2="")
E("Kyurem", arch=["dragon"], based=["boundary dragon (permafrost husk of the Original Dragon)"], sprite=["ice-wings","cracked-body"], sig="Glaciate", myth=["Tao trio remnant; fuses with Reshiram/Zekrom"], role=["legendary"], nick=["box legend (B2/W2)"], c2="")
E("Meloetta", arch=["fairy"], based=["muse / songstress"], sprite=["music-note-hair","Pirouette-forme"], sig="Relic Song", myth=["melodies move hearts; Movie 15"], role=["mythical"], c2="green")
E("Genesect", arch=["insect"], based=["cyborg fossil bug (Team Plasma)"], sprite=["cannon-back","mecha-legs"], sig="Techno Blast", myth=["ancient bug revived & weaponised; Movie 16"], role=["mythical"], c2="purple")

SIG.update({
 "Snivy":"Leaf Tornado","Servine":"Leaf Blade","Serperior":"Leaf Storm","Tepig":"Ember","Pignite":"Arm Thrust",
 "Emboar":"Flare Blitz","Oshawott":"Razor Shell","Dewott":"Razor Shell","Samurott":"Razor Shell","Patrat":"Bite",
 "Watchog":"Hypnosis","Lillipup":"Bite","Herdier":"Take Down","Stoutland":"Play Rough","Purrloin":"Sucker Punch",
 "Liepard":"Night Slash","Pansage":"Seed Bomb","Simisage":"Seed Bomb","Pansear":"Incinerate","Simisear":"Flame Burst",
 "Panpour":"Scald","Simipour":"Scald","Munna":"Hypnosis","Musharna":"Dream Eater","Pidove":"Air Cutter",
 "Tranquill":"Air Slash","Unfezant":"Sky Attack","Blitzle":"Spark","Zebstrika":"Wild Charge","Roggenrola":"Rock Blast",
 "Boldore":"Rock Blast","Gigalith":"Stone Edge","Woobat":"Air Slash","Swoobat":"Psychic","Drilbur":"Dig",
 "Excadrill":"Earthquake","Audino":"Secret Power","Timburr":"Rock Throw","Gurdurr":"Hammer Arm","Conkeldurr":"Drain Punch",
 "Tympole":"Bubble Beam","Palpitoad":"Muddy Water","Seismitoad":"Earthquake","Throh":"Circle Throw","Sawk":"Karate Chop",
 "Sewaddle":"Bug Bite","Swadloon":"Razor Leaf","Leavanny":"Leaf Blade","Venipede":"Poison Sting","Whirlipede":"Iron Defense",
 "Scolipede":"Megahorn","Cottonee":"Cotton Guard","Whimsicott":"Moonblast","Petilil":"Magical Leaf","Lilligant":"Petal Dance",
 "Basculin":"Aqua Jet","Sandile":"Bite","Krokorok":"Crunch","Krookodile":"Earthquake","Darumaka":"Fire Punch",
 "Darmanitan":"Flare Blitz","Maractus":"Petal Dance","Dwebble":"Rock Slide","Crustle":"X-Scissor","Scraggy":"Hi Jump Kick",
 "Scrafty":"Drain Punch","Sigilyph":"Air Slash","Yamask":"Shadow Ball","Cofagrigus":"Shadow Ball","Tirtouga":"Aqua Jet",
 "Carracosta":"Shell Smash","Archen":"Rock Throw","Archeops":"Acrobatics","Trubbish":"Sludge Bomb","Garbodor":"Gunk Shot",
 "Zorua":"Night Daze","Zoroark":"Night Daze","Minccino":"Tail Slap","Cinccino":"Tail Slap","Gothita":"Confusion",
 "Gothorita":"Psychic","Gothitelle":"Psychic","Solosis":"Psywave","Duosion":"Psyshock","Reuniclus":"Psychic",
 "Ducklett":"Water Pulse","Swanna":"Hurricane","Vanillite":"Icicle Spear","Vanillish":"Ice Beam","Vanilluxe":"Blizzard",
 "Deerling":"Jump Kick","Sawsbuck":"Horn Leech","Emolga":"Nuzzle","Karrablast":"Fury Cutter","Escavalier":"Megahorn",
 "Foongus":"Clear Smog","Amoonguss":"Spore","Frillish":"Water Pulse","Jellicent":"Water Spout","Alomomola":"Wish",
 "Joltik":"Electroweb","Galvantula":"Thunder","Ferroseed":"Pin Missile","Ferrothorn":"Gyro Ball","Klink":"Gear Grind",
 "Klang":"Gear Grind","Klinklang":"Gear Grind","Tynamo":"Spark","Eelektrik":"Discharge","Eelektross":"Crunch",
 "Elgyem":"Psybeam","Beheeyem":"Psychic","Litwick":"Ember","Lampent":"Will-O-Wisp","Chandelure":"Shadow Ball",
 "Axew":"Dragon Claw","Fraxure":"Dragon Claw","Haxorus":"Dragon Dance","Cubchoo":"Powder Snow","Beartic":"Icicle Crash",
 "Cryogonal":"Ice Beam","Shelmet":"Acid","Accelgor":"Bug Buzz","Stunfisk":"Mud Bomb","Mienfoo":"Drain Punch",
 "Mienshao":"Hi Jump Kick","Druddigon":"Dragon Claw","Golett":"Shadow Punch","Golurk":"Earthquake","Pawniard":"Metal Claw",
 "Bisharp":"Iron Head","Bouffalant":"Head Charge","Rufflet":"Wing Attack","Braviary":"Brave Bird","Vullaby":"Pluck",
 "Mandibuzz":"Foul Play","Heatmor":"Fire Lash","Durant":"Iron Head","Deino":"Dragon Rage","Zweilous":"Dragon Pulse",
 "Hydreigon":"Draco Meteor","Larvesta":"Flame Charge","Volcarona":"Quiver Dance","Cobalion":"Sacred Sword",
 "Terrakion":"Sacred Sword","Virizion":"Sacred Sword","Keldeo":"Secret Sword","Tornadus":"Hurricane","Thundurus":"Thunder",
 "Reshiram":"Fusion Flare","Zekrom":"Fusion Bolt","Landorus":"Earthquake","Kyurem":"Glaciate","Meloetta":"Relic Song",
 "Genesect":"Techno Blast",
})
TEAMS.update({
 "Cilan (gym)":["Pansage"],"Chili (gym)":["Pansear"],"Cress (gym)":["Panpour"],
 "Lenora (gym)":["Herdier","Watchog"],
 "Burgh (gym)":["Whirlipede","Dwebble","Leavanny"],
 "Elesa (gym)":["Emolga","Flaaffy","Zebstrika","Tynamo"],
 "Clay (gym)":["Krokorok","Palpitoad","Excadrill","Gigalith"],
 "Skyla (gym)":["Swoobat","Unfezant","Swanna","Skarmory"],
 "Brycen (gym)":["Vanillish","Cryogonal","Beartic"],
 "Drayden (gym)":["Fraxure","Druddigon","Haxorus"],
 "Shauntal (E4)":["Cofagrigus","Chandelure","Golurk","Drifblim","Jellicent"],
 "Grimsley (E4)":["Scrafty","Krookodile","Liepard","Bisharp","Absol"],
 "Marshal (E4)":["Throh","Sawk","Conkeldurr","Mienshao","Lucario"],
 "Caitlin (E4)":["Musharna","Gothitelle","Sigilyph","Reuniclus","Metagross"],
 "Alder (champion)":["Volcarona","Bouffalant","Vanilluxe","Accelgor","Escavalier","Conkeldurr"],
 "Iris (champion)":["Hydreigon","Haxorus","Lapras","Aggron","Archeops","Druddigon","Excadrill"],
})

# ============================== GEN 6 (Kalos) ==============================
E("Chespin", arch=["mammal"], based=["hedgehog / chestnut"], sprite=["nut-hood","spikes"], lore=["starter"], role=["starter"], c2="green")
E("Quilladin", arch=["mammal"], based=["chestnut burr / armadillo"], sprite=["spiky-shell"], c2="green")
E("Chesnaught", arch=["mammal"], based=["chestnut knight / hedgehog"], sprite=["armour-shell","spikes"], role=["starter"], c2="gray")
E("Fennekin", arch=["fox","canine"], based=["fennec fox"], sprite=["ear-tufts","fluffy-tail"], lore=["starter"], role=["starter"], c2="orange")
E("Braixen", arch=["fox","canine"], based=["fox mage (wand in tail)"], sprite=["twig-wand","skirt-fur"], c2="red")
E("Delphox", arch=["fox","canine"], based=["fox witch / sorceress (kitsune)"], sprite=["robe","wand-stick"], myth=["kitsune / witch"], role=["starter"], c2="red")
E("Froakie", arch=["frog"], based=["frog (bubble foam)"], sprite=["foam-collar"], lore=["starter"], trn=["Ash"], role=["starter"], c2="white")
E("Frogadier", arch=["frog"], based=["frog ninja"], sprite=["foam-cloak"], c2="white")
E("Greninja", arch=["frog"], based=["frog ninja (tongue scarf)"], sprite=["tongue-scarf","webbed"], lore=["Ash-Greninja bond forme; Smash rep"], trn=["Ash"], role=["starter"], nick=["Ash-Greninja; fan favourite"], c2="white")
E("Bunnelby", arch=["mammal"], based=["rabbit (digging ears)"], sprite=["shovel-ears"], c2="brown")
E("Diggersby", arch=["mammal"], based=["rabbit + digger (excavator)"], sprite=["mud-ears","belly"], lore=["ears dig like backhoes; surprise Huge Power tank"], c2="brown")
E("Fletchling", arch=["bird"], based=["European robin"], sprite=["orange-face"], trn=["Ash"], c2="gray")
E("Fletchinder", arch=["bird"], based=["robin (ember)"], sprite=["flame-crest"], c2="black")
E("Talonflame", arch=["bird","raptor","falcon"], based=["peregrine falcon"], sprite=["flame-feathers","talons"], sig="Brave Bird", c2="black")
E("Scatterbug", arch=["insect"], based=["caterpillar"], sprite=["black-body"], c2="")
E("Spewpa", arch=["insect","pupa"], based=["cocoon"], sprite=["fuzzy-shell"], c2="")
E("Vivillon", arch=["insect","butterfly"], based=["butterfly (regional wing patterns)"], sprite=["patterned-wings"], lore=["wing pattern depends on real-world region"], c2="")
E("Litleo", arch=["feline","lion"], based=["lion cub"], sprite=["mane-tuft"], c2="red")
E("Pyroar", arch=["feline","lion"], based=["lion (male mane / female)"], sprite=["flame-mane"], trn=["Malva (E4)"], c2="red")
E("Flabébé", arch=["fairy"], based=["fairy holding a flower"], sprite=["flower-hold"], lore=["AZ's Floette (eternal flower) plot"], c2="")
E("Floette", arch=["fairy"], based=["flower fairy"], sprite=["petal-dress"], c2="")
E("Florges", arch=["fairy"], based=["garden / bouquet fairy"], sprite=["flower-crown","gown"], trn=["Valerie? no"], c2="green")
E("Skiddo", arch=["goat"], based=["kid goat (rideable)"], sprite=["leaf-horns"], c2="brown")
E("Gogoat", arch=["goat"], based=["mountain goat (mount)"], sprite=["leaf-horns","mane"], trn=["Ramos (gym)"], c2="brown")
E("Pancham", arch=["mammal"], based=["panda cub (delinquent)"], sprite=["leaf-in-mouth","scowl"], trn=["Ash"], c2="black")
E("Pangoro", arch=["mammal"], based=["panda yakuza / bear brawler"], sprite=["cape-fur","leaf-toothpick"], c2="black")
E("Furfrou", arch=["canine"], based=["poodle (groomed trims)"], sprite=["poofy-fur"], lore=["fur can be trimmed into styles"], c2="white")
E("Espurr", arch=["feline","cat"], based=["kitten (barely-contained power)"], sprite=["blank-stare","ear-flaps"], nick=["'help me' meme face"], c2="")
E("Meowstic", arch=["feline","cat"], based=["cat (male/female psychic)"], sprite=["ear-eyes"], trn=["Olympia (gym)"], c2="blue")
E("Honedge", arch=["blade"], based=["haunted sword"], sprite=["blade-body","tassel-eye"], c2="brown")
E("Doublade", arch=["blade"], based=["twin haunted swords"], sprite=["twin-blades"], c2="brown")
E("Aegislash", arch=["blade"], based=["royal sword & shield (King Arthur / regalia)"], sprite=["sword-shield","eye"], lore=["a symbol of royalty; recognises true kings"], role=[], c2="brown")
E("Spritzee", arch=["bird"], based=["perfume bird / dodo"], sprite=["round","perfume-scent"], c2="pink")
E("Aromatisse", arch=["bird"], based=["perfumer / fragrance fairy"], sprite=["mask","poofy-body"], c2="pink")
E("Swirlix", arch=["fairy"], based=["cotton candy / poodle"], sprite=["fluffy-white"], c2="white")
E("Slurpuff", arch=["fairy"], based=["whipped cream / meringue dog"], sprite=["cream-swirl","nose"], lore=["a patissier's partner (smell)"], c2="white")
E("Inkay", arch=["cephalopod","squid"], based=["firefly squid"], sprite=["glow-spots"], lore=["evolves when held upside-down"], c2="blue")
E("Malamar", arch=["cephalopod","squid"], based=["squid (upside-down hypnotist)"], sprite=["tentacle-arms"], lore=["hypnotises via light; anime villains"], c2="blue")
E("Binacle", arch=["crustacean"], based=["two barnacles on a rock"], sprite=["twin-hands-rock"], c2="brown")
E("Barbaracle", arch=["crustacean"], based=["barnacles (Cthulhu-like seven-limbed)"], sprite=["hand-limbs","head-on-hand"], trn=["Siebold (E4)"], c2="red")
E("Skrelp", arch=["fish","seahorse"], based=["rotting kelp / seadragon"], sprite=["kelp-camouflage"], c2="brown")
E("Dragalge", arch=["fish","dragon"], based=["leafy seadragon"], sprite=["kelp-fins"], trn=["Drasna (E4)"], c2="brown")
E("Clauncher", arch=["crustacean"], based=["pistol shrimp"], sprite=["big-claw-cannon"], c2="blue")
E("Clawitzer", arch=["crustacean"], based=["pistol shrimp (cannon)"], sprite=["cannon-claw"], sig="Water Pulse (Mega Launcher)", trn=["Siebold (E4)"], c2="blue")
E("Helioptile", arch=["reptile","lizard"], based=["frilled lizard (solar panels)"], sprite=["frill-ears"], c2="yellow")
E("Heliolisk", arch=["reptile","lizard"], based=["frilled lizard / basilisk (solar)"], sprite=["sun-frill"], trn=["Clemont (gym)"], c2="")
E("Tyrunt", arch=["dinosaur","theropod"], based=["baby Tyrannosaurus rex (fossil)"], sprite=["jaws","tail"], trn=["Grant (gym)"], role=["fossil"], c2="")
E("Tyrantrum", arch=["dinosaur","theropod"], based=["T-rex king (fossil)"], sprite=["huge-jaws","tiny-arms"], lore=["ruled as an absolute despot"], trn=["Diantha (champion)"], role=["fossil"], c2="red")
E("Amaura", arch=["dinosaur"], based=["Amargasaurus (fossil, aurora)"], sprite=["sail-crest","gems"], role=["fossil"], c2="blue")
E("Aurorus", arch=["dinosaur"], based=["Amargasaurus + aurora borealis (fossil)"], sprite=["ice-sails","frills"], trn=["Diantha (champion)"], role=["fossil"], c2="blue")
E("Sylveon", arch=["mammal","fox"], based=["ribbon fairy / fox (feelers)"], sprite=["ribbon-feelers","bows"], lore=["Fairy eeveelution (affection + Fairy move)"], role=["eeveelution"], c2="white")
E("Hawlucha", arch=["bird"], based=["luchador (masked wrestler) + hawk"], sprite=["wrestler-mask","cape-wings"], sig="Flying Press", trn=["Ash","Korrina (gym)"], c2="green")
E("Dedenne", arch=["rodent"], based=["mouse / gerbil (antenna whiskers)"], sprite=["antenna-whiskers","cheeks"], trn=["Clemont's Bunnelby? no"], c2="")
E("Carbink", arch=["mineral"], based=["gemstone / geode"], sprite=["jewel-body","crown"], lore=["Diancie evolves from it (Movie 17)"], c2="blue")
E("Goomy", arch=["dragon","slug"], based=["sea slug / snail"], sprite=["goo-body","antennae"], nick=["weakest dragon; fan-beloved"], c2="")
E("Sliggoo", arch=["dragon","slug"], based=["sea slug (shell antennae)"], sprite=["slime-body"], c2="purple")
E("Goodra", arch=["dragon","slug"], based=["dragon slug / friendly dragon"], sprite=["gooey-body","horns"], lore=["pseudo; affectionate & gooey"], trn=["Ash","Diantha (champion)"], role=["pseudo"], c2="")
E("Klefki", arch=["mineral"], based=["keyring / key collector"], sprite=["key-body","ring"], lore=["collects keys; wards off thieves"], c2="")
E("Phantump", arch=["ghost"], based=["haunted stump (spirit of a lost child)"], sprite=["tree-stump","twig"], myth=["spirits of children lost in forests"], c2="brown")
E("Trevenant", arch=["ghost"], based=["haunted tree / Ent (forest guardian)"], sprite=["hollow-eye","roots"], myth=["controls trees; devours intruders"], c2="brown")
E("Pumpkaboo", arch=["ghost"], based=["jack-o-lantern (pumpkin, 4 sizes)"], sprite=["pumpkin-body"], myth=["Halloween pumpkin ghost"], c2="black")
E("Gourgeist", arch=["ghost"], based=["jack-o-lantern (Stingy Jack)"], sprite=["pumpkin-body","hair"], myth=["carries spirits to the afterworld"], c2="black")
E("Bergmite", arch=["mineral"], based=["iceberg / glacier chunk"], sprite=["ice-block"], c2="blue")
E("Avalugg", arch=["mineral"], based=["iceberg (floating continent)"], sprite=["ice-shell","legs"], trn=["Wulfric (gym)"], c2="blue")
E("Noibat", arch=["chiropteran","bat"], based=["fruit bat (ultrasonic)"], sprite=["big-ears","wings"], trn=["Ash"], c2="purple")
E("Noivern", arch=["chiropteran","bat"], based=["wyvern / bat (sound waves)"], sprite=["ear-drums","wings"], c2="")
E("Xerneas", arch=["deer"], based=["Life deer / Norse Yggdrasil stag (rainbow antlers)"], sprite=["rainbow-antlers","cross-eyes"], sig="Geomancy", myth=["Life Pokemon; grants eternal life; Movie 17"], role=["legendary"], nick=["box legend (X)"], c2="black")
E("Yveltal", arch=["bird"], based=["Death bird / Norse (Y-shape, destruction)"], sprite=["Y-wings","red-claws"], sig="Oblivion Wing", myth=["Destruction Pokemon; absorbs life when it dies; Movie 18"], role=["legendary"], nick=["box legend (Y)"], c2="black")
E("Zygarde", arch=["serpent","dragon"], based=["order serpent / Yggdrasil guardian (cells)"], sprite=["hex-cells","green-black"], sig="Thousand Arrows", myth=["monitors the ecosystem; forms from cells"], role=["legendary"], c2="black")
E("Diancie", arch=["mineral"], based=["jewel princess (Carbink evolution)"], sprite=["diamond-crown","gown"], sig="Diamond Storm", myth=["creates diamonds; Movie 17"], role=["mythical"], c2="pink")
E("Hoopa", arch=["genie"], based=["genie / djinn (portal rings)"], sprite=["golden-rings","horns"], sig="Hyperspace Hole", myth=["summons things through rings; Unbound forme; Movie 18"], role=["mythical"], c2="purple")
E("Volcanion", arch=["mineral"], based=["steampunk mecha / volcano (steam)"], sprite=["arm-nozzles","steam"], sig="Steam Eruption", myth=["first Fire/Water legend; Movie 19"], role=["mythical"], c2="black")

SIG.update({
 "Chespin":"Vine Whip","Quilladin":"Seed Bomb","Chesnaught":"Spiky Shield","Fennekin":"Ember","Braixen":"Flame Charge",
 "Delphox":"Mystical Fire","Froakie":"Water Pulse","Frogadier":"Water Pulse","Greninja":"Water Shuriken","Bunnelby":"Dig",
 "Diggersby":"Earthquake","Fletchling":"Peck","Fletchinder":"Flame Charge","Scatterbug":"String Shot","Spewpa":"Protect",
 "Vivillon":"Hurricane","Litleo":"Flame Charge","Flabébé":"Fairy Wind","Floette":"Moonblast","Florges":"Moonblast",
 "Skiddo":"Vine Whip","Gogoat":"Horn Leech","Pancham":"Arm Thrust","Pangoro":"Hammer Arm","Furfrou":"Sucker Punch",
 "Espurr":"Confusion","Meowstic":"Psychic","Honedge":"Fury Cutter","Doublade":"Slash","Aegislash":"Sacred Sword",
 "Spritzee":"Draining Kiss","Aromatisse":"Moonblast","Swirlix":"Fairy Wind","Slurpuff":"Play Rough","Inkay":"Psybeam",
 "Malamar":"Superpower","Binacle":"Rock Slide","Barbaracle":"Razor Shell","Skrelp":"Sludge Bomb","Dragalge":"Dragon Pulse",
 "Clauncher":"Water Pulse","Helioptile":"Parabolic Charge","Heliolisk":"Thunderbolt","Tyrunt":"Dragon Claw",
 "Tyrantrum":"Head Smash","Amaura":"Aurora Beam","Aurorus":"Freeze-Dry","Sylveon":"Moonblast","Dedenne":"Nuzzle",
 "Carbink":"Power Gem","Goomy":"Bubble","Sliggoo":"Dragon Pulse","Goodra":"Dragon Pulse","Klefki":"Fairy Lock",
 "Phantump":"Horn Leech","Trevenant":"Wood Hammer","Pumpkaboo":"Shadow Sneak","Gourgeist":"Seed Bomb","Bergmite":"Icy Wind",
 "Avalugg":"Avalanche","Noibat":"Air Cutter","Noivern":"Boomburst","Xerneas":"Geomancy","Yveltal":"Oblivion Wing",
 "Zygarde":"Thousand Arrows","Diancie":"Diamond Storm","Hoopa":"Hyperspace Hole","Volcanion":"Steam Eruption",
})
TEAMS.update({
 "Viola (gym)":["Surskit","Vivillon"],
 "Grant (gym)":["Amaura","Tyrunt"],
 "Korrina (gym)":["Mienfoo","Machoke","Hawlucha","Lucario"],
 "Ramos (gym)":["Jumpluff","Weepinbell","Gogoat"],
 "Clemont (gym)":["Emolga","Magneton","Heliolisk"],
 "Valerie (gym)":["Mawile","Mr. Mime","Sylveon"],
 "Olympia (gym)":["Sigilyph","Slowking","Meowstic"],
 "Wulfric (gym)":["Abomasnow","Cryogonal","Avalugg"],
 "Malva (E4)":["Pyroar","Torkoal","Chandelure","Talonflame"],
 "Siebold (E4)":["Clawitzer","Gyarados","Starmie","Barbaracle"],
 "Wikstrom (E4)":["Klefki","Probopass","Scizor","Aegislash"],
 "Drasna (E4)":["Dragalge","Druddigon","Altaria","Noivern"],
 "Diantha (champion)":["Hawlucha","Tyrantrum","Aurorus","Gourgeist","Goodra","Gardevoir"],
})

if __name__=="__main__":
    for nm,mv in SIG.items(): _ensure(nm)["signature_move"]=mv
    for trn,mons in TEAMS.items():
        for m in mons:
            e=_ensure(m)
            if trn not in e["trainer"]: e["trainer"].append(trn)
    # dedup: drop bare "Name" when a role-suffixed "Name (…)" is also present
    for e in DATA.values():
        roled={t.split(" (")[0] for t in e["trainer"] if " (" in t}
        e["trainer"]=[t for t in e["trainer"] if not (t in roled)]
    out=os.path.join(HERE,"curated_overlay.json")
    # Merge: keep any existing (not-yet-re-authored) entries, overwrite with the
    # freshly curated ones here. Lets us curate gen-by-gen without losing prior work.
    merged={}
    if os.path.exists(out): merged.update(json.load(open(out)))
    merged.update(DATA)
    json.dump(merged, open(out,"w"), ensure_ascii=False, indent=0)
    print(f"wrote {out}: {len(DATA)} re-authored, {len(merged)} total curated entries")
