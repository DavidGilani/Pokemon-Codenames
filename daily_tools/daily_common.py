# Shared helpers for the daily-puzzle schedulers (exec'd, not imported).
# explain_for(word, cat, concept, members) -> a plain-English sentence for the
# end-of-game "what each clue meant" reveal. Category numbers are internal and
# never shown to players, so they are NOT included in the text.

READ = {
 # arch (plain noun): "based on the real-world {r}"
 "golem":"rock golem","butterfly":"butterfly","fox":"fox","caterpillar":"caterpillar",
 "crow":"crow","snail":"snail","tapir":"tapir (a dream-eating baku)","crocodile":"crocodile",
 "duck":"duck","eel":"eel and sea-serpent","monkey":"monkey","octopus":"octopus","squid":"squid",
 "sloth":"sloth","cobra":"cobra","feline":"cat","rhino":"rhinoceros","otter":"sea otter",
 "mole":"mole","firefly":"firefly","jellyfish":"jellyfish","frog":"frog","bee":"bee",
 "seal":"seal and sea lion","unicorn":"unicorn","swan":"swan","gorilla":"gorilla",
 "weasel":"weasel","sludge":"sludge","rodent":"rodent","cactus":"cactus","sheep":"sheep",
 "meerkat":"meerkat","starfish":"starfish","ratite":"flightless bird (ostrich / emu)",
 "mantis":"mantis","beetle":"beetle","serpent":"snake","platypus":"platypus","penguin":"penguin",
 "scorpion":"scorpion","cephalopod":"octopus / squid","antlion":"antlion","dinosaur":"dinosaur",
 "pelican":"pelican","turtle":"turtle","panda":"panda","sealion":"sea lion","owl":"owl",
 "gecko":"gecko","hermit-crab":"hermit crab","chameleon":"chameleon","koala":"koala",
 "dolphin":"dolphin","dragonfly":"dragonfly","heron":"heron","bat":"bat","spider":"spider",
 # based (phrase): "based on {r}"
 "bone":"the bone club and skull helmet it wears","lantern":"a haunted lantern",
 "sumo":"sumo wrestlers","scarab":"the scarab beetle","polygon":"3-D polygon graphics",
 "reaper":"the Grim Reaper","keyring":"a key ring","boxer":"a boxer","santa":"Santa Claus",
 "pumpkin":"a carved pumpkin","jack-o-lantern":"a carved jack-o'-lantern","apple":"an apple",
 "sword":"a sword","knight":"an armoured knight","golem-robot":"a robot golem",
 "flytrap":"a Venus flytrap","pitcher":"the pitcher plant","candle":"a lit candle",
 "gargoyle":"a stone gargoyle","coffin":"a coffin","samurai":"a samurai","scarecrow":"a scarecrow",
 # sprite (phrase): "you can spot it on the sprite — {r}"
 "fist":"the raised fists","seeds":"the seeds on its body","mushroom":"the mushroom on its back",
 "pincers":"the big pincers","scythe":"the scythe-shaped arms","acorn":"the acorn cap",
 "ball":"a Poké Ball shape","coin":"the gold coin on its forehead","coins":"a hoard of gold coins",
 "gem":"a gemstone body","spores":"the spores it puffs out","star":"its star shape",
 "gills":"its gills","web":"its web","cocoon":"its cocoon shell","drill":"its drill horn",
 "jaws":"its huge jaws","frill":"its frilled crest","tongue":"its long tongue",
 "petals":"its flower petals","fins":"its fins","balloon":"its round balloon body",
 # lore (phrase): "from their Pokédex lore — {r}"
 "vampire":"they're vampire bats","teleport":"its signature Teleport move",
 "jynx":"an opera diva / snow-hag","ferry":"it ferries travellers across the sea",
 "fossil":"they're prehistoric fossils brought back to life","lava":"they're made of molten lava",
 "leek":"the spring onion (leek) it carries","mythical":"a mythical dragon",
 "hypnosis":"it puts foes to sleep","transform":"it can transform into any Pokémon",
 "curse":"it curses and haunts","tarot":"it foretells the future","smoke":"it belches smoke",
 "glutton":"its endless appetite","powder":"the powder it scatters","uri-geller":"the spoon-bender Uri Geller",
 "haunted-tree":"a haunted tree","carnivore-plant":"a man-eating plant","nocturnal":"it prowls at night",
 # myth
 "kitsune":"the kitsune fox-spirit","mummy":"an Egyptian mummy","jellyfish-myth":"Medusa",
 "hydra":"the many-headed hydra","mermaid":"a mermaid","phoenix":"a phoenix",
 # name / family / group
 "palindrome":"their names read the same backwards","eevee":"Eevee",
}
def _read(tail): return READ.get(tail, tail.replace("-", " "))

def explain_for(word, cat, concept, members):
    pre, _, tail = concept.partition(":")
    r = _read(tail)
    if pre == "type":
        return f"Every one is a {tail.capitalize()}-type."
    if pre == "group":
        return {"starter":"They're first-partner (starter) Pokémon.",
                "legendary":"They're all Legendary Pokémon.",
                "pseudo":"They're pseudo-legendary Pokémon."}.get(tail, f"They're all {r}.")
    if pre == "family":
        return f"They're all part of the {r} family."
    if pre == "arch":
        return f"They're all based on the real-world {r}."
    if pre == "based":
        return f"They're based on {r}."
    if pre == "sprite":
        return f"You can spot it on the sprite — {r}."
    if pre == "lore":
        return f"It's from their Pokédex lore — {r}."
    if pre == "myth":
        return f"It's rooted in mythology — {r}."
    if pre == "name":
        return f"It's wordplay on their names — {r}."
    if pre == "trainer":
        return f"They belong to {r}'s team."
    if pre == "colour":
        return f"They're all {r}."
    if pre == "habitat":
        return f"They all live in the same kind of place — {r}."
    if pre == "egg":
        return f"They're in the same egg group — {r}."
    return r[:1].upper() + r[1:] + "."
