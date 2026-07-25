-- 14_diagnostic.sql
-- Run this in the Supabase SQL editor and share the results.
-- It checks that all expected columns exist on the key tables
-- and lists the public functions that should be present.

-- 1. Column inventory for key tables
select
  table_name,
  column_name,
  data_type,
  is_nullable,
  column_default
from information_schema.columns
where table_schema = 'public'
  and table_name in ('rooms', 'players', 'cards', 'card_key', 'pokemon')
order by table_name, ordinal_position;

-- 2. Public functions
select
  routine_name,
  routine_type
from information_schema.routines
where routine_schema = 'public'
order by routine_name;

-- 3. Quick check: does rooms have all expected columns?
select
  max(case when column_name = 'started_at'      then '✓' else null end) as started_at,
  max(case when column_name = 'finished_at'     then '✓' else null end) as finished_at,
  max(case when column_name = 'turn_started_at' then '✓' else null end) as turn_started_at,
  max(case when column_name = 'clue_log'        then '✓' else null end) as clue_log,
  max(case when column_name = 'remaining_red'   then '✓' else null end) as remaining_red,
  max(case when column_name = 'remaining_blue'  then '✓' else null end) as remaining_blue,
  max(case when column_name = 'clue_count'      then '✓' else null end) as clue_count,
  max(case when column_name = 'mode'            then '✓' else null end) as mode,
  max(case when column_name = 'winner'          then '✓' else null end) as winner
from information_schema.columns
where table_schema = 'public' and table_name = 'rooms';
