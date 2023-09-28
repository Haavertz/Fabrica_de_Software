create database citizen;
use citizen;

create table STATE (
    ID_ESTADO int auto_increment,
    ESTADO varchar(30) not null,
    primary key (ID_ESTADO)
);

create table CITY (
    ID_CIDADE int auto_increment,
    CIDADE varchar(30) not null,
    primary key (ID_CIDADE)
);

create table GENDER (
    ID_SEXO int auto_increment,
    SEXO varchar(30) not null,
    primary key (ID_SEXO)
);

create table NATIONALITY (
    ID_NACIONALIDADE int auto_increment,
    NACIONALIDADE varchar(30) not null,
    primary key (ID_NACIONALIDADE)
);

create table RACE (
    ID_RACA int auto_increment,
    RACA varchar(30) not null,
    primary key (ID_RACA)
);

create table SCHOLARITY (
    ID_ESCOLARIDADE int auto_increment,
    ESCOLARIDADE varchar(30) not null,
    primary key (ID_ESCOLARIDADE)
);

create table CLIENTES (
    CPF varchar(11) not null,
    NOME varchar(30) not null,
    RG varchar(30) not null,
    ID_ESTADO int,
    ID_CIDADE int,
    ID_SEXO int,
    ID_NACIONALIDADE int,
    FONE varchar(30) not null,
    ID_RACA int,
    ID_ESCOLARIDADE int,
    constraint foreign key (ID_ESTADO) references STATE(ID_ESTADO),
    constraint foreign key (ID_CIDADE) references CITY(ID_CIDADE),
    constraint foreign key (ID_SEXO) references GENDER(ID_SEXO),
    constraint foreign key (ID_NACIONALIDADE) references NATIONALITY(ID_NACIONALIDADE),
    constraint foreign key (ID_RACA) references RACE(ID_RACA),
    constraint foreign key (ID_ESCOLARIDADE) references SCHOLARITY(ID_ESCOLARIDADE)
);


INSERT INTO CLIENTES (CPF, NOME, RG, FONE) values ('11111111111', 'João Silva', '123456789',111111111);
INSERT STATE (ESTADO) values ('Acre');
INSERT STATE (ESTADO) values ('Alagoas');
INSERT STATE (ESTADO) values ('Amapá');
INSERT STATE (ESTADO) values ('Amazonas');
INSERT STATE (ESTADO) values ('Bahia');
INSERT STATE (ESTADO) values ('Ceará');
INSERT STATE (ESTADO) values ('Distrito Federal');
INSERT STATE (ESTADO) values ('Espírito Santo');
INSERT STATE (ESTADO) values ('Goiás');
INSERT STATE (ESTADO) values ('Maranhão');
INSERT STATE (ESTADO) values ('Mato Grosso');
INSERT STATE (ESTADO) values ('Mato Grosso do Sul');
INSERT STATE (ESTADO) values ('Minas Gerais');
INSERT STATE (ESTADO) values ('Pará');
INSERT STATE (ESTADO) values ('Paraíba');
INSERT STATE (ESTADO) values ('Paraná');
INSERT STATE (ESTADO) values ('Pernambuco');
INSERT STATE (ESTADO) values ('Piauí');
INSERT STATE (ESTADO) values ('Rio de Janeiro');
INSERT STATE (ESTADO) values ('Rio Grande do Norte');
INSERT STATE (ESTADO) values ('Rio Grande do Sul');
INSERT STATE (ESTADO) values ('Rondônia');
INSERT STATE (ESTADO) values ('Roraima');
INSERT STATE (ESTADO) values ('Santa Catarina');
INSERT STATE (ESTADO) values ('São Paulo');
INSERT STATE (ESTADO) values ('Sergipe');
INSERT STATE (ESTADO) values ('Tocantins');


INSERT CITY (CIDADE) values ('Rio Branco');
INSERT CITY (CIDADE) values ('Cruzeiro do Sul');
INSERT CITY (CIDADE) values ('Sena Madureira');
INSERT CITY (CIDADE) values ('Feijó');
INSERT CITY (CIDADE) values ('Maceió');
INSERT CITY (CIDADE) values ('Arapiraca');
INSERT CITY (CIDADE) values ('Palmeira dos Índios');
INSERT CITY (CIDADE) values ('Rio Largo');
INSERT CITY (CIDADE) values ('Santana do Ipanema');
INSERT CITY (CIDADE) values ('Macapá');
INSERT CITY (CIDADE) values ('Santana');
INSERT CITY (CIDADE) values ('Laranjal do Jari');
INSERT CITY (CIDADE) values ('Oiapoque');
INSERT CITY (CIDADE) values ('Porto Grande');
INSERT CITY (CIDADE) values ('Manaus');

INSERT GENDER (SEXO) values ('Masculino');
INSERT GENDER (SEXO) values ('Feminino');
INSERT GENDER (SEXO) values ("TRANSFORMES");

INSERT NATIONALITY (NACIONALIDADE) values ('Brasileira');
INSERT NATIONALITY (NACIONALIDADE) values ('Estrangeira');

INSERT RACE (RACA) values ('Branca');
INSERT RACE (RACA) values ('Parda');
INSERT RACE (RACA) values ('Negra');
INSERT RACE (RACA) values ('Indigena');

INSERT SCHOLARITY (ESCOLARIDADE) values ('Sem Educação Formal');
INSERT SCHOLARITY (ESCOLARIDADE) values ('Ensino Fundamental Incompleto');
INSERT SCHOLARITY (ESCOLARIDADE) values ('Ensino Fundamental Completo');
INSERT SCHOLARITY (ESCOLARIDADE) values ('Ensino Médio Incompleto');
INSERT SCHOLARITY (ESCOLARIDADE) values ('Ensino Médio Completo');
INSERT SCHOLARITY (ESCOLARIDADE) values ('Ensino Superior Incompleto');
INSERT SCHOLARITY (ESCOLARIDADE) values ('Ensino Superior Completo');
INSERT SCHOLARITY (ESCOLARIDADE) values ('Desempregado');




SELECT * FROM CITY;
SELECT * FROM RACE;
SELECT * FROM SCHOLARITY;
SELECT * FROM NATIONALITY;
SELECT * FROM STATE;
SELECT * FROM GENDER;
SELECT * FROM CLIENTES;




