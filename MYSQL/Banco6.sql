create database ExercicioEderson;
use ExercicioEderson;

create table EX2_CLIENTE(
codcliente int auto_increment,
nome varchar (50) not null,
datanascimento date not null,
cpf int not null,
primary key (codcliente)
);

insert into EX2_CLIENTE (codcliente, nome, datanascimento, cpf) values (null, "Gleison", "2006-06-09", 99999999);

create table EX2_PEDIDO(
codpedido int auto_increment,
codcliente int not null,
datapedido date not null,
nf int not null, 
valortotal int not null,
primary key (codpedido),
constraint FKpedidoCliente foreign key (codcliente) references EX2_CLIENTE (codcliente)
);

insert into EX2_PEDIDO (codpedido, codcliente, datapedido, nf, valortotal) values (null, null, "2023-06-09",000000001, 20000);


create table EX2_ITEMPEDIDO(
codpedido int not null,
numeroitem int,
valorunitario int not null,
quantidade int not null,
codproduto int not null,
constraint ItempedidoPedido foreign key (codpedido) references EX2_PEDIDO (codpedido),
constraint ItempedidoProduto foreign key (codproduto) references EXE2_PRODUTO (codproduto)
);

insert into EX2_ITEMPEDIDO (codpedido, codcliente, datapedido, nf, valortotal) values (null, null, "2023-06-09",000000001, 20000);

create table EXE2_PRODUTO(
codproduto int auto_increment,
descricao varchar (300),
quantidade int not null,
primary key (codproduto)
);

create table EX2_LOG(
codlog int,
data date not null,
descricao varchar (300),
primary key (codlog)
);

create table EX2_REQUISICAO_COMPRA(
codrequisicaocompra int auto_increment,
codproduto integer,
data_req date not null,
quantidade int not null,
primary key(codrequisicaocompra),
constraint FKRequisicaoProduto foreign key (codproduto) references EXE2_PRODUTO (codproduto)
);

