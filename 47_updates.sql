-- 47: "Superseded" feedback instead of deleting it.
-- When the nightly routine reworks a board, its old QA feedback used to be
-- DELETEd so the board went back to blue. The Supabase connector now asks for a
-- human to approve every DELETE, which an unattended run can't do. So instead the
-- routine sets superseded = true: the QA overview ignores superseded rows (the
-- board shows blue again) but the history is kept.
alter table public.daily_feedback add column if not exists superseded boolean not null default false;

create or replace function public.daily_qa_overview(p_from date, p_to date)
returns table(puzzle_date date, pool text, status text, difficulty text, n_clues integer)
language sql security definer set search_path to 'public'
as $function$
  select g.d::date as puzzle_date,
         p.pool,
         case
           when dp.puzzle_date is null then 'black'
           when fb.total is null then 'blue'
           when coalesce(fb.unaddressed, 0) > 0 then 'red'
           else 'green'
         end as status,
         dp.difficulty,
         dp.n_clues
  from generate_series(p_from, p_to, interval '1 day') g(d)
  cross join (values ('gen1'), ('mixed')) p(pool)
  left join (
    select dpz.puzzle_date, dpz.pool,
           jsonb_array_length(dpz.clues) as n_clues,
           public.daily_difficulty_label(dpz.clues) as difficulty
    from daily_puzzles dpz
  ) dp on dp.puzzle_date = g.d::date and dp.pool = p.pool
  left join (
    select puzzle_date, pool, count(*) as total,
           count(*) filter (where note is not null and note not like 'auto:%' and addressed = false) as unaddressed
    from daily_feedback where not superseded group by puzzle_date, pool
  ) fb on fb.puzzle_date = g.d::date and fb.pool = p.pool
  order by g.d, (p.pool <> 'gen1');
$function$;

create or replace function public.list_daily_qa(p_from date, p_to date)
returns table(puzzle_date date, pool text, n_clues integer, difficulty text, reviewed integer)
language sql security definer set search_path to 'public'
as $function$
  select dp.puzzle_date, dp.pool,
         jsonb_array_length(dp.clues) as n_clues,
         public.daily_difficulty_label(dp.clues) as difficulty,
         (select count(*)::int from daily_feedback fb
            where fb.puzzle_date = dp.puzzle_date and fb.pool = dp.pool and not fb.superseded) as reviewed
  from daily_puzzles dp
  where dp.puzzle_date between p_from and p_to
  order by dp.puzzle_date, (dp.pool <> 'gen1'), dp.pool;
$function$;

-- Re-test the two boards reworked on 2026-11-14 night (their old notes are done).
update public.daily_feedback set superseded = true, addressed = true
 where (puzzle_date, pool) in (('2026-11-17'::date,'mixed'),('2026-11-22'::date,'mixed'));
