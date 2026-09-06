# New daily-puzzle boards filling the remaining gaps to 3 weeks ahead
# (2026-09-17 mixed, 2026-09-26 gen1, 2026-09-27 gen1+mixed). Loaded by
# fill_gaps_verify.py, which provides FACTS/GEN1/board() in scope.

# ===== 2026-09-17 Thu : HARD (mixed) =====
_chimera_excl = [n for n in FACTS if "chimera" in FACTS[n]["arch"]
                 and n not in ("Dracozolt", "Arctozolt", "Dracovish", "Arctovish")]
_raptor_excl = [n for n in FACTS if "raptor" in FACTS[n]["arch"]
                and n not in ("Archeops", "Staraptor")]
_canine_excl = [n for n in FACTS if "canine" in FACTS[n]["arch"]
                and n not in ("Manectric", "Zoroark", "Boltund")]
_mane_excl = ["Ninetales", "Growlithe", "Arcanine", "Ponyta", "Rapidash", "Flareon", "Raikou",
              "Entei", "Suicune", "Mightyena", "Vigoroth", "Absol", "Luxio", "Luxray", "Blitzle",
              "Zebstrika", "Whimsicott", "Deino", "Zweilous", "Cobalion", "Virizion", "Keldeo",
              "Litleo", "Pyroar", "Gogoat", "Lycanroc", "Mudbray", "Mudsdale", "Solgaleo",
              "Zeraora", "Rillaboom", "Zacian", "Zamazenta", "Zarude", "Glastrier", "Spectrier",
              "Wyrdeer", "Pawmot", "Koraidon", "Walking Wake", "Gouging Fire", "Raging Bolt"]
board("2026-09-17", "mixed", "Hard", [
    ("CHIMERA", 4, "arch:chimera", ["Dracozolt", "Arctozolt", "Dracovish", "Arctovish"]),
    ("TALONED", 4, "arch:raptor", ["Archeops", "Staraptor"]),
    ("CANINE", 3, "arch:canine", ["Manectric", "Zoroark", "Boltund"]),
    ("TRESSES", 2, "sprite:mane", ["Manectric", "Staraptor", "Zoroark"]),
], exclude=_chimera_excl + _raptor_excl + _canine_excl + _mane_excl)

# ===== 2026-09-26 Sat : BRUTAL (gen1) =====
# Raichu+Magneton (not Electabuzz - "ELECTRIC" would letter-clash with
# "Electabuzz" itself) for the type anchor; Charizard (not Charmeleon, which
# also clashes with "ELECTRIC", and not Vulpix, which would evo-pair with
# Ninetales - the 7-day evolution-family cap is already maxed nearby) pairs
# with Ninetales for the tail sprite; Hypno joins Alakazam for a
# psychic-mystique connection since "FIRE" and "PRIMATE" are both on 7-day
# cooldown from other recent boards.
_electric_excl = [n for n in GEN1 if "electric" in FACTS[n]["types"]
                  and n not in ("Raichu", "Magneton")]
_spatk_excl = [n for n in GEN1 if "spatk" in FACTS[n].get("stat", [])
               and n not in ("Alakazam", "Magneton", "Exeggutor")]
_primate_excl = [n for n in GEN1 if "primate" in FACTS[n]["arch"]
                 and n not in ("Machoke", "Mankey")]
_tapir_excl = [n for n in GEN1 if "tapir" in FACTS[n]["arch"] and n != "Hypno"]
board("2026-09-26", "gen1", "Brutal", [
    ("ELECTRIC", 1, "type:electric", ["Raichu", "Magneton"]),
    ("TAILED", 2, "sprite:tail", ["Ninetales", "Charizard"]),
    ("MINDBENDER", 5, "lore:hypnosis", ["Alakazam", "Hypno"]),
    ("SPECIAL", 5, "stat:special", ["Alakazam", "Magneton", "Exeggutor"]),
    ("SIMIAN", 4, "arch:primate", ["Machoke", "Mankey"]),
], exclude=_electric_excl + _spatk_excl + _primate_excl + _tapir_excl)

# ===== 2026-09-27 Sun : EVIL (gen1) =====
board("2026-09-27", "gen1", "Evil", [
    ("DUPLICATE", 5, "myth:clone", ["Mew", "Mewtwo"]),
    ("CURSED", 4, "lore:haunted", ["Haunter", "Marowak", "Jynx"]),
    ("ROYALTY", 4, "lore:royalty", ["Nidoking", "Nidoqueen"]),
    ("PIONEER", 4, "lore:pioneer", ["Rhydon", "Porygon", "Mew"]),
    ("RHINO", 3, "arch:rhino", ["Rhydon", "Nidoking"]),
], exclude=["Rhyhorn", "Cubone", "Gengar", "Gastly"])

# ===== 2026-09-27 Sun : EVIL (mixed) =====
_heavy_excl = [n for n in FACTS if "heavy" in FACTS[n].get("stat", [])
               and n not in ("Ting-Lu", "Cobalion", "Terrakion")]
_fast_excl = [n for n in FACTS if "fast" in FACTS[n].get("stat", [])
              and n not in ("Virizion", "Chi-Yu")]
_owl_excl = [n for n in FACTS if "owl" in FACTS[n]["arch"]
             and n not in ("Noctowl", "Rowlet")]
board("2026-09-27", "mixed", "Evil", [
    ("RUINOUS", 5, "myth:treasures-of-ruin", ["Wo-Chien", "Chien-Pao", "Ting-Lu", "Chi-Yu"]),
    ("MUSKETEERS", 4, "lore:musketeers", ["Cobalion", "Terrakion", "Virizion"]),
    ("HEAVYWEIGHT", 5, "stat:heavy", ["Ting-Lu", "Cobalion", "Terrakion"]),
    ("QUICKSILVER", 5, "stat:fast", ["Virizion", "Chi-Yu"]),
    ("SCREECH", 3, "arch:owl", ["Noctowl", "Rowlet"]),
], exclude=["Keldeo"] + _heavy_excl + _fast_excl + _owl_excl)
