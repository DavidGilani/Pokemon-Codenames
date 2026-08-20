#!/usr/bin/env python3
"""
EXPERIMENTAL authoring aid (not the final word on clue quality). It reliably
produces VARIED, Rule-0-safe boards from the fact bank, but the auto-picked
clues skew to plain animal-archetype words (SIMIAN, PINNIPED, ...) rather than
the cleverer sprite/lore clues a human writes. Use it to surface candidate
blues/connections and to CHECK diversity, then hand-polish the clue words.
Note: a strict 9-consecutive-day Brutal/Evil regen is over-constrained right
after a hard stretch (the fact-bank frequency cap locks out the recently-used
hard mons) — space hard tiers out or relax the caps when driving it.

Generate diverse daily puzzles from pokemon_facts.json by SEARCH (blues-first):
pick 9 varied blues, then cover them with 5 clues drawn from shared facts. This
guarantees Rule 0 (a clue's members are exactly the board-blues sharing that
attribute) and enforces all five anti-repetition rules + the mix table + gate.

Emits NN_updates.sql overwriting Aug 22..Aug 30 2026.
Mixed pool: full rules (mon <=1 blue/10d). Gen 1: softened (mon <=1 blue/5d).
"""
import csv, json, re, random, datetime, sys
from collections import defaultdict
ROOT="/home/user/Pokemon-Codenames"
FACTS=json.load(open(f"{ROOT}/pokemon_facts.json"))
GEN1={n for n,r in FACTS.items() if r["gen"]==1}

def norm(s): return re.sub(r'[^a-z]','',s.lower())
def shares3(a,b):
    a,b=norm(a),norm(b)
    for i in range(len(a)-2):
        if a[i:i+3] in b: return True
    for i in range(len(b)-2):
        if b[i:i+3] in a: return True
    return False

# ---------------- concept vocabulary ----------------
TYPE_W={t:[t.upper()] for t in ["fire","water","grass","electric","ice","fighting",
 "poison","ground","flying","psychic","bug","rock","ghost","dragon","dark","steel","fairy","normal"]}
COLOUR_W={c:[c.upper()] for c in ["pink","yellow","brown","purple","white","blue","red","green","gray","black"]}
ARCH_COMMON={  # cat 3
 "feline":["FELINE","CAT"],"canine":["HOUND","CANID"],"equine":["EQUINE","STEED"],
 "serpent":["SERPENT","SNAKE"],"snake":["SERPENT","SNAKE"],"bear":["BEAR","URSINE"],
 "rodent":["RODENT"],"bird":["BIRD"],"fish":["FISH"],"frog":["FROG"],"toad":["TOAD"],
 "insect":["INSECT"],"crab":["CRAB"],"mole":["MOLE"],"fox":["FOX","VULPINE"],
 "duck":["DUCK"],"lizard":["LIZARD"],"turtle":["TURTLE"],"owl":["OWL"],"wolf":["WOLF"],
 "shark":["SHARK"],"moth":["MOTH"],"mantis":["MANTIS"],"beetle":["BEETLE"],
 "seahorse":["SEAHORSE"],"boar":["BOAR"],"pig":["SWINE"],"gecko":["GECKO"],
 "crocodile":["CROC","GATOR"],"penguin":["PENGUIN"],"gorilla":["GORILLA"],
 "monkey":["MONKEY"],"tiger":["TIGER"],"lion":["LION"],"leopard":["LEOPARD"],
 "zebra":["ZEBRA"],"bull":["BULL"],"otter":["OTTER"],"seal":["PINNIPED"],
 "dinosaur":["DINOSAUR","SAURIAN"],"dragon":["DRAKE"],"rat":["RAT-KIN"],
}
ARCH_TECH={  # cat 4
 "cephalopod":["CEPHALOPOD","KRAKEN","MOLLUSK","INKLING"],"crustacean":["CRUSTACEAN","SHELLFISH"],
 "primate":["PRIMATE","SIMIAN","APE"],"raptor":["RAPTOR","BIRDOFPREY"],
 "mustelid":["MUSTELID","WEASEL","FERRET","POLECAT"],"pachyderm":["PACHYDERM"],
 "marsupial":["MARSUPIAL"],"chiropteran":["CHIROPTERA"],"trilobite":["TRILOBITE"],
 "ammonite":["AMMONITE"],"cetacean":["CETACEAN","LEVIATHAN"],"pinniped":["PINNIPED"],
 "echinoderm":["ECHINODERM"],"arthropod":["ARTHROPOD"],"proboscidean":["PROBOSCIS"],
 "plesiosaur":["PLESIOSAUR"],"pterosaur":["PTEROSAUR"],"lagomorph":["LAGOMORPH"],
 "mollusc":["MOLLUSC"],"hydra":["HYDRA"],"theropod":["THEROPOD"],"ratite":["RATITE"],
 "corvid":["CORVID"],"isopod":["ISOPOD"],"pangolin":["PANGOLIN"],"scorpion":["SCORPION"],
 "arachnid":["ARACHNID"],"tapir":["TAPIR"],"mammoth":["MAMMOTH"],"rhino":["RHINO"],
 "elephant":["ELEPHANT"],"hippo":["HIPPO"],"cnidarian":["CNIDARIAN"],"jellyfish":["JELLYFISH"],
 "wyvern":["WYVERN"],"platypus":["PLATYPUS"],"kangaroo":["KANGAROO"],"unicorn":["UNICORN"],
 "phoenix":["PHOENIX"],"ninja":["NINJA"],"samurai":["SAMURAI"],"starfish":["STARFISH"],
 "mermaid":["MERMAID"],"bivalve":["BIVALVE"],"caterpillar":["LARVA"],"pupa":["PUPA"],
 "wasp":["WASP"],"butterfly":["BUTTERFLY"],"carp":["CARP"],"goldfish":["GOLDFISH"],
 "armadillo":["ARMADILLO"],"tadpole":["TADPOLE"],"bat":["FLITTER"],
}
# sprite/feature tags -> cat 2 word(s)
TAG2={
 "horn":["HORN"],"horns":["HORNS"],"wings":["WINGS"],"tail":["TAIL"],"claws":["CLAWS"],
 "fangs":["FANGS"],"shell":["SHELL"],"spikes":["SPIKES"],"pincers":["PINCERS"],"tongue":["TONGUE"],
 "blades":["BLADES","SWORDS"],"balloon":["BALLOON"],"eggs":["EGGS"],"six":["SIX"],"star":["STAR"],
 "mane":["MANE"],"tusks":["TUSKS"],"tusk":["TUSKS"],"bone-club":["BONE"],"drum":["DRUM"],
 "coils":["COILS"],"hood":["HOOD"],"scythes":["SCYTHES"],"scales":["SCALES"],"antennae":["ANTENNAE"],
 "crest":["CREST"],"beak":["BEAK"],"leek":["LEEK"],"gloves":["GLOVES"],"coin":["COIN"],
 "pendulum":["PENDULUM"],"spoon":["SPOON"],"spoons":["SPOONS"],"pouch":["POUCH"],"ribbon":["RIBBON"],
 "bows":["BOWS"],"rings":["RINGS"],"belt":["BELT"],"armour":["ARMOUR"],"keys":["KEYS"],
 "lantern":["LANTERN"],"paper":["PAPER"],"three-heads":["TRIO"],"two-heads":["TWINS"],
 "cannons":["CANNONS"],"trident":["TRIDENT"],"whiskers":["WHISKERS"],"petals":["PETALS"],
 "flower":["FLOWER"],"bloom":["BLOOM"],"vines":["VINES"],"bulb":["BULB"],"mushroom":["MUSHROOM"],
 "jelly":["JELLY"],"jewels":["JEWELS"],"pearl":["PEARL"],"muscle":["MUSCLE"],"four-arms":["QUAD-ARMS"],
 "helmet":["HELMET"],"hat":["HAT"],"rag":["RAG"],"boulder":["BOULDER"],"drills":["DRILLS"],
 "drill-horn":["DRILL"],"gem":["GEM"],"fur":["FUR"],"fluff":["FLUFF"],"curls":["RINGLETS"],
 "snout":["SNOUT"],"fins":["FINS"],"stripes":["STRIPES"],"lips":["LIPS"],"gown":["GOWN"],
 "hooves":["HOOVES"],"guitar":["GUITAR"],"axe-jaw":["AXE"],"suckers":["SUCKERS"],"clam":["CLAM"],
 "skull":["SKULL"],"opera":["OPERA"],"kimono":["KIMONO"],"grin":["WIDE-GRIN"],
}
# lore / connection tags -> (concept, cat, words)
LORE={
 "starter":("starter",1,["STARTER"]),"legendary":("legendary",1,["LEGENDARY"]),
 "mythical":("mythical",5,["MYTHICAL","MYTH"]),"eeveelution":("eeveelution",3,["EEVEE"]),
 "fossil":("fossil",4,["FOSSIL","EXTINCT","RELIC","PREHISTORIC","ANCIENT","REVIVED"]),
 "pseudo":("pseudo",5,["PSEUDO","PSEUDOLEGEND"]),"mega":("mega",5,["MEGA"]),
 "transform":("transform",5,["TRANSFORM","SHAPESHIFT"]),"imposter":("transform",5,["IMPOSTER"]),
 "clone":("clone",5,["CLONE","REPLICA"]),
 "kitsune":("mythology",5,["KITSUNE","NINE-TAILS"]),"phoenix":("mythology",5,["PHOENIX"]),
 "folklore":("mythology",5,["FOLKLORE","LEGEND-LORE"]),"golem-mythos":("mythology",5,["AUTOMATON"]),
 "intimidate":("intimidate",5,["INTIMIDATE","MENACE","DAUNT","COW"]),
 "levitate":("levitate",5,["LEVITATE","FLOAT","HOVER"]),
 "trickster":("trickster",5,["TRICKSTER","MISCHIEF"]),"illusion":("trickster",5,["ILLUSION"]),
 "move:earthquake":("move:earthquake",4,["EARTHQUAKE","QUAKE","TREMOR"]),
 "move:hyper-beam":("move:hyperbeam",4,["HYPER-BEAM"]),"move:fly":("move:fly",4,["SKYWARD"]),
 "move:submission":("move:submission",4,["SUBMISSION"]),
 "kanto":("region:kanto",3,["KANTO"]),"johto":("region:johto",3,["JOHTO"]),
 "hoenn":("region:hoenn",3,["HOENN"]),"sinnoh":("region:sinnoh",3,["SINNOH"]),
 "unova":("region:unova",3,["UNOVA"]),"kalos":("region:kalos",3,["KALOS"]),
 "alola":("region:alola",3,["ALOLA"]),"galar":("region:galar",3,["GALAR"]),
 "safari":("route:safari",4,["SAFARI"]),"bird-trio":("bird-trio",4,["TRIO-BIRDS"]),
 "rival-magmar":("rivals",4,["RIVALS"]),"rival-electabuzz":("rivals",4,["RIVALS"]),
 "siblings":("siblings",4,["SIBLINGS"]),"boxer":("boxer",3,["BOXER"]),"wrestler":("wrestler",3,["WRESTLER"]),
 "kick":("kick",3,["KICK"]),"sleep":("sleep",3,["SLUMBER"]),"orphan":("orphan",4,["ORPHAN"]),
 "wields":("wields",4,["WIELD"]),"opera":("opera",4,["OPERA"]),"ghost-lore":("ghost",3,["SPOOKY","WRAITH"]),
}
# egg groups and evo methods as connection concepts (cat 5)
EGG_W={"monster":"BEAST-EGG","water1":"SEA-EGG","water2":"FISH-EGG","water3":"SHELL-EGG",
 "bug":"BUG-EGG","flying":"WING-EGG","field":"FIELD-EGG","fairy":"FAY-EGG","grass":"FLORA-EGG",
 "human":"HUMANOID","mineral":"MINERAL-EGG","amorphous":"FORMLESS","dragon":"DRAGON-EGG",
 "monster,dragon":"","undiscovered":"","ditto":""}
EVO_W={"stone":("evo:stone",5,["STONE-EVO","STONE-BORN"]),"trade":("evo:trade",5,["TRADE-EVO","TRADED"]),
 "friendship":("evo:friendship",5,["BOND-EVO","AFFECTION"]),"fossil":("evo:fossil",5,["REVIVED-FOSSIL"])}
STAT_W={"fast":("stat:fast",5,["SPEEDSTER","FLEET"]),"heavy":("stat:heavy",5,["HEAVYWEIGHT","COLOSSAL"]),
 "tanky":("stat:tanky",5,["JUGGERNAUT","BULWARK"]),"atk":("stat:atk",5,["BRUISER","POWERHOUSE"]),
 "spatk":("stat:spatk",5,["MASTERMIND","SAVANT"])}

# Only DISTINCTIVE signature features are safe as clues under automation: a
# neutral is unlikely to share them untagged (unlike generic tail/wings/horn).
TAG2_SAFE={"leek","bone-club","spoons","spoon","coin","pendulum","star","balloon",
 "drum","trident","lantern","keys","paper","guitar","gown","skull","kimono","six",
 "eggs","mushroom","pearl","clam","coils","hood","scythes","axe-jaw","suckers",
 "cannons","three-heads","two-heads","whiskers","tongue","opera"}

# Too obscure / unfun as everyday clue words — skip (mon still cluable other ways).
OBSCURE_ARCH={"echinoderm","chiropteran","pangolin","isopod","arthropod","proboscidean",
 "plesiosaur","pterosaur","cnidarian","ratite","corvid","bivalve","lagomorph","tapir",
 "mollusc","hydra","theropod","scorpion","arachnid","caterpillar","pupa","platypus",
 "armadillo","carp","goldfish","tadpole","wyvern","ammonite","mermaid","unicorn",
 "automaton","bat","wolf","leopard","zebra","gecko","boar","pig","larva"}

def mon_concepts(nm):
    """Rule-0-safe concepts `nm` can be clued by (complete/objective attributes
    + distinctive signature features only)."""
    r=FACTS[nm]; out=[]
    for t in r["types"]:
        out.append((f"type:{t}",1,TYPE_W[t]))
    out.append((f"colour:{r['color']}",1,COLOUR_W.get(r["color"],[r["color"].upper()])))
    for a in r["arch"]:
        if a in OBSCURE_ARCH: continue
        if a in ARCH_COMMON: out.append((f"arch:{a}",3,ARCH_COMMON[a]))
        elif a in ARCH_TECH: out.append((f"arch:{a}",4,ARCH_TECH[a]))
    for tg in r["tags"]:
        if tg.startswith("move:"): continue          # incomplete tagging -> unsafe
        if tg in TAG2 and tg in TAG2_SAFE: out.append((f"tag:{tg}",2,TAG2[tg]))
        elif tg in LORE and not tg.startswith("move:"): out.append(LORE[tg])
    if r["evo"] in EVO_W: out.append(EVO_W[r["evo"]])   # complete + objective
    # egg groups + raw stats dropped: invisible / fuzzy -> unfair to guessers.
    seen={}
    for c,cat,words in out:
        if c.startswith("move:"): continue
        if c not in seen: seen[c]=(cat,words)
    return [(c,cat,words) for c,(cat,words) in seen.items()]

_CC={}
def concepts_of(nm):
    if nm not in _CC: _CC[nm]=mon_concepts(nm)
    return _CC[nm]

# ---------------- corpus (kept history Aug 8..21) ----------------
rows=list(csv.DictReader(open("/root/.claude/uploads/eeb0f753-042d-524e-85cc-2ca2ce41ced3/31a19a47-daily_puzzles_rows.csv")))
USES=defaultdict(list); BLUE_USED=defaultdict(list)
for r in rows:
    T={t['position']:t for t in json.loads(r['tiles'])}
    blues={t['name'] for t in T.values() if t['colour']=='blue'}
    for b in blues: BLUE_USED[b].append(r['puzzle_date'])
    for c in json.loads(r['clues']):
        USES[c['word']].append((r['puzzle_date'], frozenset(T[p]['name'] for p in c.get('t',[]))))
# concept seed for the 5-day window before Aug 22 (map recent words -> concepts)
SEED_MAP={'FOSSIL':'fossil','MORPH':'transform','PSEUDO':'pseudo','MEGA':'mega','WIELD':'wields',
 'RIVALS':'rivals','PIXEL':'tag:digital','TRICKSTER':'trickster','NIGHTMARE':'ghost','THIEF':'tag:thief',
 'STARTER':'starter','SLEEP':'sleep','MASCOT':'tag:mascot','SERPENT':'arch:serpent','GRIN':'ghost',
 'HORN':'tag:horn','SHELL':'tag:shell','SPOONS':'tag:spoons','ORPHAN':'orphan','WATER':'type:water',
 'AURA':'tag:aura','GOWN':'tag:gown','THREE':'tag:three-heads','HEADS':'tag:three-heads',
 'BLADES':'tag:blades','SWORDS':'tag:blades','ARMS':'tag:four-arms','FROG':'arch:frog','TONGUE':'tag:tongue'}
CONCEPT_SEED=defaultdict(list)
for r in rows:
    if r['puzzle_date']>='2026-08-17':
        for c in json.loads(r['clues']):
            cc=SEED_MAP.get(c['word'])
            if cc: CONCEPT_SEED[(r['pool'],cc)].append(r['puzzle_date'])

def days(a,b): return (datetime.date.fromisoformat(a)-datetime.date.fromisoformat(b)).days

# ---------------- tier category templates ----------------
# label(cats): highs(cat>=4)>=4 Evil; ==3 Brutal; else ones(cat==1) 0/1/2/3 -> Hard/Chall/Med/Easy
def label(cats):
    highs=sum(1 for c in cats if c>=4); ones=sum(1 for c in cats if c==1)
    if highs>=4: return 'Evil'
    if highs>=3: return 'Brutal'
    if ones==0: return 'Hard'
    if ones==1: return 'Challenging'
    if ones==2: return 'Medium'
    return 'Easy'

def tier_ok(tier, clues):
    cats=[c for _,c,_,_ in clues]
    if label(cats)!=tier: return False
    cat2=sum(1 for c in cats if c==2)
    nums=[len(m) for _,_,_,m in clues]; ssum=sum(nums); ones1=sum(1 for n in nums if n==1)
    if tier=='Evil' and cat2>0: return False
    if tier in('Hard','Brutal') and cat2>1: return False
    if len(set(cats))<3 and tier!='Easy': return False
    if tier in('Brutal','Evil'):
        if ones1>1 or ssum<11: return False
    return True

SCHEDULE=[("2026-08-22","Brutal"),("2026-08-23","Evil"),("2026-08-24","Easy"),
 ("2026-08-25","Medium"),("2026-08-26","Challenging"),("2026-08-27","Hard"),
 ("2026-08-28","Hard"),("2026-08-29","Brutal"),("2026-08-30","Evil")]

# ---------------- search ----------------
def eligible_pool(pool, date, new_blue, cap):
    base=GEN1 if pool=='gen1' else set(FACTS)
    out=[]
    for nm in base:
        if pool=='mixed' and nm in GEN1 and FACTS[nm]['gen']!=1: pass
        bad=False
        for od in BLUE_USED.get(nm,[]):
            if 0<=days(date,od)<=cap: bad=True
        for od in new_blue.get(nm,[]):
            if 0<=days(date,od)<=cap: bad=True
        if not bad: out.append(nm)
    return out

def pick_words(clues, names, date, new_word, rng):
    """Assign a distinct word to each clue: passes letter rule vs all names and
    the 7-day word rule (corpus+new). Returns list of words or None."""
    used=set()
    result=[]
    for concept,cat,words,members in clues:
        cand=list(words); rng.shuffle(cand)
        chosen=None
        for w in cand:
            if w in used: continue
            if any(shares3(w,nm) for nm in names): continue
            if any(0<=days(date,od)<=7 for od,_ in USES.get(w,[])): continue
            if any(0<=days(date,od)<=7 for od in new_word.get(w,[])): continue
            chosen=w; break
        if not chosen: return None
        used.add(chosen); result.append(chosen)
    return result

def concept_set(nm):
    return _CS.setdefault(nm, {c for c,_,_ in concepts_of(nm)})
_CS={}

PATTERNS={
 'Easy':[[(1,3),(1,2),(1,2),(2,1),(2,1)],[(1,2),(1,2),(1,2),(2,2),(2,1)],
         [(1,2),(1,3),(1,2),(2,1),(2,1)]],
 'Medium':[[(1,2),(1,2),(2,2),(3,2),(4,1)],[(1,2),(1,2),(2,2),(3,1),(4,2)],
           [(1,2),(1,3),(2,1),(3,2),(4,1)],[(1,2),(1,2),(2,1),(3,2),(4,2)]],
 'Challenging':[[(1,2),(2,2),(3,2),(3,2),(4,1)],[(1,2),(2,1),(3,2),(3,2),(4,2)],
                [(1,1),(2,2),(3,2),(3,2),(4,2)],[(1,2),(2,2),(3,3),(3,1),(4,1)]],
 'Hard':[[(2,1),(3,2),(3,2),(4,2),(4,2)],[(3,2),(3,2),(3,1),(4,2),(4,2)],
         [(2,1),(3,3),(3,1),(4,2),(4,2)],[(2,1),(3,2),(4,2),(3,2),(4,2)]],
 'Brutal':[[(3,1),(3,2),(4,2),(4,2),(4,2)],[(2,1),(3,2),(4,2),(4,2),(4,2)],
           [(4,1),(4,2),(4,2),(3,2),(3,2)],[(3,2),(3,1),(4,2),(4,2),(4,2)]],
 'Evil':[[(4,1),(4,2),(4,2),(4,2),(4,2)],[(3,1),(4,2),(4,2),(5,2),(5,2)],
         [(3,1),(4,2),(4,2),(4,2),(5,2)],[(3,2),(4,2),(4,2),(4,2),(5,1)]],
}


def build_board(pool, date, tier, new_blue, new_word, new_concept, rng):
    """Pure-partition builder: fill the tier pattern slot by slot, each clue's
    members drawn from mons that (a) have the slot concept and (b) have NONE of
    the already-chosen concepts. That keeps each blue tied to exactly one chosen
    concept -> Rule 0 is automatic, and no neutral shares a chosen concept."""
    cap=4 if pool=='gen1' else 7
    cw=3
    pats=PATTERNS[tier]
    need_types=4 if pool=='gen1' else 5
    pool_mons=set(eligible_pool(pool,date,new_blue,cap))
    if len(pool_mons)<9: return None
    concept_pool=defaultdict(lambda:[None,None,[]])
    for nm in pool_mons:
        for c,cat,words in concepts_of(nm):
            if any(0<=days(date,od)<=cw for od in CONCEPT_SEED.get((pool,c),[])): continue
            if any(0<=days(date,od)<=cw for od in new_concept.get((pool,c),[])): continue
            e=concept_pool[c]; e[0]=cat; e[1]=words; e[2].append(nm)
    by_cat=defaultdict(list)
    for c,(cat,words,mem) in concept_pool.items():
        by_cat[cat].append((c,words,mem))
    base=GEN1 if pool=='gen1' else set(FACTS)
    for _ in range(6000):
        pat=rng.choice(pats)
        chosen=[]; blues=[]; chosen_c=set(); ok=True
        for cat,size in pat:
            opts=[o for o in by_cat.get(cat,[]) if o[0] not in chosen_c
                  and not any(o[0] in concept_set(b) for b in blues)]
            rng.shuffle(opts); placed=False
            for c,words,mem in opts:
                pure=[m for m in mem if m not in blues and not (concept_set(m) & chosen_c)]
                if len(pure)<size: continue
                rng.shuffle(pure); members=pure[:size]
                chosen.append((c,cat,words,members)); chosen_c.add(c)
                blues.extend(members); placed=True; break
            if not placed: ok=False; break
        if not ok or len(blues)!=9: continue
        if len({FACTS[b]['types'][0] for b in blues})<need_types: continue
        if pool=='mixed' and len({FACTS[b]['gen'] for b in blues})<3: continue
        cand_neu=[nm for nm in base if nm not in blues and not (concept_set(nm) & chosen_c)]
        if len(cand_neu)<16: continue
        rng.shuffle(cand_neu); neutrals=cand_neu[:16]
        names=blues+neutrals
        words_out=pick_words(chosen,names,date,new_word,rng)
        if not words_out: continue
        final=[(w,cat,c,sorted(members)) for (c,cat,words,members),w in zip(chosen,words_out)]
        return dict(date=date,pool=pool,tier=tier,clues=final,blues=blues,neutrals=neutrals)
    return None

# ---------------- run ----------------
def generate():
    rng=random.Random(20260822)
    new_blue=defaultdict(list); new_word=defaultdict(list); new_concept=defaultdict(list)
    boards=[]
    for date,tier in SCHEDULE:
        for pool in ('gen1','mixed'):
            b=None
            for attempt in range(12):
                b=build_board(pool,date,tier,new_blue,new_word,new_concept,
                              random.Random(rng.randrange(1<<30)))
                if b: break
            if not b:
                print(f"FAILED to build {date} {pool} {tier}")
                return None
            for nm in b['blues']: new_blue[nm].append(date)
            for w,cat,c,mem in b['clues']:
                new_word[w].append(date); new_concept[(pool,c)].append(date)
            boards.append(b)
            print(f"OK {date} {pool} {tier}: "+", ".join(f"{w}({c})" for w,cat,c,mem in b['clues']))
    return boards

if __name__=="__main__":
    bs=generate()
    if bs: json.dump(bs, open("/tmp/claude-0/boards.json","w"))
    print("\nBUILT" if bs else "\nINCOMPLETE")
