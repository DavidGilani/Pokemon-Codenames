#!/usr/bin/env python3
"""
Build pokemon_facts.json — an AUTHORING-ONLY fact bank for daily-puzzle clue
generation (never shipped to the site). One record per Pokemon:

  dex   national dex number
  gen   generation (1-9)
  types list of type strings (lowercase)
  color primary body colour (for colour clues; separate from type)
  evo   evolution method INTO this mon: level|stone|trade|friendship|fossil|
        trade-item|special|none  (none = base form / no-evolve)
  egg   egg group(s)
  arch  real-world animal archetypes usable as clues:
          common (Cat 3): feline, canine, equine, serpent, bear, rodent, bird,
            fish, frog, turtle, insect, crab, ...
          technical (Cat 4): cephalopod, crustacean, primate, raptor, mustelid,
            pachyderm, gastropod, marsupial, chiropteran, lagomorph, ...
  tags  freeform clue hooks: sprite features (horn, wings, claws, tail, tusks,
        shell, fangs, mane, spikes, pincers, tongue, three-heads, ...); role
        (starter, legendary, mythical, pseudo, fossil, baby, eeveelution, mega);
        mythology (kitsune, phoenix, genie, golem, ...); region (kanto, ...);
        notable moves as move:earthquake etc.
  stat  base-stat standouts: fast, slow, heavy, light, tanky, glass, atk, spatk
  wk    well-known flag (1 popular / 0 obscure) — daily prefers wk=1

This is consumed by build_daily.py, which enforces the diversity guardrails
(Pokemon-frequency cap, clue-concept tracking, cross-type/gen spread).
"""
import json, sys

# ============================ GEN 1 (1-151) ============================
# color/type/egg/evo are canonical; arch/tags/stat curated for clue value.
GEN1 = {
 "Bulbasaur":   dict(dex=1, types=["grass","poison"], color="green", evo="none", egg=["monster","grass"], arch=["toad"], tags=["starter","kanto","bulb","seed","fangs"], stat=[], wk=1),
 "Ivysaur":     dict(dex=2, types=["grass","poison"], color="green", evo="level", egg=["monster","grass"], arch=["toad"], tags=["kanto","bud","fangs"], stat=[], wk=0),
 "Venusaur":    dict(dex=3, types=["grass","poison"], color="green", evo="level", egg=["monster","grass"], arch=["toad"], tags=["starter","kanto","bloom","flower","mega","fangs"], stat=["tanky"], wk=1),
 "Charmander":  dict(dex=4, types=["fire"], color="red", evo="none", egg=["monster","dragon"], arch=["lizard"], tags=["starter","kanto","flame-tail","claws"], stat=[], wk=1),
 "Charmeleon":  dict(dex=5, types=["fire"], color="red", evo="level", egg=["monster","dragon"], arch=["lizard"], tags=["kanto","flame-tail","horn","claws"], stat=[], wk=0),
 "Charizard":   dict(dex=6, types=["fire","flying"], color="red", evo="level", egg=["monster","dragon"], arch=["dragon","lizard"], tags=["starter","kanto","wings","flame-tail","mega","gmax","fangs"], stat=["fast"], wk=1),
 "Squirtle":    dict(dex=7, types=["water"], color="blue", evo="none", egg=["monster","water1"], arch=["turtle"], tags=["starter","kanto","shell","tail"], stat=[], wk=1),
 "Wartortle":   dict(dex=8, types=["water"], color="blue", evo="level", egg=["monster","water1"], arch=["turtle"], tags=["kanto","shell","ears","tail"], stat=[], wk=0),
 "Blastoise":   dict(dex=9, types=["water"], color="blue", evo="level", egg=["monster","water1"], arch=["turtle"], tags=["starter","kanto","shell","cannons","mega","gmax"], stat=["tanky"], wk=1),
 "Caterpie":    dict(dex=10, types=["bug"], color="green", evo="none", egg=["bug"], arch=["insect","caterpillar"], tags=["kanto","antenna"], stat=[], wk=1),
 "Metapod":     dict(dex=11, types=["bug"], color="green", evo="level", egg=["bug"], arch=["insect","pupa"], tags=["kanto","cocoon","shell"], stat=["tanky"], wk=0),
 "Butterfree":  dict(dex=12, types=["bug","flying"], color="white", evo="level", egg=["bug"], arch=["insect","butterfly"], tags=["kanto","wings","gmax","compound-eyes"], stat=[], wk=1),
 "Weedle":      dict(dex=13, types=["bug","poison"], color="brown", evo="none", egg=["bug"], arch=["insect","caterpillar"], tags=["kanto","stinger","nose"], stat=[], wk=0),
 "Kakuna":      dict(dex=14, types=["bug","poison"], color="yellow", evo="level", egg=["bug"], arch=["insect","pupa"], tags=["kanto","cocoon"], stat=[], wk=0),
 "Beedrill":    dict(dex=15, types=["bug","poison"], color="yellow", evo="level", egg=["bug"], arch=["insect","wasp"], tags=["kanto","stingers","wings","mega","lances"], stat=["fast"], wk=1),
 "Pidgey":      dict(dex=16, types=["normal","flying"], color="brown", evo="none", egg=["flying"], arch=["bird"], tags=["kanto","beak","wings"], stat=[], wk=0),
 "Pidgeotto":   dict(dex=17, types=["normal","flying"], color="brown", evo="level", egg=["flying"], arch=["bird","raptor"], tags=["kanto","crest","beak"], stat=[], wk=0),
 "Pidgeot":     dict(dex=18, types=["normal","flying"], color="brown", evo="level", egg=["flying"], arch=["bird","raptor"], tags=["kanto","crest","wings","mega"], stat=["fast"], wk=1),
 "Rattata":     dict(dex=19, types=["normal"], color="purple", evo="none", egg=["field"], arch=["rodent","rat"], tags=["kanto","buck-teeth","whiskers","tail"], stat=["fast"], wk=1),
 "Raticate":    dict(dex=20, types=["normal"], color="brown", evo="level", egg=["field"], arch=["rodent","rat"], tags=["kanto","buck-teeth","whiskers"], stat=[], wk=0),
 "Spearow":     dict(dex=21, types=["normal","flying"], color="brown", evo="none", egg=["flying"], arch=["bird"], tags=["kanto","beak","wings"], stat=[], wk=0),
 "Fearow":      dict(dex=22, types=["normal","flying"], color="brown", evo="level", egg=["flying"], arch=["bird","raptor"], tags=["kanto","beak","long-neck"], stat=["fast"], wk=0),
 "Ekans":       dict(dex=23, types=["poison"], color="purple", evo="none", egg=["field","dragon"], arch=["serpent","snake"], tags=["kanto","coils","fangs","rattle"], stat=[], wk=0),
 "Arbok":       dict(dex=24, types=["poison"], color="purple", evo="level", egg=["field","dragon"], arch=["serpent","snake","cobra"], tags=["kanto","hood","fangs"], stat=[], wk=1),
 "Pikachu":     dict(dex=25, types=["electric"], color="yellow", evo="stone", egg=["field","fairy"], arch=["rodent","mouse"], tags=["kanto","mascot","cheeks","tail","gmax"], stat=["fast"], wk=1),
 "Raichu":      dict(dex=26, types=["electric"], color="yellow", evo="stone", egg=["field","fairy"], arch=["rodent","mouse"], tags=["kanto","cheeks","tail","bolt-tail"], stat=["fast"], wk=1),
 "Sandshrew":   dict(dex=27, types=["ground"], color="yellow", evo="none", egg=["field"], arch=["pangolin","armadillo"], tags=["kanto","curl","claws","burrow"], stat=[], wk=0),
 "Sandslash":   dict(dex=28, types=["ground"], color="yellow", evo="level", egg=["field"], arch=["pangolin","armadillo"], tags=["kanto","spikes","spiky-ball","claws"], stat=[], wk=0),
 "Nidoran-f":   dict(dex=29, types=["poison"], color="blue", evo="none", egg=["monster","field"], arch=["rodent"], tags=["kanto","ears","spines"], stat=[], wk=0),
 "Nidorina":    dict(dex=30, types=["poison"], color="blue", evo="level", egg=["monster","field"], arch=["rodent"], tags=["kanto","ears","spines"], stat=[], wk=0),
 "Nidoqueen":   dict(dex=31, types=["poison","ground"], color="blue", evo="stone", egg=["undiscovered"], arch=["pachyderm"], tags=["kanto","queen","royalty","spikes","scales","horn"], stat=["tanky"], wk=1),
 "Nidoran-m":   dict(dex=32, types=["poison"], color="purple", evo="none", egg=["monster","field"], arch=["rodent"], tags=["kanto","ears","horn"], stat=[], wk=0),
 "Nidorino":    dict(dex=33, types=["poison"], color="purple", evo="level", egg=["monster","field"], arch=["rodent"], tags=["kanto","horn","spines"], stat=[], wk=0),
 "Nidoking":    dict(dex=34, types=["poison","ground"], color="purple", evo="stone", egg=["undiscovered"], arch=["pachyderm"], tags=["kanto","king","royalty","horn","spikes","tail","move:earthquake"], stat=["atk"], wk=1),
 "Clefairy":    dict(dex=35, types=["fairy"], color="pink", evo="none", egg=["fairy"], arch=[], tags=["kanto","wings","curl","moon","star"], stat=[], wk=1),
 "Clefable":    dict(dex=36, types=["fairy"], color="pink", evo="stone", egg=["fairy"], arch=[], tags=["kanto","wings","moon","moonstone","fairy-mythos"], stat=[], wk=1),
 "Vulpix":      dict(dex=37, types=["fire"], color="brown", evo="none", egg=["field"], arch=["fox","canine"], tags=["kanto","curls","tails","kitsune"], stat=[], wk=1),
 "Ninetales":   dict(dex=38, types=["fire"], color="yellow", evo="stone", egg=["field"], arch=["fox","canine"], tags=["kanto","nine-tails","kitsune","mythical-lore"], stat=[], wk=1),
 "Jigglypuff":  dict(dex=39, types=["normal","fairy"], color="pink", evo="none", egg=["fairy"], arch=[], tags=["kanto","balloon","round","sing","mascot"], stat=[], wk=1),
 "Wigglytuff":  dict(dex=40, types=["normal","fairy"], color="pink", evo="stone", egg=["fairy"], arch=[], tags=["kanto","balloon","round","ears"], stat=["tanky"], wk=1),
 "Zubat":       dict(dex=41, types=["poison","flying"], color="blue", evo="none", egg=["flying"], arch=["chiropteran","bat"], tags=["kanto","wings","fangs","no-eyes"], stat=[], wk=1),
 "Golbat":      dict(dex=42, types=["poison","flying"], color="blue", evo="level", egg=["flying"], arch=["chiropteran","bat"], tags=["kanto","wings","fangs","big-mouth"], stat=[], wk=0),
 "Oddish":      dict(dex=43, types=["grass","poison"], color="blue", evo="none", egg=["grass"], arch=[], tags=["kanto","leaves","bulb"], stat=[], wk=1),
 "Gloom":       dict(dex=44, types=["grass","poison"], color="blue", evo="level", egg=["grass"], arch=[], tags=["kanto","drool","flower"], stat=[], wk=0),
 "Vileplume":   dict(dex=45, types=["grass","poison"], color="red", evo="stone", egg=["grass"], arch=[], tags=["kanto","petals","flower","rafflesia"], stat=[], wk=1),
 "Paras":       dict(dex=46, types=["bug","grass"], color="red", evo="none", egg=["bug","grass"], arch=["insect","crab"], tags=["kanto","mushroom","claws"], stat=[], wk=0),
 "Parasect":    dict(dex=47, types=["bug","grass"], color="red", evo="level", egg=["bug","grass"], arch=["insect","crab"], tags=["kanto","mushroom","fungus"], stat=[], wk=0),
 "Venonat":     dict(dex=48, types=["bug","poison"], color="purple", evo="none", egg=["bug"], arch=["insect"], tags=["kanto","big-eyes","fuzzy"], stat=[], wk=0),
 "Venomoth":    dict(dex=49, types=["bug","poison"], color="purple", evo="level", egg=["bug"], arch=["insect","moth"], tags=["kanto","wings","dust"], stat=[], wk=0),
 "Diglett":     dict(dex=50, types=["ground"], color="brown", evo="none", egg=["field"], arch=["mole"], tags=["kanto","nose","burrow","dig"], stat=[], wk=1),
 "Dugtrio":     dict(dex=51, types=["ground"], color="brown", evo="level", egg=["field"], arch=["mole"], tags=["kanto","three-heads","trio","burrow"], stat=["fast"], wk=1),
 "Meowth":      dict(dex=52, types=["normal"], color="white", evo="none", egg=["field"], arch=["feline","cat"], tags=["kanto","coin","charm","whiskers","gmax"], stat=[], wk=1),
 "Persian":     dict(dex=53, types=["normal"], color="white", evo="level", egg=["field"], arch=["feline","cat"], tags=["kanto","gem","whiskers","sleek"], stat=["fast"], wk=1),
 "Psyduck":     dict(dex=54, types=["water"], color="yellow", evo="none", egg=["water1","field"], arch=["duck","platypus"], tags=["kanto","headache","bill"], stat=[], wk=1),
 "Golduck":     dict(dex=55, types=["water"], color="blue", evo="level", egg=["water1","field"], arch=["platypus","duck"], tags=["kanto","bill","forehead-gem","webbed"], stat=["fast"], wk=1),
 "Mankey":      dict(dex=56, types=["fighting"], color="white", evo="none", egg=["field"], arch=["primate","monkey"], tags=["kanto","angry","fists"], stat=[], wk=1),
 "Primeape":    dict(dex=57, types=["fighting"], color="brown", evo="level", egg=["field"], arch=["primate","monkey"], tags=["kanto","furious","fists"], stat=["fast"], wk=1),
 "Growlithe":   dict(dex=58, types=["fire"], color="brown", evo="none", egg=["field"], arch=["canine","dog"], tags=["kanto","pup","stripes","loyal"], stat=[], wk=1),
 "Arcanine":    dict(dex=59, types=["fire"], color="brown", evo="stone", egg=["field"], arch=["canine","dog"], tags=["kanto","stripes","mane","legendary-lore"], stat=["fast"], wk=1),
 "Poliwag":     dict(dex=60, types=["water"], color="blue", evo="none", egg=["water1"], arch=["frog","tadpole"], tags=["kanto","swirl","tail"], stat=[], wk=1),
 "Poliwhirl":   dict(dex=61, types=["water"], color="blue", evo="level", egg=["water1"], arch=["frog"], tags=["kanto","swirl","gloves"], stat=[], wk=0),
 "Poliwrath":   dict(dex=62, types=["water","fighting"], color="blue", evo="stone", egg=["water1"], arch=["frog"], tags=["kanto","swirl","muscles"], stat=["tanky"], wk=0),
 "Abra":        dict(dex=63, types=["psychic"], color="brown", evo="none", egg=["human"], arch=[], tags=["kanto","sleep","teleport"], stat=["fast"], wk=1),
 "Kadabra":     dict(dex=64, types=["psychic"], color="brown", evo="level", egg=["human"], arch=[], tags=["kanto","spoon","psychic-power","whiskers"], stat=["fast"], wk=1),
 "Alakazam":    dict(dex=65, types=["psychic"], color="brown", evo="trade", egg=["human"], arch=[], tags=["kanto","spoons","genius","psychic-power","mega"], stat=["spatk","fast"], wk=1),
 "Machop":      dict(dex=66, types=["fighting"], color="gray", evo="none", egg=["human"], arch=["primate"], tags=["kanto","muscle","tail"], stat=["atk"], wk=1),
 "Machoke":     dict(dex=67, types=["fighting"], color="gray", evo="level", egg=["human"], arch=["primate"], tags=["kanto","muscle","belt"], stat=["atk"], wk=0),
 "Machamp":     dict(dex=68, types=["fighting"], color="gray", evo="trade", egg=["human"], arch=["primate"], tags=["kanto","four-arms","muscle","gmax","move:submission"], stat=["atk"], wk=1),
 "Bellsprout":  dict(dex=69, types=["grass","poison"], color="green", evo="none", egg=["grass"], arch=["plant"], tags=["kanto","pitcher","vine"], stat=[], wk=0),
 "Weepinbell":  dict(dex=70, types=["grass","poison"], color="green", evo="level", egg=["grass"], arch=["plant"], tags=["kanto","pitcher","bell"], stat=[], wk=0),
 "Victreebel":  dict(dex=71, types=["grass","poison"], color="green", evo="stone", egg=["grass"], arch=["plant"], tags=["kanto","pitcher","venus-flytrap","vine"], stat=[], wk=1),
 "Tentacool":   dict(dex=72, types=["water","poison"], color="blue", evo="none", egg=["water3"], arch=["cnidarian","jellyfish"], tags=["kanto","jelly","tentacles"], stat=[], wk=0),
 "Tentacruel":  dict(dex=73, types=["water","poison"], color="blue", evo="level", egg=["water3"], arch=["cnidarian","jellyfish"], tags=["kanto","jewels","tentacles"], stat=["fast"], wk=1),
 "Geodude":     dict(dex=74, types=["rock","ground"], color="brown", evo="none", egg=["mineral"], arch=[], tags=["kanto","boulder","fists","rock"], stat=[], wk=1),
 "Graveler":    dict(dex=75, types=["rock","ground"], color="brown", evo="level", egg=["mineral"], arch=[], tags=["kanto","boulder","four-arms","rock"], stat=[], wk=0),
 "Golem":       dict(dex=76, types=["rock","ground"], color="brown", evo="trade", egg=["mineral"], arch=[], tags=["kanto","boulder","shell","golem-mythos","move:earthquake"], stat=["tanky"], wk=1),
 "Ponyta":      dict(dex=77, types=["fire"], color="yellow", evo="none", egg=["field"], arch=["equine","horse"], tags=["kanto","mane-fire","hooves"], stat=["fast"], wk=1),
 "Rapidash":    dict(dex=78, types=["fire"], color="yellow", evo="level", egg=["field"], arch=["equine","horse","unicorn"], tags=["kanto","blaze-mane","horn","hooves"], stat=["fast"], wk=1),
 "Slowpoke":    dict(dex=79, types=["water","psychic"], color="pink", evo="none", egg=["monster","water1"], arch=[], tags=["kanto","tail","dopey"], stat=["slow"], wk=1),
 "Slowbro":     dict(dex=80, types=["water","psychic"], color="pink", evo="level", egg=["monster","water1"], arch=[], tags=["kanto","shell-tail","mega"], stat=["tanky","slow"], wk=1),
 "Magnemite":   dict(dex=81, types=["electric","steel"], color="gray", evo="none", egg=["mineral"], arch=[], tags=["kanto","magnet","screw","float"], stat=[], wk=1),
 "Magneton":    dict(dex=82, types=["electric","steel"], color="gray", evo="level", egg=["mineral"], arch=[], tags=["kanto","magnets","three","cluster"], stat=[], wk=1),
 "Farfetch'd":  dict(dex=83, types=["normal","flying"], color="brown", evo="none", egg=["flying","field"], arch=["bird","duck"], tags=["kanto","leek","wields"], stat=[], wk=1),
 "Doduo":       dict(dex=84, types=["normal","flying"], color="brown", evo="none", egg=["flying"], arch=["bird","ratite"], tags=["kanto","two-heads","beak"], stat=["fast"], wk=0),
 "Dodrio":      dict(dex=85, types=["normal","flying"], color="brown", evo="level", egg=["flying"], arch=["bird","ratite"], tags=["kanto","three-heads","beak"], stat=["fast"], wk=1),
 "Seel":        dict(dex=86, types=["water"], color="white", evo="none", egg=["water1","field"], arch=["pinniped","seal"], tags=["kanto","tusk","horn"], stat=[], wk=0),
 "Dewgong":     dict(dex=87, types=["water","ice"], color="white", evo="level", egg=["water1","field"], arch=["pinniped","seal"], tags=["kanto","sleek","tusk","dugong"], stat=[], wk=0),
 "Grimer":      dict(dex=88, types=["poison"], color="purple", evo="none", egg=["amorphous"], arch=[], tags=["kanto","ooze","sludge"], stat=[], wk=1),
 "Muk":         dict(dex=89, types=["poison"], color="purple", evo="level", egg=["amorphous"], arch=[], tags=["kanto","sludge","gmax","toxic"], stat=["tanky"], wk=1),
 "Shellder":    dict(dex=90, types=["water"], color="purple", evo="none", egg=["water3"], arch=["mollusc","clam"], tags=["kanto","clam","pearl","tongue"], stat=[], wk=1),
 "Cloyster":    dict(dex=91, types=["water","ice"], color="purple", evo="stone", egg=["water3"], arch=["mollusc","bivalve"], tags=["kanto","shell","spikes","pearl"], stat=["tanky"], wk=1),
 "Gastly":      dict(dex=92, types=["ghost","poison"], color="purple", evo="none", egg=["amorphous"], arch=[], tags=["kanto","gas","vapour","ghost-lore"], stat=[], wk=1),
 "Haunter":     dict(dex=93, types=["ghost","poison"], color="purple", evo="level", egg=["amorphous"], arch=[], tags=["kanto","hands","tongue","ghost-lore"], stat=[], wk=1),
 "Gengar":      dict(dex=94, types=["ghost","poison"], color="purple", evo="trade", egg=["amorphous"], arch=[], tags=["kanto","grin","shadow","mega","gmax","ghost-lore"], stat=["fast"], wk=1),
 "Onix":        dict(dex=95, types=["rock","ground"], color="gray", evo="none", egg=["mineral"], arch=["serpent"], tags=["kanto","rock-snake","boulder-body","long"], stat=["tanky"], wk=1),
 "Drowzee":     dict(dex=96, types=["psychic"], color="yellow", evo="none", egg=["human"], arch=["tapir"], tags=["kanto","pendulum","dreams","baku-mythos"], stat=[], wk=1),
 "Hypno":       dict(dex=97, types=["psychic"], color="yellow", evo="level", egg=["human"], arch=["tapir"], tags=["kanto","pendulum","hypnosis","sleep"], stat=[], wk=1),
 "Krabby":      dict(dex=98, types=["water"], color="red", evo="none", egg=["water3"], arch=["crustacean","crab"], tags=["kanto","pincers","claws"], stat=[], wk=0),
 "Kingler":     dict(dex=99, types=["water"], color="red", evo="level", egg=["water3"], arch=["crustacean","crab"], tags=["kanto","big-claw","pincers","gmax"], stat=["atk"], wk=1),
 "Voltorb":     dict(dex=100, types=["electric"], color="red", evo="none", egg=["mineral"], arch=[], tags=["kanto","ball","poke-ball","self-destruct"], stat=[], wk=1),
 "Electrode":   dict(dex=101, types=["electric"], color="red", evo="level", egg=["mineral"], arch=[], tags=["kanto","sphere","ball","explode"], stat=["fast"], wk=1),
 "Exeggcute":   dict(dex=102, types=["grass","psychic"], color="pink", evo="none", egg=["grass"], arch=[], tags=["kanto","six","eggs","seeds"], stat=[], wk=1),
 "Exeggutor":   dict(dex=103, types=["grass","psychic"], color="yellow", evo="stone", egg=["grass"], arch=[], tags=["kanto","palm","three-heads","coconut"], stat=[], wk=1),
 "Cubone":      dict(dex=104, types=["ground"], color="brown", evo="none", egg=["monster"], arch=[], tags=["kanto","skull","bone-club","orphan","wields"], stat=[], wk=1),
 "Marowak":     dict(dex=105, types=["ground"], color="brown", evo="level", egg=["monster"], arch=[], tags=["kanto","bone-club","skull","wields","move:earthquake"], stat=[], wk=1),
 "Hitmonlee":   dict(dex=106, types=["fighting"], color="brown", evo="special", egg=["human"], arch=[], tags=["kanto","kick","legs","siblings"], stat=["atk"], wk=1),
 "Hitmonchan":  dict(dex=107, types=["fighting"], color="brown", evo="special", egg=["human"], arch=[], tags=["kanto","gloves","punch","boxer","siblings","wields"], stat=[], wk=1),
 "Lickitung":   dict(dex=108, types=["normal"], color="pink", evo="none", egg=["monster"], arch=[], tags=["kanto","tongue","lick"], stat=["tanky"], wk=1),
 "Koffing":     dict(dex=109, types=["poison"], color="purple", evo="none", egg=["amorphous"], arch=[], tags=["kanto","gas","skull-face","float"], stat=[], wk=1),
 "Weezing":     dict(dex=110, types=["poison"], color="purple", evo="level", egg=["amorphous"], arch=[], tags=["kanto","twin","gas","smog"], stat=["tanky"], wk=1),
 "Rhyhorn":     dict(dex=111, types=["ground","rock"], color="gray", evo="none", egg=["monster","field"], arch=["pachyderm","rhino"], tags=["kanto","horn","hide"], stat=["tanky"], wk=0),
 "Rhydon":      dict(dex=112, types=["ground","rock"], color="gray", evo="level", egg=["monster","field"], arch=["pachyderm","rhino"], tags=["kanto","drill-horn","hide","move:earthquake"], stat=["atk"], wk=1),
 "Chansey":     dict(dex=113, types=["normal"], color="pink", evo="friendship", egg=["fairy"], arch=[], tags=["kanto","egg","belly-egg","nurse"], stat=["tanky"], wk=1),
 "Tangela":     dict(dex=114, types=["grass"], color="blue", evo="none", egg=["grass"], arch=[], tags=["kanto","vines","tangle"], stat=[], wk=0),
 "Kangaskhan":  dict(dex=115, types=["normal"], color="brown", evo="none", egg=["monster"], arch=["marsupial","kangaroo"], tags=["kanto","pouch","baby","mega"], stat=["tanky"], wk=1),
 "Horsea":      dict(dex=116, types=["water"], color="blue", evo="none", egg=["water1","dragon"], arch=["fish","seahorse"], tags=["kanto","snout","fins"], stat=[], wk=0),
 "Seadra":      dict(dex=117, types=["water"], color="blue", evo="level", egg=["water1","dragon"], arch=["fish","seahorse"], tags=["kanto","spines","fins"], stat=["fast"], wk=0),
 "Goldeen":     dict(dex=118, types=["water"], color="red", evo="none", egg=["water2"], arch=["fish"], tags=["kanto","horn","fins","goldfish"], stat=[], wk=0),
 "Seaking":     dict(dex=119, types=["water"], color="red", evo="level", egg=["water2"], arch=["fish"], tags=["kanto","horn","fins","goldfish"], stat=[], wk=0),
 "Staryu":      dict(dex=120, types=["water"], color="brown", evo="none", egg=["water3"], arch=["echinoderm","starfish"], tags=["kanto","star","core-gem"], stat=[], wk=1),
 "Starmie":     dict(dex=121, types=["water","psychic"], color="purple", evo="stone", egg=["water3"], arch=["echinoderm","starfish"], tags=["kanto","star","core-gem","spin"], stat=["fast"], wk=1),
 "Mr. Mime":    dict(dex=122, types=["psychic","fairy"], color="pink", evo="special", egg=["human"], arch=[], tags=["kanto","mime","barrier","panes"], stat=[], wk=1),
 "Scyther":     dict(dex=123, types=["bug","flying"], color="green", evo="none", egg=["bug"], arch=["insect","mantis"], tags=["kanto","scythes","blades","wings"], stat=["fast"], wk=1),
 "Jynx":        dict(dex=124, types=["ice","psychic"], color="red", evo="special", egg=["human"], arch=[], tags=["kanto","lips","gown","opera"], stat=[], wk=1),
 "Electabuzz":  dict(dex=125, types=["electric"], color="yellow", evo="none", egg=["human"], arch=[], tags=["kanto","stripes","rival-magmar"], stat=["fast"], wk=1),
 "Magmar":      dict(dex=126, types=["fire"], color="red", evo="none", egg=["human"], arch=[], tags=["kanto","duckbill","flame","rival-electabuzz"], stat=[], wk=1),
 "Pinsir":      dict(dex=127, types=["bug"], color="brown", evo="none", egg=["bug"], arch=["insect","beetle"], tags=["kanto","pincers","horns","mega","stag-beetle"], stat=["atk"], wk=1),
 "Tauros":      dict(dex=128, types=["normal"], color="brown", evo="none", egg=["field"], arch=["bovine","bull"], tags=["kanto","three-tails","horns","safari"], stat=["fast"], wk=1),
 "Magikarp":    dict(dex=129, types=["water"], color="red", evo="none", egg=["water2","dragon"], arch=["fish","carp"], tags=["kanto","splash","useless","whiskers"], stat=[], wk=1),
 "Gyarados":    dict(dex=130, types=["water","flying"], color="blue", evo="level", egg=["water2","dragon"], arch=["serpent","dragon"], tags=["kanto","serpent","fangs","mega","move:hyper-beam"], stat=["atk"], wk=1),
 "Lapras":      dict(dex=131, types=["water","ice"], color="blue", evo="none", egg=["monster","water1"], arch=["plesiosaur"], tags=["kanto","shell-back","ferry","gmax","nessie"], stat=["tanky"], wk=1),
 "Ditto":       dict(dex=132, types=["normal"], color="purple", evo="none", egg=["ditto"], arch=[], tags=["kanto","blob","transform","imposter","clone"], stat=[], wk=1),
 "Eevee":       dict(dex=133, types=["normal"], color="brown", evo="none", egg=["field"], arch=["mammal"], tags=["kanto","eeveelution","fluffy","gmax","evolution-mythos"], stat=[], wk=1),
 "Vaporeon":    dict(dex=134, types=["water"], color="blue", evo="stone", egg=["field"], arch=["mermaid"], tags=["kanto","eeveelution","fins","stone"], stat=["tanky"], wk=1),
 "Jolteon":     dict(dex=135, types=["electric"], color="yellow", evo="stone", egg=["field"], arch=[], tags=["kanto","eeveelution","spiky","stone"], stat=["fast"], wk=1),
 "Flareon":     dict(dex=136, types=["fire"], color="red", evo="stone", egg=["field"], arch=[], tags=["kanto","eeveelution","fluff","stone"], stat=["atk"], wk=1),
 "Porygon":     dict(dex=137, types=["normal"], color="pink", evo="none", egg=["mineral"], arch=[], tags=["kanto","polygon","digital","pixel","trade-item"], stat=[], wk=1),
 "Omanyte":     dict(dex=138, types=["rock","water"], color="blue", evo="none", egg=["water1","water3"], arch=["mollusc","ammonite"], tags=["kanto","fossil","spiral-shell","tentacles"], stat=[], wk=1),
 "Omastar":     dict(dex=139, types=["rock","water"], color="blue", evo="level", egg=["water1","water3"], arch=["mollusc","ammonite","cephalopod"], tags=["kanto","fossil","spiral","spikes"], stat=[], wk=1),
 "Kabuto":      dict(dex=140, types=["rock","water"], color="brown", evo="none", egg=["water1","water3"], arch=["arthropod","trilobite"], tags=["kanto","fossil","dome","horseshoe-crab"], stat=[], wk=1),
 "Kabutops":    dict(dex=141, types=["rock","water"], color="brown", evo="level", egg=["water1","water3"], arch=["arthropod","trilobite"], tags=["kanto","fossil","scythe-arms","blades"], stat=["fast"], wk=1),
 "Aerodactyl":  dict(dex=142, types=["rock","flying"], color="purple", evo="none", egg=["flying"], arch=["pterosaur","raptor"], tags=["kanto","fossil","wings","fangs","mega"], stat=["fast"], wk=1),
 "Snorlax":     dict(dex=143, types=["normal"], color="black", evo="friendship", egg=["monster"], arch=["bear"], tags=["kanto","belly","sleep","gmax","heavy"], stat=["heavy","tanky"], wk=1),
 "Articuno":    dict(dex=144, types=["ice","flying"], color="blue", evo="none", egg=["undiscovered"], arch=["bird"], tags=["kanto","legendary","ice-crest","wings","bird-trio"], stat=[], wk=1),
 "Zapdos":      dict(dex=145, types=["electric","flying"], color="yellow", evo="none", egg=["undiscovered"], arch=["bird"], tags=["kanto","legendary","spiky","wings","bird-trio"], stat=["fast"], wk=1),
 "Moltres":     dict(dex=146, types=["fire","flying"], color="yellow", evo="none", egg=["undiscovered"], arch=["bird","phoenix"], tags=["kanto","legendary","flame-wings","phoenix","bird-trio"], stat=[], wk=1),
 "Dratini":     dict(dex=147, types=["dragon"], color="blue", evo="none", egg=["water1","dragon"], arch=["serpent","dragon"], tags=["kanto","serpent","orb"], stat=[], wk=1),
 "Dragonair":   dict(dex=148, types=["dragon"], color="blue", evo="level", egg=["water1","dragon"], arch=["serpent","dragon"], tags=["kanto","serpent","neck-orb","mystical"], stat=[], wk=1),
 "Dragonite":   dict(dex=149, types=["dragon","flying"], color="brown", evo="level", egg=["water1","dragon"], arch=["dragon"], tags=["kanto","pseudo","antennae","wings","move:hyper-beam"], stat=["atk","tanky"], wk=1),
 "Mewtwo":      dict(dex=150, types=["psychic"], color="purple", evo="none", egg=["undiscovered"], arch=[], tags=["kanto","legendary","clone","mega","psychic-power"], stat=["spatk","fast"], wk=1),
 "Mew":         dict(dex=151, types=["psychic"], color="pink", evo="none", egg=["undiscovered"], arch=[], tags=["kanto","mythical","pink","clone-origin","transform"], stat=[], wk=1),
}

# ==================== GEN 2-9 (curated well-known set) ====================
# Includes every Pokemon already used in mixed puzzles + popular additions for
# variety. gen is explicit per record here.
LATER = {
 # --- Gen 2 ---
 "Meganium":    dict(gen=2, dex=154, types=["grass"], color="green", evo="level", egg=["monster","grass"], arch=["dinosaur"], tags=["starter","johto","petals","fangs"], stat=["tanky"], wk=1),
 "Typhlosion":  dict(gen=2, dex=157, types=["fire"], color="blue", evo="level", egg=["field"], arch=[], tags=["starter","johto","flame-collar","badger"], stat=["fast"], wk=1),
 "Feraligatr":  dict(gen=2, dex=160, types=["water"], color="blue", evo="level", egg=["monster","water1"], arch=["reptile","crocodile"], tags=["starter","johto","jaws","fangs","gator"], stat=["atk"], wk=1),
 "Ampharos":    dict(gen=2, dex=181, types=["electric"], color="yellow", evo="level", egg=["field","monster"], arch=[], tags=["johto","tail-orb","beacon","mega","sheep"], stat=[], wk=1),
 "Bellossom":   dict(gen=2, dex=182, types=["grass"], color="green", evo="stone", egg=["grass"], arch=[], tags=["johto","petals","hula","flower"], stat=[], wk=1),
 "Espeon":      dict(gen=2, dex=196, types=["psychic"], color="purple", evo="friendship", egg=["field"], arch=[], tags=["johto","eeveelution","forehead-gem","fork-tail"], stat=["fast","spatk"], wk=1),
 "Umbreon":     dict(gen=2, dex=197, types=["dark"], color="black", evo="friendship", egg=["field"], arch=[], tags=["johto","eeveelution","rings","glow"], stat=["tanky"], wk=1),
 "Steelix":     dict(gen=2, dex=208, types=["steel","ground"], color="gray", evo="trade-item", egg=["mineral"], arch=["serpent"], tags=["johto","iron-snake","mega","move:earthquake"], stat=["tanky"], wk=1),
 "Scizor":      dict(gen=2, dex=212, types=["bug","steel"], color="red", evo="trade-item", egg=["bug"], arch=["insect","mantis"], tags=["johto","red-claws","pincers","blades","mega"], stat=["atk"], wk=1),
 "Heracross":   dict(gen=2, dex=214, types=["bug","fighting"], color="blue", evo="level", egg=["bug"], arch=["insect","beetle"], tags=["johto","horn","mega","stag-beetle"], stat=["atk"], wk=1),
 "Skarmory":    dict(gen=2, dex=227, types=["steel","flying"], color="gray", evo="level", egg=["flying"], arch=["bird","raptor"], tags=["johto","armour","blades","wings"], stat=["tanky"], wk=1),
 "Houndoom":    dict(gen=2, dex=229, types=["dark","fire"], color="black", evo="level", egg=["field"], arch=["canine","dog"], tags=["johto","horns","hound","mega"], stat=["fast","spatk"], wk=1),
 "Donphan":     dict(gen=2, dex=232, types=["ground"], color="gray", evo="level", egg=["field"], arch=["pachyderm","elephant"], tags=["johto","tusks","move:earthquake","proboscidean"], stat=["tanky"], wk=1),
 "Tyranitar":   dict(gen=2, dex=248, types=["rock","dark"], color="green", evo="level", egg=["monster"], arch=["dinosaur"], tags=["johto","pseudo","dino","mega","sandstorm"], stat=["atk","tanky"], wk=1),
 # --- Gen 3 ---
 "Sceptile":    dict(gen=3, dex=254, types=["grass"], color="green", evo="level", egg=["monster","dragon"], arch=["reptile","gecko"], tags=["starter","hoenn","leaf-blade","mega","tail"], stat=["fast"], wk=1),
 "Blaziken":    dict(gen=3, dex=257, types=["fire","fighting"], color="red", evo="level", egg=["field"], arch=["bird"], tags=["starter","hoenn","kick","talons","mega"], stat=["atk"], wk=1),
 "Swampert":    dict(gen=3, dex=260, types=["water","ground"], color="blue", evo="level", egg=["monster","water1"], arch=["amphibian","mudfish"], tags=["starter","hoenn","mud","fins","mega"], stat=["atk","tanky"], wk=1),
 "Gardevoir":   dict(gen=3, dex=282, types=["psychic","fairy"], color="white", evo="level", egg=["human","amorphous"], arch=[], tags=["hoenn","gown","elegant","mega"], stat=["spatk"], wk=1),
 "Sableye":     dict(gen=3, dex=302, types=["dark","ghost"], color="purple", evo="none", egg=["human"], arch=[], tags=["hoenn","gem-eyes","gremlin","mega","folklore"], stat=[], wk=1),
 "Aggron":      dict(gen=3, dex=306, types=["steel","rock"], color="gray", evo="level", egg=["monster"], arch=["dinosaur"], tags=["hoenn","armour","horns","mega","iron"], stat=["tanky"], wk=1),
 "Manectric":   dict(gen=3, dex=310, types=["electric"], color="yellow", evo="level", egg=["field"], arch=["canine"], tags=["hoenn","mane","mega","jackal"], stat=["fast"], wk=0),
 "Flygon":      dict(gen=3, dex=330, types=["ground","dragon"], color="green", evo="level", egg=["bug","dragon"], arch=["insect","dragon"], tags=["hoenn","goggles","wings","desert-spirit"], stat=["fast"], wk=1),
 "Milotic":     dict(gen=3, dex=350, types=["water"], color="pink", evo="trade-item", egg=["water1","dragon"], arch=["fish","serpent","eel"], tags=["hoenn","ribbon","elegant","tender"], stat=["tanky"], wk=1),
 "Absol":       dict(gen=3, dex=359, types=["dark"], color="white", evo="none", egg=["field"], arch=["feline","canine"], tags=["hoenn","disaster","horn","mega","scythe-horn"], stat=["atk","fast"], wk=1),
 "Salamence":   dict(gen=3, dex=373, types=["dragon","flying"], color="blue", evo="level", egg=["dragon"], arch=["dragon"], tags=["hoenn","pseudo","crescent","wings","mega","move:hyper-beam"], stat=["atk","fast"], wk=1),
 "Metagross":   dict(gen=3, dex=376, types=["steel","psychic"], color="blue", evo="level", egg=["mineral"], arch=[], tags=["hoenn","pseudo","legs","x-face","mega"], stat=["atk","tanky"], wk=1),
 "Rayquaza":    dict(gen=3, dex=384, types=["dragon","flying"], color="green", evo="none", egg=["undiscovered"], arch=["serpent","dragon"], tags=["hoenn","legendary","sky","mega","ozone"], stat=["atk"], wk=1),
 # --- Gen 4 ---
 "Torterra":    dict(gen=4, dex=389, types=["grass","ground"], color="green", evo="level", egg=["monster","grass"], arch=["turtle","tortoise"], tags=["starter","sinnoh","tree","shell","move:earthquake"], stat=["tanky"], wk=1),
 "Infernape":   dict(gen=4, dex=392, types=["fire","fighting"], color="brown", evo="level", egg=["field","human"], arch=["primate","monkey"], tags=["starter","sinnoh","flame-head","fists"], stat=["fast","atk"], wk=1),
 "Empoleon":    dict(gen=4, dex=395, types=["water","steel"], color="blue", evo="level", egg=["water1","field"], arch=["bird","penguin"], tags=["starter","sinnoh","trident","emperor","royalty"], stat=["spatk","tanky"], wk=1),
 "Staraptor":   dict(gen=4, dex=398, types=["normal","flying"], color="brown", evo="level", egg=["flying"], arch=["bird","raptor"], tags=["sinnoh","hawk-crest","talons","move:fly"], stat=["atk","fast"], wk=1),
 "Luxray":      dict(gen=4, dex=405, types=["electric"], color="blue", evo="level", egg=["field"], arch=["feline","lion"], tags=["sinnoh","mane","x-ray-eyes","intimidate"], stat=["atk"], wk=1),
 "Roserade":    dict(gen=4, dex=407, types=["grass","poison"], color="green", evo="stone", egg=["fairy","grass"], arch=[], tags=["sinnoh","bouquet","masquerade","thorns"], stat=["spatk","fast"], wk=1),
 "Rampardos":   dict(gen=4, dex=409, types=["rock"], color="blue", evo="level", egg=["monster"], arch=["dinosaur"], tags=["sinnoh","fossil","skull","headbutt"], stat=["atk"], wk=0),
 "Bastiodon":   dict(gen=4, dex=411, types=["rock","steel"], color="gray", evo="level", egg=["monster"], arch=["dinosaur"], tags=["sinnoh","fossil","shield-face","wall"], stat=["tanky"], wk=0),
 "Garchomp":    dict(gen=4, dex=445, types=["dragon","ground"], color="blue", evo="level", egg=["monster","dragon"], arch=["shark","dragon"], tags=["sinnoh","pseudo","fins","jet","mega","move:earthquake"], stat=["atk","fast"], wk=1),
 "Lucario":     dict(gen=4, dex=448, types=["fighting","steel"], color="blue", evo="friendship", egg=["field","human"], arch=["canine","jackal"], tags=["sinnoh","aura","jackal","mega"], stat=["atk","fast"], wk=1),
 "Hippowdon":   dict(gen=4, dex=450, types=["ground"], color="brown", evo="level", egg=["field"], arch=["pachyderm","hippo"], tags=["sinnoh","sandstorm","jaws","move:earthquake"], stat=["tanky"], wk=0),
 "Drapion":     dict(gen=4, dex=452, types=["poison","dark"], color="purple", evo="level", egg=["bug","water3"], arch=["arachnid","scorpion"], tags=["sinnoh","pincers","claws"], stat=["fast"], wk=0),
 "Lumineon":    dict(gen=4, dex=457, types=["water"], color="blue", evo="level", egg=["water2"], arch=["fish"], tags=["sinnoh","fins","glow","neon"], stat=[], wk=0),
 "Weavile":     dict(gen=4, dex=461, types=["dark","ice"], color="black", evo="friendship", egg=["field"], arch=["mustelid","weasel"], tags=["sinnoh","claws","thief","sneak","feathers"], stat=["fast","atk"], wk=1),
 "Magnezone":   dict(gen=4, dex=462, types=["electric","steel"], color="gray", evo="special", egg=["mineral"], arch=[], tags=["sinnoh","magnets","ufo","float"], stat=["spatk"], wk=0),
 "Rhyperior":   dict(gen=4, dex=464, types=["ground","rock"], color="gray", evo="trade-item", egg=["monster","field"], arch=["pachyderm","rhino"], tags=["sinnoh","drills","armour","move:earthquake"], stat=["atk","tanky"], wk=1),
 "Tangrowth":   dict(gen=4, dex=465, types=["grass"], color="blue", evo="special", egg=["grass"], arch=[], tags=["sinnoh","vines","tangle"], stat=["tanky"], wk=0),
 "Electivire":  dict(gen=4, dex=466, types=["electric"], color="yellow", evo="trade-item", egg=["human"], arch=[], tags=["sinnoh","tails","stripes","brawn"], stat=["atk"], wk=0),
 "Magmortar":   dict(gen=4, dex=467, types=["fire"], color="red", evo="trade-item", egg=["human"], arch=[], tags=["sinnoh","cannons","flame"], stat=["spatk"], wk=0),
 "Togekiss":    dict(gen=4, dex=468, types=["fairy","flying"], color="white", evo="stone", egg=["flying","fairy"], arch=["bird"], tags=["sinnoh","egg-wings","jubilee","grace"], stat=["spatk","tanky"], wk=1),
 "Leafeon":     dict(gen=4, dex=470, types=["grass"], color="green", evo="special", egg=["field"], arch=[], tags=["sinnoh","eeveelution","leaf","sprout"], stat=["tanky"], wk=1),
 "Glaceon":     dict(gen=4, dex=471, types=["ice"], color="blue", evo="special", egg=["field"], arch=[], tags=["sinnoh","eeveelution","frost","diamond-dust"], stat=["spatk"], wk=1),
 "Gliscor":     dict(gen=4, dex=472, types=["ground","flying"], color="purple", evo="special", egg=["bug"], arch=["chiropteran","bat","scorpion"], tags=["sinnoh","fangs","wings","tail"], stat=["tanky"], wk=0),
 "Mamoswine":   dict(gen=4, dex=473, types=["ice","ground"], color="brown", evo="special", egg=["field"], arch=["proboscidean","mammoth"], tags=["sinnoh","tusks","fur","move:earthquake"], stat=["atk"], wk=1),
 "Gallade":     dict(gen=4, dex=475, types=["psychic","fighting"], color="white", evo="stone", egg=["human","amorphous"], arch=[], tags=["sinnoh","elbow-blades","chivalry","mega"], stat=["atk"], wk=1),
 "Froslass":    dict(gen=4, dex=478, types=["ice","ghost"], color="white", evo="stone", egg=["fairy","mineral"], arch=[], tags=["sinnoh","kimono","yuki-onna","folklore"], stat=["fast"], wk=1),
 "Spiritomb":   dict(gen=4, dex=442, types=["ghost","dark"], color="purple", evo="none", egg=["amorphous"], arch=[], tags=["sinnoh","keystone","108-souls","folklore","forbidden"], stat=["tanky"], wk=1),
 "Mismagius":   dict(gen=4, dex=429, types=["ghost"], color="purple", evo="stone", egg=["amorphous"], arch=[], tags=["sinnoh","witch-hat","hex","levitate","folklore"], stat=["fast"], wk=1),
 "Honchkrow":   dict(gen=4, dex=430, types=["dark","flying"], color="black", evo="stone", egg=["flying"], arch=["bird","corvid"], tags=["sinnoh","crow","boss","hat"], stat=["atk"], wk=0),
 "Liepard":     dict(gen=5, dex=510, types=["dark"], color="purple", evo="level", egg=["field"], arch=["feline","leopard"], tags=["unova","sleek-cat","prowl","thief"], stat=["fast"], wk=1),
 # --- Gen 5 ---
 "Serperior":   dict(gen=5, dex=497, types=["grass"], color="green", evo="level", egg=["field","grass"], arch=["serpent","snake"], tags=["starter","unova","regal","coils"], stat=["fast"], wk=1),
 "Emboar":      dict(gen=5, dex=500, types=["fire","fighting"], color="red", evo="level", egg=["field"], arch=["boar","pig"], tags=["starter","unova","beard","fists","tusks"], stat=["atk"], wk=1),
 "Samurott":    dict(gen=5, dex=503, types=["water"], color="blue", evo="level", egg=["field"], arch=["pinniped","otter"], tags=["starter","unova","whiskers","seamitar","samurai"], stat=["atk"], wk=1),
 "Zoroark":     dict(gen=5, dex=571, types=["dark"], color="gray", evo="level", egg=["field"], arch=["canine","fox"], tags=["unova","ponytail","illusion","trickster","kitsune"], stat=["fast","spatk"], wk=1),
 "Excadrill":   dict(gen=5, dex=530, types=["ground","steel"], color="brown", evo="level", egg=["field"], arch=["mole"], tags=["unova","drills","claws","burrow","move:earthquake"], stat=["atk","fast"], wk=1),
 "Audino":      dict(gen=5, dex=531, types=["normal"], color="pink", evo="none", egg=["fairy"], arch=[], tags=["unova","ears","nurse","mega","healer"], stat=["tanky"], wk=1),
 "Krookodile":  dict(gen=5, dex=553, types=["ground","dark"], color="red", evo="level", egg=["field"], arch=["reptile","crocodile"], tags=["unova","jaws","shades","intimidate","move:earthquake"], stat=["atk","fast"], wk=1),
 "Scrafty":     dict(gen=5, dex=560, types=["dark","fighting"], color="red", evo="level", egg=["field","dragon"], arch=["reptile","lizard"], tags=["unova","hoodie","crest","thug"], stat=["tanky"], wk=1),
 "Zebstrika":   dict(gen=5, dex=523, types=["electric"], color="black", evo="level", egg=["field"], arch=["equine","zebra"], tags=["unova","stripes","mane","hooves"], stat=["fast"], wk=1),
 "Chandelure":  dict(gen=5, dex=609, types=["ghost","fire"], color="black", evo="stone", egg=["amorphous"], arch=[], tags=["unova","lantern","chandelier","levitate","will-o-wisp","folklore"], stat=["spatk"], wk=1),
 "Haxorus":     dict(gen=5, dex=612, types=["dragon"], color="yellow", evo="level", egg=["monster","dragon"], arch=["dragon"], tags=["unova","axe-jaw","tusks","blades"], stat=["atk"], wk=1),
 "Beartic":     dict(gen=5, dex=614, types=["ice"], color="white", evo="level", egg=["field"], arch=["bear","polar-bear"], tags=["unova","ice-beard","claws"], stat=["atk"], wk=1),
 "Cryogonal":   dict(gen=5, dex=615, types=["ice"], color="blue", evo="none", egg=["mineral"], arch=[], tags=["unova","snowflake","crystal","chains"], stat=["fast"], wk=0),
 "Mienshao":    dict(gen=5, dex=620, types=["fighting"], color="purple", evo="level", egg=["human","field"], arch=["mustelid","weasel"], tags=["unova","sleeves","martial-arts"], stat=["fast","atk"], wk=0),
 "Druddigon":   dict(gen=5, dex=621, types=["dragon"], color="red", evo="none", egg=["monster","dragon"], arch=["dragon"], tags=["unova","rough-skin","claws"], stat=["atk"], wk=0),
 "Golurk":      dict(gen=5, dex=623, types=["ground","ghost"], color="green", evo="level", egg=["mineral"], arch=[], tags=["unova","golem-mythos","automaton","rocket","seal"], stat=["atk","tanky"], wk=1),
 "Bisharp":     dict(gen=5, dex=625, types=["dark","steel"], color="red", evo="level", egg=["human"], arch=[], tags=["unova","blades","warlord","helmet","axe"], stat=["atk"], wk=1),
 "Braviary":    dict(gen=5, dex=628, types=["normal","flying"], color="red", evo="level", egg=["flying"], arch=["bird","raptor","eagle"], tags=["unova","eagle","valour","talons"], stat=["atk"], wk=1),
 "Hydreigon":   dict(gen=5, dex=635, types=["dark","dragon"], color="blue", evo="level", egg=["dragon"], arch=["hydra","dragon"], tags=["unova","pseudo","three-heads","hydra-mythos"], stat=["spatk","fast"], wk=1),
 "Volcarona":   dict(gen=5, dex=637, types=["bug","fire"], color="white", evo="level", egg=["bug"], arch=["insect","moth"], tags=["unova","sun-wings","embers","moth"], stat=["spatk"], wk=1),
 "Alomomola":   dict(gen=5, dex=594, types=["water"], color="pink", evo="none", egg=["water1","water2"], arch=["fish"], tags=["unova","heart","nurse","caretaker"], stat=["tanky"], wk=0),
 # --- Gen 6 ---
 "Chesnaught":  dict(gen=6, dex=652, types=["grass","fighting"], color="green", evo="level", egg=["field"], arch=[], tags=["starter","kalos","armour","spikes","knight"], stat=["tanky"], wk=1),
 "Delphox":     dict(gen=6, dex=655, types=["fire","psychic"], color="red", evo="level", egg=["field"], arch=["fox","canine"], tags=["starter","kalos","wand","robe","witch","kitsune"], stat=["spatk"], wk=1),
 "Greninja":    dict(gen=6, dex=658, types=["water","dark"], color="blue", evo="level", egg=["water1"], arch=["frog","ninja"], tags=["starter","kalos","tongue-scarf","ninja","shuriken"], stat=["fast"], wk=1),
 "Talonflame":  dict(gen=6, dex=663, types=["fire","flying"], color="red", evo="level", egg=["flying"], arch=["bird","falcon","raptor"], tags=["kalos","talons","embers","move:fly"], stat=["fast"], wk=1),
 "Aegislash":   dict(gen=6, dex=681, types=["steel","ghost"], color="brown", evo="special", egg=["mineral"], arch=[], tags=["kalos","sword","shield","hilt","royal-blade"], stat=["atk","tanky"], wk=1),
 "Malamar":     dict(gen=6, dex=687, types=["dark","psychic"], color="blue", evo="special", egg=["water1","water2"], arch=["cephalopod","squid"], tags=["kalos","squid","hypnosis","upside-down"], stat=["atk"], wk=1),
 "Sylveon":     dict(gen=6, dex=700, types=["fairy"], color="pink", evo="friendship", egg=["field"], arch=[], tags=["kalos","eeveelution","bows","ribbons","feelers"], stat=["spatk","tanky"], wk=1),
 "Florges":     dict(gen=6, dex=671, types=["fairy"], color="white", evo="stone", egg=["fairy"], arch=[], tags=["kalos","flower","garden","blossom","elegant"], stat=["spatk","tanky"], wk=1),
 "Goodra":      dict(gen=6, dex=706, types=["dragon"], color="purple", evo="level", egg=["dragon"], arch=["dragon","slug"], tags=["kalos","pseudo","slime","horns","gooey"], stat=["tanky"], wk=1),
 "Trevenant":   dict(gen=6, dex=709, types=["ghost","grass"], color="brown", evo="special", egg=["grass","amorphous"], arch=[], tags=["kalos","haunted-tree","folklore","roots"], stat=["tanky"], wk=0),
 "Gourgeist":   dict(gen=6, dex=711, types=["ghost","grass"], color="brown", evo="trade", egg=["amorphous"], arch=[], tags=["kalos","pumpkin","jack-o-lantern","halloween","folklore"], stat=["tanky"], wk=0),
 "Noivern":     dict(gen=6, dex=715, types=["flying","dragon"], color="purple", evo="level", egg=["flying","dragon"], arch=["chiropteran","bat","wyvern"], tags=["kalos","sound","wings","ears"], stat=["fast"], wk=1),
 # --- Gen 7 ---
 "Decidueye":   dict(gen=7, dex=724, types=["grass","ghost"], color="brown", evo="level", egg=["flying"], arch=["bird","owl"], tags=["starter","alola","archer","hood","owl"], stat=["atk"], wk=1),
 "Incineroar":  dict(gen=7, dex=727, types=["fire","dark"], color="red", evo="level", egg=["field","human"], arch=["feline","tiger"], tags=["starter","alola","belt-fire","wrestler","heel","intimidate"], stat=["atk"], wk=1),
 "Primarina":   dict(gen=7, dex=730, types=["water","fairy"], color="blue", evo="level", egg=["water1","field"], arch=["pinniped","sea-lion"], tags=["starter","alola","opera","diva","song"], stat=["spatk"], wk=1),
 "Lycanroc":    dict(gen=7, dex=745, types=["rock"], color="brown", evo="level", egg=["field"], arch=["canine","wolf"], tags=["alola","wolf","mane","howl"], stat=["fast"], wk=1),
 "Toxapex":     dict(gen=7, dex=748, types=["poison","water"], color="purple", evo="level", egg=["water1"], arch=["echinoderm","starfish"], tags=["alola","spikes","crown-of-thorns","venom"], stat=["tanky"], wk=1),
 "Mudsdale":    dict(gen=7, dex=750, types=["ground"], color="brown", evo="level", egg=["field"], arch=["equine","horse","draft-horse"], tags=["alola","hooves","clydesdale","kick"], stat=["tanky","atk"], wk=1),
 "Bewear":      dict(gen=7, dex=760, types=["normal","fighting"], color="pink", evo="level", egg=["field"], arch=["bear"], tags=["alola","hug","dangerous","ribbon"], stat=["atk"], wk=1),
 "Mimikyu":     dict(gen=7, dex=778, types=["ghost","fairy"], color="white", evo="none", egg=["amorphous"], arch=[], tags=["alola","rag","disguise","pikachu-costume","folklore"], stat=["fast"], wk=1),
 "Bruxish":     dict(gen=7, dex=779, types=["water","psychic"], color="pink", evo="none", egg=["water2"], arch=["fish"], tags=["alola","teeth","grind","triggerfish"], stat=["fast"], wk=0),
 "Kommo-o":     dict(gen=7, dex=784, types=["dragon","fighting"], color="gray", evo="level", egg=["dragon"], arch=["dragon"], tags=["alola","scales","drums","clanging"], stat=["tanky"], wk=1),
 "Golisopod":   dict(gen=7, dex=768, types=["bug","water"], color="gray", evo="level", egg=["bug","water3"], arch=["crustacean","isopod"], tags=["alola","armour","claws","chivalry"], stat=["atk","tanky"], wk=1),
 "Kartana":     dict(gen=7, dex=798, types=["grass","steel"], color="white", evo="none", egg=["undiscovered"], arch=[], tags=["alola","paper","origami","blade","ultra-beast"], stat=["atk","fast"], wk=1),
 "Salazzle":    dict(gen=7, dex=758, types=["poison","fire"], color="purple", evo="level", egg=["monster","dragon"], arch=["reptile","lizard"], tags=["alola","toxic","salamander","allure"], stat=["fast"], wk=0),
 # --- Gen 8 ---
 "Rillaboom":   dict(gen=8, dex=812, types=["grass"], color="brown", evo="level", egg=["grass","field"], arch=["primate","gorilla"], tags=["starter","galar","drum","rhythm","mane"], stat=["atk"], wk=1),
 "Cinderace":   dict(gen=8, dex=815, types=["fire"], color="white", evo="level", egg=["field","human"], arch=["lagomorph","rabbit"], tags=["starter","galar","striker","fireball","footballer"], stat=["fast","atk"], wk=1),
 "Inteleon":    dict(gen=8, dex=818, types=["water"], color="blue", evo="level", egg=["water1","field"], arch=["reptile","lizard"], tags=["starter","galar","secret-agent","sniper","gecko"], stat=["fast","spatk"], wk=1),
 "Corviknight": dict(gen=8, dex=823, types=["flying","steel"], color="black", evo="level", egg=["flying"], arch=["bird","corvid","raven"], tags=["galar","armour","taxi","raven","knight"], stat=["tanky"], wk=1),
 "Toxtricity":  dict(gen=8, dex=849, types=["electric","poison"], color="purple", evo="level", egg=["human"], arch=["reptile"], tags=["galar","guitar","punk","amp","rocker"], stat=["spatk"], wk=1),
 "Grimmsnarl":  dict(gen=8, dex=861, types=["dark","fairy"], color="purple", evo="level", egg=["fairy","human"], arch=[], tags=["galar","hair","goblin","trickster","folklore"], stat=["atk"], wk=1),
 "Frosmoth":    dict(gen=8, dex=873, types=["ice","bug"], color="white", evo="friendship", egg=["bug"], arch=["insect","moth"], tags=["galar","ice-wings","scales","moth"], stat=["spatk"], wk=1),
 "Grapploct":   dict(gen=8, dex=853, types=["fighting"], color="blue", evo="level", egg=["water1","water2"], arch=["cephalopod","octopus"], tags=["galar","suckers","grappler","judo"], stat=["atk"], wk=0),
 "Dragapult":   dict(gen=8, dex=887, types=["dragon","ghost"], color="green", evo="level", egg=["amorphous","dragon"], arch=["dragon"], tags=["galar","pseudo","stealth-bomber","missile","dreepy"], stat=["fast"], wk=1),
 "Mudbray":     dict(gen=7, dex=749, types=["ground"], color="brown", evo="none", egg=["field"], arch=["equine","donkey"], tags=["alola","hooves","stubborn","mud"], stat=["atk"], wk=0),
 "Octillery":   dict(gen=2, dex=224, types=["water"], color="red", evo="level", egg=["water1","water2"], arch=["cephalopod","octopus"], tags=["johto","suckers","cannon","pot"], stat=["atk"], wk=0),
 "Ursaring":    dict(gen=2, dex=217, types=["normal"], color="brown", evo="level", egg=["field"], arch=["bear"], tags=["johto","chest-ring","claws","forager"], stat=["atk"], wk=1),
 "Klefki":      dict(gen=6, dex=707, types=["steel","fairy"], color="gray", evo="none", egg=["mineral"], arch=[], tags=["kalos","keys","keyring","collector"], stat=[], wk=1),
 "Wailord":     dict(gen=3, dex=321, types=["water"], color="blue", evo="level", egg=["field","water2"], arch=["cetacean","whale"], tags=["hoenn","whale","huge","float"], stat=["tanky"], wk=1),
 "Tyrantrum":   dict(gen=6, dex=697, types=["rock","dragon"], color="red", evo="level", egg=["monster","dragon"], arch=["dinosaur","theropod"], tags=["kalos","fossil","king-jaw","t-rex","despot"], stat=["atk"], wk=1),
 "Blissey":     dict(gen=2, dex=242, types=["normal"], color="pink", evo="friendship", egg=["fairy"], arch=[], tags=["johto","egg","pouch-egg","nurse","happy"], stat=["tanky"], wk=1),
}

FACTS = {}
FACTS.update({k: dict(gen=1, **v) for k, v in GEN1.items()})
FACTS.update(LATER)

# ============================ VALIDATION ============================
VALID_TYPES = {"normal","fire","water","electric","grass","ice","fighting","poison",
 "ground","flying","psychic","bug","rock","ghost","dragon","dark","steel","fairy"}
VALID_EVO = {"none","level","stone","trade","friendship","fossil","trade-item","special"}

def validate():
    errs=[]
    seen_dex={}
    for name, r in FACTS.items():
        for f in ("dex","gen","types","color","evo","egg","arch","tags","stat"):
            if f not in r: errs.append(f"{name}: missing {f}")
        if r["dex"] in seen_dex: errs.append(f"{name}: dex {r['dex']} dup with {seen_dex[r['dex']]}")
        seen_dex[r["dex"]]=name
        for t in r["types"]:
            if t not in VALID_TYPES: errs.append(f"{name}: bad type {t}")
        if r["evo"] not in VALID_EVO: errs.append(f"{name}: bad evo {r['evo']}")
        if not r["types"]: errs.append(f"{name}: no types")
    return errs

if __name__ == "__main__":
    errs = validate()
    if errs:
        print("VALIDATION ERRORS:")
        for e in errs: print("  x", e)
        sys.exit(1)
    # Coverage summary
    from collections import Counter
    print(f"Records: {len(FACTS)}")
    gens=Counter(r["gen"] for r in FACTS.values())
    print("By gen:", dict(sorted(gens.items())))
    typ=Counter(t for r in FACTS.values() for t in r["types"])
    print("Type coverage:", {k:typ[k] for k in sorted(typ)})
    json.dump(FACTS, open("/home/user/Pokemon-Codenames/pokemon_facts.json","w"), indent=0, ensure_ascii=False)
    print("wrote pokemon_facts.json")
