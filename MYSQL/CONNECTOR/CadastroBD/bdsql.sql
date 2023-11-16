create database menucadastro;
use menucadastro;

create table cadastro(
id int auto_increment primary key,
nome varchar(75) not null,
sobrenome varchar(75) not null,
cpf varchar(11) not null,
email varchar(255) not null,
telefone varchar(12) not null,
endereco varchar(255) not null,
data_nascimento varchar(255) not null,
complemento varchar(10),
cep varchar(8) not null,
senha varchar(255) not null
);

describe cadastro;

insert into cadastro (nome, sobrenome, cpf, email, telefone, endereco, data_nascimento, complemento, cep, senha) 
value ("Gleison","Morais","12345678911","gleisonmorales@gmail.com","67991827644", "Rua do Pelicano", "25/07/2002","1210","79097021","123");