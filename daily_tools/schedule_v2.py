#!/usr/bin/env python3
"""
Reschedule the upcoming dailies (2026-08-23 .. 2026-09-06) so each date's tier
matches its weekday (Mon Easy / Tue Medium / Wed Challenging / Thu Hard /
Fri Hard / Sat Brutal / Sun Evil), enforce the Brutal/Evil structural gate
(sum of clue numbers >= 11, <=1 single-tile clue), and re-check every anti-rep,
letter, spread, coverage and category rule. Corpus = real history <= Aug 20 +
the fresh Aug 21 + Aug 22 boards (Aug 22 already live & correct). Emits
32_updates.sql. Boards are read from daily_tools/boards_v2.py.
"""
import csv, json, re, random, datetime, hashlib
from collections import defaultdict
ROOT="/home/user/Pokemon-Codenames"
FACTS=json.load(open(f"{ROOT}/pokemon_facts.json"))
GEN1={n for n,r in FACTS.items() if r["gen"]==1}
random.seed(2026)
# Stable per-board seed (Python's hash() is salted per process, which made
# neutral fills — and thus the greedy hint search — non-reproducible run to run).
def _sd(x): return int(hashlib.md5(repr(x).encode()).hexdigest()[:8], 16)

WEEKDAY_TIER={0:"Easy",1:"Medium",2:"Challenging",3:"Hard",4:"Hard",5:"Brutal",6:"Evil"}
def tier_for(date): return WEEKDAY_TIER[datetime.date.fromisoformat(date).weekday()]
# Boards from EVO_FROM onward are re-authored under the evolution-family cap and
# re-emitted. Earlier dates are already played: kept as anti-rep corpus only.
EVO_FROM="2026-08-27"

def norm(s): return re.sub(r'[^a-z]','',s.lower())
def shares3(a,b):
    a,b=norm(a),norm(b)
    for i in range(len(a)-2):
        if a[i:i+3] in b: return a[i:i+3]
    for i in range(len(b)-2):
        if b[i:i+3] in a: return b[i:i+3]
    return None
def days(a,b): return (datetime.date.fromisoformat(a)-datetime.date.fromisoformat(b)).days

# ---- corpus dicts ----
USES=defaultdict(list); BLUE_USED=defaultdict(list); CONCEPT=defaultdict(list)
rows=list(csv.DictReader(open("/root/.claude/uploads/eeb0f753-042d-524e-85cc-2ca2ce41ced3/31a19a47-daily_puzzles_rows.csv")))
for r in rows:
    if r['puzzle_date']>'2026-08-20': continue
    T={t['position']:t for t in json.loads(r['tiles'])}
    for t in T.values():
        if t['colour']=='blue': BLUE_USED[t['name']].append(r['puzzle_date'])
    for c in json.loads(r['clues']):
        USES[c['word']].append((r['puzzle_date'], frozenset(T[p]['name'] for p in c.get('t',[]))))
AUG21=[
 ("2026-08-21",[("TEAM-ROCKET",["Arbok","Weezing"],"trainer:rocket"),("MONOTREME",["Psyduck","Golduck"],"arch:platypus"),
  ("VAMPIRE",["Zubat","Golbat"],"lore:vampire"),("PITCHER",["Bellsprout","Weepinbell"],"based:pitcher"),
  ("DOODLER",["Jigglypuff"],"lore:doodle")]),
 ("2026-08-21",[("PALINDROME",["Girafarig","Alomomola","Eevee"],"name:palindrome"),("ICE-CREAM",["Vanillite","Vanilluxe"],"based:icecream"),
  ("PENGUIN",["Piplup","Eiscue"],"arch:penguin"),("DRUMMER",["Rillaboom"],"lore:drummer"),("PUNK-ROCKER",["Toxtricity"],"lore:punk")]),
]
for d,cl in AUG21:
    for w,m,cc in cl:
        USES[w].append((d,frozenset(m))); CONCEPT[cc].append(d)
        for nm in m: BLUE_USED[nm].append(d)

# Corpus is history <= Aug 20 + Aug 21 only. Aug 22 onward is (re)authored in
# boards_v2.py and emitted, so today (Sat Aug 22) also gets the Brutal gate.
B=[]
def board(date,pool,tier,clues,exclude=()): B.append(dict(date=date,pool=pool,tier=tier,clues=clues,exclude=list(exclude)))
exec(open(f"{ROOT}/daily_tools/daily_common.py").read())  # explain_for
exec(open(f"{ROOT}/daily_tools/boards_v2.py").read())

def hint_for(nm, names, used):
    # Each candidate is (word, cat, explain). A hint points at ONE blue, so its
    # explanation names that Pokemon and says what the hint word refers to.
    # Word SELECTION is unchanged (first candidate that passes) — only the extra
    # explain string is new, shown on the finish screen under "clues you revealed".
    r=FACTS[nm]; cands=[]
    def sub(x): return x.replace("-"," ").lower()
    def art(x): return "an" if x[:1].lower() in "aeio" else "a"  # rough a/an (u->"a")
    for s in r["sprite"]:
        cands.append((s.upper().replace(" ","-"),2, f"Look for the {sub(s)} on {nm}'s sprite."))
    for a in r["arch"]:
        cands.append((a.upper(),3, f"{nm} is based on {art(sub(a))} {sub(a)}."))
    for b in r["based_on"]:
        for part in re.split(r"[\(/,]",b):
            w=part.strip().upper().replace(" ","-")
            if w: cands.append((w,3, f"{nm} is based on the {sub(w)}."))
    if r.get("genus"):
        cands.append((r["genus"].split()[0].upper(),2, f"{nm} is the {r['genus']}."))
    if r.get("color_primary"):
        cands.append((r["color_primary"].upper()+"-BODY",2, f"{nm} is mostly {r['color_primary'].lower()}."))
    for eg in r.get("egg",[]):
        cands.append((eg.upper()+"-EGG",3, f"{nm} is in the {sub(eg)} egg group."))
    for mv in r.get("moves",[]):
        cands.append((mv.upper().replace(" ","-"),3, f"{nm} is known for the move {sub(mv).title()}."))
    if r.get("habitat"):
        cands.append((r["habitat"].upper().replace(" ","-"),3, f"{nm} is found in the {sub(r['habitat'])}."))
    if r.get("color_secondary"):
        cands.append((r["color_secondary"].upper()+"-MARKS",2, f"{nm} has {r['color_secondary'].lower()} markings."))
    cands.append(("TYPE-"+r["types"][0].upper(),1, f"{nm} is a {r['types'][0].capitalize()}-type."))
    for w,c,ex in cands:
        if w in used: continue
        if any(shares3(w,x) for x in names): continue
        return w,c,ex
    return None,None,None

def evo_groups(clues):
    """Clues that group a Pokemon with its own evolution: >=2 members sharing an
    evolution family. Returns list of (word, family). The user cap: <=1 such
    group per board, <=3 across any rolling 7-day window (both pools)."""
    out=[]
    for w,c,cc,m in clues:
        byfam=defaultdict(list)
        for nm in m:
            if nm in FACTS: byfam[FACTS[nm]["family"]].append(nm)
        for f,mem in byfam.items():
            if len(mem)>=2: out.append((w,f))
    return out

def label(cats):
    highs=sum(1 for c in cats if c>=4); ones=sum(1 for c in cats if c==1)
    if highs>=4: return "Evil"
    if highs>=3: return "Brutal"
    if ones==0: return "Hard"
    if ones==1: return "Challenging"
    if ones==2: return "Medium"
    return "Easy"

errors=[]; assembled=[]
nb=defaultdict(list); nw=defaultdict(list); ng=defaultdict(list); nc=defaultdict(list)
evo_log=[]  # (date, word) for each evolution-family clue-group, for the 7-day cap
seen_dates=set()
for b in sorted(B,key=lambda x:(x["date"],x["pool"])):
    d,pool,where=b["date"],b["pool"],f'{b["date"]} {b["pool"]}'
    seen_dates.add((d,pool))
    poolset=GEN1 if pool=="gen1" else set(FACTS)
    clues=b["clues"]; blues=[]
    for w,c,cc,m in clues:
        for nm in m:
            if nm not in blues: blues.append(nm)
    for nm in blues:
        if nm not in FACTS: errors.append(f"{where}: {nm} not in facts")
        elif nm not in poolset: errors.append(f"{where}: {nm} not in {pool} pool")
    if len(blues)!=9: errors.append(f"{where}: {len(blues)} blues {blues}")
    cats=[c for w,c,cc,m in clues]
    # weekday tier
    want=tier_for(d)
    if b["tier"]!=want: errors.append(f"{where}: tier {b['tier']} != weekday {want}")
    if label(cats)!=b["tier"]: errors.append(f'{where}: label {label(cats)}!=tier {b["tier"]}')
    cat2=sum(1 for c in cats if c==2)
    if b["tier"] in("Hard","Brutal") and cat2>1: errors.append(f"{where}: cat2={cat2}>1")
    if b["tier"]=="Evil" and cat2>0: errors.append(f"{where}: Evil has cat2={cat2}")
    if len(set(cats))<3 and b["tier"]!="Easy": errors.append(f"{where}: <3 distinct cats")
    # A TYPE clue must cover EVERY blue of that type — otherwise its number is
    # a lie (e.g. STEEL x3 when 5 blues are Steel-type). Types are objective and
    # players count them, so this has to be exact. (Colour data is fuzzier, so
    # not enforced here.)
    if d>=EVO_FROM:  # only enforce on re-authored/emitted boards (past ones are grandfathered)
        for w,c,cc,m in clues:
            if cc.startswith("type:"):
                ty=cc.split(":",1)[1]
                allty=sorted(nm for nm in blues if ty in FACTS[nm]["types"])
                if sorted(m)!=allty:
                    errors.append(f"{where}: type clue {w} lists {sorted(m)} but every {ty}-type blue is {allty}")
    # Brutal/Evil structural gate
    if b["tier"] in("Brutal","Evil"):
        nums=[len(m) for w,c,cc,m in clues]
        if sum(nums)<11: errors.append(f"{where}: {b['tier']} sum {sum(nums)}<11")
        if sum(1 for n in nums if n==1)>1: errors.append(f"{where}: {b['tier']} >1 single-tile clue")
    # Evolution-family cap: <=1 clue per board may group a mon with its own
    # evolution line; <=3 such groups across any rolling 7-day window (both pools).
    # Dates before EVO_FROM predate the rule (already played) -- grandfathered:
    # kept as anti-rep corpus but not re-authored and not evo-checked/counted.
    eg=evo_groups(clues)
    if d>=EVO_FROM:
        if len(eg)>1:
            errors.append(f"{where}: {len(eg)} evolution-family clues (max 1) {eg}")
        for w,f in eg: evo_log.append((d,w))
        recent_evo=sum(1 for od,_ in evo_log if 0<=days(d,od)<7)
        if recent_evo>3:
            errors.append(f"{where}: {recent_evo} evolution-family clues in trailing 7d (max 3)")
    ptypes={FACTS[n]["types"][0] for n in blues}
    need=4 if pool=="gen1" else 5
    if len(ptypes)<need: errors.append(f"{where}: {len(ptypes)} types (<{need}) {sorted(ptypes)}")
    if pool=="mixed" and len({FACTS[n]["gen"] for n in blues})<3: errors.append(f"{where}: <3 gens")
    dt=d; cap=5 if pool=="gen1" else 10
    for w,c,cc,m in clues:
        grp=frozenset(m)
        for od,om in USES.get(w,[]):
            if 0<days(dt,od)<=7: errors.append(f"{where}: WORD '{w}' <7d ({od})")
            if 0<days(dt,od)<=14 and om==grp: errors.append(f"{where}: GROUP '{w}' <14d ({od})")
        for od in nw[w]:
            if 0<days(dt,od)<=7: errors.append(f"{where}: WORD '{w}' <7d (new {od})")
        for od in CONCEPT.get(cc,[])+nc[cc]:
            if 0<days(dt,od)<=5: errors.append(f"{where}: CONCEPT '{cc}' <5d ({od})")
        nw[w].append(d); ng[(w,grp)].append(d); nc[cc].append(d)
    for nm in blues:
        for od in BLUE_USED.get(nm,[])+nb[nm]:
            if 0<days(dt,od)<=cap: errors.append(f"{where}: BLUE '{nm}' <{cap}d ({od})")
        nb[nm].append(d)
    cluewords=[w for w,c,cc,m in clues]
    ban_types={cc.split(":")[1] for w,c,cc,m in clues if cc.startswith("type:")}
    ban_cols={cc.split(":")[1] for w,c,cc,m in clues if cc.startswith("colour:")}
    def ok_sem(nm):
        r=FACTS[nm]
        if ban_types & set(r["types"]): return False
        if r["color_primary"] in ban_cols: return False
        return True
    cand=[nm for nm in poolset if nm not in blues and nm not in set(b["exclude"])
          and nm.isascii() and FACTS[nm].get("wk",0)==1 and ok_sem(nm)
          and not any(shares3(w,nm) for w in cluewords)]
    cand=sorted(cand)  # set iteration is hash-salted; sort first for reproducibility
    rng=random.Random(_sd((d,pool))); rng.shuffle(cand)
    neutrals=cand[:16]
    if len(neutrals)<16: errors.append(f"{where}: only {len(neutrals)} neutrals")
    names=blues+neutrals
    for w,c,cc,m in clues:
        for nm in names:
            f=shares3(w,nm)
            if f: errors.append(f"{where}: LETTER clue {w}~{nm}({f})")
    hints={}; used=set()
    for nm in blues:
        hw,hc,he=hint_for(nm,names,used)
        if not hw: errors.append(f"{where}: no hint for {nm}"); continue
        hints[nm]=(hw,hc,he); used.add(hw)
    b.update(blues=blues,neutrals=neutrals,hints=hints); assembled.append(b)

# every date in the window must have both pools
start=datetime.date(2026,8,22); end=datetime.date(2026,9,6)
dd=start
while dd<=end:
    for pool in("gen1","mixed"):
        if (dd.isoformat(),pool) not in seen_dates:
            errors.append(f"MISSING {dd.isoformat()} {pool} ({tier_for(dd.isoformat())})")
    dd+=datetime.timedelta(days=1)

print("=== VERIFY reschedule Aug23-Sep06 ===")
if errors:
    for e in errors: print("  x",e)
    print(len(errors),"errors")
else:
    print("  ALL VALID —",len(assembled),"boards")
    def jarr(o):
        parts=[]
        for x in o:
            fields=['"word": '+json.dumps(x["word"]),'"number": %d'%x["number"],
                    '"cat": %d'%x["cat"],'"t": ['+", ".join(map(str,x["t"]))+"]"]
            if x.get("explain"): fields.append('"explain": '+json.dumps(x["explain"]))
            parts.append("{"+", ".join(fields)+"}")
        return "["+", ".join(parts)+"]"
    def sq(s): return "'"+s.replace("'","''")+"'"
    L=["-- 33_updates.sql : re-author dailies 2026-08-27 .. 2026-09-06 under the new",
       "-- evolution-family cap (<=1 evo-pair clue per board, <=3 per rolling 7 days)",
       "-- -- most boards now group blues by cross-family handles, not evo lines.",
       "-- Weekday difficulty and Brutal/Evil overlap gate unchanged. Supersedes",
       "-- 32_updates for these dates; Aug 22-26 (already played) are left as-is.","",
       "insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values"]
    R=[]
    for b in assembled:
        if b["date"]<EVO_FROM: continue  # already played; not re-emitted
        blues,neutrals,hints=b["blues"],b["neutrals"],b["hints"]; names=blues+neutrals
        perm=list(range(25)); random.Random(_sd(("p",b["date"],b["pool"]))).shuffle(perm)
        pos={nm:perm[i] for i,nm in enumerate(names)}
        tiles=sorted([{"name":nm,"colour":"blue" if nm in blues else "neutral","position":pos[nm]} for nm in names],key=lambda t:t["position"])
        co=[{"word":w,"number":len(m),"cat":c,"t":sorted(pos[x] for x in m),
             "explain":explain_for(w,c,cc,m)} for w,c,cc,m in b["clues"]]
        random.Random(_sd(("c",b["date"],b["pool"]))).shuffle(co)
        ho=[{"word":hints[nm][0],"number":1,"cat":hints[nm][1],"t":[pos[nm]],"explain":hints[nm][2]} for nm in blues]
        random.Random(_sd(("h",b["date"],b["pool"]))).shuffle(ho)
        tj="["+", ".join('{"name": %s, "colour": %s, "position": %d}'%(json.dumps(t["name"]),json.dumps(t["colour"]),t["position"]) for t in tiles)+"]"
        R.append("  (%s, %s,\n   %s::jsonb,\n   %s::jsonb,\n   %s::jsonb)"%(sq(b["date"]),sq(b["pool"]),sq(jarr(co)),sq(jarr(ho)),sq(tj)))
    L.append(",\n".join(R))
    L.append("on conflict (puzzle_date, pool) do update")
    L.append("  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;")
    open(f"{ROOT}/33_updates.sql","w").write("\n".join(L)+"\n")
    print("wrote 33_updates.sql")
