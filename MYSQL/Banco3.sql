create database Exercicio_003 character set utf8mb4 collate utf8mb4_unicode_ci;
use Exercicio_003;

/*
rename table video2 to video; #vai alterar o nome da tabela
alter table video change temporada2 temporada int;  #vai alterar dentro da tabela que vc escolheu
alter table video add column id_cliente int; #vai adicionar mais uma coluna na tabela 
drop - deletar

*/

######################## Tables ##########################
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
##########################################################

describe mensalidade;
describe Ator;
describe Usuario;
describe Video;

rename table video to mensalidade; #vai alterar o nome da tabela
alter table Video change temporada2 temporada int; #vai alterar dentro da tabela que vc escolheu
alter table Usuario add column id_cliente int; #vai adicionar mais uma coluna na tabela 
