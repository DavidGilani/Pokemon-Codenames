-- 40_updates.sql — instant email when a comment is posted or reported.
--
-- A BEFORE trigger on daily_comments queues an email via Resend's API using
-- pg_net (async HTTP from Postgres), then marks the row notified so the nightly
-- digest doesn't repeat it. Fires on:
--   * a new comment
--   * a comment being hidden by a player report (visible -> hidden)
-- Config lives in app_config (anon can't read it):
--   resend_api_key  – the Resend API key (no key = do nothing; nightly digest
--                     still covers it)
--   notify_email    – where to send (defaults to the owner's address)
-- Any failure is swallowed so an email problem can never block a comment.
-- (Already applied to the live DB via MCP. The API key is NOT committed.)

create extension if not exists pg_net with schema extensions;

create or replace function public._notify_comment()
returns trigger
language plpgsql security definer set search_path to 'public', 'extensions'
as $function$
declare
  v_key text; v_to text; v_subj text; v_text text; v_pool text;
begin
  if tg_op = 'INSERT' then
    v_subj := '💬 New comment on Pokémon Codenames';
  elsif tg_op = 'UPDATE' and old.status = 'visible' and new.status = 'hidden' then
    v_subj := '⚠️ Comment reported on Pokémon Codenames';
  else
    return new;
  end if;

  select value into v_key from public.app_config where key = 'resend_api_key';
  if coalesce(v_key, '') = '' then return new; end if;
  select value into v_to from public.app_config where key = 'notify_email';
  v_to := coalesce(nullif(v_to, ''), 'davidgilani@hotmail.co.uk');
  v_pool := case when new.pool = 'gen1' then 'Gen I' else 'All-gens' end;

  v_text := concat_ws(E'\n',
    case when tg_op = 'UPDATE'
      then 'A player reported this comment, so it is now HIDDEN until you review it.'
      else 'Someone just left a comment:' end,
    '',
    'Puzzle: ' || to_char(new.puzzle_date, 'Dy DD Mon YYYY') || ' – ' || v_pool,
    'Name:   ' || coalesce(new.username, 'Anonymous trainer'),
    '',
    '"' || new.body || '"',
    '',
    'To hide, restore or delete it, open the Comments section at the bottom of your private QA page.');

  begin
    perform net.http_post(
      url     := 'https://api.resend.com/emails',
      body    := jsonb_build_object(
                   'from', 'Pokémon Codenames <onboarding@resend.dev>',
                   'to', jsonb_build_array(v_to),
                   'subject', v_subj,
                   'text', v_text),
      headers := jsonb_build_object(
                   'Authorization', 'Bearer ' || v_key,
                   'Content-Type', 'application/json'));
    new.notified := true;   -- emailed now, so the nightly digest can skip it
  exception when others then
    null;                   -- never block the comment over an email problem
  end;
  return new;
end;
$function$;

drop trigger if exists daily_comments_notify on public.daily_comments;
create trigger daily_comments_notify
  before insert or update of status on public.daily_comments
  for each row execute function public._notify_comment();

revoke execute on function public._notify_comment() from public, anon, authenticated;
