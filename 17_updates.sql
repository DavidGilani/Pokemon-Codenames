-- 17_updates.sql
--
-- Allow null team and role on players rows so observers can be inserted
-- without a team or role assignment. The lobby join already inserted nulls
-- for both columns; this makes that explicit and supports the observer join
-- added in 16_updates.sql.

alter table public.players alter column role drop not null;
alter table public.players alter column team drop not null;
