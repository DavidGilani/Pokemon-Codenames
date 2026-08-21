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
