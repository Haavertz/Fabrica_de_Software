create database vagas_modelo character set utf8mb4 collate utf8mb4_unicode_ci; -- Banco de Dados Criptografado
use vagas_modelo;

create table cadastro_modelo(
    id_modelo int auto_increment not null primary key,
    nome varchar(255) not null,
    cpf varchar(20) not null,
    email varchar(255) not null,
    fone varchar(50) not null,
    data_nascimento varchar(50) not null
);

create table adicionar_servico(
    id_servico int auto_increment not null primary key,
    nome_servico varchar(255) not null,
    vagas int not null,
    data_comeco varchar(30) not null,
    horario_comeco varchar(10) not null,
    descricao varchar(500) not null
);

create table login_adm(
    login varchar(255),
    senha varchar(30)
);

insert into cadastro_modelo (id_modelo, nome, cpf, email, fone, data_nascimento) values (null, "Gleison", "345678", "@gmail.com", "6799199812", "10/10/2000");
insert into adicionar_servico (id_servico, nome_servico, vagas, data_comeco, horario_comeco, descricao) values (null, "Cabelo", 10, "17/11/2023", "10:10", "Cortar o cabelo de graça");

SET @id_servico := LAST_INSERT_ID();

select * from adicionar_servico;
select * from cadastro_modelo;

delimiter $

create trigger tgr_cadastromodelo_insert after insert on cadastro_modelo
for each row
begin
    update adicionar_servico set vagas = vagas - 1 where id_servico = @id_servico;
end $

delimiter ;

insert into cadastro_modelo (id_modelo, nome, cpf, email, fone, data_nascimento) values (null, "Joao", "1235678", "@gmail.com", "6799546712", "20/20/3000");

-- drop trigger tgr_cadastromodelo_insert;

insert into login_adm values ("SenacModelos", "abc123");
-- drop database vagas_modelo;
