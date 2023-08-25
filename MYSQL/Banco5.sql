create database Project character set utf8mb4 collate utf8mb4_unicode_ci;
use Project;

create table ADM(
id int auto_increment,
cpf int not null,
nome varchar (50) not null,
email varchar (50) not null,
senha varchar(50) not null,
fone int not null,
primary key (id)
);

create table vagas_psg(
id int auto_increment,
nome varchar (50) not null,
cpf int not null,
data_nascimento date not null,
escolaridade varchar (20) not null,
responsavel varchar (50) not null,
fone int not null,
email varchar (200) not null,
primary key(id)
#vagas_psg integer, constraint fk_VagaEdital foreign key(FK_ID_Edital)
);

create table projeto(
id int auto_increment,
nome varchar(50) not null,
cnpj int not null,
fone int not null,
email varchar (50) not null,
cpf_titular int not null,
descricao varchar(300) not null,
primary key (id)
);

create table Vagas(
id int auto_increment,
email varchar (50),


);