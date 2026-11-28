-- 49: Gems, share links and friend badges (phase 2).
-- Earning (per player per day, UK/UTC date):
--   +5  for pressing Share/Copy on a finished daily        (max 3 a day = 15)
--   +10 when someone opens your link and FINISHES that day's puzzle (win or lose)
--   +20 instead, if that person had never finished a daily before
--   friend rewards max 3 friends a day (so up to 60) – each friend counts once a day
-- Spending (asked every time, never automatic):
--   25 to save a streak when it breaks, 75 to roll a random uncaught Pokémon.
-- Everything is keyed by the device's auth user id, like the Pokédex.

create table if not exists public.gem_ledger (
  id         bigserial primary key,
  user_id    uuid not null,
  delta      integer not null,
  reason     text not null,          -- share | friend | friend_new | streak_save | roll
  ref        text,
  created_at timestamptz not null default now()
);
create index if not exists gem_ledger_user on public.gem_ledger (user_id, created_at);
alter table public.gem_ledger enable row level security;

create table if not exists public.ref_codes (
  user_id uuid primary key,
  code    text not null unique
);
alter table public.ref_codes enable row level security;

create table if not exists public.referrals (
  referrer    uuid not null,
  friend      uuid not null,
  puzzle_date date not null,
  is_new      boolean not null,
  rewarded    boolean not null,
  created_at  timestamptz not null default now(),
  primary key (referrer, friend, puzzle_date)
);
alter table public.referrals enable row level security;

create or replace function public._gem_balance(p_user uuid)
returns integer language sql stable security definer set search_path to 'public' as $$
  select coalesce(sum(delta), 0)::int from gem_ledger where user_id = p_user;
$$;

-- This player's share code (created on first use).
create or replace function public.my_ref_code()
returns text language plpgsql security definer set search_path to 'public' as $$
declare c text;
begin
  if auth.uid() is null then return null; end if;
  select code into c from ref_codes where user_id = auth.uid();
  if c is null then
    loop
      c := substr(md5(random()::text || clock_timestamp()::text), 1, 8);
      begin
        insert into ref_codes (user_id, code) values (auth.uid(), c);
        exit;
      exception when unique_violation then
        -- either the code clashed (retry) or this user raced us (re-read)
        select code into c from ref_codes where user_id = auth.uid();
        if c is not null then exit; end if;
      end;
    end loop;
  end if;
  return c;
end $$;

-- Gems + friend stats for the badges.
create or replace function public.my_gem_status()
returns jsonb language sql security definer set search_path to 'public' as $$
  select jsonb_build_object(
    'balance', _gem_balance(auth.uid()),
    'shares_today', (select count(*) from gem_ledger where user_id = auth.uid()
                      and reason = 'share' and created_at::date = current_date),
    'friend_finishes', (select count(*) from referrals where referrer = auth.uid()),
    'friends', (select count(distinct friend) from referrals where referrer = auth.uid())
  ) where auth.uid() is not null;
$$;

-- +5 for a share, max 3 a day. Returns {awarded, balance}.
create or replace function public.claim_share_gems()
returns jsonb language plpgsql security definer set search_path to 'public' as $$
declare n int; got int := 0;
begin
  if auth.uid() is null then return null; end if;
  perform pg_advisory_xact_lock(hashtext('gems:' || auth.uid()::text));
  select count(*) into n from gem_ledger
   where user_id = auth.uid() and reason = 'share' and created_at::date = current_date;
  if n < 3 then
    insert into gem_ledger (user_id, delta, reason) values (auth.uid(), 5, 'share');
    got := 5;
  end if;
  return jsonb_build_object('awarded', got, 'balance', _gem_balance(auth.uid()));
end $$;

-- Called by the FRIEND's device after finishing today's daily, having arrived
-- through a share link with code p_code. Credits the sharer.
create or replace function public.record_referral(p_code text, p_attempt uuid)
returns jsonb language plpgsql security definer set search_path to 'public' as $$
declare a record; r uuid; isnew boolean; today_n int; ok boolean := false; n int;
begin
  if auth.uid() is null or p_code is null then return null; end if;
  select * into a from daily_attempts
   where id = p_attempt and user_id = auth.uid() and outcome is not null and puzzle_date = current_date;
  if not found then return jsonb_build_object('credited', false); end if;
  select user_id into r from ref_codes where code = p_code;
  if r is null or r = auth.uid() then return jsonb_build_object('credited', false); end if;
  perform pg_advisory_xact_lock(hashtext('gems:' || r::text));
  isnew := not exists (select 1 from daily_attempts
                        where user_id = auth.uid() and outcome is not null and id <> a.id
                          and finished_at < a.finished_at);
  select count(*) into today_n from referrals
   where referrer = r and puzzle_date = current_date and rewarded;
  insert into referrals (referrer, friend, puzzle_date, is_new, rewarded)
  values (r, auth.uid(), current_date, isnew, today_n < 3)
  on conflict do nothing;
  get diagnostics n = row_count;
  if n = 1 and today_n < 3 then
    insert into gem_ledger (user_id, delta, reason, ref)
    values (r, case when isnew then 20 else 10 end,
            case when isnew then 'friend_new' else 'friend' end, auth.uid()::text);
    ok := true;
  end if;
  return jsonb_build_object('credited', ok);
end $$;

-- Spend gems (streak saves). Fails cleanly if the balance is too low.
create or replace function public.spend_gems(p_amount integer, p_reason text, p_ref text default null)
returns jsonb language plpgsql security definer set search_path to 'public' as $$
declare bal int;
begin
  if auth.uid() is null or p_amount <= 0 or p_reason not in ('streak_save') then return null; end if;
  perform pg_advisory_xact_lock(hashtext('gems:' || auth.uid()::text));
  bal := _gem_balance(auth.uid());
  if bal < p_amount then return jsonb_build_object('ok', false, 'balance', bal); end if;
  insert into gem_ledger (user_id, delta, reason, ref) values (auth.uid(), -p_amount, p_reason, p_ref);
  return jsonb_build_object('ok', true, 'balance', bal - p_amount);
end $$;

-- 75 gems: a random Pokémon not yet in your Pokédex ('gen1' = 1–151, else any).
create or replace function public.pokedex_roll(p_scope text default 'all')
returns jsonb language plpgsql security definer set search_path to 'public' as $$
declare bal int; pk record;
begin
  if auth.uid() is null then return null; end if;
  perform pg_advisory_xact_lock(hashtext('gems:' || auth.uid()::text));
  bal := _gem_balance(auth.uid());
  if bal < 75 then return jsonb_build_object('ok', false, 'balance', bal); end if;
  select p.id, p.name into pk from pokemon p
   where (p_scope <> 'gen1' or p.id <= 151)
     and not exists (select 1 from pokedex d where d.user_id = auth.uid() and d.pokemon_id = p.id)
   order by random() limit 1;
  if pk.id is null then return jsonb_build_object('ok', false, 'balance', bal, 'complete', true); end if;
  insert into pokedex (user_id, pokemon_id, rolled_on) values (auth.uid(), pk.id, current_date);
  insert into gem_ledger (user_id, delta, reason, ref) values (auth.uid(), -75, 'roll', pk.id::text);
  return jsonb_build_object('ok', true, 'balance', bal - 75, 'id', pk.id, 'name', pk.name);
end $$;

grant execute on function public.my_ref_code(), public.my_gem_status(), public.claim_share_gems(),
  public.record_referral(text, uuid), public.spend_gems(integer, text, text),
  public.pokedex_roll(text) to anon, authenticated;
revoke execute on function public._gem_balance(uuid) from public, anon, authenticated;
