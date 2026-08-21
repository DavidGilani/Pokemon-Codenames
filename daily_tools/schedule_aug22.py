#!/usr/bin/env python3
"""
Author (creativity-first) + verify + emit daily puzzles Aug 22..Aug 30 2026,
replacing the bland auto-generated ones. Clues are hand-written from the fact
bank; this tool only VERIFIES (all 5 anti-rep rules, mix/tier, letter rule,
type/gen spread, coverage) and ASSEMBLES (auto-hints from sprite features,
auto-safe neutrals, position/clue shuffles) then emits one SQL file.
"""
import csv, json, re, random, datetime
from collections import defaultdict
ROOT="/home/user/Pokemon-Codenames"
FACTS=json.load(open(f"{ROOT}/pokemon_facts.json"))
GEN1={n for n,r in FACTS.items() if r["gen"]==1}
random.seed(2208)

def norm(s): return re.sub(r'[^a-z]','',s.lower())
def shares3(a,b):
    a,b=norm(a),norm(b)
    for i in range(len(a)-2):
        if a[i:i+3] in b: return a[i:i+3]
    for i in range(len(b)-2):
        if b[i:i+3] in a: return b[i:i+3]
    return None
def days(a,b): return (datetime.date.fromisoformat(a)-datetime.date.fromisoformat(b)).days

# ---- corpus: real history <= Aug 20, PLUS the fresh Aug 21 boards (which replace
#      the old ones and count toward anti-rep for Aug 22+). ----
USES=defaultdict(list); BLUE_USED=defaultdict(list); CONCEPT=defaultdict(list)
rows=list(csv.DictReader(open("/root/.claude/uploads/eeb0f753-042d-524e-85cc-2ca2ce41ced3/31a19a47-daily_puzzles_rows.csv")))
for r in rows:
    if r['puzzle_date']>'2026-08-20': continue
    T={t['position']:t for t in json.loads(r['tiles'])}
    for t in T.values():
        if t['colour']=='blue': BLUE_USED[t['name']].append(r['puzzle_date'])
    for c in json.loads(r['clues']):
        USES[c['word']].append((r['puzzle_date'], frozenset(T[p]['name'] for p in c.get('t',[]))))
# fresh Aug 21 (word, [members], concept)
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

# ---- authored boards ----
# each board: (date, pool, tier, [ (word,cat,concept,[members]) ], exclude=[...])
B=[]
def board(date,pool,tier,clues,exclude=()): B.append(dict(date=date,pool=pool,tier=tier,clues=clues,exclude=list(exclude)))
exec(open(f"{ROOT}/daily_tools/boards_creative.py").read())

# ---- auto-hint: first sprite/arch/based word that passes the letter rule ----
def hint_for(nm, names, used):
    r=FACTS[nm]; cands=[]
    for s in r["sprite"]: cands.append((s.upper().replace(" ","-"),2))
    for a in r["arch"]: cands.append((a.upper(),3))
    for b in r["based_on"]:
        w=re.split(r"[\(/]",b)[0].strip().upper().replace(" ","-")
        if w: cands.append((w,3))
    cands.append(("TYPE-"+r["types"][0].upper(),1))
    for w,c in cands:
        if w in used: continue
        if any(shares3(w,x) for x in names): continue
        return w,c
    return None,None

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
for b in sorted(B,key=lambda x:(x["date"],x["pool"])):
    d,pool,where=b["date"],b["pool"],f'{b["date"]} {b["pool"]}'
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
    if label(cats)!=b["tier"]: errors.append(f'{where}: label {label(cats)}!=tier {b["tier"]}')
    cat2=sum(1 for c in cats if c==2)
    if b["tier"] in("Hard","Brutal") and cat2>1: errors.append(f"{where}: cat2={cat2}>1")
    if len(set(cats))<3 and b["tier"]!="Easy": errors.append(f"{where}: <3 distinct cats")
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
    # neutrals: ASCII well-known; exclude letter-clashers, the exclude list, and any
    # mon that shares a TYPE used by a type-clue or the COLOUR of a colour-clue (Rule 0).
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
    rng=random.Random(hash((d,pool))&0xffffffff); rng.shuffle(cand)
    neutrals=cand[:16]
    if len(neutrals)<16: errors.append(f"{where}: only {len(neutrals)} neutrals")
    names=blues+neutrals
    for w,c,cc,m in clues:
        for nm in names:
            f=shares3(w,nm)
            if f: errors.append(f"{where}: LETTER clue {w}~{nm}({f})")
    # hints
    hints={}; used=set()
    for nm in blues:
        hw,hc=hint_for(nm,names,used)
        if not hw: errors.append(f"{where}: no hint for {nm}"); continue
        hints[nm]=(hw,hc); used.add(hw)
    b.update(blues=blues,neutrals=neutrals,hints=hints); assembled.append(b)

print("=== VERIFY Aug22-30 ===")
if errors:
    for e in errors: print("  x",e)
    print(len(errors),"errors")
else:
    print("  ALL VALID —",len(assembled),"boards")
    def jarr(o):
        return "["+", ".join("{"+", ".join(['"word": '+json.dumps(x["word"]),'"number": %d'%x["number"],'"cat": %d'%x["cat"],'"t": ['+", ".join(map(str,x["t"]))+"]"])+"}" for x in o)+"]"
    def sq(s): return "'"+s.replace("'","''")+"'"
    L=["-- 30_updates.sql : creative daily puzzles 2026-08-22 .. 2026-08-30 (fact-bank authored).",
       "-- Replaces the earlier auto-generated boards for these dates.","",
       "insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values"]
    R=[]
    for b in assembled:
        blues,neutrals,hints=b["blues"],b["neutrals"],b["hints"]; names=blues+neutrals
        perm=list(range(25)); random.Random(hash(("p",b["date"],b["pool"]))&0xffffffff).shuffle(perm)
        pos={nm:perm[i] for i,nm in enumerate(names)}
        tiles=sorted([{"name":nm,"colour":"blue" if nm in blues else "neutral","position":pos[nm]} for nm in names],key=lambda t:t["position"])
        co=[{"word":w,"number":len(m),"cat":c,"t":sorted(pos[x] for x in m)} for w,c,cc,m in b["clues"]]
        random.Random(hash(("c",b["date"],b["pool"]))&0xffffffff).shuffle(co)
        ho=[{"word":hints[nm][0],"number":1,"cat":hints[nm][1],"t":[pos[nm]]} for nm in blues]
        random.Random(hash(("h",b["date"],b["pool"]))&0xffffffff).shuffle(ho)
        tj="["+", ".join('{"name": %s, "colour": %s, "position": %d}'%(json.dumps(t["name"]),json.dumps(t["colour"]),t["position"]) for t in tiles)+"]"
        R.append("  (%s, %s,\n   %s::jsonb,\n   %s::jsonb,\n   %s::jsonb)"%(sq(b["date"]),sq(b["pool"]),sq(jarr(co)),sq(jarr(ho)),sq(tj)))
    L.append(",\n".join(R))
    L.append("on conflict (puzzle_date, pool) do update")
    L.append("  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;")
    open(f"{ROOT}/30_updates.sql","w").write("\n".join(L)+"\n")
    print("wrote 30_updates.sql")
