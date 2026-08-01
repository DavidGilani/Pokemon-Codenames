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

- **The site owner is usually on mobile.** When giving SQL to run, **always
  print it as a copyable code block in chat**, formatted to paste straight
  into the Supabase SQL editor.
- **Pull requests**: when a PR is created, **always include the PR URL** in
  chat. Assume any PR already created has been merged — so for follow-up
  work, **create a brand-new PR** (or, when asked, commit straight to `main`)
  rather than reusing an old branch/PR.
- Prefer **friendly, non-jargon UI language** ("clue giver"/"clue receiver",
  "neutral" not "bystander", no "spymaster").
- Keep changes shippable on `main` (Vercel auto-deploys from it).
