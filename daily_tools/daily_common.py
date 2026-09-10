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
 # sprite (phrase): "you can spot it on the sprite – {r}"
 "fist":"the raised fists","seeds":"the seeds on its body","mushroom":"the mushroom on its back",
 "pincers":"the big pincers","scythe":"the scythe-shaped arms","acorn":"the acorn cap",
 "ball":"a Poké Ball shape","coin":"the gold coin on its forehead","coins":"a hoard of gold coins",
 "gem":"a gemstone body","spores":"the spores it puffs out","star":"its star shape",
 "gills":"its gills","web":"its web","cocoon":"its cocoon shell","drill":"its drill horn",
 "jaws":"its huge jaws","frill":"its frilled crest","tongue":"its long tongue",
 "petals":"its flower petals","fins":"its fins","balloon":"its round balloon body",
 # lore (phrase): "from their Pokédex lore – {r}"
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
 # extra concept phrasings (stat / lore / fantastical archetypes / based)
 "defense":"a rock-solid defence stat","heavy":"being seriously heavy","special":"a huge Special stat",
 "speed":"blistering Speed","ancient":"prehistoric relics dug up as fossils",
 "doll":"a possessed doll","royalty":"royalty – a king or queen","brawl":"bare-knuckle brawlers",
 "martial-arts":"trained martial artists","mind":"raw psychic mind-power","gears":"living clockwork gears",
 "willowisp":"a will-o'-the-wisp flame","mythical":"rare mythical Pokémon","poison-gas":"the toxic gas they belch",
 "ice-storm":"a howling blizzard","haunted-object":"an everyday object turned haunted","polygon":"blocky 3-D graphics",
 "lava":"molten lava","volcano":"an erupting volcano","legendary":"the legendary birds","sea-serpent":"a sea serpent",
 "raptor":"bird of prey","canine":"dog","oni":"an oni demon","blue":"Blue, the Kanto Champion",
 "clone":"a genetically-engineered clone","haunted":"they're each linked to something haunted or cursed",
 "pioneer":"each was a landmark 'first' in Pokémon history","treasures-of-ruin":"the cursed Treasures of Ruin",
 "musketeers":"the legendary Musketeer trio","fast":"blistering speed",
 "amorphous":"shapeless ooze","intimidate":"their shared Intimidate ability",
}
# fantastical archetypes that shouldn't read "based on the real-world ..."
_FANCIFUL = {"genie":"wish-granting genies","deity":"guardian deities","chimera":"stitched-together chimeras",
             "alien":"alien visitors","dragon":"dragons","serpent":"snakes"}
def _read(tail): return READ.get(tail, tail.replace("-", " "))

def _names(members):
    """Readable 'A, B and C' for weaving member names into the explanation."""
    ms = list(members or [])
    if not ms: return ""
    if len(ms) == 1: return ms[0]
    if len(ms) == 2: return f"{ms[0]} and {ms[1]}"
    return ", ".join(ms[:-1]) + f" and {ms[-1]}"

# NOTE ON EXPLANATIONS (owner feedback, Sep 2026): these template strings are the
# BASELINE / fallback only. They read a bit thin ("It's from their Pokédex lore –
# kappa"), so when AUTHORING a board, prefer a bespoke `explain` (optional 5th
# element of the clue tuple) that says something concrete: quote/paraphrase the
# real Pokédex entry, name the actual Ability and what it does, name the specific
# myth and the link. See daily_puzzle_notes.md → "Clue explanations". The
# functions below are only used when a clue has no bespoke explain.
def explain_for(word, cat, concept, members):
    pre, _, tail = concept.partition(":")
    r = _read(tail)
    if pre == "type":
        art = "an" if tail[:1].lower() in "aeiou" else "a"
        return f"Every one of these is {art} {tail.capitalize()}-type Pokémon."
    if pre == "group":
        return {"starter":"They're all first-partner (starter) Pokémon — the ones you choose at the start of a game.",
                "legendary":"They're all Legendary Pokémon.",
                "pseudo":"They're all pseudo-legendary Pokémon (a 600-base-stat three-stage line)."}.get(tail, f"They're all {r}.")
    if pre == "family":
        return f"They're all part of the {r} evolutionary family."
    if pre == "arch":
        if tail in _FANCIFUL:
            return f"They're all based on {_FANCIFUL[tail]}."
        return f"They're all based on the same real-world creature — the {r}."
    if pre == "stat":
        return f"They share a standout base stat — {r}."
    if pre == "based":
        return f"They're each based on {r}."
    if pre == "sprite":
        return f"Look closely at the sprite and you'll spot it — {r}."
    if pre == "lore":
        return f"It comes from their Pokédex lore — {r}."
    if pre == "myth":
        return f"It's rooted in mythology and folklore — {r}."
    if pre == "name":
        return f"It's a play on their names — {r}."
    if pre == "trainer":
        return f"They're all on {r}'s team."
    if pre == "colour":
        return f"They're all {r} in colour."
    if pre == "habitat":
        return f"They all live in the same kind of place — {r}."
    if pre == "egg":
        return f"They're in the same Egg Group — {r} — so they can breed together."
    if pre == "ability":
        return f"They all share the same Ability: {tail.replace('-', ' ').title()}."
    if pre == "move":
        return f"They can all learn the move {tail.replace('-', ' ').title()}."
    return r[:1].upper() + r[1:] + "."
