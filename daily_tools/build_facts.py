#!/usr/bin/env python3
"""
Build pokemon_facts.json (+ .csv) — the AUTHORING-ONLY fact bank for daily-puzzle
clue generation (never shipped to the site). COMPLETE national dex, gens 1-9.

Two layers:
  OBJECTIVE (auto, all 1025, from vendored PokeAPI CSVs — daily_tools/pokeapi_csv,
    provenance https://github.com/PokeAPI/pokeapi): dex, gen, region, types,
    color_primary, abilities (incl. hidden), genus, shape, habitat, egg groups,
    evolution method + family, legendary/mythical/baby, base stats, weight, height,
    derived stat standouts.
  CURATED (hand-authored overlay curated_overlay.json, split by kind; thorough for
    well-known mons, sparse for obscure ones rather than fabricated): color_secondary,
    arch (animal archetype), sprite (distinctive visual features), moves (notable/
    signature), lore (Pokedex flavour / pun), mythology (folklore origin), location
    (distinctive place found), trainer (popular trainer/character), role
    (starter/pseudo/fossil/etc.), other (catch-all), wk (well-known flag).

Any creative clue an author writes is CHECKED against the objective columns; the
curated columns are idea material, not the correctness backstop.
"""
import csv, json, os, sys
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__))
CSV=os.path.join(HERE,"pokeapi_csv")
def load(f): return list(csv.DictReader(open(os.path.join(CSV,f))))
def norm_name(n): return n.replace("’","'")
REGION={1:"Kanto",2:"Johto",3:"Hoenn",4:"Sinnoh",5:"Unova",6:"Kalos",7:"Alola",8:"Galar",9:"Paldea"}

def build_base():
    species=load("pokemon_species.csv")
    colors={r["id"]:r["identifier"] for r in load("pokemon_colors.csv")}
    shapes={r["id"]:r["identifier"] for r in load("pokemon_shapes.csv")}
    habitats={r["id"]:r["identifier"] for r in load("pokemon_habitats.csv")}
    names={}; genus={}
    for r in load("pokemon_species_names.csv"):
        if r["local_language_id"]=="9":
            names[r["pokemon_species_id"]]=norm_name(r["name"]); genus[r["pokemon_species_id"]]=r.get("genus","")
    egg_names={r["id"]:r["identifier"] for r in load("egg_groups.csv")}
    sp_egg={}
    for r in load("pokemon_egg_groups.csv"): sp_egg.setdefault(r["species_id"],[]).append(egg_names[r["egg_group_id"]])
    type_names={r["id"]:r["identifier"] for r in load("types.csv")}
    poke=load("pokemon.csv"); default_pid={}; weight={}; height={}
    for r in poke:
        if r.get("is_default")=="1":
            default_pid[r["species_id"]]=r["id"]; weight[r["species_id"]]=int(r["weight"]); height[r["species_id"]]=int(r["height"])
    ptypes={}
    for r in load("pokemon_types.csv"): ptypes.setdefault(r["pokemon_id"],[]).append((int(r["slot"]),type_names[r["type_id"]]))
    stat_names={r["id"]:r["identifier"] for r in load("stats.csv")}
    pstats={}
    for r in load("pokemon_stats.csv"): pstats.setdefault(r["pokemon_id"],{})[stat_names[r["stat_id"]]]=int(r["base_stat"])
    ab_names={}
    for r in load("ability_names.csv"):
        if r["local_language_id"]=="9": ab_names[r["ability_id"]]=r["name"]
    p_ab={}
    for r in sorted(load("pokemon_abilities.csv"), key=lambda x:(x["pokemon_id"],x["slot"])):
        p_ab.setdefault(r["pokemon_id"],[]).append((ab_names.get(r["ability_id"],""), r["is_hidden"]=="1"))
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
    # evolution family: base species (no evolves_from) per chain; + stage depth
    chain_base={}; byid={s["id"]:s for s in species}
    for s in species:
        cid=s["evolution_chain_id"]
        if not s["evolves_from_species_id"]:
            chain_base[cid]=s["id"]
    def stage(s):
        d=0; cur=s
        while cur["evolves_from_species_id"] and cur["evolves_from_species_id"] in byid:
            d+=1; cur=byid[cur["evolves_from_species_id"]]
            if d>4: break
        return d
    def gender(s):
        gr=int(s["gender_rate"])
        return "genderless" if gr==-1 else "female-only" if gr==8 else "male-only" if gr==0 else "both"
    out={}
    for s in species:
        sid=s["id"]
        if int(sid)>1025: continue
        pid=default_pid.get(sid)
        if not pid: continue
        st=pstats.get(pid,{})
        abils=[a for a,_ in p_ab.get(pid,[]) if a]
        base_sid=chain_base.get(s["evolution_chain_id"], sid)
        out[names.get(sid,s["identifier"])]=dict(
            dex=int(sid), gen=int(s["generation_id"]), region=REGION[int(s["generation_id"])],
            types=[t for _,t in sorted(ptypes.get(pid,[]))], color=colors[s["color_id"]],
            abilities=abils, genus=genus.get(sid,""), shape=shapes.get(s["shape_id"],""),
            habitat=habitats.get(s["habitat_id"],""), egg=sp_egg.get(sid,[]),
            evo=evo_method.get(sid,"none" if not s["evolves_from_species_id"] else "level"),
            family=names.get(base_sid,""), stage=stage(s), gender=gender(s), baby=s["is_baby"]=="1",
            legendary=s["is_legendary"]=="1", mythical=s["is_mythical"]=="1",
            base=st, weight=weight.get(sid,0), height=height.get(sid,0),
            _base_sid=base_sid)
    return out

def stat_tags(b,w):
    t=[]
    if b.get("speed",0)>=100: t.append("fast")
    if b.get("attack",0)>=120: t.append("atk")
    if b.get("special-attack",0)>=120: t.append("spatk")
    if b.get("defense",0)>=110 or (b.get("hp",0)>=100 and b.get("defense",0)+b.get("special-defense",0)>=180): t.append("tanky")
    if w>=2500: t.append("heavy")
    if w and w<=30: t.append("light")
    return t

# --- migrate legacy flat `tags` into split curated columns ---
ROLE={"starter","legendary","mythical","pseudo","fossil","eeveelution","mega","gmax","baby"}
MYTH={"kitsune","phoenix","folklore","golem-mythos","fairy-mythos","mythical-lore",
 "legendary-lore","mystical","baku-mythos","nessie","ghost-lore","forbidden","108-souls","yuki-onna"}
LORE_TOK={"orphan","wields","opera","king","charm","mascot","thief","imposter","clone",
 "transform","intimidate","levitate","trickster","illusion","disaster","disguise","sleep",
 "rivals","siblings","boxer","wrestler","grappler","sniper","secret-agent","striker","punk",
 "rocker","knight","samurai","ninja","archer","witch","diva","nurse","despot","boss","loyal",
 "angry","splash","useless","royalty","queen","emperor","allure","chivalry","valour","judo"}
REGION_TOK={"kanto","johto","hoenn","sinnoh","unova","kalos","alola","galar","paldea"}
def bucket_tags(tags):
    sprite=[]; role=[]; myth=[]; lore=[]; moves=[]; other=[]
    for t in tags:
        if t.startswith("move:"): moves.append(t.split(":",1)[1])
        elif t.startswith("rival"): lore.append("rivals")
        elif t in ROLE: role.append(t)
        elif t in MYTH: myth.append(t)
        elif t in LORE_TOK: lore.append(t)
        elif t in REGION_TOK: pass          # region is now its own objective column
        else: sprite.append(t)              # default: treat as a sprite/visual hook
    dedup=lambda L: list(dict.fromkeys(L))
    return dedup(sprite),dedup(role),dedup(myth),dedup(lore),dedup(moves),dedup(other)

def main():
    base=build_base()
    overlay={}
    ov=os.path.join(HERE,"curated_overlay.json")
    if os.path.exists(ov): overlay=json.load(open(ov))
    facts={}
    for nm,r in base.items():
        o=overlay.get(nm,{})
        # legacy: an overlay entry may still carry a flat `tags` list -> bucket it.
        ls,lrole,lmyth,llore,lmoves,lother=bucket_tags(o.get("tags",[]))
        role=list(dict.fromkeys(o.get("role",[])+lrole))
        if r["legendary"] and "legendary" not in role: role.append("legendary")
        if r["mythical"] and "mythical" not in role: role.append("mythical")
        if r["baby"] and "baby" not in role: role.append("baby")
        dd=lambda L: list(dict.fromkeys(L))
        facts[nm]=dict(
            dex=r["dex"], gen=r["gen"], region=r["region"],
            types=r["types"], color_primary=r["color"], color_secondary=o.get("color_secondary",""),
            abilities=r["abilities"], genus=r["genus"], shape=r["shape"], habitat=r["habitat"],
            egg=r["egg"], evo=r["evo"], family=r["family"], stage=r["stage"], gender=r["gender"],
            legendary=r["legendary"], mythical=r["mythical"], baby=r["baby"],
            base=r["base"], weight=r["weight"], height=r["height"], stat=stat_tags(r["base"],r["weight"]),
            arch=o.get("arch",[]), based_on=o.get("based_on",[]),
            sprite=dd(o.get("sprite",[])+ls), moves=dd(o.get("moves",[])+lmoves),
            signature_move=o.get("signature_move",""),
            lore=dd(o.get("lore",[])+llore), mythology=dd(o.get("mythology",[])+lmyth),
            location=o.get("location",[]), trainer=o.get("trainer",[]),
            nickname=o.get("nickname",[]), role=role, other=dd(o.get("other",[])+lother),
            wk=o.get("wk", 1 if (r["legendary"] or r["mythical"]) else 0))
    json.dump(facts, open(os.path.join(HERE,"..","pokemon_facts.json"),"w"), ensure_ascii=False, indent=0)
    # CSV
    cols=["name","dex","gen","region","type1","type2","color_primary","color_secondary",
          "abilities","genus","shape","habitat","evo","family","stage","gender","legendary","mythical","baby",
          "hp","attack","defense","sp_attack","sp_defense","speed","weight_kg","height_m",
          "egg_groups","stat_standouts","arch","based_on","sprite","moves","signature_move","lore",
          "mythology","location","trainer","community_nickname","role","other","well_known"]
    J=lambda L: ", ".join(L)
    with open(os.path.join(HERE,"..","pokemon_facts.csv"),"w",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=cols); w.writeheader()
        for name,r in sorted(facts.items(),key=lambda kv:kv[1]["dex"]):
            b=r["base"]
            w.writerow({"name":name,"dex":r["dex"],"gen":r["gen"],"region":r["region"],
                "type1":r["types"][0] if r["types"] else "","type2":r["types"][1] if len(r["types"])>1 else "",
                "color_primary":r["color_primary"],"color_secondary":r["color_secondary"],
                "abilities":J(r["abilities"]),"genus":r["genus"],"shape":r["shape"],"habitat":r["habitat"],
                "evo":r["evo"],"family":r["family"],"stage":r["stage"],"gender":r["gender"],"legendary":r["legendary"],"mythical":r["mythical"],"baby":r["baby"],
                "hp":b.get("hp",""),"attack":b.get("attack",""),"defense":b.get("defense",""),
                "sp_attack":b.get("special-attack",""),"sp_defense":b.get("special-defense",""),
                "speed":b.get("speed",""),"weight_kg":round(r["weight"]/10,1),"height_m":round(r["height"]/10,1),
                "egg_groups":J(r["egg"]),"stat_standouts":J(r["stat"]),"arch":J(r["arch"]),"based_on":J(r["based_on"]),
                "sprite":J(r["sprite"]),"moves":J(r["moves"]),"signature_move":r["signature_move"],"lore":J(r["lore"]),
                "mythology":J(r["mythology"]),"location":J(r["location"]),"trainer":J(r["trainer"]),
                "community_nickname":J(r["nickname"]),"role":J(r["role"]),"other":J(r["other"]),"well_known":r["wk"]})
    print("records:",len(facts))
    print("by gen:",dict(sorted(Counter(r['gen'] for r in facts.values()).items())))
    print("with abilities:",sum(1 for r in facts.values() if r['abilities']),
          "| with genus:",sum(1 for r in facts.values() if r['genus']),
          "| with shape:",sum(1 for r in facts.values() if r['shape']),
          "| curated arch:",sum(1 for r in facts.values() if r['arch']))
    bad=[n for n,r in facts.items() if not r['types'] or not r['abilities']]
    if bad: print("WARN missing types/abilities:",bad[:10])
    print("OK")

if __name__=="__main__": main()
