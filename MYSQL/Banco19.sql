create database prod;
use prod;

create table produtos (
    referencia varchar(3) primary key,
    descricao varchar(50) unique,
    estoque int not null default 0
);

insert into produtos values ("001", "Feijão", 10);
insert into produtos values ("002", "Arroz", 5);
insert into produtos values ("003", "Farinha", 15);

create table itensvenda (
    venda int,
    produto varchar(3),
    quantidade int
);

insert into itensvenda values (1, "001", 3);
insert into itensvenda values (1, "002", 1);
insert into itensvenda values (1, "003", 5);

delimiter $

create table der (
    venda int
)$
insert into der values (3)$

select * from der$

delimiter ;

delimiter $
create trigger tgr_itensVenda_Insert after insert on itensvenda for each row begin
    Update produtos set estoque = estoque - new.quantidade 
    where referencia = new.produto;
end$
show triggers$

delimiter ;

select * from produtos;
select * from itensvenda;

insert into itensvenda values (1, "002", 3);
insert into itensvenda values (1, "001", 5); 


delimiter $

create trigger tgr_itensVenda_Delete after delete on itensvenda for each row begin
    Update produtos set estoque = estoque + old.quantidade 
    where referencia = old.produto;
end$
show triggers$

delimiter ;

DELETE FROM itensvenda WHERE produto = "001";

set sql_safe_updates = 0;

show triggers;


DELETE FROM itensvenda WHERE produto = "001";

drop trigger tgr_itensVenda_Delete;