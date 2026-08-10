# 1-player Daily Puzzle — design notes & prototype

Scratch/design doc (not wired into the live app yet). Captures the plan, some
worked example puzzles, and how we can learn from real player data.

## The concept (as agreed for the first cut)

- **One player.** No clue giver — the clues are pre-written ("by the AI").
- **5×5 board, 9 blue tiles** (same tile counts as a co-op board: 9 blue,
  15 neutral, 1 assassin).
- The player is given **exactly 5 clues**, each with a number, that between them
  cover all 9 blue tiles (e.g. 2+2+2+2+1, or 3+2+2+1+1).
- The player gets **one turn** to find all 9 blue tiles. Success = all 9 found.
- **Two puzzles per day:** one drawn from **Gen I only**, and one drawn from
  **any generation (mixed)**. Same two puzzles for everyone that day
  (a "Wordle-style" daily), each with a shareable result.
- **Board-first generation** (owner preference): deal the 25 tiles randomly
  first, THEN write clues for whatever blues came up. This yields far more
  interesting, creative clues than choosing blues to fit a clue.
- **Player help:** the player may request **up to 3 extra clues** (one at a
  time) if stuck, so they can still finish with some assistance. (Track how many
  hints were used in the result/stats.)

## Locked decisions (from owner feedback)

- **Board:** 9 blue + **16 neutral**. **No red tiles and NO assassin** — both
  play identically to a neutral for a solo player, so the board is just 9 blue
  vs 16 neutral. (Earlier drafts kept an assassin; it was removed.)
- **Scoring:** you may keep tapping until you either find all 9 blue (win) or
  make your **5th mistake** (i.e. 4 mistakes allowed; the 5th ends the game —
  loosened from 3 so players get a bit more rope). On finish, reveal the full
  board, show **which Pokémon each clue was pointing to**, and show a **share
  button**. Score = blues found / 9, plus neutrals hit and time taken.
- **Share text carries NO board grid** — that would hand the answers to whoever
  you share with. Share only: outcome (all 9 or not), mistakes, guesses, time,
  and the difficulty label.
- **Difficulty badge (shown to the player):** derived from the clue-category
  spread — `highs`(cat≥4)≥4 → Evil, ≥3 → Brutal; else by count of cat-1 clues:
  0 → Hard, 1 → Challenging, 2 → Medium, 3+ → Easy.
- **Brutal / Evil structural gate (NEW):** the category spread above is
  necessary but NOT sufficient. For a board to ship as **Brutal or Evil** it must
  ALSO satisfy both:
  1. **At most ONE `× 1` clue** (i.e. at most one clue that points to a single
     tile). The rest must each group ≥ 2 blues.
  2. **The clue numbers must sum to ≥ 11** — i.e. at least **two overlaps**
     (a blue appearing under a second clue) beyond the 9 tiles. This forces the
     "which tile is double-clued?" ambiguity that makes the top tiers actually
     hard. If a board hits the category spread but fails either test, tighten the
     clues (merge singletons, add overlap) or label it Hard instead.
- **Randomise TILE positions (NEW — important):** the 9 blue tiles must be
  scattered to random grid positions, NOT left in a fixed pattern. The
  board-authoring convention put blues at positions `0,2,4,6,8,10,12,14,16`
  (a fixed checkerboard) on every board, which produced the exact same visual
  layout every single day — a dead giveaway for regulars. When emitting a
  puzzle, apply an independent random permutation of the 25 positions and remap
  the tiles AND every clue/hint `t` array through it together. (`28_updates.sql`
  retro-shuffled all saved boards.)
- **Randomise clue order (NEW):** the 5 base clues (and the hint list) must be
  shuffled, NOT listed in board order. Do not order clues to follow the tiles
  top-to-bottom / left-to-right — that quietly leaks which clue maps to which
  region of the grid. Shuffle the `clues` array (and `hints`) before storing.
- **No clue reuse within a rolling 2 weeks (NEW):** to keep the daily fresh for
  regulars, a **(clue word → exact target Pokémon)** pairing and a **(clue word →
  exact group of Pokémon)** pairing may NOT repeat within the **previous 14 days**
  of puzzles, counting **both pools together**. E.g. if `FINS → Garchomp` or
  `PSEUDO → {Garchomp, Tyranitar, Salamence}` was used in the last fortnight,
  pick a different handle. Also avoid leaning on the same clue *word* many days
  running even against different Pokémon — vary the vocabulary.
- **Extra clues are conditional + unlimited.** Hints carry hidden target
  positions; `daily_hint_next` serves the un-shown hint covering the most
  STILL-UNREVEALED blues (tie-break: easier category first). So **every blue
  must be covered by at least one hint** (grouped is fine), and hints should be
  **easier** than the base clues. The player can keep asking until no helpful
  clue remains.
- **Clues:** all **5 shown at once**. Single words.
  - **Group generously:** a clue can cover as many blues as genuinely fit
    (2, 3, 4, even more) — don't split a clean group into singletons. If BUG
    covers 4 blues, make it `BUG × 4`.
  - **Overlap is GOOD and preferred where achievable:** a blue may appear in
    more than one clue (numbers can sum to >9), which adds a nice "which tile is
    double-clued?" layer — but **no two clues may cover the *exact same* set**
    of blues.
  - **Anti-clues (number 0):** a clue may state a category with `× 0`, meaning
    **none of your blues are in it**. Use it to eliminate a tempting neutral —
    e.g. `LEGENDARY × 0` tells the player the legendary bird Articuno is NOT
    theirs, disambiguating a `BIRD` clue. Anti-clues count as one of the 5 and
    cover no tiles.
  - **Not traps:** clues are our best attempt to lead the player to all 9 blues
    and away from neutrals; we do NOT plant neutral collisions on purpose. Some
    residual risk is fine (and unavoidable on a random board) — note it, don't
    engineer it.
- **Timer:** runs for the attempt (starts on first tap) and is included in the
  shareable result.
- **Stats:** show blues found, neutrals hit, hints used, and time.
  **Streaks:** deferred — they'd rely on browser cache (`localStorage`), which
  breaks across devices without login, so not worth it for v1.
- **Generation:** two dailies — one Gen-I-only, one mixed (any generation).

## Where the clues come from — my recommendation

**Pre-generate puzzles offline and store them; do NOT call an LLM live in the
browser.** Reasons: there's no backend to hold an API key safely, clue quality
needs a human glance before it goes live, and a daily puzzle only needs one new
puzzle per day (cheap to batch a month ahead).

Concretely:
1. A small generator (script or just me, by hand at first) produces a dated
   puzzle: 25 Pokémon, which 9 are blue, and 5 clues with numbers + the blue
   tiles each clue is meant to link (kept server-side / not shown).
2. Store puzzles in a new Supabase table `daily_puzzles(date, board jsonb,
   clues jsonb, ...)` with RLS so the answer key isn't readable until after
   you submit (mirroring how `card_key` is hidden today).
3. The client loads **today's** puzzle, shows the 5 clues, takes one turn,
   scores it, and shows a shareable emoji-grid result.

**Do I need the Supabase human data to write clues?** Not strictly — public
Pokémon knowledge (types, colours, evolutions, Pokédex lore, name puns,
habitats, legendary groupings) is more than enough to write strong clues, and
the worked examples below were written that way. But your real data is genuinely
useful for **calibrating difficulty and tone** — seeing what words real clue
givers reach for, how ambitious their numbers are, and which links land. So
it's worth exporting.

## How to export the learning data (run in Supabase SQL editor)

This dumps, per finished game, the full board (Pokémon + secret colour) and the
clues + guesses that were actually played. Export the result as CSV/JSON from
the Supabase UI and send it over — I'll use it to tune clue style/difficulty.

```sql
select jsonb_pretty(jsonb_build_object(
  'mode',      r.mode,
  'clue_log',  r.clue_log,   -- [{team, word, number}]
  'guess_log', r.guess_log,  -- [{clue_index, name, colour, correct}]
  'board', (
    select jsonb_agg(
      jsonb_build_object('name', c.name, 'colour', k.colour)
      order by c.position
    )
    from cards c
    join card_key k on k.room_id = c.room_id and k.position = c.position
    where c.room_id = r.id
  )
)) as game
from rooms r
where r.clue_log is not null
  and r.clue_log <> '[]'::jsonb
order by r.created_at desc
limit 500;
```

(If `created_at` doesn't exist on `rooms`, drop the `order by` line.)

## Rule 0 — every clue must be CORRECT (non-negotiable)

A clue is **incorrect** if the property it names is true of **any tile that is
not one of your blues** (a neutral or the assassin). It doesn't matter that the
player *might* still guess right — the clue itself is wrong if it links tiles
that aren't all blue.

- ❌ `PSYCHIC × 2` when a neutral (or the assassin) is also Psychic-type.
- ❌ `BLUE × 3` when there are blue-coloured neutrals on the board (dense boards
  make colour clues frequently illegal — check every tile).
- ✅ Correct means: the clue's property holds for **exactly** its listed blues
  and for **no other tile** on the board.

This is why the generator is board-first + re-deal: on a random board most
type/colour words are *incorrect* (shared by a neutral), so we lean on narrower
handles (sprite/lore/pun/stats) or re-deal. Always verify correctness against
all 25 tiles before locking a clue. `WYRM × 3` for the dragons is fine only if
no neutral/assassin is Dragon-type (note: a dragon-*looking* Gyarados is
Water/Flying, so it is correctly excluded — that nuance is fair difficulty).

## Clue-difficulty categories (aim for a spread of 1–5)

Tag every clue with a difficulty category. A good puzzle **mixes** them — some
easy anchors, some sophisticated ones — so it's achievable but has bite.

- **Category 1 — Type / Colour.** The simplest: `FIRE`, `GHOST`, `WATER`,
  `PINK`, `YELLOW`. Easiest to read, but on a dense board they're often
  *incorrect* (see Rule 0) — use only when the property is unique to the blues.
- **Category 2 — Sprite / visual.** Something you can see in the on-tile image:
  `SKULL` (Cubone), `PUPA` (Kakuna), `FROG` (Greninja), `HEADS` (Hydreigon),
  `SIX` (Exeggcute). A step up because you read the picture, not a label.
- **Category 3 — Trait / behaviour.** How it acts or what it does: `DIGGER`,
  `KICK` (Blaziken), `NINJA`, `SLEEP`.
- **Category 4 — Lore / Pokédex flavour / pun.** Dex nicknames and wordplay:
  `AURA` (Lucario, the Aura Pokémon), `ORPHAN` (Cubone), `KING`→Nido**king**,
  `LAND-SHARK` (Garchomp).
- **Category 5 — Stats / deep Pokédex / anti-clue / connection / mythology.** The
  most sophisticated. These link tiles that share **nothing visible**, so they're
  the hardest to spot:
  - **Stats:** base-stat standouts (**highest Special Attack**, **huge HP**,
    **fastest**, **heaviest**).
  - **Anti-clues** (`LEGENDARY × 0` = none of your blues are legendary).
  - **Connection (NEW):** a hidden relationship with no on-tile tell — same
    **Ability** (`INTIMIDATE`, `LEVITATE`), a shared **signature move**, same
    **evolution method** (`TRADE`, `STONE`), same **egg group**, or **debut
    region** (mixed only). Cross-type by nature; keep to well-known facts.
  - **Mythology / folklore origin (NEW):** the real myth a Pokémon is built on —
    `KITSUNE` (Ninetales), `PHOENIX`, `GENIE`, `GOLEM`. Knowledge-gated.

- **NEW mid-hard category — Real-world archetype (Cat 3–4).** The *real animal*
  the Pokémon is based on, **spanning types**: `CANINE`, `FELINE`, `RAPTOR`,
  `PRIMATE`, `CEPHALOPOD`, `CRUSTACEAN`, `SERPENT`, `EQUINE`, `URSINE`. Harder
  than a type clue because you must abstract past the Pokémon's typing (a Fire
  dog + a Normal dog + a Dark dog all = `CANINE`). Tag the obvious ones Cat 3,
  the abstract ones Cat 4.

**Category 2 is nearly as easy as Category 1.** A sprite clue (`HORN`, `THREE`,
`SHELL`, `BLADES`) is *read, not thought* — so a board built mostly from Cat-2
clues plays easy even with zero Cat-1 clues. That's why the top tiers **cap**
Cat-2 usage (see the mix table below).

## Category mix per difficulty tier (balancing)

Difficulty is not just "how many Cat-1 clues" — it's the whole mix, and the
easy-to-read categories (1 and 2) are **capped** from Hard upward so the
knowledge categories carry the weight. Target mix over the 5 base clues:

| Tier | Cat 1 | Cat 2 (sprite) | Cat 3–5 | also required |
|------|-------|----------------|---------|---------------|
| Easy | 3–4 | rest | — | — |
| Medium | 2 | ~2 | ≥1 (Cat 3–4) | — |
| Challenging | 1 | ≤2 | ≥2 (Cat 3–4) | — |
| **Hard** | 0 | **≤1** | exactly **2 Cat 4–5** + ≥1 Cat 3 | — |
| **Brutal** | 0 | ≤1 | exactly **3 Cat 4–5** | ≤1 `×1` clue, sum ≥ 11 |
| **Evil** | 0 | **0** | **≥4 Cat 4–5** | ≤1 `×1` clue, sum ≥ 11 |

This keeps the **displayed** badge (`highs`=cat≥4: ≥4→Evil, 3→Brutal; else by
Cat-1 count 0/1/2/3+ → Hard/Challenging/Medium/Easy) in agreement with the
authored intent: Hard = exactly 2 highs, Brutal = exactly 3, Evil = ≥4.

Guidance beyond the table: never make all five Category 1; prefer richer
multi-tile Cat 4–5 clues over strings of `×1` sprite clues.

**No disguised-type clues (IMPORTANT).** A higher-category clue must not simply
be a type word in disguise. `BLAZE`/`FLAME`/`INFERNO` = Fire, `SHADE`/`PHANTOM`
= Ghost, `WYRM`/`DRAKE` = Dragon, `DIRT`/`EARTH` = Ground, `AQUA`/`WAVE` =
Water, `BOLT`/`VOLT` = Electric, `FROST` = Ice, `TOXIN` = Poison, `PETAL`/`LEAF`
= Grass, etc. If the blues a clue links share **only a type**, a fancy synonym
adds no challenge over the plain type word — so **do not use it as one of the 5
base clues**. Instead:
- Use the **honest type word** (`FIRE`, `GHOST`, `WATER`…) as a plain Cat-1
  anchor — but **at most 1–2 type/colour anchors per board**.
- Make the other 3–4 clues **genuinely non-type**: group by sprite feature
  (`HORN`, `THREE`, `BLADES`, `SHELL`), lore/pun (`FOSSIL`, `PSEUDO`, `ORPHAN`,
  `ROYALS`, `BOND`), behaviour (`DIGGER`, `SING`, `KICK`), or stats — and prefer
  groupings that **span multiple types** (that's what makes them hard).
- Colour clues (`PINK`, `YELLOW`) are fine and are NOT type disguises — colour
  is a legitimate separate handle (as in classic Codenames).

**Skew harder (playtest feedback):** the first live puzzles played **too easy**.
The main lever is not just *which* categories but *how the hard ones group*:

- **Make higher-category clues cover MULTIPLE blues, not single tiles.** A
  Category-4/5 clue that links 3–4 blues (e.g. a shared Pokédex trait, a
  base-stat standout like *highest Special Attack*, or a subtle lore theme) is
  far more challenging — and more satisfying — than five easy 1-tile clues.
- Avoid puzzles that are mostly "one clue → one obvious Pokémon". Those solve
  themselves. Prefer fewer, richer, multi-tile clues at the harder tiers.
- Use the `daily_attempts` data (times, mistakes, ratings) to calibrate: if
  win-rates and speeds are high and ratings skew "too easy", push more
  Category-4/5 grouped clues.

## Generation scope

- **Gen I daily:** draw only from Gen I (Pokédex 1–151).
- **Mixed daily:** draw from **all generations, Gen I–IX**. The Supabase
  `pokemon` table contains **every Pokémon from all 9 generations**, so any
  national-dex name resolves to a sprite — use the full dex for the mixed pool.

## Clue-word restriction rule (IMPORTANT — must match the live site)

The live site (`clueOverlapsPokemon` in `app.js`) rejects a clue that shares a
**4+ character substring** with any Pokémon on the board (either direction),
case/punctuation-insensitive.

**For authoring Daily puzzles we use a STRICTER rule:** a clue word must not
share **3 or more consecutive letters** with ANY Pokémon on the board (blue,
neutral, or assassin), in either direction. So:
- ❌ `RAT` for Raticate, `CHOP` for Machop, `CROW` for Murkrow, `FAIRY` for
  Clefairy (the clue is a fragment of the name).
- ❌ `PINK` when **Weepin**bell is on the board (`pin`), `GROUND` when
  H**oun**doom is on the board (`oun`), `COCOON` when Tenta**coo**l is present
  (`coo`), `GRASS` when La**pras** is present (`ras`).
- ✅ Use a synonym/alt handle instead: `ROSY` (not PINK), `DIRT` (not GROUND),
  `PUPA` (not COCOON), `PLANT`/`PITCHER` (not GRASS).

Always run this check against all 25 names before locking a clue.

## Use the sprites — niche, specific clues welcome

Clues are chosen with the **on-tile sprite** in mind, not just type/colour.
Sprite details unlock clues that separate look-alikes:
- `FIST` / `PUNCH` for Machop (its sprite punches toward the camera) — a way to
  clue it *without* the word "fight", which would also point at a Fighting
  assassin like Poliwrath.
- `PUPA` (Kakuna's cocoon), `SKULL` (Cubone's helmet), `SIX` (Exeggcute's six
  eggs), `TONGUE` (Lickitung), `GIFT` (Delibird's sack), `DINO` (Tyranitar),
  `PITCHER` (Victreebel/Weepinbell).

## Board-first + re-deal (how the generator should work)

Deal 25 random tiles (9 blue / 15 neutral / 1 assassin) first, then try to
cover all 9 blues with ≤5 clean clues. **Most random boards can't be covered in
5 clean clues** — the 9 blues usually form only 2–3 natural groups plus several
loners. So the generator must **re-deal** until it finds a board whose blues
cluster enough for 5 clues (this is cheap). Concretely, keep a board only if the
blues can be covered by clue-groups (shared type/colour/shape/lore) that are
**absent from every neutral and the assassin**, in ≤5 groups. Then hand-/AI-
finish the exact clue words (adding sprite/pun handles) and run the letter-rule
and assassin checks.

## Worked test examples

Current batch: **`daily_puzzle_batch_v2.json`** — 4 board-first puzzles (2 Gen I,
2 mixed) generated by the re-deal method above, each solvable in exactly 5 clues,
all passing the strict letter rule, with `decoys` noted (inherent risk, not
planted) and `kind`/sprite rationale per clue.

## Clue-writing principles (learned from the exported player data)

Strong human clues in the export were single words of a few kinds — the register
to target:
- **Type:** Bird, Water, Poison, Ghost, Dragon, Psychic.
- **Colour:** Blue, Pink.
- **Shape/trait:** Round, Pointy, Legless.
- **Lore / pun / sprite:** Pearl→Shellder, Otter→Buizel, Ruff→(dog),
  King→Nido**king**, Fist→Machop's punching sprite.

Hard rules for our solo clues (helpers, never traps):
1. Every clue points only at blue tiles; before locking it, confirm no neutral
   and **especially not the assassin** plausibly matches.
2. Prefer the **narrowest** word that links the intended blues (e.g. "TURTLE"
   not "WATER" when non-turtle Water neutrals are about).
3. **Mix the clue kinds** across the 5 — don't lean on types alone; on a random
   board a type is usually shared by a neutral/assassin.
4. **Group generously** (a clue can cover 4+ blues) and **favour overlap** —
   reuse a blue across clues for depth — but **no two clues share the identical
   set** of blues.
5. Obey the **letter rule** (no 3+ consecutive letters of any board name).
6. Consider the **sprite** for niche clues.
7. Consider an **anti-clue** (`× 0`) to fence off a dangerous neutral.

## Status — mode is now BUILT (v1 live on `main`)

- `20_updates.sql` creates the `daily_puzzles` table (RLS on, no direct reads)
  and the key-hiding RPCs: `get_daily_puzzle` (board without colours),
  `daily_reveal` (one tile's colour), `daily_hint` (one extra clue on request),
  `daily_solution` (full board for the end reveal). It seeds **two puzzles for
  today** — a Gen I board and a mixed (Gen I–VIII sample) board — each with
  `cat` difficulty tags and 3 hint clues.
- Client: a "Daily puzzle" card on the landing page (Gen I / All gens), a solo
  play screen with the 5 clues (+ Lv difficulty badges, anti-clues shown as
  `× 0`), tap-to-reveal via RPC, hearts/mistakes, hint button (up to 3), a timer
  that starts on the first tap, and a shareable emoji-grid result.

### Editing / adding puzzles in Supabase (the owner's edit path)
`daily_puzzles` rows are plain jsonb — edit `clues`, `hints`, or `tiles`
directly in the Supabase table editor, or `insert` a new `(puzzle_date, pool)`
row. `get_daily_puzzle` serves the latest row with `puzzle_date <= today`, so to
schedule ahead just insert future-dated rows.

### Next
1. Feedback on the two seeded puzzles (difficulty/tone/clue mix)?
2. Generate a reviewable multi-day batch (proper Gen I–IX for the mixed pool).
3. Optional hardening: enforce "finished" server-side before `daily_solution`
   can be called (v1 trusts the client).
