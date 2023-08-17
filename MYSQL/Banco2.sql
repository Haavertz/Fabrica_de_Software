create database Senac character set utf8mb4 collate utf8mb4_unicode_ci;
use Senac;

/*
# Comenta
--Comenta
//**
create database senac2 character set utf8mb4 collate utf8mb4_unicode_ci;
create table aluno( 
id int auto_increment,
nome varchar(30) not null,
fone varchar(30) not null,
email varchar(30) not null,
primary key (id)
);
describe aluno

*/

##################### Tables #######################
create table Video(
temporada int,
episodio int,
titulo varchar(100)not null,
ano int default (2023),
duracao int not null,
produtora varchar(50) not null,
tipo varchar(30) not null,
primary key (titulo)
);
create table Ator(
nome varchar(30) not null,
data_nascimento varchar (50) not null default (2023),
local_nascimento varchar (500) not null,
primary key (nome)
);
create table Usuario(
id int auto_increment,
cpf varchar(11) not null,
nome varchar(50) not null,
senha char(123) not null,
cartao varchar(20) not null,
telefone int not null,
primary key (id)
);
create table mensalidade(
mes_ano int not null,
valor_pago float not null,
data_pagto date not null,
primary key (mes_ano)
);
####################################################

describe mensalidade;
describe Ator;
describe Usuario;
describe Video;
