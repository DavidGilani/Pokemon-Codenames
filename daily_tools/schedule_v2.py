#!/usr/bin/env python3
"""
Canonical daily-puzzle verifier + SQL emitter.

Self-contained and reproducible in a FRESH CHECKOUT (this is the file the
nightly maintainer runs). It:

  * auto-detects the repo root from its own location, so it runs the same in a
    normal clone or in the nightly clone dir;
  * loads the anti-repetition corpus from daily_tools/live_boards.json -- the
    committed mirror of every board currently live in Supabase (refresh it
    FIRST; the nightly workflow does). No session-specific CSV / scratchpad
    paths;
  * computes its gap window from *today* (today .. today+GAP_DAYS), not a
    hard-coded date range;
  * reads hand-authored boards from daily_tools/boards_v2.py, SKIPS any
    (date,pool) that already exists live (those are the DB's job, not ours),
    and verifies + emits ONLY genuinely-new boards.

Author new boards by adding board(...) calls to boards_v2.py, then run:
    python3 daily_tools/schedule_v2.py
until it prints ALL VALID. On success, new-board upserts are written to
daily_tools/pending_upserts.sql (nothing is written when there are no new
boards -- a clean checkout with everything already live prints "0 new boards").

Rules mirrored here are the ones in daily_puzzle_notes.md / CLAUDE.md.
"""
import os, json, re, random, datetime, hashlib
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAP_DAYS = 21                      # ensure both pools exist for [today, today+21]
TODAY = datetime.date.today()

FACTS = json.load(open(f"{ROOT}/pokemon_facts.json"))
GEN1 = {n for n, r in FACTS.items() if r["gen"] == 1}
random.seed(2026)

# Stable per-board seed (Python's hash() is salted per process).
def _sd(x): return int(hashlib.md5(repr(x).encode()).hexdigest()[:8], 16)

WEEKDAY_TIER = {0:"Easy",1:"Medium",2:"Challenging",3:"Hard",4:"Hard",5:"Brutal",6:"Evil"}
def tier_for(date): return WEEKDAY_TIER[datetime.date.fromisoformat(date).weekday()]

# QA "human-flourish" whitelist: (date,pool) the owner has signed off on despite
# missing a soft structural gate (distinct-cats / Brutal-Evil sum). AI-generated
# boards must still pass every rule; entries here are manual QA overrides only.
# (Already-live boards are skipped before verification anyway, so this only
# matters for a NEW board the owner is hand-authoring with an override.)
FLOURISH = set()

def norm(s): return re.sub(r'[^a-z]','',s.lower())
def shares3(a,b):
    a,b=norm(a),norm(b)
    for i in range(len(a)-2):
        if a[i:i+3] in b: return a[i:i+3]
    for i in range(len(b)-2):
        if b[i:i+3] in a: return b[i:i+3]
    return None
def days(a,b): return (datetime.date.fromisoformat(a)-datetime.date.fromisoformat(b)).days

# ---- anti-rep corpus (from the committed live snapshot) ----
# live_boards.json rows: {date, pool, clues:[{word, n, cat, m:[blue names]}]}.
# blues of a board = union of every clue's members (m). That's all the anti-rep
# checks need (word/group recency, blue frequency, evolution-family window).
try:
    LIVE = json.load(open(f"{ROOT}/daily_tools/live_boards.json"))
except FileNotFoundError:
    LIVE = []
USES = defaultdict(list)        # word -> [(date, frozenset(members))]
BLUE_USED = defaultdict(list)   # name -> [date]
EVO_HIST = []                   # (date, word) evolution-family clue-groups in corpus
LIVE_DATES = set()              # (date, pool) already live -- never re-emitted
for row in LIVE:
    d = row["date"]; LIVE_DATES.add((d, row["pool"]))
    board_blues = set()
    for c in (row.get("clues") or []):
        m = c.get("m") or []
        grp = frozenset(m)
        USES[c["word"]].append((d, grp))
        board_blues.update(m)
        byfam = defaultdict(list)
        for nm in m:
            if nm in FACTS: byfam[FACTS[nm]["family"]].append(nm)
        for fam, mem in byfam.items():
            if len(mem) >= 2: EVO_HIST.append((d, c["word"]))
    for nm in board_blues:
        BLUE_USED[nm].append(d)

# ---- hand-authored boards ----
B = []
def board(date,pool,tier,clues,exclude=()): B.append(dict(date=date,pool=pool,tier=tier,clues=clues,exclude=list(exclude)))
exec(open(f"{ROOT}/daily_tools/daily_common.py").read())  # explain_for
exec(open(f"{ROOT}/daily_tools/boards_v2.py").read())

def hint_for(nm, names, used):
    r=FACTS[nm]; cands=[]
    def sub(x): return x.replace("-"," ").lower()
    def art(x): return "an" if x[:1].lower() in "aeiou" else "a"
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
    out=[]
    for w,c,cc,m,*_x in clues:
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

errors=[]; assembled=[]; skipped_live=0
nb=defaultdict(list); nw=defaultdict(list); nc_evo=[]  # new-board accumulators
authored_dates=set()

for b in sorted(B,key=lambda x:(x["date"],x["pool"])):
    d,pool,where=b["date"],b["pool"],f'{b["date"]} {b["pool"]}'
    # Already live? The DB owns it; leave it be. (Keeps stale historical entries
    # in boards_v2.py from being re-verified/re-emitted.)
    if (d,pool) in LIVE_DATES:
        skipped_live+=1
        continue
    authored_dates.add((d,pool))
    poolset=GEN1 if pool=="gen1" else set(FACTS)
    clues=b["clues"]; blues=[]
    for w,c,cc,m,*_x in clues:
        for nm in m:
            if nm not in blues: blues.append(nm)
    for nm in blues:
        if nm not in FACTS: errors.append(f"{where}: {nm} not in facts")
        elif nm not in poolset: errors.append(f"{where}: {nm} not in {pool} pool")
    if len(blues)!=9: errors.append(f"{where}: {len(blues)} blues {blues}")
    cats=[c for w,c,cc,m,*_x in clues]
    want=tier_for(d)
    if b["tier"]!=want: errors.append(f"{where}: tier {b['tier']} != weekday {want}")
    if label(cats)!=b["tier"]: errors.append(f'{where}: label {label(cats)}!=tier {b["tier"]}')
    cat2=sum(1 for c in cats if c==2)
    if b["tier"] in("Hard","Brutal") and cat2>1: errors.append(f"{where}: cat2={cat2}>1")
    if b["tier"]=="Evil" and cat2>0: errors.append(f"{where}: Evil has cat2={cat2}")
    if len(set(cats))<3 and b["tier"]!="Easy" and (d,pool) not in FLOURISH: errors.append(f"{where}: <3 distinct cats")
    if not (1<=len(clues)<=5): errors.append(f"{where}: {len(clues)} clues (must be 1-5)")
    for w,c,cc,m,*_x in clues:
        if cc.startswith("type:"):
            ty=cc.split(":",1)[1]
            allty=sorted(nm for nm in blues if ty in FACTS[nm]["types"])
            if sorted(m)!=allty:
                errors.append(f"{where}: type clue {w} lists {sorted(m)} but every {ty}-type blue is {allty}")
    sets=[(w,frozenset(m)) for w,c,cc,m,*_x in clues]
    for i,(wi,si) in enumerate(sets):
        for j,(wj,sj) in enumerate(sets):
            if i==j or not si: continue
            if si<sj or (si==sj and i<j):
                errors.append(f"{where}: clue {wi} {sorted(si)} is contained in {wj} {sorted(sj)} (redundant split)")
    if b["tier"] in("Brutal","Evil") and (d,pool) not in FLOURISH:
        nums=[len(m) for w,c,cc,m,*_x in clues]
        if sum(nums)<11: errors.append(f"{where}: {b['tier']} sum {sum(nums)}<11")
        if sum(1 for n in nums if n==1)>1: errors.append(f"{where}: {b['tier']} >1 single-tile clue")
    # Evolution-family cap: <=1 per board, <=3 across any rolling 7-day window
    # (both the live corpus around it and other new boards this run).
    eg=evo_groups(clues)
    if len(eg)>1: errors.append(f"{where}: {len(eg)} evolution-family clues (max 1) {eg}")
    if eg:
        recent_evo=sum(1 for od,_ in (EVO_HIST+nc_evo) if 0<abs(days(d,od))<=7)+len(eg)
        if recent_evo>3: errors.append(f"{where}: {recent_evo} evolution-family clues in trailing/leading 7d (max 3)")
    for w,f in eg: nc_evo.append((d,w))
    ptypes={FACTS[n]["types"][0] for n in blues}
    need=4 if pool=="gen1" else 5
    if len(ptypes)<need: errors.append(f"{where}: {len(ptypes)} types (<{need}) {sorted(ptypes)}")
    if pool=="mixed" and len({FACTS[n]["gen"] for n in blues})<3: errors.append(f"{where}: <3 gens")
    cap=5 if pool=="gen1" else 10
    for w,c,cc,m,*_x in clues:
        grp=frozenset(m)
        for od,om in USES.get(w,[])+nw[w]:
            if 0<abs(days(d,od))<=7: errors.append(f"{where}: WORD '{w}' within 7d of {od}")
            if 0<abs(days(d,od))<=14 and om==grp: errors.append(f"{where}: GROUP '{w}' within 14d of {od}")
        nw[w].append((d,grp))
    for nm in blues:
        for od in BLUE_USED.get(nm,[])+nb[nm]:
            if 0<abs(days(d,od))<=cap: errors.append(f"{where}: BLUE '{nm}' within {cap}d of {od}")
        nb[nm].append(d)
    cluewords=[w for w,c,cc,m,*_x in clues]
    ban_types={cc.split(":")[1] for w,c,cc,m,*_x in clues if cc.startswith("type:")}
    ban_cols={cc.split(":")[1] for w,c,cc,m,*_x in clues if cc.startswith("colour:")}
    def ok_sem(nm):
        r=FACTS[nm]
        if ban_types & set(r["types"]): return False
        if r["color_primary"] in ban_cols: return False
        return True
    cand=[nm for nm in poolset if nm not in blues and nm not in set(b["exclude"])
          and nm.isascii() and FACTS[nm].get("wk",0)==1 and ok_sem(nm)
          and not any(shares3(w,nm) for w in cluewords)]
    cand=sorted(cand)
    rng=random.Random(_sd((d,pool))); rng.shuffle(cand)
    neutrals=cand[:16]
    if len(neutrals)<16: errors.append(f"{where}: only {len(neutrals)} neutrals")
    names=blues+neutrals
    for w,c,cc,m,*_x in clues:
        for nm in names:
            f=shares3(w,nm)
            if f: errors.append(f"{where}: LETTER clue {w}~{nm}({f})")
    hints={}; used=set()
    for nm in blues:
        hw,hc,he=hint_for(nm,names,used)
        if not hw: errors.append(f"{where}: no hint for {nm}"); continue
        hints[nm]=(hw,hc,he); used.add(hw)
    b.update(blues=blues,neutrals=neutrals,hints=hints); assembled.append(b)

# Gap check: every day in [today, today+GAP_DAYS] needs BOTH pools, covered
# either by the live corpus or by a newly-authored board this run.
covered=set(LIVE_DATES)|authored_dates
missing=[]
for i in range(GAP_DAYS+1):
    dd=(TODAY+datetime.timedelta(days=i)).isoformat()
    for pool in("gen1","mixed"):
        if (dd,pool) not in covered: missing.append(f"{dd} {pool} ({tier_for(dd)})")

print(f"=== VERIFY dailies (today={TODAY}, window +{GAP_DAYS}d) ===")
print(f"  corpus: {len(LIVE)} live boards | authored this run: {len(assembled)} new, {skipped_live} already-live skipped")
if missing:
    print(f"  {len(missing)} GAP(S) with no board yet:")
    for m in missing: print("   -",m)
if errors:
    for e in errors: print("  x",e)
    print(len(errors),"errors")
elif not assembled:
    print("  ALL VALID - 0 new boards to emit" + (" (gaps above need authoring in boards_v2.py)" if missing else "; pipeline full"))
else:
    print("  ALL VALID -",len(assembled),"new board(s)")
    def jarr(o):
        parts=[]
        for x in o:
            fields=['"word": '+json.dumps(x["word"]),'"number": %d'%x["number"],
                    '"cat": %d'%x["cat"],'"t": ['+", ".join(map(str,x["t"]))+"]"]
            if x.get("explain"): fields.append('"explain": '+json.dumps(x["explain"]))
            parts.append("{"+", ".join(fields)+"}")
        return "["+", ".join(parts)+"]"
    def sq(s): return "'"+s.replace("'","''")+"'"
    L=["-- pending_upserts.sql : NEW daily boards emitted by schedule_v2.py.",
       f"-- Generated {TODAY} for dates not yet live in Supabase.",
       "-- Apply via the base64 do-block pattern (keeps the JSON exact), or run",
       "-- directly. Weekday tier + Brutal/Evil overlap gate enforced.","",
       "insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values"]
    R=[]
    for b in assembled:
        blues,neutrals,hints=b["blues"],b["neutrals"],b["hints"]; names=blues+neutrals
        perm=list(range(25)); random.Random(_sd(("p",b["date"],b["pool"]))).shuffle(perm)
        pos={nm:perm[i] for i,nm in enumerate(names)}
        tiles=sorted([{"name":nm,"colour":"blue" if nm in blues else "neutral","position":pos[nm]} for nm in names],key=lambda t:t["position"])
        co=[{"word":w,"number":len(m),"cat":c,"t":sorted(pos[x] for x in m),
             "explain":(_x[0] if _x else explain_for(w,c,cc,m))} for w,c,cc,m,*_x in b["clues"]]
        random.Random(_sd(("c",b["date"],b["pool"]))).shuffle(co)
        ho=[{"word":hints[nm][0],"number":1,"cat":hints[nm][1],"t":[pos[nm]],"explain":hints[nm][2]} for nm in blues]
        random.Random(_sd(("h",b["date"],b["pool"]))).shuffle(ho)
        tj="["+", ".join('{"name": %s, "colour": %s, "position": %d}'%(json.dumps(t["name"]),json.dumps(t["colour"]),t["position"]) for t in tiles)+"]"
        R.append("  (%s, %s,\n   %s::jsonb,\n   %s::jsonb,\n   %s::jsonb)"%(sq(b["date"]),sq(b["pool"]),sq(jarr(co)),sq(jarr(ho)),sq(tj)))
    L.append(",\n".join(R))
    L.append("on conflict (puzzle_date, pool) do update")
    L.append("  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;")
    open(f"{ROOT}/daily_tools/pending_upserts.sql","w").write("\n".join(L)+"\n")
    print("  wrote daily_tools/pending_upserts.sql")
