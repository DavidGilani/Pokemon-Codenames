-- 28_updates.sql
--
-- Fix: every daily puzzle had its 9 blue tiles in the SAME fixed grid pattern
-- (positions 0,2,4,6,8,10,12,14,16 — a fixed checkerboard), because the board
-- generator always placed blues at those indices. This shuffles the physical
-- tile positions of EVERY saved daily puzzle (current + future-dated) with an
-- independent random permutation per board, remapping the tiles AND the clue /
-- hint target positions ('t') together so everything stays consistent.
--
-- Safe to run once. Re-running just reshuffles again (still valid).

-- Helper: remap the 't' (target position) array inside a clues/hints jsonb array
-- through a permutation, where p_perm[oldpos + 1] = newpos.
create or replace function public._remap_clue_positions(p_clues jsonb, p_perm int[])
returns jsonb
language sql
immutable
as $$
  select coalesce(jsonb_agg(
    case
      when c ? 't' then jsonb_set(
        c, '{t}',
        (select coalesce(jsonb_agg(p_perm[(e)::int + 1] order by p_perm[(e)::int + 1]), '[]'::jsonb)
         from jsonb_array_elements_text(c->'t') e)
      )
      else c
    end
    order by ord
  ), '[]'::jsonb)
  from jsonb_array_elements(p_clues) with ordinality as x(c, ord);
$$;

-- Shuffle positions for every daily puzzle row.
do $$
declare
  r record;
  perm int[];
begin
  for r in select puzzle_date, pool, tiles, clues, hints from daily_puzzles loop
    -- perm is a random permutation of 0..24; perm[oldpos+1] = new position.
    perm := (select array_agg(p order by random()) from generate_series(0, 24) p);

    update daily_puzzles dp
       set tiles = (
             select jsonb_agg(
               jsonb_set(t, '{position}', to_jsonb(perm[((t->>'position')::int) + 1]))
               order by perm[((t->>'position')::int) + 1]
             )
             from jsonb_array_elements(r.tiles) t
           ),
           clues = public._remap_clue_positions(r.clues, perm),
           hints = public._remap_clue_positions(r.hints, perm)
     where dp.puzzle_date = r.puzzle_date and dp.pool = r.pool;
  end loop;
end $$;
