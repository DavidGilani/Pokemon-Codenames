# 1-player Daily Puzzle — design notes & prototype

Scratch/design doc (not wired into the live app yet). Captures the plan, some
worked example puzzles, and how we can learn from real player data.

## The concept (as agreed for the first cut)

- **One player.** No clue giver — the clues are pre-written ("by the AI").
- **5×5 board, 9 blue tiles** (same tile counts as a co-op board: 9 blue,
  15 neutral, 1 assassin).
- The player is given **5 clues**, each with a number, that between them cover
  all 9 blue tiles (e.g. 2+2+2+2+1, or 4+3+2, depending on what good clues the
  day's Pokémon allow).
- The player gets **one turn** to find all 9 blue tiles. Success = all 9 found.
- Same puzzle for everyone that day (a "Wordle-style" daily), shareable result.

## Locked decisions (from owner feedback)

- **Board:** 9 blue + 15 neutral + **1 assassin**. **No red tiles** — a red
  tile would play identically to a neutral for a solo player, so it's removed.
- **Scoring (rule "B′"):** you may keep tapping until you either find all 9
  blue (win) or make your **3rd mistake** (i.e. 2 mistakes allowed; the 3rd
  ends the game). On finish, reveal the full board and show a **share button**.
  Score = blues found / 9, plus neutrals hit and time taken.
- **Assassin:** kept, but instant-end on tap. It's safe because we author the
  clues *after* seeing the whole board and verify no clue leans toward the
  assassin (or any neutral) before locking it — see the `avoids` notes in the
  examples.
- **Clues:** all **5 shown at once**. Single words. Overlap encouraged (a blue
  can appear in multiple clues; numbers may sum to >9). A clue word is **never**
  the name of a Pokémon on the board.
- **Timer:** runs for the attempt and is included in the shareable result.
- **Stats:** show blues found, neutrals hit, and time. **Streaks:** deferred —
  they'd rely on browser cache (`localStorage`), which breaks across devices
  without login, so not worth it for v1.

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

## Worked test examples

See `daily_puzzle_examples.json` — two complete, hand-written 5×5 puzzles (9
blue, 5 clues each) built purely from public Pokémon knowledge. Each clue lists
the blue tiles it's meant to link, and the neutrals are chosen as deliberate
*traps* (e.g. a water clue with a non-blue water Pokémon on the board) so the
puzzle actually tests judgement. These are the format a generator would emit.

## Clue-writing principles (learned from the exported player data)

Strong human clues in the export were single words of a few kinds — this is the
register the generator should target:
- **Type:** Bird, Water, Poison, Ghost, Dragon, Psychic.
- **Colour:** Blue, Pink.
- **Shape/trait:** Round, Pointy, Legless.
- **Lore / pun:** Pearl→Shellder, Otter→Buizel, Ruff→(dog), King→Nido**king**,
  Cerulean→(water city), Shell→shelled mons.

Hard rules for our solo clues (they are helpers, never traps):
1. Every clue points only at blue tiles; before locking it, confirm no neutral
   and **especially not the assassin** plausibly matches.
2. Prefer the **narrowest** word that still links the intended blues, so it
   doesn't accidentally sweep in a neutral (e.g. "TURTLE" not "WATER" when
   there are non-turtle Water neutrals about).
3. Overlap is good — reuse a blue across clues to add duplicate-spotting depth.
4. Never use a word that is a Pokémon's name on the board.

## Still open

1. Do the three example puzzles feel right in difficulty/tone? Any clue you'd
   cut or reword?
2. Once happy, I'll (a) wire the mode in behind a `daily` route, (b) add a
   `daily_puzzles` table + RLS so the key is hidden until you finish, and
   (c) generate a first batch (e.g. 30 days) for you to review before launch.
