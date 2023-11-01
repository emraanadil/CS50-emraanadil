-- names of songs by Post malone;
select name from songs where artist_id = (select id from artists where name = "Post Malone");