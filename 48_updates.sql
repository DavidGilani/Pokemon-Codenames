-- 48: Pokédex. A player "catches" the answer Pokémon of every daily they WIN,
-- except any Pokémon an extra-clue hint pointed to. Works for anonymous players
-- (keyed by the device's auth user id) – accounts later just keep the same id.
-- caught_on = first day caught by solving; rolled_on = first day got from a gem
-- roll (phase 2). A Pokémon can have both.

create table if not exists public.pokedex (
  user_id    uuid not null,
  pokemon_id integer not null references public.pokemon(id),
  caught_on  date,
  rolled_on  date,
  primary key (user_id, pokemon_id)
);
alter table public.pokedex enable row level security;  -- RPC access only

-- Same name matching the tile RPCs use (spaces/hyphens ignored).
create or replace function public._pokemon_id_by_name(p_name text)
returns integer language sql stable set search_path to 'public' as $$
  select id from pokemon
   where lower(replace(replace(name,' ',''),'-','')) = lower(replace(replace(p_name,' ',''),'-',''))
   limit 1;
$$;

-- Record today's catches for a finished, WON attempt. p_hinted = names of the
-- Pokémon an extra clue pointed to (they escape). Answers come from the puzzle
-- itself, never from the client. Returns the newly caught Pokémon.
create or replace function public.daily_record_catches(p_id uuid, p_hinted text[] default '{}')
returns jsonb language plpgsql security definer set search_path to 'public' as $$
declare a record; res jsonb;
begin
  select * into a from daily_attempts where id = p_id and user_id = auth.uid() and outcome = 'win';
  if not found then return '[]'::jsonb; end if;
  with blues as (
    select _pokemon_id_by_name(t->>'name') pid, t->>'name' nm
      from daily_puzzles dp, jsonb_array_elements(dp.tiles) t
     where dp.puzzle_date = a.puzzle_date and dp.pool = a.pool and t->>'colour' = 'blue'
       and not (lower(t->>'name') = any (select lower(x) from unnest(coalesce(p_hinted,'{}')) x))
  ), ins as (
    insert into pokedex (user_id, pokemon_id, caught_on)
    select auth.uid(), pid, a.puzzle_date from blues where pid is not null
    on conflict (user_id, pokemon_id) do update set caught_on = excluded.caught_on
      where pokedex.caught_on is null
    returning pokemon_id
  )
  select coalesce(jsonb_agg(jsonb_build_object('id', p.id, 'name', p.name)), '[]'::jsonb) into res
    from ins join pokemon p on p.id = ins.pokemon_id;
  return res;
end $$;

-- One-off credit for wins from before the Pokédex existed. Hint targets weren't
-- recorded then, so every answer of a past win counts. Idempotent.
create or replace function public._pokedex_backfill(p_user uuid)
returns void language sql security definer set search_path to 'public' as $$
  insert into pokedex (user_id, pokemon_id, caught_on)
  select p_user, x.pid, min(x.d) from (
    select _pokemon_id_by_name(t->>'name') pid, a.puzzle_date d
      from daily_attempts a
      join daily_puzzles dp on dp.puzzle_date = a.puzzle_date and dp.pool = a.pool
      cross join jsonb_array_elements(dp.tiles) t
     where a.user_id = p_user and a.outcome = 'win' and a.finished_at < '2026-11-29'
       and t->>'colour' = 'blue'
  ) x where x.pid is not null
  group by x.pid
  on conflict (user_id, pokemon_id) do update set caught_on = least(pokedex.caught_on, excluded.caught_on);
$$;

-- The player's Pokédex: every Pokémon they have, plus how many exist per gen.
create or replace function public.get_pokedex()
returns jsonb language plpgsql security definer set search_path to 'public' as $$
declare res jsonb;
begin
  if auth.uid() is null then return null; end if;
  perform _pokedex_backfill(auth.uid());
  select jsonb_build_object(
    'mine', coalesce((select jsonb_agg(jsonb_build_object(
              'id', p.id, 'name', p.name, 'gen', p.generation,
              'caught_on', d.caught_on, 'rolled_on', d.rolled_on) order by p.id)
            from pokedex d join pokemon p on p.id = d.pokemon_id
           where d.user_id = auth.uid()), '[]'::jsonb),
    'per_gen', (select jsonb_object_agg(generation, n) from
                 (select generation, count(*) n from pokemon group by 1) g)
  ) into res;
  return res;
end $$;

grant execute on function public.daily_record_catches(uuid, text[]) to anon, authenticated;
grant execute on function public.get_pokedex() to anon, authenticated;
revoke execute on function public._pokedex_backfill(uuid) from public, anon, authenticated;
