#!/usr/bin/env python3
"""
Author (creativity-first) + verify + emit daily puzzles 2026-08-31 .. 2026-09-06.
Corpus for anti-repetition = real history <= Aug 20, the fresh Aug 21 boards,
AND the Aug 22-30 boards (daily_tools/boards_creative.py). New boards are read
from daily_tools/boards_sep.py. Emits 31_updates.sql.
"""
import csv, json, re, random, datetime
from collections import defaultdict
ROOT="/home/user/Pokemon-Codenames"
FACTS=json.load(open(f"{ROOT}/pokemon_facts.json"))
GEN1={n for n,r in FACTS.items() if r["gen"]==1}
random.seed(3109)

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
# fresh Aug 21
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

# ---- fold in Aug 22-30 boards as corpus ----
B=[]
def board(date,pool,tier,clues,exclude=()): B.append(dict(date=date,pool=pool,tier=tier,clues=clues,exclude=list(exclude)))
exec(open(f"{ROOT}/daily_tools/boards_creative.py").read())
for b in B:
    for w,c,cc,m in b["clues"]:
        USES[w].append((b["date"],frozenset(m))); CONCEPT[cc].append(b["date"])
        for nm in m: BLUE_USED[nm].append(b["date"])
B=[]  # reset; now load the new week

# ---- authored boards for the new week ----
exec(open(f"{ROOT}/daily_tools/boards_sep.py").read())

# ---- auto-hint: first sprite/arch/based word that passes the letter rule ----
def hint_for(nm, names, used):
    r=FACTS[nm]; cands=[]
    for s in r["sprite"]: cands.append((s.upper().replace(" ","-"),2))
    for a in r["arch"]: cands.append((a.upper(),3))
    for b in r["based_on"]:
        for part in re.split(r"[\(/,]",b):
            w=part.strip().upper().replace(" ","-")
            if w: cands.append((w,3))
    # fallbacks so every mon can be hinted: genus, colour, egg group, moves, habitat
    if r.get("genus"): cands.append((r["genus"].split()[0].upper(),2))
    if r.get("color_primary"): cands.append((r["color_primary"].upper()+"-BODY",2))
    for eg in r.get("egg",[]): cands.append((eg.upper()+"-EGG",3))
    for mv in r.get("moves",[]): cands.append((mv.upper().replace(" ","-"),3))
    if r.get("habitat"): cands.append((r["habitat"].upper().replace(" ","-"),3))
    if r.get("color_secondary"): cands.append((r["color_secondary"].upper()+"-MARKS",2))
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

# ---- per-clue explanation sentence for the end-of-game reveal ----
CATNAME={1:"the easy one — type or family",2:"look at the sprite",
         3:"a real-world basis",4:"a trickier grouping",5:"a deeper connection"}
READ={
 # arch (plain noun): "based on the real-world {r}"
 "golem":"rock golem","butterfly":"butterfly","fox":"fox","caterpillar":"caterpillar",
 "crow":"crow","snail":"snail","tapir":"tapir (a dream-eating baku)","crocodile":"crocodile",
 "duck":"duck","eel":"eel and sea-serpent","monkey":"monkey","octopus":"octopus","squid":"squid",
 "sloth":"sloth","cobra":"cobra","feline":"cat","rhino":"rhinoceros","otter":"sea otter",
 "mole":"mole","firefly":"firefly","jellyfish":"jellyfish","frog":"frog","bee":"bee",
 "seal":"seal and sea lion","unicorn":"unicorn","swan":"swan","gorilla":"gorilla",
 "weasel":"weasel","sludge":"blob of living sludge",
 # based (phrase): "based on {r}"
 "bone":"the bone club and skull helmet it wears","lantern":"a haunted lantern",
 "sumo":"sumo wrestlers","scarab":"the scarab beetle","polygon":"3-D polygon graphics",
 # sprite (phrase): "you can spot it on the sprite — {r}"
 "fist":"the raised fists","seeds":"the seeds on its body","mushroom":"the mushroom on its back",
 "pincers":"the big pincers","scythe":"the scythe-shaped arms","acorn":"the acorn cap",
 "ball":"a Poké Ball shape","coin":"the gold coin on its forehead","coins":"a hoard of gold coins",
 "gem":"a gemstone body","spores":"the spores it puffs out",
 # lore (phrase): "from their Pokédex lore — {r}"
 "vampire":"they're vampire bats","teleport":"its signature Teleport move",
 "jynx":"an opera diva / snow-hag","ferry":"it ferries travellers across the sea",
 "fossil":"they're prehistoric fossils brought back to life","lava":"they're made of molten lava",
 "leek":"the spring onion (leek) it carries","mythical":"a mythical dragon",
 # family
 "eevee":"Eevee",
}
def _read(tail): return READ.get(tail, tail.replace("-"," "))
def explain_for(word,cat,concept,members):
    pre,_,tail=concept.partition(":"); r=_read(tail)
    if pre=="type": reason=f"Every one is a {tail.capitalize()}-type."
    elif pre=="group": reason={"starter":"They're first-partner (starter) Pokémon.",
        "legendary":"They're all Legendary Pokémon.","pseudo":"They're pseudo-legendary Pokémon."}.get(tail,f"They're all {r}.")
    elif pre=="family": reason=f"They're all part of the {r} family."
    elif pre=="arch": reason=f"They're all based on the real-world {r}."
    elif pre=="based": reason=f"They're based on {r}."
    elif pre=="sprite": reason=f"You can spot it on the sprite — {r}."
    elif pre=="lore": reason=f"It's from their Pokédex lore — {r}."
    elif pre=="myth": reason=f"It's rooted in mythology — {r}."
    elif pre=="name": reason=f"It's wordplay on their names — {r}."
    elif pre=="trainer": reason=f"They belong to {r}'s team."
    elif pre=="colour": reason=f"They're all {r}."
    else: reason=r[:1].upper()+r[1:]+"."
    return f"{reason} (Category {cat}: {CATNAME[cat]}.)"

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
    hints={}; used=set()
    for nm in blues:
        hw,hc=hint_for(nm,names,used)
        if not hw: errors.append(f"{where}: no hint for {nm}"); continue
        hints[nm]=(hw,hc); used.add(hw)
    b.update(blues=blues,neutrals=neutrals,hints=hints); assembled.append(b)

print("=== VERIFY Aug31-Sep06 ===")
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
    L=[open(f"{ROOT}/daily_tools/daily_offline_schema.sql").read(),
       "-- ------------------------------------------------------------------",
       "-- Puzzle data: 2026-08-31 .. 2026-09-06 (fact-bank authored, with per-clue explanations).","",
       "insert into public.daily_puzzles (puzzle_date, pool, clues, hints, tiles) values"]
    R=[]
    for b in assembled:
        blues,neutrals,hints=b["blues"],b["neutrals"],b["hints"]; names=blues+neutrals
        perm=list(range(25)); random.Random(hash(("p",b["date"],b["pool"]))&0xffffffff).shuffle(perm)
        pos={nm:perm[i] for i,nm in enumerate(names)}
        tiles=sorted([{"name":nm,"colour":"blue" if nm in blues else "neutral","position":pos[nm]} for nm in names],key=lambda t:t["position"])
        co=[{"word":w,"number":len(m),"cat":c,"t":sorted(pos[x] for x in m),
             "explain":explain_for(w,c,cc,m)} for w,c,cc,m in b["clues"]]
        random.Random(hash(("c",b["date"],b["pool"]))&0xffffffff).shuffle(co)
        ho=[{"word":hints[nm][0],"number":1,"cat":hints[nm][1],"t":[pos[nm]]} for nm in blues]
        random.Random(hash(("h",b["date"],b["pool"]))&0xffffffff).shuffle(ho)
        tj="["+", ".join('{"name": %s, "colour": %s, "position": %d}'%(json.dumps(t["name"]),json.dumps(t["colour"]),t["position"]) for t in tiles)+"]"
        R.append("  (%s, %s,\n   %s::jsonb,\n   %s::jsonb,\n   %s::jsonb)"%(sq(b["date"]),sq(b["pool"]),sq(jarr(co)),sq(jarr(ho)),sq(tj)))
    L.append(",\n".join(R))
    L.append("on conflict (puzzle_date, pool) do update")
    L.append("  set clues = excluded.clues, hints = excluded.hints, tiles = excluded.tiles;")
    open(f"{ROOT}/31_updates.sql","w").write("\n".join(L)+"\n")
    print("wrote 31_updates.sql")
