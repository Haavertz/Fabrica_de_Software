create database Selects;
use Selects;

create table selec(
cpf varchar (12) not null,
nome varchar (100) not null
);

insert into selec values (321321419, "Gleison");
insert into selec values (312312331, "Ronaldo");
insert into selec values (921341232, "Jorge");
insert into selec values (125123121, "Geovanna");
insert into selec values (312541243, "Roberta");

select cpf from selec; #Busca apenas a coluna cpf na tabela selec
select nome from selec; #Busca apenas a coluna nome na tabela selec
select * from selec ORDER BY nome;
select * from selec ORDER BY nome DESC;
select * from selec;

#ORDER BY - ordena em forma crescente ou alfabetica ORDER BY DESC - decresente e alfabetica

create table city(
estado varchar(150) not null,
cidade varchar(150) not null,
pais varchar(150) not null
);

insert into city values ("Paraiba","Guarabira","Brasil");
insert into city values ("Espinosa","MG","Brasil");
insert into city values ("Brasilian","BR","Brasil");
insert into city values ("Mato Grosso do Sul","CG","Brasil");

select * from city where cidade="CG"; #Literalmente Filtra o Coding








