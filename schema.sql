drop table if exists entries; 
create table entries(
id integer primary key autoincrement,
title String not null,
text String not null
);