-- 46: Fix blank tile images for Nidoran♀, Nidoran♂ and Flabébé.
-- Daily boards use the official names, but the `pokemon` table stored plain
-- spellings ("Nidoran (F)", "Flabebe"), so the name lookup missed and the tile
-- had no picture. Give those rows their proper names (and the Treasures of Ruin
-- their official hyphens, for consistency in Classic games too).
update public.pokemon set name = 'Nidoran♀'  where id = 29;
update public.pokemon set name = 'Nidoran♂'  where id = 32;
update public.pokemon set name = 'Flabébé'   where id = 669;
update public.pokemon set name = 'Wo-Chien'  where id = 1001;
update public.pokemon set name = 'Chien-Pao' where id = 1002;
update public.pokemon set name = 'Ting-Lu'   where id = 1003;
update public.pokemon set name = 'Chi-Yu'    where id = 1004;
