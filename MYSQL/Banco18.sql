create database instagram;
use instagram;

create table insta(
Impressions int not null,
From_Home int not null, 
From_Hashtags int not null,
From_Explore text,
From_Other varchar(100),
Saves text not null,
Comments text not null,
Shares text not null,
Likes text not null,
Profile_Visits text not null,
Follows_ text,
Caption text,
Hashtags text
);

select * from insta;