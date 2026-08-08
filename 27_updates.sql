-- 27_updates.sql
--
-- Make daily feedback self-describing: record each attempt's authored difficulty
-- label (Easy..Evil) on the daily_attempts row, computed SERVER-SIDE from the
-- puzzle's clue-category spread when the attempt starts. This lets analytics ask
-- "did the boards we CALLED Hard actually play hard?" without trusting the client.

-- 1. Column to hold the label.
alter table public.daily_attempts add column if not exists difficulty text;

-- 2. Shared helper: difficulty label from a clues jsonb array.
--    Mirrors the client dailyDifficulty(): highs = clues with cat >= 4,
--    ones = clues with cat = 1.  highs>=4 -> Evil, >=3 -> Brutal; else by ones:
--    0 -> Hard, 1 -> Challenging, 2 -> Medium, 3+ -> Easy.
create or replace function public.daily_difficulty_label(p_clues jsonb)
returns text
language sql
immutable
as $$
  with s as (
    select
      count(*) filter (where coalesce((c->>'cat')::int, 1) >= 4) as highs,
      count(*) filter (where coalesce((c->>'cat')::int, 1) = 1)  as ones
    from jsonb_array_elements(coalesce(p_clues, '[]'::jsonb)) c
  )
  select case
    when highs >= 4 then 'Evil'
    when highs >= 3 then 'Brutal'
    when ones = 0 then 'Hard'
    when ones = 1 then 'Challenging'
    when ones = 2 then 'Medium'
    else 'Easy'
  end
  from s;
$$;

-- 3. Start an attempt AND stamp its difficulty from the puzzle's clues.
create or replace function public.daily_start_attempt(p_date date, p_pool text)
returns uuid
language plpgsql
security definer
set search_path = public
as $$
declare
  v_id uuid;
  v_diff text;
begin
  select daily_difficulty_label(dp.clues) into v_diff
  from daily_puzzles dp
  where dp.puzzle_date = p_date and dp.pool = p_pool;

  insert into daily_attempts (user_id, puzzle_date, pool, difficulty)
  values (auth.uid(), p_date, p_pool, v_diff)
  returning id into v_id;
  return v_id;
end;
$$;

grant execute on function public.daily_difficulty_label(jsonb)   to authenticated;
grant execute on function public.daily_start_attempt(date, text) to authenticated;

-- 4. Backfill difficulty for existing finished attempts where we still have the
--    puzzle row (best-effort; leaves NULL if the puzzle was later overwritten).
update public.daily_attempts a
   set difficulty = daily_difficulty_label(dp.clues)
  from public.daily_puzzles dp
 where a.difficulty is null
   and dp.puzzle_date = a.puzzle_date
   and dp.pool = a.pool;
