-- 38_updates.sql — streak correctness: current streak is 0 unless still alive.
--
-- daily_streak() reconstructs win streaks from daily_attempts with the classic
-- islands-and-gaps trick (consecutive calendar dates group into one run; a
-- missed day starts a new run — so gaps already break a streak). But it reported
-- the MOST RECENT run's length as `current` without checking the run is recent,
-- so a streak that ended days ago still came back non-zero. The client masks this
-- (it only shows a streak whose last win was today/yesterday), but fix it at the
-- source so `current` is 0 unless the last win is today or yesterday.
-- (Already applied to the live DB via MCP.)

create or replace function public.daily_streak()
returns table(pool text, current integer, best integer, last_win date)
language sql security definer set search_path to 'public'
as $function$
  with w as (   -- one row per (pool, date) the user won
    select pool, puzzle_date
    from daily_attempts
    where user_id = auth.uid() and outcome = 'win'
    group by pool, puzzle_date
  ),
  g as (        -- islands trick: consecutive dates share (date - row_number)
    select pool, puzzle_date,
           (puzzle_date - (row_number() over (partition by pool order by puzzle_date))::int) as grp
    from w
  ),
  runs as (
    select pool, grp, count(*)::int as len, max(puzzle_date) as end_date
    from g group by pool, grp
  ),
  cur as (      -- the most recent run, but only "current" if it's still alive
    select distinct on (pool) pool,
           case when end_date >= current_date - 1 then len else 0 end as current,
           end_date as last_win
    from runs order by pool, end_date desc
  ),
  bst as (
    select pool, max(len) as best from runs group by pool
  )
  select p.pool,
         coalesce(cur.current, 0) as current,
         coalesce(bst.best, 0) as best,
         cur.last_win
  from (values ('gen1'), ('mixed')) p(pool)
  left join cur on cur.pool = p.pool
  left join bst on bst.pool = p.pool;
$function$;
grant execute on function public.daily_streak() to anon, authenticated;
