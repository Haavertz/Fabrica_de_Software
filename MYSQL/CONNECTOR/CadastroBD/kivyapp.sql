create database kivyaplication;
use kivyaplication;

create table cadastro(
id_cadastro int auto_increment,
nome varchar(100) not null,
cpf varchar(11) not null,
senha varchar(30) not null,
gmail varchar(100),
primary key (id_cadastro)
);

insert into cadastro (nome, cpf, senha, gmail) value ("Gleison", "12345132681", "123", "gleisonjejin@gmail.com");
insert into cadastro (nome, cpf, senha, gmail) value ("Eduardo", "09823132421", "321", "eduardodudu@gmail.com");
select * from cadastro;
