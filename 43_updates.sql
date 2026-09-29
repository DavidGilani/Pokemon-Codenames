-- 43: QA "Completions" table – people who finished each pool's daily, for
-- today, yesterday, the daily average (since tracking began, full days only)
-- and the best day ever (with its date).
create or replace function public.daily_completion_stats()
returns jsonb
language sql
security definer
set search_path to 'public'
as $$
  with per_day as (
    select puzzle_date d,
           count(distinct user_id) filter (where pool = 'gen1')  gen1,
           count(distinct user_id) filter (where pool = 'mixed') mixed,
           count(distinct user_id)                                total
    from daily_attempts
    where outcome is not null and puzzle_date <= current_date
    group by 1),
  span as (
    select min(d) first_day,
           greatest((current_date - min(d)), 1) full_days  -- days before today
    from per_day),
  past as (select * from per_day where d < current_date),
  best as (select * from per_day order by total desc, d desc limit 1),
  row_of as (
    select jsonb_build_object('gen1', coalesce(gen1, 0), 'mixed', coalesce(mixed, 0),
                              'total', coalesce(total, 0)) j, d
    from per_day)
  select jsonb_build_object(
    'today',     coalesce((select j from row_of where d = current_date), '{"gen1":0,"mixed":0,"total":0}'),
    'yesterday', coalesce((select j from row_of where d = current_date - 1), '{"gen1":0,"mixed":0,"total":0}'),
    'average', (select jsonb_build_object(
        'gen1',  round(coalesce(sum(gen1), 0)::numeric  / (select full_days from span), 1),
        'mixed', round(coalesce(sum(mixed), 0)::numeric / (select full_days from span), 1),
        'total', round(coalesce(sum(total), 0)::numeric / (select full_days from span), 1))
      from past),
    'best', (select jsonb_build_object('gen1', gen1, 'mixed', mixed, 'total', total, 'date', d) from best),
    'since', (select first_day from span)
  );
$$;

grant execute on function public.daily_completion_stats() to anon, authenticated;
