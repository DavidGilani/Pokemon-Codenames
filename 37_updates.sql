-- 37_updates.sql — protect QA feedback from drive-by / injected submissions.
--
-- The QA page (?qa=…) and its RPCs are only obscured, and the nightly generator
-- ACTS on daily_feedback notes — so an anonymous stranger who found the page (or
-- called the RPC directly) could steer editorial decisions. Fix without adding
-- logins: a shared secret. submit_daily_feedback now takes p_secret and stamps
-- the row `trusted` only when it matches the stored QA secret. The nightly
-- generator only acts on trusted rows; untrusted submissions are inert.
--
-- The owner uses a private QA link: /?qa=<secret>. (Secret is stored in
-- app_config, which anon cannot read; the SECURITY DEFINER function checks it.)
-- (Already applied to the live DB via MCP; the secret value is NOT committed.)

create table if not exists public.app_config (
  key   text primary key,
  value text not null
);
alter table public.app_config enable row level security;  -- no policies → anon can't read

alter table public.daily_feedback add column if not exists trusted boolean not null default false;

-- Back-fill: every existing feedback row was submitted by the owner before the
-- gate existed, so trust them all (so nothing already-flagged is lost).
update public.daily_feedback set trusted = true where trusted = false;

create or replace function public.submit_daily_feedback(
  p_date date, p_pool text, p_rating text, p_note text,
  p_outcome text default null, p_mistakes integer default null,
  p_hints integer default null, p_duration integer default null,
  p_secret text default null)
returns uuid
language plpgsql security definer set search_path to 'public'
as $function$
declare
  v_id uuid;
  v_ok boolean;
begin
  select p_secret is not null and p_secret = value
    into v_ok
  from public.app_config where key = 'qa_secret';
  v_ok := coalesce(v_ok, false);

  insert into public.daily_feedback
    (puzzle_date, pool, rating, note, outcome, mistakes, hints, duration, created_by, trusted)
  values
    (p_date, p_pool, nullif(p_rating,''), nullif(p_note,''), p_outcome, p_mistakes, p_hints, p_duration, auth.uid(), v_ok)
  returning id into v_id;
  return v_id;
end;
$function$;
grant execute on function public.submit_daily_feedback(date, text, text, text, text, integer, integer, integer, text) to anon, authenticated;
