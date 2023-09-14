create database universidade;
use universidade;

create table departamento (
codigo int auto_increment,
nome varchar (30) not null,
telefone varchar (30) not null,
centro varchar (30) not null,
primary key (codigo)
);

create table aluno (
numerodematricula int auto_increment,
nome varchar (30) not null,
cpf varchar (30) not null,
endereco varchar (50) not null,
rua varchar (30) not null,
cidade varchar (30) not null,
cep varchar (40) not null,
telefones varchar (100) not null,
datanasc date,
sexo varchar (30) not null,
departamento varchar (40) not null,
curso varchar (30) not null,
primary key (numerodematricula)
);

create table curso (
nome varchar (30) not null,
tipo varchar (30) not null,
tecnico varchar (30) not null,
graduacao varchar (30) not null,
mestrado varchar (40) not null,
doutorado varchar (40) not null,
departamento varchar (30) not null,
coordenador varchar (30) not null,
vice_coordenador varchar (30) not null,
primary key (nome)
);

create table professor ( 
nome varchar (30) not null,
cpf varchar (30) not null,
departamento varchar (30) not null,
telefone varchar (30) not null,
primary key (nome) 
);
