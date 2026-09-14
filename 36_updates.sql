-- 36_updates.sql — daily analytics: lightweight event log + a stats RPC.
--
-- (a) daily_events: a tiny append-only log so we can measure things that aren't
--     a finished attempt — e.g. how many players tap Share / Copy result, and
--     tutorial starts/completions. RLS on, no direct reads; writes go through
--     log_daily_event (SECURITY DEFINER) so anon can insert but not read/tamper.
-- (b) daily_stats(): aggregates for the owner stats panel at the bottom of the
--     QA page (?qa=1). Returns one jsonb blob so the client makes a single call.
--     (Already applied to the live DB via MCP.)

create table if not exists public.daily_events (
  id          bigint generated always as identity primary key,
  user_id     uuid,
  event       text not null,               -- 'share' | 'copy' | 'tutorial_start' | 'tutorial_complete' | …
  pool        text,                         -- 'gen1' | 'mixed' | null
  puzzle_date date,
  created_at  timestamptz not null default now()
);
create index if not exists daily_events_created_idx on public.daily_events (created_at);
create index if not exists daily_events_event_idx   on public.daily_events (event);

alter table public.daily_events enable row level security;
-- No policies → no direct anon/authenticated read or write; everything goes
-- through the SECURITY DEFINER functions below.

create or replace function public.log_daily_event(
  p_event text, p_pool text default null, p_date date default null)
returns void
language sql security definer set search_path to 'public'
as $function$
  insert into public.daily_events (user_id, event, pool, puzzle_date)
  -- guard the event vocabulary so the log can't be spammed with arbitrary text
  select auth.uid(), p_event, p_pool, p_date
  where p_event in ('share','copy','tutorial_start','tutorial_complete');
$function$;
grant execute on function public.log_daily_event(text, text, date) to anon, authenticated;

create or replace function public.daily_stats()
returns jsonb
language sql security definer set search_path to 'public'
as $function$
  with att as (select * from daily_attempts),
  months as (
    select to_char(date_trunc('month', started_at), 'YYYY-MM') as month,
           count(distinct user_id)                              as users,
           count(distinct user_id) filter (where outcome is not null) as completers,
           count(*) filter (where outcome is not null)          as completed,
           count(*) filter (where outcome = 'win')              as wins
    from att group by 1),
  month_share as (
    select to_char(date_trunc('month', created_at), 'YYYY-MM') as month,
           count(distinct user_id) as sharers
    from daily_events where event in ('share','copy') group by 1),
  ratings as (select rating, count(*) n from att where rating is not null group by 1),
  pools as (
    select pool, count(distinct user_id) users,
           count(*) filter (where outcome is not null) completed,
           count(*) filter (where outcome = 'win') wins
    from att group by 1),
  retention as (
    select case when d = 1 then '1 day' when d between 2 and 4 then '2-4 days'
                when d between 5 and 9 then '5-9 days' else '10+ days' end as bucket,
           count(*) users, min(d) srt
    from (select user_id, count(distinct puzzle_date) d
          from att where outcome is not null group by 1) t
    group by 1),
  events as (select event, count(*) n, count(distinct user_id) u from daily_events group by 1)
  select jsonb_build_object(
    'months', (select coalesce(jsonb_agg(jsonb_build_object(
        'month', m.month, 'users', m.users, 'completers', m.completers,
        'completed', m.completed, 'wins', m.wins, 'sharers', coalesce(ms.sharers, 0)
      ) order by m.month), '[]'::jsonb)
      from months m left join month_share ms on ms.month = m.month),
    'ratings', (select coalesce(jsonb_agg(jsonb_build_object('rating', rating, 'n', n) order by n desc), '[]'::jsonb) from ratings),
    'pools', (select coalesce(jsonb_agg(jsonb_build_object('pool', pool, 'users', users, 'completed', completed, 'wins', wins) order by pool), '[]'::jsonb) from pools),
    'retention', (select coalesce(jsonb_agg(jsonb_build_object('bucket', bucket, 'users', users) order by srt), '[]'::jsonb) from retention),
    'events', (select coalesce(jsonb_object_agg(event, jsonb_build_object('n', n, 'users', u)), '{}'::jsonb) from events)
  );
$function$;
grant execute on function public.daily_stats() to anon, authenticated;
