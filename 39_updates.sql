-- 39_updates.sql — daily puzzle comments (post-completion), with moderation.
--
-- Players who have FINISHED a day's puzzle can leave one short comment on it
-- (optionally with a display name, else "Anonymous trainer"). Comments are only
-- shown on the finish screen, so only people who've completed the puzzle see
-- them (no spoiler risk for others).
--
-- Safety:
--  * _comment_is_clean(): a server-side word filter (can't be bypassed from the
--    browser). Normalises leetspeak (sh1t, a$$), strips punctuation inside words
--    (f-u-c-k, f.u.c.k), glues runs of single letters (f u c k), and collapses
--    stretched letters (fuuuuck). Terms live in comment_banned_terms so the list
--    can be edited in the Supabase table editor without a deploy:
--      mode 'any'  – blocked anywhere inside a word (distinctive slurs/swears)
--      mode 'word' – blocked only as a whole word (short words that hide inside
--                    innocent ones: "ass" in "class", "hell" in "Shellder")
--  * Links are refused (spam), 3–280 chars, one comment per player per puzzle.
--  * Any player can report a comment: it's hidden immediately pending review.
--  * The owner can hide / restore / delete from the QA page (secret-gated), and
--    the nightly email lists new + reported comments (`notified` flag).
-- (Already applied to the live DB via MCP.)

create table if not exists public.daily_comments (
  id           uuid primary key default gen_random_uuid(),
  puzzle_date  date not null,
  pool         text not null,
  user_id      uuid,
  username     text,
  body         text not null,
  status       text not null default 'visible',   -- visible | hidden | removed
  report_count int  not null default 0,
  reported_at  timestamptz,
  notified     boolean not null default false,    -- included in a nightly email yet?
  created_at   timestamptz not null default now()
);
create unique index if not exists daily_comments_one_per_user
  on public.daily_comments (user_id, puzzle_date, pool);
create index if not exists daily_comments_board_idx
  on public.daily_comments (puzzle_date, pool, created_at desc);
alter table public.daily_comments enable row level security;   -- RPC access only

create table if not exists public.daily_comment_reports (
  comment_id uuid not null references public.daily_comments(id) on delete cascade,
  user_id    uuid not null,
  created_at timestamptz not null default now(),
  primary key (comment_id, user_id)
);
alter table public.daily_comment_reports enable row level security;

create table if not exists public.comment_banned_terms (
  term text primary key,
  mode text not null default 'any' check (mode in ('any','word'))
);
alter table public.comment_banned_terms enable row level security;

insert into public.comment_banned_terms (term, mode) values
  -- blocked anywhere inside a word
  ('fuck','any'),('fuk','any'),('fvck','any'),('shit','any'),('cunt','any'),('bitch','any'),
  ('wank','any'),('bollock','any'),('asshole','any'),('arsehole','any'),('dickhead','any'),
  ('bastard','any'),('bullshit','any'),('jizz','any'),('dildo','any'),('porn','any'),
  ('whore','any'),('slut','any'),('nigger','any'),('nigga','any'),('faggot','any'),
  ('retard','any'),('spastic','any'),('tranny','any'),('kike','any'),('chink','any'),
  ('wetback','any'),('beaner','any'),('hitler','any'),('killyourself','any'),
  -- blocked only as whole words
  ('ass','word'),('arse','word'),('fag','word'),('cock','word'),('dick','word'),
  ('piss','word'),('crap','word'),('damn','word'),('hell','word'),('wtf','word'),
  ('stfu','word'),('cum','word'),('tit','word'),('twat','word'),('pussy','word'),
  ('prick','word'),('rape','word'),('nazi','word'),('heil','word'),('kkk','word'),
  ('paki','word'),('spic','word'),('coon','word'),('gook','word'),('dyke','word'),
  ('negro','word'),('homo','word'),('kys','word'),('fk','word'),('fck','word'),
  ('boob','word'),('boobs','word'),('sex','word'),('sexy','word')
on conflict (term) do nothing;

create or replace function public._comment_is_clean(p_text text)
returns boolean
language plpgsql stable security definer set search_path to 'public'
as $function$
declare
  t text; toks text[]; tok text; s text; buf text := '';
  cands text[] := '{}'; c text; r record;
begin
  -- lower-case + common leetspeak / symbol swaps
  t := translate(lower(coalesce(p_text, '')), '013457@$!|8', 'oieastasiib');
  -- candidate "words": each whitespace token stripped to letters (so f-u-c-k and
  -- f.u.c.k become fuck); consecutive single letters glued (f u c k -> fuck)
  toks := regexp_split_to_array(t, '\s+');
  foreach tok in array toks loop
    s := regexp_replace(tok, '[^a-z]', '', 'g');
    if length(s) = 1 then
      buf := buf || s;
    else
      if length(buf) > 1 then cands := cands || buf; end if;
      buf := '';
      if s <> '' then cands := cands || s; end if;
    end if;
  end loop;
  if length(buf) > 1 then cands := cands || buf; end if;

  for r in select term, mode from public.comment_banned_terms loop
    foreach c in array cands loop
      if r.mode = 'any' then
        if position(r.term in c) > 0
           or position(r.term in regexp_replace(c, '(.)\1{2,}', '\1\1', 'g')) > 0
           or position(regexp_replace(r.term, '(.)\1+', '\1', 'g') in regexp_replace(c, '(.)\1+', '\1', 'g')) > 0
        then return false; end if;
      else
        if c = r.term or c = r.term || 's'
           or regexp_replace(c, '(.)\1{2,}', '\1\1', 'g') = r.term
           or (length(r.term) > 3 and regexp_replace(c, '(.)\1+', '\1', 'g') = r.term)
        then return false; end if;
      end if;
    end loop;
  end loop;
  return true;
end;
$function$;

create or replace function public._qa_ok(p_secret text)
returns boolean
language sql stable security definer set search_path to 'public'
as $function$
  select coalesce((select p_secret is not null and p_secret = value
                   from public.app_config where key = 'qa_secret'), false);
$function$;

create or replace function public.post_daily_comment(
  p_date date, p_pool text, p_username text, p_body text)
returns uuid
language plpgsql security definer set search_path to 'public'
as $function$
declare
  v_uid uuid := auth.uid();
  v_body text := btrim(coalesce(p_body, ''));
  v_name text := nullif(btrim(coalesce(p_username, '')), '');
  v_id uuid;
begin
  if v_uid is null then raise exception 'Please reload the page and try again.'; end if;
  if not exists (select 1 from public.daily_attempts
                 where user_id = v_uid and puzzle_date = p_date and pool = p_pool
                   and outcome is not null) then
    raise exception 'Finish this puzzle to leave a comment.';
  end if;
  if length(v_body) < 3 then raise exception 'Your comment is a bit short!'; end if;
  if length(v_body) > 280 then raise exception 'Please keep comments under 280 characters.'; end if;
  if v_name is not null and length(v_name) > 20 then
    raise exception 'Please keep your name under 20 characters.';
  end if;
  if v_body ~* '(https?://|www\.|\.com\b|\.co\.uk\b)' then
    raise exception 'Links aren''t allowed in comments.';
  end if;
  if not public._comment_is_clean(v_body) or not public._comment_is_clean(v_name) then
    raise exception 'Please keep it friendly – that comment contains language we don''t allow.';
  end if;
  begin
    insert into public.daily_comments (puzzle_date, pool, user_id, username, body)
    values (p_date, p_pool, v_uid, v_name, v_body)
    returning id into v_id;
  exception when unique_violation then
    raise exception 'You''ve already commented on this puzzle.';
  end;
  return v_id;
end;
$function$;

create or replace function public.get_daily_comments(p_date date, p_pool text)
returns table(id uuid, username text, body text, created_at timestamptz, is_mine boolean)
language sql stable security definer set search_path to 'public'
as $function$
  select c.id, coalesce(c.username, 'Anonymous trainer'), c.body, c.created_at,
         (c.user_id = auth.uid())
  from public.daily_comments c
  where c.puzzle_date = p_date and c.pool = p_pool
    and (c.status = 'visible' or c.user_id = auth.uid())   -- you always see your own
    and c.status <> 'removed'
  order by c.created_at desc
  limit 200;
$function$;

create or replace function public.report_daily_comment(p_id uuid)
returns void
language plpgsql security definer set search_path to 'public'
as $function$
begin
  if auth.uid() is null then return; end if;
  insert into public.daily_comment_reports (comment_id, user_id)
  values (p_id, auth.uid()) on conflict do nothing;
  update public.daily_comments
     set report_count = (select count(*) from public.daily_comment_reports where comment_id = p_id),
         status = case when status = 'visible' then 'hidden' else status end,
         reported_at = now(),
         notified = false            -- make sure the next email mentions it
   where id = p_id and user_id is distinct from auth.uid();
end;
$function$;

-- Owner moderation (QA page). Secret-gated.
create or replace function public.list_daily_comments_admin(p_secret text, p_limit int default 100)
returns table(id uuid, puzzle_date date, pool text, username text, body text,
              status text, report_count int, created_at timestamptz)
language plpgsql stable security definer set search_path to 'public'
as $function$
begin
  if not public._qa_ok(p_secret) then raise exception 'Not allowed.'; end if;
  return query
    select c.id, c.puzzle_date, c.pool, coalesce(c.username, 'Anonymous trainer'), c.body,
           c.status, c.report_count, c.created_at
    from public.daily_comments c
    where c.status <> 'removed'
    order by (c.status = 'hidden') desc, c.created_at desc
    limit greatest(1, least(coalesce(p_limit, 100), 500));
end;
$function$;

create or replace function public.moderate_daily_comment(p_id uuid, p_action text, p_secret text)
returns void
language plpgsql security definer set search_path to 'public'
as $function$
begin
  if not public._qa_ok(p_secret) then raise exception 'Not allowed.'; end if;
  if p_action = 'hide' then
    update public.daily_comments set status = 'hidden' where id = p_id;
  elsif p_action = 'restore' then
    update public.daily_comments set status = 'visible', report_count = 0 where id = p_id;
    delete from public.daily_comment_reports where comment_id = p_id;
  elsif p_action = 'remove' then
    update public.daily_comments set status = 'removed' where id = p_id;
  else
    raise exception 'Unknown action.';
  end if;
end;
$function$;

grant execute on function public.post_daily_comment(date, text, text, text) to anon, authenticated;
grant execute on function public.get_daily_comments(date, text) to anon, authenticated;
grant execute on function public.report_daily_comment(uuid) to anon, authenticated;
grant execute on function public.list_daily_comments_admin(text, int) to anon, authenticated;
grant execute on function public.moderate_daily_comment(uuid, text, text) to anon, authenticated;
revoke execute on function public._comment_is_clean(text) from public, anon, authenticated;
revoke execute on function public._qa_ok(text) from public, anon, authenticated;
