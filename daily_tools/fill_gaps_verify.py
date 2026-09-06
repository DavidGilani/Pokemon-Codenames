#!/usr/bin/env python3
"""
Verifier for the 4 gap-fill daily boards (2026-09-17 mixed, 2026-09-26 gen1,
2026-09-27 gen1, 2026-09-27 mixed). Mirrors the rules in schedule_v2.py /
daily_puzzle_notes.md, but loads the anti-repetition corpus from a fresh
Supabase export (CORPUS_PATH) instead of a stale uploaded CSV, so it actually
runs in a clean checkout. Edit NEW_BOARDS below, then:
    python3 daily_tools/fill_gaps_verify.py
until it prints ALL VALID. On success it writes 34_updates.sql.
"""
import json, re, random, datetime, hashlib
from collections import defaultdict

ROOT = "/home/user/pc"
CORPUS_PATH = "/tmp/claude-0/-home-user-Pokemon-Codenames/c0fbb6b3-049d-5dbe-a7b5-bfafcbd38cd9/scratchpad/corpus.json"
FACTS = json.load(open(f"{ROOT}/pokemon_facts.json"))
GEN1 = {n for n, r in FACTS.items() if r["gen"] == 1}
random.seed(2026)


def _sd(x):
    return int(hashlib.md5(repr(x).encode()).hexdigest()[:8], 16)


WEEKDAY_TIER = {0: "Easy", 1: "Medium", 2: "Challenging", 3: "Hard", 4: "Hard", 5: "Brutal", 6: "Evil"}


def tier_for(date):
    return WEEKDAY_TIER[datetime.date.fromisoformat(date).weekday()]


def norm(s):
    return re.sub(r'[^a-z]', '', s.lower())


def shares3(a, b):
    a, b = norm(a), norm(b)
    for i in range(len(a) - 2):
        if a[i:i + 3] in b:
            return a[i:i + 3]
    for i in range(len(b) - 2):
        if b[i:i + 3] in a:
            return b[i:i + 3]
    return None


def days(a, b):
    return (datetime.date.fromisoformat(a) - datetime.date.fromisoformat(b)).days


# ---- corpus (fresh Supabase export; ALL live rows) ----
CORPUS = json.load(open(CORPUS_PATH))
USES = defaultdict(list)      # word -> [(date, frozenset(members))]
BLUE_USED = defaultdict(list)  # name -> [date]
EVO_HIST = []                  # (date, word) evolution-family clue-groups in corpus
for row in CORPUS:
    rd = row["puzzle_date"]
    T = {t["position"]: t for t in row["tiles"]}
    blues = [t["name"] for t in row["tiles"] if t["colour"] == "blue"]
    for nm in blues:
        BLUE_USED[nm].append(rd)
    for c in row["clues"]:
        grp = frozenset(T[p]["name"] for p in c.get("t", []))
        USES[c["word"]].append((rd, grp))
        byfam = defaultdict(list)
        for nm in grp:
            if nm in FACTS:
                byfam[FACTS[nm]["family"]].append(nm)
        for fam, mem in byfam.items():
            if len(mem) >= 2:
                EVO_HIST.append((rd, c["word"]))

CORPUS_DATES = {(r["puzzle_date"], r["pool"]) for r in CORPUS}

# ===================== NEW BOARDS TO AUTHOR =====================
B = []


def board(date, pool, tier, clues, exclude=()):
    B.append(dict(date=date, pool=pool, tier=tier, clues=clues, exclude=list(exclude)))


NEW_BOARDS_MODULE = f"{ROOT}/daily_tools/fill_gaps_boards.py"
exec(open(f"{ROOT}/daily_tools/daily_common.py").read())  # explain_for
exec(open(NEW_BOARDS_MODULE).read())
# ==================================================================


def evo_groups(clues):
    out = []
    for w, c, cc, m in clues:
        byfam = defaultdict(list)
        for nm in m:
            if nm in FACTS:
                byfam[FACTS[nm]["family"]].append(nm)
        for f, mem in byfam.items():
            if len(mem) >= 2:
                out.append((w, f))
    return out


def label(cats):
    highs = sum(1 for c in cats if c >= 4)
    ones = sum(1 for c in cats if c == 1)
    if highs >= 4:
        return "Evil"
    if highs >= 3:
        return "Brutal"
    if ones == 0:
        return "Hard"
    if ones == 1:
        return "Challenging"
    if ones == 2:
        return "Medium"
    return "Easy"


def hint_for(nm, names, used):
    r = FACTS[nm]
    cands = []

    def sub(x):
        return x.replace("-", " ").lower()

    def art(x):
        return "an" if x[:1].lower() in "aeiou" else "a"

    for s in r["sprite"]:
        cands.append((s.upper().replace(" ", "-"), 2, f"Look for the {sub(s)} on {nm}'s sprite."))
    for a in r["arch"]:
        cands.append((a.upper(), 3, f"{nm} is based on {art(sub(a))} {sub(a)}."))
    for b in r["based_on"]:
        for part in re.split(r"[\(/,]", b):
            w = part.strip().upper().replace(" ", "-")
            if w:
                cands.append((w, 3, f"{nm} is based on the {sub(w)}."))
    if r.get("genus"):
        cands.append((r["genus"].split()[0].upper(), 2, f"{nm} is the {r['genus']}."))
    if r.get("color_primary"):
        cands.append((r["color_primary"].upper() + "-BODY", 2, f"{nm} is mostly {r['color_primary'].lower()}."))
    for eg in r.get("egg", []):
        cands.append((eg.upper() + "-EGG", 3, f"{nm} is in the {sub(eg)} egg group."))
    for mv in r.get("moves", []):
        cands.append((mv.upper().replace(" ", "-"), 3, f"{nm} is known for the move {sub(mv).title()}."))
    if r.get("habitat"):
        cands.append((r["habitat"].upper().replace(" ", "-"), 3, f"{nm} is found in the {sub(r['habitat'])}."))
    if r.get("color_secondary"):
        cands.append((r["color_secondary"].upper() + "-MARKS", 2, f"{nm} has {r['color_secondary'].lower()} markings."))
    cands.append(("TYPE-" + r["types"][0].upper(), 1, f"{nm} is a {r['types'][0].capitalize()}-type."))
    for w, c, ex in cands:
        if w in used:
            continue
        if any(shares3(w, x) for x in names):
            continue
        return w, c, ex
    return None, None, None


errors = []
assembled = []
nb = defaultdict(list)
nw = defaultdict(list)
nc_evo = []  # (date, word) new evo-family groups, for the rolling-7d cap (both new+corpus)

for b in sorted(B, key=lambda x: (x["date"], x["pool"])):
    d, pool, where = b["date"], b["pool"], f'{b["date"]} {b["pool"]}'
    if (d, pool) in CORPUS_DATES:
        errors.append(f"{where}: already exists in live corpus - refusing to overwrite")
    poolset = GEN1 if pool == "gen1" else set(FACTS)
    clues = b["clues"]
    blues = []
    for w, c, cc, m in clues:
        for nm in m:
            if nm not in blues:
                blues.append(nm)
    for nm in blues:
        if nm not in FACTS:
            errors.append(f"{where}: {nm} not in facts")
        elif nm not in poolset:
            errors.append(f"{where}: {nm} not in {pool} pool")
    if len(blues) != 9:
        errors.append(f"{where}: {len(blues)} blues {blues}")
    cats = [c for w, c, cc, m in clues]
    want = tier_for(d)
    if b["tier"] != want:
        errors.append(f"{where}: tier {b['tier']} != weekday {want}")
    if label(cats) != b["tier"]:
        errors.append(f'{where}: label {label(cats)}!=tier {b["tier"]}')
    cat2 = sum(1 for c in cats if c == 2)
    if b["tier"] in ("Hard", "Brutal") and cat2 > 1:
        errors.append(f"{where}: cat2={cat2}>1")
    if b["tier"] == "Evil" and cat2 > 0:
        errors.append(f"{where}: Evil has cat2={cat2}")
    if len(set(cats)) < 3 and b["tier"] != "Easy":
        errors.append(f"{where}: <3 distinct cats")
    if not (1 <= len(clues) <= 5):
        errors.append(f"{where}: {len(clues)} clues (must be 1-5)")
    for w, c, cc, m in clues:
        if cc.startswith("type:"):
            ty = cc.split(":", 1)[1]
            allty = sorted(nm for nm in blues if ty in FACTS[nm]["types"])
            if sorted(m) != allty:
                errors.append(f"{where}: type clue {w} lists {sorted(m)} but every {ty}-type blue is {allty}")
    sets = [(w, frozenset(m)) for w, c, cc, m in clues]
    for i, (wi, si) in enumerate(sets):
        for j, (wj, sj) in enumerate(sets):
            if i == j or not si:
                continue
            if si < sj or (si == sj and i < j):
                errors.append(f"{where}: clue {wi} {sorted(si)} is contained in {wj} {sorted(sj)} (redundant split)")
    if b["tier"] in ("Brutal", "Evil"):
        nums = [len(m) for w, c, cc, m in clues]
        if sum(nums) < 11:
            errors.append(f"{where}: {b['tier']} sum {sum(nums)}<11")
        if sum(1 for n in nums if n == 1) > 1:
            errors.append(f"{where}: {b['tier']} >1 single-tile clue")
    eg = evo_groups(clues)
    if len(eg) > 1:
        errors.append(f"{where}: {len(eg)} evolution-family clues (max 1) {eg}")
    if eg:
        # Only a board that itself contributes an evo-family clue can be blamed
        # for pushing a rolling window over the cap - pre-existing corpus days
        # around it are already live and outside this run's control.
        recent_evo = sum(1 for od, _ in (EVO_HIST + nc_evo) if 0 < abs(days(d, od)) <= 7) + len(eg)
        if recent_evo > 3:
            errors.append(f"{where}: {recent_evo} evolution-family clues in trailing/leading 7d (max 3)")
    for w, f in eg:
        nc_evo.append((d, w))
    ptypes = {FACTS[n]["types"][0] for n in blues}
    need = 4 if pool == "gen1" else 5
    if len(ptypes) < need:
        errors.append(f"{where}: {len(ptypes)} types (<{need}) {sorted(ptypes)}")
    if pool == "mixed" and len({FACTS[n]["gen"] for n in blues}) < 3:
        errors.append(f"{where}: <3 gens")
    dt = d
    cap = 5 if pool == "gen1" else 10
    for w, c, cc, m in clues:
        grp = frozenset(m)
        for od, om in USES.get(w, []) + nw[w]:
            if 0 < abs(days(dt, od)) <= 7:
                errors.append(f"{where}: WORD '{w}' within 7d of {od}")
            if 0 < abs(days(dt, od)) <= 14 and om == grp:
                errors.append(f"{where}: GROUP '{w}' within 14d of {od}")
        nw[w].append((d, grp))
    for nm in blues:
        for od in BLUE_USED.get(nm, []) + nb[nm]:
            if 0 < abs(days(dt, od)) <= cap:
                errors.append(f"{where}: BLUE '{nm}' within {cap}d of {od}")
        nb[nm].append(d)
    cluewords = [w for w, c, cc, m in clues]
    ban_types = {cc.split(":")[1] for w, c, cc, m in clues if cc.startswith("type:")}
    ban_cols = {cc.split(":")[1] for w, c, cc, m in clues if cc.startswith("colour:")}

    def ok_sem(nm):
        r = FACTS[nm]
        if ban_types & set(r["types"]):
            return False
        if r["color_primary"] in ban_cols:
            return False
        return True

    cand = [nm for nm in poolset if nm not in blues and nm not in set(b["exclude"])
            and nm.isascii() and FACTS[nm].get("wk", 0) == 1 and ok_sem(nm)
            and not any(shares3(w, nm) for w in cluewords)]
    cand = sorted(cand)
    rng = random.Random(_sd((d, pool)))
    rng.shuffle(cand)
    neutrals = cand[:16]
    if len(neutrals) < 16:
        errors.append(f"{where}: only {len(neutrals)} neutrals")
    names = blues + neutrals
    for w, c, cc, m in clues:
        for nm in names:
            f = shares3(w, nm)
            if f:
                errors.append(f"{where}: LETTER clue {w}~{nm}({f})")
    hints = {}
    used = set()
    for nm in blues:
        hw, hc, he = hint_for(nm, names, used)
        if not hw:
            errors.append(f"{where}: no hint for {nm}")
            continue
        hints[nm] = (hw, hc, he)
        used.add(hw)
    b.update(blues=blues, neutrals=neutrals, hints=hints)
    assembled.append(b)

print("=== VERIFY gap-fill boards ===")
if errors:
    for e in errors:
        print("  x", e)
    print(len(errors), "errors")
else:
    print("  ALL VALID -", len(assembled), "boards")

    def jarr(o):
        parts = []
        for x in o:
            fields = ['"word": ' + json.dumps(x["word"]), '"number": %d' % x["number"],
                      '"cat": %d' % x["cat"], '"t": [' + ", ".join(map(str, x["t"])) + "]"]
            if x.get("explain"):
                fields.append('"explain": ' + json.dumps(x["explain"]))
            parts.append("{" + ", ".join(fields) + "}")
        return "[" + ", ".join(parts) + "]"

    def sq(s):
        return "'" + s.replace("'", "''") + "'"

    L = ["-- 35_updates.sql : fill remaining daily-puzzle gaps to 3 weeks ahead",
         "-- (2026-09-17 mixed, 2026-09-26 gen1, 2026-09-27 gen1+mixed).",
         "-- Weekday difficulty tiers and the Brutal/Evil overlap gate as usual.", "",
         "insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values"]
    R = []
    for b in assembled:
        blues, neutrals, hints = b["blues"], b["neutrals"], b["hints"]
        names = blues + neutrals
        perm = list(range(25))
        random.Random(_sd(("p", b["date"], b["pool"]))).shuffle(perm)
        pos = {nm: perm[i] for i, nm in enumerate(names)}
        tiles = sorted([{"name": nm, "colour": "blue" if nm in blues else "neutral", "position": pos[nm]} for nm in names], key=lambda t: t["position"])
        co = [{"word": w, "number": len(m), "cat": c, "t": sorted(pos[x] for x in m),
               "explain": explain_for(w, c, cc, m)} for w, c, cc, m in b["clues"]]
        random.Random(_sd(("c", b["date"], b["pool"]))).shuffle(co)
        ho = [{"word": hints[nm][0], "number": 1, "cat": hints[nm][1], "t": [pos[nm]], "explain": hints[nm][2]} for nm in blues]
        random.Random(_sd(("h", b["date"], b["pool"]))).shuffle(ho)
        tj = "[" + ", ".join('{"name": %s, "colour": %s, "position": %d}' % (json.dumps(t["name"]), json.dumps(t["colour"]), t["position"]) for t in tiles) + "]"
        R.append("  (%s, %s,\n   %s::jsonb,\n   %s::jsonb,\n   %s::jsonb)" % (sq(b["date"]), sq(b["pool"]), sq(jarr(co)), sq(jarr(ho)), sq(tj)))
    L.append(",\n".join(R))
    L.append("on conflict (puzzle_date, pool) do update")
    L.append("  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;")
    open(f"{ROOT}/35_updates.sql", "w").write("\n".join(L) + "\n")
    print("wrote 35_updates.sql")
