#!/usr/bin/env python3
"""
Build pokemon_facts.json — the AUTHORING-ONLY fact bank for daily-puzzle clue
generation (never shipped to the site). COMPLETE national dex, gens 1-9 (~1025).

Base facts come from the PokeAPI data CSVs vendored in daily_tools/pokeapi_csv/
(offline, reproducible). Provenance: https://github.com/PokeAPI/pokeapi
(data/v2/csv). On top of the base, a small CURATED overlay (curated_overlay.json)
adds hand-picked clue hooks (animal archetypes + distinctive sprite/lore tags)
for the most-used mons; stat-standout + role tags are derived for the WHOLE dex.

Per record:
  dex, gen, types[], color, egg[], evo (level|stone|trade|friendship|special|none)
  legendary, mythical (bool, from data)
  base{hp,attack,defense,special-attack,special-defense,speed}, weight (hg)
  stat[]  derived standouts: fast/atk/spatk/tanky/heavy
  arch[]  curated animal archetypes (empty if not yet curated -> AI fills at
          authoring time; the base facts still enable type/colour/egg/stat/role
          clues, and any creative clue is correctness-checked against base facts)
  tags[]  curated hooks + derived role flags (starter/pseudo from overlay;
          legendary/mythical from data)
  wk      well-known preference flag

IMPORTANT — names: normalised to match the Supabase `pokemon` table (straight
apostrophe). A handful of special-spelling mons (Nidoran, Type: Null, gender
forms) should be spelling-verified against the table before use as tiles.
"""
import csv, json, os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
CSV=os.path.join(HERE,"pokeapi_csv")
def load(f): return list(csv.DictReader(open(os.path.join(CSV,f))))

def norm_name(n):
    return n.replace("’","'")   # curly apostrophe -> straight

def build_base():
    species=load("pokemon_species.csv")
    colors={r["id"]:r["identifier"] for r in load("pokemon_colors.csv")}
    names={}
    for r in load("pokemon_species_names.csv"):
        if r["local_language_id"]=="9": names[r["pokemon_species_id"]]=norm_name(r["name"])
    egg_names={r["id"]:r["identifier"] for r in load("egg_groups.csv")}
    sp_egg={}
    for r in load("pokemon_egg_groups.csv"): sp_egg.setdefault(r["species_id"],[]).append(egg_names[r["egg_group_id"]])
    type_names={r["id"]:r["identifier"] for r in load("types.csv")}
    poke=load("pokemon.csv")
    default_pid={}; weight={}
    for r in poke:
        if r.get("is_default")=="1":
            default_pid[r["species_id"]]=r["id"]; weight[r["species_id"]]=int(r["weight"])
    ptypes={}
    for r in load("pokemon_types.csv"): ptypes.setdefault(r["pokemon_id"],[]).append((int(r["slot"]),type_names[r["type_id"]]))
    stat_names={r["id"]:r["identifier"] for r in load("stats.csv")}
    pstats={}
    for r in load("pokemon_stats.csv"): pstats.setdefault(r["pokemon_id"],{})[stat_names[r["stat_id"]]]=int(r["base_stat"])
    trig={r["id"]:r["identifier"] for r in load("evolution_triggers.csv")}
    evo_method={}
    for r in load("pokemon_evolution.csv"):
        t=trig.get(r["evolution_trigger_id"],"")
        if r.get("evolution_item_id"): m="stone"
        elif t=="trade": m="trade"
        elif t=="level-up" and r.get("minimum_happiness"): m="friendship"
        elif t=="level-up": m="level"
        elif t=="use-item": m="stone"
        else: m=t or "special"
        evo_method[r["evolved_species_id"]]=m
    out={}
    for s in species:
        sid=s["id"]
        if int(sid)>1025: continue
        pid=default_pid.get(sid)
        if not pid: continue
        st=pstats.get(pid,{})
        out[names.get(sid,s["identifier"])]=dict(
            dex=int(sid), gen=int(s["generation_id"]),
            types=[t for _,t in sorted(ptypes.get(pid,[]))], color=colors[s["color_id"]],
            egg=sp_egg.get(sid,[]),
            evo=evo_method.get(sid, "none" if not s["evolves_from_species_id"] else "level"),
            legendary=s["is_legendary"]=="1", mythical=s["is_mythical"]=="1",
            base=st, weight=weight.get(sid,0))
    return out

def stat_tags(b, w):
    t=[]
    if b.get("speed",0)>=100: t.append("fast")
    if b.get("attack",0)>=120: t.append("atk")
    if b.get("special-attack",0)>=120: t.append("spatk")
    if b.get("defense",0)>=110 or (b.get("hp",0)>=100 and b.get("defense",0)+b.get("special-defense",0)>=180): t.append("tanky")
    if w>=2500: t.append("heavy")
    return t

def main():
    base=build_base()
    overlay={}
    ov_path=os.path.join(HERE,"curated_overlay.json")
    if os.path.exists(ov_path): overlay=json.load(open(ov_path))
    facts={}
    for nm,r in base.items():
        ov=overlay.get(nm,{})
        tags=list(ov.get("tags",[]))
        if r["legendary"] and "legendary" not in tags: tags.append("legendary")
        if r["mythical"] and "mythical" not in tags: tags.append("mythical")
        facts[nm]=dict(
            dex=r["dex"], gen=r["gen"], types=r["types"], color=r["color"], egg=r["egg"],
            evo=r["evo"], legendary=r["legendary"], mythical=r["mythical"],
            base=r["base"], weight=r["weight"],
            arch=ov.get("arch",[]), tags=tags, stat=stat_tags(r["base"], r["weight"]),
            wk=ov.get("wk", 1 if (r["legendary"] or r["mythical"]) else 0))
    json.dump(facts, open(os.path.join(HERE,"..","pokemon_facts.json"),"w"), ensure_ascii=False, indent=0)
    from collections import Counter
    print("records:",len(facts))
    print("by gen:",dict(sorted(Counter(r['gen'] for r in facts.values()).items())))
    print("with curated arch:",sum(1 for r in facts.values() if r['arch']))
    print("types:",len({t for r in facts.values() for t in r['types']}))
    # quick integrity check
    bad=[n for n,r in facts.items() if not r['types'] or not r['color']]
    if bad: print("WARN missing types/color:",bad[:10]); sys.exit(1)
    print("OK")

if __name__=="__main__": main()
