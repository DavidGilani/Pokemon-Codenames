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

- **Board:** 9 blue + 15 neutral + **1 assassin**. **No red tiles** — a red
  tile would play identically to a neutral for a solo player, so it's removed.
- **Scoring (rule "B′"):** you may keep tapping until you either find all 9
  blue (win) or make your **3rd mistake** (i.e. 2 mistakes allowed; the 3rd
  ends the game). On finish, reveal the full board and show a **share button**.
  Score = blues found / 9, plus neutrals hit and time taken.
- **Assassin:** kept, but instant-end on tap. It's safe because we author the
  clues *after* seeing the whole board and verify no clue leans toward the
  assassin before locking it. When a blue shares the assassin's obvious theme
  (e.g. a blue Fighting type with a Fighting assassin), we must clue that blue
  by a DIFFERENT handle (name-pun/sprite/colour), never the shared theme.
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
- **Category 5 — Stats / deep Pokédex / anti-clue.** The most sophisticated:
  base-stat standouts (**highest Special Attack**, **huge HP**, **fastest**,
  **heaviest**), obscure dex facts, and **anti-clues** (`LEGENDARY × 0` = none
  of your blues are legendary — used to fence off a tempting neutral). These
  link tiles that share nothing visible, so they're the hardest to spot.

Guidance: try for roughly **1–2 Category-1 anchors + a couple of 2–3 + at least
one 4–5** per puzzle. Never make all five Category 1.

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
