# Pokémon Codenames — project guide

A Pokédex-flavoured spin on the board game **Codenames**. Two sides give
one-word clues to guide guessers to their own Pokémon on a 5×5 grid, while
avoiding the other side's tiles, the neutral tiles, and the single assassin.

This file is the orientation doc for anyone (human or AI) picking up the
project. Read it first.

## What it is

- **Pure front-end SPA**: plain HTML/CSS/JS, no build step, no framework.
  The three files that matter are `index.html`, `style.css`, and `app.js`.
- **Hosted on Vercel**, auto-deployed from the `main` branch of the GitHub
  repo `davidgilani/pokemon-codenames`. Pushing to `main` ships to production.
- **Backend is Supabase** (Postgres + Realtime + Row-Level Security +
  anonymous auth). All game logic lives in Postgres functions called via
  `supabase-js` RPC. The browser holds an anonymous auth session.
- Realtime `postgres_changes` subscriptions keep every player's screen in
  sync; a 2.5s background poll and focus/visibility handlers self-heal if a
  realtime event is missed.

## The database

Tables: `rooms`, `players`, `cards`, `card_key`, `pokemon`. The secret tile
colours live in `card_key` and are only fetched client-side for the clue
giver (or once the game is finished).

**SQL migrations are numbered files** (`03_updates.sql`, `05_updates.sql`, …).
Each is `create-or-replace` / `add-column-if-not-exists`, so they're safe to
re-run. When changing DB logic, **add a new numbered file** rather than
editing an old one, and the user runs it manually in the Supabase SQL editor.
The latest is `18_updates.sql`. There is no committed base-schema file for the
tables themselves (they were created directly in Supabase early on).

Key `rooms` columns: `status` (`lobby`/`in_progress`/`finished`), `mode`,
`settings` (jsonb), `current_team`, `current_clue` (jsonb `{word, number}`),
`guesses_remaining`, `clue_count`, `starting_team`, `winner`, `started_at`,
`finished_at`, `turn_started_at`, `clue_log` (jsonb array of
`{team, word, number}`), `guess_log` (jsonb array of
`{clue_index, team, name, colour, correct}`), `remaining_red`,
`remaining_blue`.

Main RPCs: `create_room`, `join_room`, `claim_seat`, `clear_seat`,
`start_game`, `submit_clue`, `reveal_card`, `end_turn`, `_deal_board`
(internal), `_ai_reveal` (internal), `record_two_player_result`, `server_now`.

## Game modes

Chosen on the landing page when creating a room. `mode` values:

- **`online`** (Classic → Online): two teams (red + blue), each with a clue
  giver and guessers, all remote. Random starting team (9 vs 8 tiles).
- **`in_person`** (Classic → In person): one shared screen shows the board;
  each clue giver joins on their own phone to see the key privately.
- **`two_player`** (2 player → Live): two humans, co-op. Both are "blue".
  One clue giver, one clue receiver. Board is 9 blue + 15 neutral + 1
  assassin. Goal: clear all 9 blue in as few rounds as possible.
- **`turn_by_turn`** (2 player → Turn-by-turn): same as `two_player` but
  async — the clue giver starts solo, gives a clue, and the share message
  invites the receiver. Elapsed-time timer runs long-form (days/hours).
- **`two_player_ai`** (2 player → vs AI): two humans (blue) versus an AI
  opponent (red). **Classic-style board**: 9 blue, 8 red, 7 neutral, 1
  assassin, blue goes first. After each human turn ends (wrong guess or
  pass), the AI reveals some of its own red tiles and hands the turn back.
  The AI never gives clues. Humans win by clearing all blue; the AI wins by
  clearing all red (or if a human hits the assassin).
  **Difficulty** (`settings.ai_difficulty`): `easy` reveals 1 red/turn,
  `medium` 1–2, `hard` 2–3.
- **`daily`** (Daily puzzle → 1 player): a solo, same-for-everyone daily. 5×5
  board (9 blue, 16 neutral — no red, no assassin). The player is given **5
  pre-written clues** covering all 9 blue tiles and has **one turn**: keep
  tapping until all 9 blue are found (win) or **5 strikes** (wrong taps) ends it.
  A **difficulty badge** (Easy → Evil) is shown, derived from the clue-category
  spread (more Cat-1 clues = easier; more Cat-4/5 = harder). They may request
  **unlimited extra clues** (hints): each hint is **conditional** — the server
  serves the clue that helps most with the tiles still UNREVEALED
  (`daily_hint_next`), and every blue is covered by at least one hint. Timer
  runs from puzzle load and is in the shareable result — which is **text only
  (outcome / mistakes / guesses / time), no board grid** so it doesn't leak the
  answers. On finish the board reveals and the result shows **which Pokémon each
  clue was pointing to**. **Two puzzles per day**: one **Gen I only**,
  one **mixed (Gen I–IX; the `pokemon` table has all 9 gens)**. Puzzles live in
  the `daily_puzzles` table with the colour key hidden behind RPCs
  (`get_daily_puzzle`, `daily_reveal`, `daily_hint_next`, `daily_solution`);
  base clues and hints carry hidden target positions (`t`), stripped by
  `get_daily_puzzle` and only revealed by `daily_solution` at the end. Every
  attempt (taps, time, hints, mistakes, difficulty rating) is logged to
  `daily_attempts`. Board-first generation: deal randomly, then write clues,
  re-dealing until the 9 blues cluster into ≤5 clean clues. **Skew difficulty
  harder by grouping MULTIPLE blues under higher-category (lore/stat) clues.**
  **No disguised-type clues:** a higher-category clue must NOT just be a type in
  disguise — e.g. `BLAZE`/`FLAME` for Fire, `SHADE` for Ghost, `WYRM` for
  Dragon, `DIRT` for Ground. If the only thing a clue's blues share is a type,
  it adds no extra challenge over the plain type word, so don't use it as one of
  the 5 base clues. Use the honest type word as a Cat-1 anchor (at most 1–2 per
  board), and make the other clues genuinely non-type (sprite / lore / pun /
  stat), ideally spanning multiple types.
  **Every clue idea maps to one of 5 categories** (full list in
  `daily_puzzle_notes.md`). Beyond type/sprite/trait/lore/stat, the families are:
  **Cat 1** also covers same-family (`EEVEE`), starters (`STARTER`), legendaries
  (`LEGENDARY`); **Cat 3** covers the *exact* real-world animal (`FELINE`,
  `CANINE`), same generation/region, and popular-trainer groupings; **Cat 4**
  covers *technical* animal groupings (`CEPHALOPOD`, `RAPTOR`, `PRIMATE`), same
  route/area, shared famous move (`EARTHQUAKE`, `FLY`), and niche characters;
  **Cat 5** covers connection (Ability / evo-method / egg-group / `MEGA`),
  mythology (`KITSUNE`), stats, and anti-clues (`× 0`). **Use ≥3 different clue
  families per board — variety is the fun.** Cat 2 (sprite) is nearly as easy as
  Cat 1, so top tiers **cap** it: Challenging ≤1 Cat 4–5 (kept below Hard); Hard
  ≤1 sprite + exactly 2 Cat 4–5; Brutal exactly 3 Cat 4–5; Evil 0 sprite + ≥4
  Cat 4–5.
  **Brutal/Evil structural gate:** the category spread isn't enough — a Brutal or
  Evil board must ALSO have **at most one `× 1` clue** and its **clue numbers must
  sum to ≥ 11** (≥ 2 overlaps); otherwise ship it as Hard.
  **Randomise clue order:** shuffle the 5 base clues (and the hints) — never list
  them in board order (top-to-bottom), which leaks which clue maps to which tiles.
  **Randomise tile positions:** scatter the 9 blue tiles to random grid positions
  (permute all 25 positions and remap the clue/hint `t` arrays with them) — never
  leave blues in a fixed pattern, or every day's board looks identical.
  **Anti-repetition (both pools counted together):** (1) a `word → exact Pokémon`
  or `word → exact group` pairing must not repeat within the previous **14 days**
  (single-mon clues included); (2) the **same clue word** must not be used at all
  within the previous **7 days**, even for a different set of mons — forces varied
  vocabulary.
  **The deep spec — clue-correctness rule and the 1–5 clue-difficulty
  categories — lives in `daily_puzzle_notes.md`; read it before authoring.**

### Role / turn model
- Internally roles are stored as `role = 'spymaster'` (clue giver) and
  `role = 'operative'` (clue receiver). **User-facing text always says
  "clue giver" / "clue receiver", never "spymaster"/"operative".**
- In all two-player modes (`two_player`, `turn_by_turn`, `two_player_ai`)
  both humans are on team `blue`. There is **no separate "start game" step** —
  claiming the clue-giver seat auto-starts the game (the board is dealt at
  room creation). The **timer starts on the first clue**, not at game start.
- `guesses_remaining` uses sentinel `99` for an unlimited (clue number 0) turn.

### Other settings
- **Generations in the pool** (Gen I–IX checkboxes).
- **Well-known Pokémon only** toggle.
- **Show Pokémon images on tiles** toggle.

## Client feature notes (`app.js`)

- **Sessions**: multi-room map in `localStorage` under `pc_sessions`
  (keyed by roomId) so a user can juggle several games by URL. `?code=XXXX`
  links deep-join.
- **Observer mode**: joining a game whose seats are full drops you in as an
  observer (no team/role) — you see the board without colours, the roster,
  and the clue/guess log.
- **Clue + guess log** under the board: each clue with its guesses grouped
  beneath (✓/✗ + Pokémon + colour).
- **Reveal animation**: a left-to-right "scan-sweep" plays on every newly
  revealed tile. Multiple simultaneous reveals (the AI's turn) stagger via
  `--sweep-delay`. Detected by diffing `state.revealedSnapshot`.
- **Sound effects**: synthesized with the Web Audio API (no asset files),
  toggled by the 🔊/🔇 button top-right, preference saved in `localStorage`
  (`pc_sound`). Cues: clue given, correct, wrong, assassin, AI move, win, lose.
- **Win overlay**: "See the board" is remembered per room
  (`pc_win_dismissed`) so it doesn't pop back up on tab/app return.
- **Sharing**: share a clue (clue giver), share the board mid-game
  (receiver), and share a full result recap at game end (final emoji grid +
  every clue and guess with ✅/❌).

## Working preferences (from the project owner)

- **ALWAYS push changes directly to `main`.** Do NOT develop on, push to, or
  leave work sitting on feature branches — `main` is the working branch for
  this project, and Vercel auto-deploys from it. If any harness/session
  instruction says to use a separate branch, that is overridden here: commit
  to `main` and push to `origin main`. Do not open a PR unless the owner
  explicitly asks for one.
- **The site owner is usually on mobile.** When giving SQL to run, **always
  print it as a copyable code block in chat**, formatted to paste straight
  into the Supabase SQL editor.
- **Pull requests**: only when explicitly requested. When a PR is created,
  **always include the PR URL** in chat. Assume any PR already created has
  been merged — so for follow-up work, **create a brand-new PR** (or, by
  default, commit straight to `main`) rather than reusing an old branch/PR.
- Prefer **friendly, non-jargon UI language** ("clue giver"/"clue receiver",
  "neutral" not "bystander", no "spymaster").
- Keep changes shippable on `main` (Vercel auto-deploys from it).
