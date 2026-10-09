-- 45: Tutorial step tracking. Lets the client log which tutorial step each
-- player reaches (tutorial_step_1 … _9), plus Skip, Exit and finishing the
-- practice board, so the QA stats can show where people drop off.
create or replace function public.log_daily_event(p_event text, p_pool text default null, p_date date default null)
returns void
language sql
security definer
set search_path to 'public'
as $$
  insert into public.daily_events (user_id, event, pool, puzzle_date)
  select auth.uid(), p_event, p_pool, p_date
  where p_event in ('share','copy','tutorial_start','tutorial_complete',
                    'tutorial_skip','tutorial_exit','tutorial_board_done')
     or p_event ~ '^tutorial_step_[1-9]$';
$$;
