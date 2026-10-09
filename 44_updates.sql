-- 44: Speed ranking on the daily share card. For a winning attempt, how many
-- other players solved the same board faster (so the card can say "top 10%",
-- "top 25%", "top half" or "fastest time so far today"). Only wins count –
-- a player's best winning time is used, so one person can't fill the list.
create or replace function public.daily_time_rank(p_id uuid)
returns jsonb
language sql
security definer
set search_path to 'public'
as $$
  with me as (
    select puzzle_date, pool, duration_ms, user_id
    from daily_attempts
    where id = p_id and user_id = auth.uid()
      and outcome = 'win' and duration_ms is not null),
  field as (
    select a.user_id, min(a.duration_ms) best
    from daily_attempts a join me on a.puzzle_date = me.puzzle_date and a.pool = me.pool
    where a.outcome = 'win' and a.duration_ms is not null
    group by a.user_id)
  select case when not exists (select 1 from me) then null else jsonb_build_object(
    'total',  (select count(*) from field),
    'faster', (select count(*) from field, me where field.user_id <> me.user_id and field.best < me.duration_ms)
  ) end;
$$;

grant execute on function public.daily_time_rank(uuid) to anon, authenticated;
