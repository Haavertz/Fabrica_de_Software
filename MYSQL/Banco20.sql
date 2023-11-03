create database hub;
use hub;

create table cliente(
Cpf varchar(11) not null primary key,
Nome varchar(100) not null,
Email varchar(100) not null,
Telefone varchar(13) not null,
Nascimento varchar(10) not null,
Genero varchar(15) not null,
Palestra varchar(3),
TermoUso bool,
PermDados bool
);

delimiter $$

create trigger tgr_DimVagas after insert on cliente
for each row
begin
    update palestra
    set quantidade_vaga = quantidade_vaga - 1
    where sala = new.Palestra;
end;
$$

delimiter ;

create table palestra(
sala varchar(3) primary key,
nome_palestrante varchar(100) not null,
nome_palestra varchar(50) not null,
descricao_palestra varchar(300) not null,
quantidade_vaga int not null
);


delimiter $$

create trigger tgr_Delet after delete on cliente
for each row
begin
    update palestra
    set quantidade_vaga = quantidade_vaga + 1
    where sala = old.Palestra;
end;
$$

delimiter ;


#Palestra

select * from palestra;

insert into palestra(sala, nome_palestrante, nome_palestra, descricao_palestra, quantidade_vaga) value ("305","Kleber Engenheiro","Engenharia de Software","Palestra Engenharia de Software no mercado atual",10);
insert into palestra(sala, nome_palestrante, nome_palestra, descricao_palestra, quantidade_vaga) value ("306","Jéder Muniz da Silva","Workshop","Workshop – Introdução ao Revit Architecture",10);
insert into palestra(sala, nome_palestrante, nome_palestra, descricao_palestra, quantidade_vaga) value ("307","Gabriel Ferreira Medeiros","Modelagem","Modelagem 3D",10);
insert into palestra(sala, nome_palestrante, nome_palestra, descricao_palestra, quantidade_vaga) value ("308","Dias Barber","Freestyle Livre","Creative cut - Freestyle Livre",10);

#Clientes 

insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("99999999999","Gleison","gleison06@gmail.com",38991827622,"2006-06-09","Masculino","305","1","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("12312312219","Ronaldo","ronardo42@gmail.com",38991827622,"2001-10-23","Masculino","306","0","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("41251512422","Juberto","jubertin0@gmail.com",38991827622,"2003-12-01","Masculino","307","1","0");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("61623123122","Juninho","juninho25@gmail.com",38991827622,"2008-02-11","Masculino","308","1","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("78645894545","Bianca","bian77@gmail.com",38991827622,"2002-02-09","Feminino","306","0","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("12312321321","Carvalho","bianca22@gmail.com",38991827622,"2002-02-09","Feminino","305","0","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("12124123421","Odin","odin999@gmail.com",38991827622,"2002-02-09","Masculino","305","0","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("31212451221","Roberta","robertinha00@gmail.com",38991827622,"2006-06-09","Feminino","305","1","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("42161232132","Wesley","Wesley055@gmail.com",38991827622,"2001-10-23","Masculino","306","0","0");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("74532131232","Jhoy","jhoy44@gmail.com",38991827622,"2003-12-01","Masculino","307","1","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("76321312215","juliano","juninho25@gmail.com",38991827622,"2008-02-11","Masculino","308","1","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("12623213215","Luiza","bianca22@gmail.com",38991827622,"2002-02-09","Feminino","306","0","1");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("78598657652","Durkard","Durk231@gmail.com",38991827622,"2002-02-09","Feminino","305","0","0");
insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("15125812371","Jhonnatan","Jhonnatan2211@gmail.com",38991827622,"2002-02-09","Masculino","305","0","0");

#insert into cliente(Cpf, Nome, Email, Telefone, Nascimento, Genero, Palestra, TermoUso, PermDados) values ("51234123313","Igor","igorFe82@gmail.com",38991827622,"2002-02-09","Masculino","305","0","1");

select * from cliente;
select * from palestra;

DELETE FROM cliente WHERE cpf = "99999999999";
DELETE FROM cliente WHERE cpf = "31212451221";
DELETE FROM cliente WHERE cpf = "12623213215";
DELETE FROM cliente WHERE cpf = "61623123122";

show triggers;

select * from cliente;
select * from palestra;


