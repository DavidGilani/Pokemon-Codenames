#!/usr/bin/env python3
"""
EXPERIMENT: draw the 9 blues for a board completely at random from the pool,
then try to auto-discover shared attributes (type/arch/based_on/egg/habitat/
color/genus/legendary) that cover all 9 in <=5 clue-groups, obeying the
tier's category-mix rules. If a random draw can't be covered, redraw and
try again. This is the alternative to hand-authoring blues around clue
ideas -- see boards_v2.py's approach for comparison.

Targets 2026-08-27 (Thursday -> Hard) for both pools, checked against the
same anti-rep/letter/spread rules as schedule_v2.py, using the *rest* of
32_updates.sql's Aug22-Sep6 boards (everything except the old Aug27 board)
as the "recent" corpus so this genuinely slots into the live schedule.
"""
import csv, json, re, random, datetime, itertools
from collections import defaultdict
ROOT="/home/user/Pokemon-Codenames"
FACTS=json.load(open(f"{ROOT}/pokemon_facts.json"))
GEN1={n for n,r in FACTS.items() if r["gen"]==1}
import sys
TARGET_DATE=sys.argv[1] if len(sys.argv)>1 else "2026-08-27"
TIER=sys.argv[2] if len(sys.argv)>2 else "Hard"
REPLACED_DATES={TARGET_DATE}

def norm(s): return re.sub(r'[^a-z]','',s.lower())
def shares3(a,b):
    a,b=norm(a),norm(b)
    for i in range(len(a)-2):
        if a[i:i+3] in b: return a[i:i+3]
    for i in range(len(b)-2):
        if b[i:i+3] in a: return b[i:i+3]
    return None
def days(a,b): return (datetime.date.fromisoformat(a)-datetime.date.fromisoformat(b)).days

# ---- corpus: real history <=Aug20 + Aug21 + all of boards_v2.py EXCEPT the
# Aug27 board (which this script is replacing) ----
USES=defaultdict(list); BLUE_USED=defaultdict(list); CONCEPT=defaultdict(list)
rows=list(csv.DictReader(open("/root/.claude/uploads/eeb0f753-042d-524e-85cc-2ca2ce41ced3/31a19a47-daily_puzzles_rows.csv")))
for r in rows:
    if r['puzzle_date']>'2026-08-20': continue
    T={t['position']:t for t in json.loads(r['tiles'])}
    for t in T.values():
        if t['colour']=='blue': BLUE_USED[t['name']].append(r['puzzle_date'])
    for c in json.loads(r['clues']):
        USES[c['word']].append((r['puzzle_date'], frozenset(T[p]['name'] for p in c.get('t',[]))))

B=[]
def board(date,pool,tier,clues,exclude=()): B.append(dict(date=date,pool=pool,tier=tier,clues=clues,exclude=list(exclude)))
exec(open(f"{ROOT}/daily_tools/daily_common.py").read())
exec(open(f"{ROOT}/daily_tools/boards_v2.py").read())
for b in B:
    if b["date"] in REPLACED_DATES: continue  # being replaced
    for w,c,cc,m in b["clues"]:
        USES[w].append((b["date"], frozenset(m))); CONCEPT[cc].append(b["date"])
        for nm in m: BLUE_USED[nm].append(b["date"])

# 33_updates.sql already replaced 2026-08-27 with a fresh random-draw board;
# fold those words/concepts/blues into the corpus (they're live/about-to-be-live)
# even though boards_v2.py still has the old text for that date.
EXTRA_27=[
 ("2026-08-27",[("BIRD",["Dodrio","Farfetch'd","Moltres","Zapdos"],"arch:bird"),
  ("RED",["Charizard","Seaking"],"colour:red"),
  ("GROUND",["Arbok","Farfetch'd","Raticate"],"egg:ground"),
  ("GRASSLAND",["Arbok","Dodrio","Farfetch'd","Ivysaur","Raticate"],"habitat:grassland")]),
 ("2026-08-27",[("BLUE",["Beldum","Grapploct","Mareanie"],"colour:blue"),
  ("NO-EGGS",["Igglybuff","Ogerpon","Solgaleo"],"egg:no-eggs"),
  ("GROUND",["Mienshao","Skiddo"],"egg:ground"),
  ("MINERAL",["Beldum","Vanilluxe"],"arch:mineral")]),
]
if TARGET_DATE!="2026-08-27":
    for d,cl in EXTRA_27:
        for w,m,cc in cl:
            USES[w].append((d,frozenset(m))); CONCEPT[cc].append(d)
            for nm in m: BLUE_USED[nm].append(d)

def label(cats):
    highs=sum(1 for c in cats if c>=4); ones=sum(1 for c in cats if c==1)
    if highs>=4: return "Evil"
    if highs>=3: return "Brutal"
    if ones==0: return "Hard"
    if ones==1: return "Challenging"
    if ones==2: return "Medium"
    return "Easy"

# attribute-key -> (fetch function returning list of values, base cat)
def attrs(nm):
    r=FACTS[nm]; out=[]
    for t in r["types"]: out.append((f"type:{t}", t.upper(), 1))
    if r.get("legendary") or r.get("mythical"): out.append(("group:legendary","LEGENDARY",1))
    for a in r.get("arch",[]): out.append((f"arch:{a}", a.upper(), 3))
    for bo in r.get("based_on",[]):
        for part in re.split(r"[\(/,+]",bo):
            w=part.strip().strip("()").strip()
            if w and len(w)>=3: out.append((f"based:{w.lower()}", w.upper().replace(" ","-"), 4))
    for eg in r.get("egg",[]): out.append((f"egg:{eg}", eg.upper(), 5))
    if r.get("habitat"): out.append((f"habitat:{r['habitat']}", r["habitat"].upper().replace(" ","-"), 4))
    if r.get("color_primary"): out.append((f"colour:{r['color_primary']}", r["color_primary"].upper(), 2))
    if r.get("genus"): out.append((f"genus:{r['genus']}", r["genus"].split()[0].upper(), 2))
    return out

def try_cover(blues, pool):
    # concept-key -> members among blues
    by_key=defaultdict(list)
    for nm in blues:
        for key,word,cat in attrs(nm):
            by_key[key].append(nm)
    groups=[]
    for key,members in by_key.items():
        _,word,cat=next(x for x in attrs(members[0]) if x[0]==key)
        # single-member clues waste a slot for most categories, but a lone
        # type/legendary (cat1) anchor clue is a normal, valid single-tile clue
        if len(members)<2 and cat!=1: continue
        groups.append((key,word,cat,tuple(sorted(set(members)))))
    groups.sort(key=lambda g:-len(g[3]))
    groups=groups[:14]  # bound the combinations search (itertools blows up otherwise)
    best=None
    seen_group_sets=set()
    for combo_size in (3,4,5):
        for combo in itertools.combinations(groups, combo_size):
            covered=set()
            for _,_,_,m in combo: covered.update(m)
            if covered!=set(blues): continue
            # no blue double-counted more than needed; allow overlap (that's fine/good)
            cats=[c for _,_,c,_ in combo]
            ones=sum(1 for c in cats if c==1); twos=sum(1 for c in cats if c==2)
            threes=sum(1 for c in cats if c==3); highs=sum(1 for c in cats if c>=4)
            if TIER=="Hard":
                if ones!=0 or twos>1 or highs!=2 or threes<1 or len(set(cats))<3: continue
            elif TIER=="Challenging":
                if ones!=1 or not(1<=twos<=2) or threes<2 or highs>1 or len(set(cats))<3: continue
            elif TIER=="Medium":
                if ones!=2 or len(set(cats))<3: continue
            key_sig=frozenset(k for k,_,_,_ in combo)
            if key_sig in seen_group_sets: continue
            seen_group_sets.add(key_sig)
            best=combo
            return best
    return None

def build_clues(combo):
    out=[]
    for key,word,cat,members in combo:
        out.append((word,cat,key,list(members)))
    return out

def ok_sem_neutral(nm, ban_keys, blues, exclude_set):
    if nm in blues or nm in exclude_set: return False
    if not nm.isascii(): return False
    if FACTS[nm].get("wk",0)!=1: return False
    for key,_,_ in attrs(nm):
        if key in ban_keys: return False
    return True

def try_board(pool, seed):
    rng=random.Random(seed)
    poolset=list(GEN1) if pool=="gen1" else list(FACTS)
    dt=TARGET_DATE; cap=5 if pool=="gen1" else 10
    eligible=[nm for nm in poolset if nm.isascii() and FACTS[nm].get("wk",0)==1
              and not any(0<abs(days(dt,od))<=cap for od in BLUE_USED.get(nm,[]))]
    if len(eligible)<9: return None
    blues=rng.sample(eligible,9)
    fams=[FACTS[n]["family"] for n in blues]
    if len(set(fams))<len(fams): return None  # no two blues from the same evolution line
    ptypes={FACTS[n]["types"][0] for n in blues}
    need=4 if pool=="gen1" else 5
    if len(ptypes)<need: return None
    if pool=="mixed" and len({FACTS[n]["gen"] for n in blues})<3: return None
    combo=try_cover(blues,pool)
    if not combo: return None
    clues=build_clues(combo)
    # anti-rep on words/groups/concepts
    for w,c,cc,m in clues:
        grp=frozenset(m)
        for od,om in USES.get(w,[]):
            if 0<abs(days(dt,od))<=7: return None
            if 0<abs(days(dt,od))<=14 and om==grp: return None
        for od in CONCEPT.get(cc,[]):
            if 0<abs(days(dt,od))<=5: return None
    # letter rule vs blues+clue words themselves
    cluewords=[w for w,c,cc,m in clues]
    for i,w in enumerate(cluewords):
        for nm in blues:
            if shares3(w,nm): return None
        for w2 in cluewords:
            if w2!=w and shares3(w,w2): return None
    ban_keys={cc for w,c,cc,m in clues}
    cand=[nm for nm in poolset if ok_sem_neutral(nm,ban_keys,blues,set())
          and not any(shares3(w,nm) for w in cluewords)]
    rng.shuffle(cand)
    neutrals=cand[:16]
    if len(neutrals)<16: return None
    names=blues+neutrals
    for w,c,cc,m in clues:
        for nm in names:
            if shares3(w,nm): return None
    return dict(blues=blues,neutrals=neutrals,clues=clues)

def hint_for(nm, names, used):
    r=FACTS[nm]; cands=[]
    for s in r["sprite"]: cands.append((s.upper().replace(" ","-"),2))
    for a in r["arch"]: cands.append((a.upper(),3))
    for b in r["based_on"]:
        for part in re.split(r"[\(/,+]",b):
            w=part.strip().strip("()").strip().upper().replace(" ","-")
            if w: cands.append((w,3))
    if r.get("genus"): cands.append((r["genus"].split()[0].upper(),2))
    if r.get("color_primary"): cands.append((r["color_primary"].upper(),2))
    for eg in r.get("egg",[]): cands.append((eg.upper(),3))
    for mv in r.get("moves",[]): cands.append((mv.upper().replace(" ","-"),3))
    if r.get("habitat"): cands.append((r["habitat"].upper().replace(" ","-"),3))
    if r.get("color_secondary"): cands.append((r["color_secondary"].upper()+"-MARKS",2))
    cands.append(("TYPE-"+r["types"][0].upper(),1))
    for w,c in cands:
        if w in used: continue
        if any(shares3(w,x) for x in names): continue
        return w,c
    return None,None

RESULTS={}
for pool in ("gen1","mixed"):
    found=None
    for attempt in range(200000):
        r=try_board(pool, attempt*7919+1)
        if r: found=r; break
    print(pool, "->", "FOUND after %d attempts"%attempt if found else "NOT FOUND in 20000 draws")
    if found:
        print("  blues:", found["blues"])
        for w,c,cc,m in found["clues"]:
            print(f"    {w} (cat{c}, {cc}): {m}")
        names=found["blues"]+found["neutrals"]; used=set(w for w,c,cc,m in found["clues"])
        hints={}
        for nm in found["blues"]:
            hw,hc=hint_for(nm,names,used)
            if not hw:
                print("  ! no hint for",nm); found=None; break
            hints[nm]=(hw,hc); used.add(hw)
        if found:
            found["hints"]=hints
            RESULTS[pool]=found

if len(RESULTS)==2:
    def jarr(o):
        parts=[]
        for x in o:
            fields=['"word": '+json.dumps(x["word"]),'"number": %d'%x["number"],
                    '"cat": %d'%x["cat"],'"t": ['+", ".join(map(str,x["t"]))+"]"]
            if x.get("explain"): fields.append('"explain": '+json.dumps(x["explain"]))
            parts.append("{"+", ".join(fields)+"}")
        return "["+", ".join(parts)+"]"
    def sq(s): return "'"+s.replace("'","''")+"'"
    L=[f"-- replace {TARGET_DATE} ({TIER}) with boards generated by TRUE random draw of",
       "-- the 9 blues, then auto-discovered shared attributes (type/arch/based-on/",
       "-- egg-group/habitat/colour) covering all 9 in <=5 clean single-word clues.",
       "-- Random draw excludes any two blues sharing an evolution family. Supersedes",
       "-- the previous board for this date.","",
       "insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values"]
    R=[]
    for pool,found in RESULTS.items():
        blues,neutrals,hints=found["blues"],found["neutrals"],found["hints"]; names=blues+neutrals
        rng=random.Random(hash(("p",TARGET_DATE,pool))&0xffffffff)
        perm=list(range(25)); rng.shuffle(perm)
        pos={nm:perm[i] for i,nm in enumerate(names)}
        tiles=sorted([{"name":nm,"colour":"blue" if nm in blues else "neutral","position":pos[nm]} for nm in names],key=lambda t:t["position"])
        co=[{"word":w,"number":len(m),"cat":c,"t":sorted(pos[x] for x in m),
             "explain":explain_for(w,c,cc,m)} for w,c,cc,m in found["clues"]]
        random.Random(hash(("c",TARGET_DATE,pool))&0xffffffff).shuffle(co)
        ho=[{"word":hints[nm][0],"number":1,"cat":hints[nm][1],"t":[pos[nm]]} for nm in blues]
        random.Random(hash(("h",TARGET_DATE,pool))&0xffffffff).shuffle(ho)
        tj="["+", ".join('{"name": %s, "colour": %s, "position": %d}'%(json.dumps(t["name"]),json.dumps(t["colour"]),t["position"]) for t in tiles)+"]"
        R.append("  (%s, %s,\n   %s::jsonb,\n   %s::jsonb,\n   %s::jsonb)"%(sq(TARGET_DATE),sq(pool),sq(jarr(co)),sq(jarr(ho)),sq(tj)))
    L.append(",\n".join(R))
    L.append("on conflict (puzzle_date, pool) do update")
    L.append("  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;")
    outname=f"33_updates_{TARGET_DATE}.sql"
    open(f"{ROOT}/{outname}","w").write("\n".join(L)+"\n")
    print("wrote",outname)
else:
    print("MISSING pools, not writing SQL:", set(("gen1","mixed"))-set(RESULTS))
