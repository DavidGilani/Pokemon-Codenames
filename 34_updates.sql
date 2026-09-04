-- 34_updates.sql — fix blank tiles for space/hyphen name mismatches.
--
-- Board tiles join to the `pokemon` table by name. Boards (and pokemon_facts.json)
-- use hyphens for the Treasures of Ruin — Ting-Lu, Wo-Chien, Chien-Pao, Chi-Yu —
-- but the `pokemon` table stores them with spaces ("Ting Lu", …). The old join
--   lower(pk.name) = lower(t->>'name')
-- therefore missed, so pokemon_id/sprite_url came back null and the tile rendered
-- with no image. Normalise by stripping BOTH spaces and hyphens on each side
-- (verified against the live table: this collapses no two distinct Pokémon, and
-- leaves ♀/♂/'/. untouched so Nidoran♀ ≠ Nidoran♂). Applied to all three
-- tile-serving RPCs. (Already applied to the live DB via MCP.)

create or replace function public.get_daily_puzzle(p_pool text)
 returns table(puzzle_date date, clues jsonb, tiles jsonb)
 language sql security definer set search_path to 'public'
as $function$
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
      left join pokemon pk on lower(replace(replace(pk.name,' ',''),'-','')) = lower(replace(replace(t->>'name',' ',''),'-',''))
    ) as tiles
  from daily_puzzles dp
  where dp.pool = p_pool and dp.puzzle_date <= current_date
  order by dp.puzzle_date desc
  limit 1;
$function$;

create or replace function public.get_daily_full(p_pool text)
 returns table(puzzle_date date, tiles jsonb, sealed text)
 language sql security definer set search_path to 'public'
as $function$
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
      left join pokemon pk on lower(replace(replace(pk.name,' ',''),'-','')) = lower(replace(replace(t->>'name',' ',''),'-',''))
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
$function$;

create or replace function public.get_daily_qa(p_date date, p_pool text)
 returns table(puzzle_date date, tiles jsonb, sealed text)
 language sql security definer set search_path to 'public'
as $function$
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
      left join pokemon pk on lower(replace(replace(pk.name,' ',''),'-','')) = lower(replace(replace(t->>'name',' ',''),'-',''))
    ) as tiles,
    public._daily_seal(jsonb_build_object(
      'c', (select jsonb_object_agg(t->>'position', t->>'colour') from jsonb_array_elements(dp.tiles) t),
      'h', coalesce(dp.hints, '[]'::jsonb),
      'k', dp.clues
    )) as sealed
  from daily_puzzles dp
  where dp.pool = p_pool and dp.puzzle_date = p_date
  limit 1;
$function$;
