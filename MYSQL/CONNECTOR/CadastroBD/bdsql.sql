create database menucadastro;
use menucadastro;

create table cadastro(
id int auto_increment primary key,
nome varchar(75) not null,
sobrenome varchar(75) not null,
cpf varchar(11),
email varchar(255) not null,
telefone int default(0) not null,
endereco varchar(255) not null,
data_nascimento varchar(255) not null,
complento varchar(10),
cep varchar(8) not null
senha varchar(255) not null,
);

