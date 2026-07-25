-- 13_updates.sql
-- Fix claim_seat error messages: replace "spymaster" with "clue giver"
-- so players see friendly language when a role is already taken.

create or replace function public.claim_seat(
  p_room_id uuid,
  p_team    text,
  p_role    text
)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_room rooms;
begin
  select * into v_room from rooms where id = p_room_id;
  if not found then raise exception 'Room not found'; end if;
  if v_room.status <> 'lobby' then raise exception 'The game has already started'; end if;

  if p_role not in ('spymaster', 'operative') then
    raise exception 'Invalid role';
  end if;
  if p_team not in ('red', 'blue') then
    raise exception 'Invalid team';
  end if;

  -- In two-player modes only one clue giver is allowed (no team restriction)
  if v_room.mode in ('two_player', 'turn_by_turn') then
    if p_role = 'spymaster' and exists (
      select 1 from players
      where room_id = p_room_id and role = 'spymaster' and user_id <> auth.uid()
    ) then
      raise exception 'There is already a clue giver in this game';
    end if;
  else
    -- Classic modes: one clue giver per team
    if p_role = 'spymaster' and exists (
      select 1 from players
      where room_id = p_room_id and team = p_team and role = 'spymaster' and user_id <> auth.uid()
    ) then
      raise exception 'There is already a clue giver for this team';
    end if;
  end if;

  update players
     set team = p_team,
         role = p_role
   where room_id = p_room_id
     and user_id = auth.uid();

  if not found then
    raise exception 'You are not in this room';
  end if;
end;
$$;

grant execute on function public.claim_seat(uuid, text, text) to authenticated;
