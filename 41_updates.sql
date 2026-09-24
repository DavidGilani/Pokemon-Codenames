-- 41_updates.sql — holiday / special-day themes.
--
-- daily_themes: one row per themed date (applies to BOTH pools that day):
--   name    – short name shown in the banner / share text ("Halloween")
--   emoji   – the day's emoji ("🎃")
--   banner  – the line shown on the welcome pop-up, puzzle page and homepage
--   effect  – optional seasonal effect for the page ('snow' on Christmas Day)
--   extra   – per-pool extras, e.g. {"ditto": {"gen1": [..], "mixed": [..]}}
--             = tile positions drawn as "Ditto versions" (April Fools)
-- get_daily_theme(date, pool) returns the day's theme as jsonb (null if none).
-- The boards themselves are authored separately (see holiday_boards.md); the
-- banner/emoji/effect appear on the date even if a board isn't themed.
-- (Already applied to the live DB via MCP.)

create table if not exists public.daily_themes (
  theme_date date primary key,
  name   text not null,
  emoji  text not null,
  banner text not null,
  effect text,
  extra  jsonb not null default '{}'::jsonb
);
alter table public.daily_themes enable row level security;  -- read via RPC only

insert into public.daily_themes (theme_date, name, emoji, banner, effect) values
 ('2026-10-31','Halloween','🎃','Happy Halloween! Today''s puzzles have a spooky twist.',null),
 ('2026-11-05','Bonfire Night','🎆','Remember, remember… it''s Bonfire Night – expect some fireworks!',null),
 ('2026-11-08','Diwali','🪔','Happy Diwali! Today''s puzzles celebrate the festival of lights.',null),
 ('2026-11-13','Friday the 13th','🐈‍⬛','Friday the 13th – feeling lucky?',null),
 ('2026-12-24','Christmas Eve','🎄','It''s Christmas Eve! Today''s puzzles are feeling festive.',null),
 ('2026-12-25','Christmas Day','🎁','Merry Christmas! Enjoy today''s festive puzzles.','snow'),
 ('2026-12-26','Boxing Day','🥊','Happy Boxing Day! Gloves on for today''s puzzles.',null),
 ('2026-12-31','New Year''s Eve','🥂','Happy New Year''s Eve! One last puzzle for the year.',null),
 ('2027-01-01','New Year''s Day','🗓️','Happy New Year! Start the year with a fresh puzzle.',null),
 ('2027-02-06','Lunar New Year','🐐','Happy Lunar New Year – welcome to the Year of the Goat!',null),
 ('2027-02-09','Pancake Day','🥞','Happy Pancake Day! Flip through today''s puzzles.',null),
 ('2027-02-14','Valentine''s Day','💘','Happy Valentine''s Day! Today''s puzzles are full of love.',null),
 ('2027-02-27','Pokémon Day','⭐','Happy Pokémon Day! Celebrating 31 years of Pokémon.',null),
 ('2027-03-07','Mother''s Day','💐','Happy Mother''s Day! Today''s puzzles celebrate Pokémon mums.',null),
 ('2027-03-17','St Patrick''s Day','☘️','Happy St Patrick''s Day! Feeling lucky?',null),
 ('2027-03-28','Easter Sunday','🐣','Happy Easter! Hop into today''s puzzles.',null),
 ('2027-04-01','Ditto Day','🃏','Happy April Fools! Something''s not quite right about today''s board…',null),
 ('2027-04-22','Earth Day','🌍','Happy Earth Day! Today''s puzzles are all about our planet.',null),
 ('2027-05-04','May the 4th','🚀','May the 4th be with you! Today''s puzzles are out of this world.',null),
 ('2027-06-20','Father''s Day','👔','Happy Father''s Day! Today''s puzzles celebrate Pokémon dads.',null),
 ('2027-06-21','Summer Solstice','☀️','Happy summer solstice – the longest day of the year!',null),
 ('2027-08-08','Our 1st Birthday','🎂','Pokémon Codenames is one year old today – thanks for playing!',null),
 ('2027-08-13','Friday the 13th','🐈‍⬛','Friday the 13th – feeling lucky?',null),
 ('2027-09-01','Back to School','🎒','Back to school! Time to put your Pokémon knowledge to the test.',null)
on conflict (theme_date) do nothing;

create or replace function public.get_daily_theme(p_date date default null, p_pool text default null)
returns jsonb
language sql stable security definer set search_path to 'public'
as $function$
  select jsonb_build_object(
           'name', t.name, 'emoji', t.emoji, 'banner', t.banner, 'effect', t.effect,
           'ditto', coalesce(t.extra -> 'ditto' -> coalesce(p_pool, ''), '[]'::jsonb))
  from public.daily_themes t
  where t.theme_date = coalesce(p_date, current_date);
$function$;
grant execute on function public.get_daily_theme(date, text) to anon, authenticated;
