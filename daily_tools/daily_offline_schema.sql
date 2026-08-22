-- 31_updates.sql
--
-- Two daily-puzzle upgrades (batched with the Aug 31 - Sep 6 puzzle data below):
--
--   (1) Per-clue explanations. Each base clue now carries an "explain" sentence
--       (why the clue points at those Pokemon + which category it is). The end
--       screen shows it under each clue. get_daily_puzzle strips it mid-game so
--       it can't leak the answers early.
--
--   (2) Offline play. New RPC get_daily_full returns the whole puzzle "sealed":
--       the colour key + hints (with targets) + clues (with targets and
--       explanations), XOR-obfuscated + base64 so it isn't plain text in the
--       network response. The client unseals it once at load and then does every
--       reveal / hint / finish LOCALLY, so a player who loses connection after
--       the page has loaded can still finish the puzzle.
--
-- Safe to re-run (create-or-replace + upsert).

-- ----------------------------------------------------------------------------
-- _daily_seal: XOR-obfuscate a jsonb payload with a fixed repeating key, then
-- base64-encode it. The matching key + un-seal live in app.js. This is light
-- obfuscation (not encryption) - enough that the answers aren't readable at a
-- glance, while letting the whole puzzle be played offline once loaded.
-- ----------------------------------------------------------------------------
create or replace function public._daily_seal(p jsonb)
returns text
language plpgsql
immutable
set search_path = public
as $$
declare
  b bytea;
  i int;
  n int;
  k int[] := array[142,55,91,44,116,17,163];
begin
  b := convert_to(p::text, 'UTF8');
  n := octet_length(b);
  for i in 0..n-1 loop
    b := set_byte(b, i, get_byte(b, i) # k[(i % 7) + 1]);
  end loop;
  return encode(b, 'base64');
end;
$$;

-- ----------------------------------------------------------------------------
-- get_daily_puzzle: serve today's board + base clues WITHOUT target positions
-- OR the explanation text (both must stay hidden until the game ends).
-- ----------------------------------------------------------------------------
create or replace function public.get_daily_puzzle(p_pool text)
returns table(puzzle_date date, clues jsonb, tiles jsonb)
language sql
security definer
set search_path = public
as $$
  select dp.puzzle_date,
    (
      select jsonb_agg((c - 't' - 'explain') order by ord)
      from jsonb_array_elements(dp.clues) with ordinality as x(c, ord)
    ) as clues,
    (
      select jsonb_agg(
        jsonb_build_object(
          'position',   (t->>'position')::int,
          'name',       t->>'name',
          'pokemon_id', pk.id,
          'sprite_url', pk.sprite_url
        ) order by (t->>'position')::int
      )
      from jsonb_array_elements(dp.tiles) t
      left join pokemon pk on lower(pk.name) = lower(t->>'name')
    ) as tiles
  from daily_puzzles dp
  where dp.pool = p_pool and dp.puzzle_date <= current_date
  order by dp.puzzle_date desc
  limit 1;
$$;

-- ----------------------------------------------------------------------------
-- get_daily_full: today's board (tiles WITHOUT colours, for rendering) plus a
-- sealed blob carrying everything needed to play + finish OFFLINE:
--   c = { position -> colour },  h = hints (with t),  k = clues (with t+explain)
-- ----------------------------------------------------------------------------
create or replace function public.get_daily_full(p_pool text)
returns table(puzzle_date date, tiles jsonb, sealed text)
language sql
security definer
set search_path = public
as $$
  select dp.puzzle_date,
    (
      select jsonb_agg(
        jsonb_build_object(
          'position',   (t->>'position')::int,
          'name',       t->>'name',
          'pokemon_id', pk.id,
          'sprite_url', pk.sprite_url
        ) order by (t->>'position')::int
      )
      from jsonb_array_elements(dp.tiles) t
      left join pokemon pk on lower(pk.name) = lower(t->>'name')
    ) as tiles,
    public._daily_seal(jsonb_build_object(
      'c', (
        select jsonb_object_agg(t->>'position', t->>'colour')
        from jsonb_array_elements(dp.tiles) t
      ),
      'h', coalesce(dp.hints, '[]'::jsonb),
      'k', dp.clues
    )) as sealed
  from daily_puzzles dp
  where dp.pool = p_pool and dp.puzzle_date <= current_date
  order by dp.puzzle_date desc
  limit 1;
$$;

grant execute on function public.get_daily_puzzle(text) to authenticated;
grant execute on function public.get_daily_full(text)   to authenticated;

