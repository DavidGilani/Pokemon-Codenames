"""
Pokemon Codenames - one-off ingestion script.

Pulls the base Pokemon species for generations 1-9 from PokeAPI and loads them
into the `pokemon` table in Supabase. Run this locally whenever you want to
(re)build the reference data. It upserts on id, so it is safe to run repeatedly.

Only nine API calls are made in total (one per generation), which respects
PokeAPI's fair-use policy. Sprite image URLs are constructed from the id rather
than fetched, so we never hammer the API.

Usage:
    1. pip install -r requirements.txt
    2. Create a .env file next to this script with:
           SUPABASE_URL=...
           SUPABASE_SERVICE_ROLE_KEY=...
    3. python ingest_pokemon.py
"""

import os
import time

import requests
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_ROLE_KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]

POKEAPI = "https://pokeapi.co/api/v2"
OFFICIAL_ART = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
    "sprites/pokemon/other/official-artwork/{id}.png"
)

GENERATIONS = range(1, 10)  # generations 1 through 9

# Display-name overrides for species whose slug does not title-case cleanly.
# Extend this freely - anything not listed just gets its slug prettified.
NAME_OVERRIDES = {
    "mr-mime": "Mr. Mime",
    "mime-jr": "Mime Jr.",
    "mr-rime": "Mr. Rime",
    "ho-oh": "Ho-Oh",
    "porygon-z": "Porygon-Z",
    "type-null": "Type: Null",
    "jangmo-o": "Jangmo-o",
    "hakamo-o": "Hakamo-o",
    "kommo-o": "Kommo-o",
    "tapu-koko": "Tapu Koko",
    "tapu-lele": "Tapu Lele",
    "tapu-bulu": "Tapu Bulu",
    "tapu-fini": "Tapu Fini",
    "nidoran-f": "Nidoran (F)",
    "nidoran-m": "Nidoran (M)",
    "farfetchd": "Farfetch'd",
    "sirfetchd": "Sirfetch'd",
    "flabebe": "Flabebe",
}

# A starter set of well-known Pokemon for the "well-known only" toggle.
# This is content, not logic - grow or trim it to taste. Entries are slugs.
WELL_KNOWN = {
    # Gen 1
    "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard",
    "squirtle", "wartortle", "blastoise", "caterpie", "pidgey", "rattata",
    "pikachu", "raichu", "sandshrew", "clefairy", "vulpix", "jigglypuff",
    "wigglytuff", "zubat", "meowth", "psyduck", "growlithe", "poliwag",
    "abra", "machop", "geodude", "ponyta", "slowpoke", "magnemite",
    "gastly", "haunter", "gengar", "onix", "cubone", "hitmonlee", "koffing",
    "rhyhorn", "chansey", "kangaskhan", "horsea", "goldeen", "staryu",
    "mr-mime", "scyther", "jynx", "electabuzz", "magmar", "pinsir", "tauros",
    "magikarp", "gyarados", "lapras", "ditto", "eevee", "vaporeon", "jolteon",
    "flareon", "porygon", "snorlax", "articuno", "zapdos", "moltres",
    "dratini", "dragonair", "dragonite", "mewtwo", "mew",
    # Gen 2
    "chikorita", "cyndaquil", "totodile", "togepi", "ampharos", "espeon",
    "umbreon", "murkrow", "wobbuffet", "steelix", "scizor", "heracross",
    "sneasel", "houndoom", "tyranitar", "lugia", "ho-oh", "celebi",
    # Gen 3
    "treecko", "torchic", "mudkip", "gardevoir", "sableye", "aggron",
    "mawile", "manectric", "wailord", "flygon", "milotic", "absol",
    "salamence", "metagross", "latias", "latios", "kyogre", "groudon",
    "rayquaza", "jirachi", "deoxys",
    # Gen 4
    "turtwig", "chimchar", "piplup", "luxray", "garchomp", "lucario",
    "hippowdon", "toxicroak", "weavile", "magnezone", "leafeon", "glaceon",
    "gliscor", "mamoswine", "gallade", "rotom", "dialga", "palkia", "giratina",
    "darkrai", "arceus",
    # Gen 5
    "snivy", "tepig", "oshawott", "zoroark", "sawk", "throh", "scrafty",
    "hydreigon", "volcarona", "reshiram", "zekrom", "kyurem", "genesect",
    # Gen 6
    "chespin", "fennekin", "froakie", "greninja", "talonflame", "aegislash",
    "sylveon", "goodra", "xerneas", "yveltal", "zygarde",
    # Gen 7
    "rowlet", "litten", "popplio", "decidueye", "incineroar", "primarina",
    "mimikyu", "kommo-o", "tapu-koko", "solgaleo", "lunala", "necrozma",
    # Gen 8
    "grookey", "scorbunny", "sobble", "corviknight", "dragapult",
    "zacian", "zamazenta", "eternatus",
    # Gen 9
    "sprigatito", "fuecoco", "quaxly", "meowscarada", "skeledirge",
    "quaquaval", "koraidon", "miraidon",
}


def prettify(slug):
    if slug in NAME_OVERRIDES:
        return NAME_OVERRIDES[slug]
    return " ".join(word.capitalize() for word in slug.split("-"))


def species_id_from_url(url):
    return int(url.rstrip("/").split("/")[-1])


def fetch_generation(gen):
    resp = requests.get(f"{POKEAPI}/generation/{gen}", timeout=30)
    resp.raise_for_status()
    data = resp.json()

    rows = []
    for species in data["pokemon_species"]:
        sid = species_id_from_url(species["url"])
        slug = species["name"]
        rows.append(
            {
                "id": sid,
                "name": prettify(slug),
                "slug": slug,
                "generation": gen,
                "sprite_url": OFFICIAL_ART.format(id=sid),
                "is_well_known": slug in WELL_KNOWN,
            }
        )
    return rows


def main():
    supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

    all_rows = []
    for gen in GENERATIONS:
        print(f"Fetching generation {gen}...")
        all_rows.extend(fetch_generation(gen))
        time.sleep(1)  # be gentle on PokeAPI's fair-use policy

    all_rows.sort(key=lambda r: r["id"])

    print(f"Upserting {len(all_rows)} Pokemon into Supabase...")
    batch_size = 200
    for i in range(0, len(all_rows), batch_size):
        batch = all_rows[i : i + batch_size]
        supabase.table("pokemon").upsert(batch).execute()
        print(f"  upserted {i + len(batch)} / {len(all_rows)}")

    well_known = sum(1 for r in all_rows if r["is_well_known"])
    print(f"Done. {len(all_rows)} Pokemon loaded, {well_known} flagged well-known.")


if __name__ == "__main__":
    main()
