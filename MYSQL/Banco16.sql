create database citizen;
use citizen;

create table STATE (
    ID_ESTADO int auto_increment,
    ESTADO varchar(100) not null,
    primary key (ID_ESTADO)
);

create table CITY (
    ID_CIDADE int auto_increment,
    CIDADE varchar(100) not null,
    primary key (ID_CIDADE)
);

create table GENDER (
    ID_SEXO int auto_increment,
    SEXO varchar(100) not null,
    primary key (ID_SEXO)
);

create table NATIONALITY (
    ID_NACIONALIDADE int auto_increment,
    NACIONALIDADE varchar(100) not null,
    primary key (ID_NACIONALIDADE)
);

create table RACE (
    ID_RACA int auto_increment,
    RACA varchar(100) not null,
    primary key (ID_RACA)
);

create table SCHOLARITY (
    ID_ESCOLARIDADE int auto_increment,
    ESCOLARIDADE varchar(100) not null,
    primary key (ID_ESCOLARIDADE)
);

create table CLIENTES (
    CPF varchar(11) not null,
    NOME varchar(100) not null,
    RG varchar(50) not null,
    ID_ESTADO int not null,
    ID_CIDADE int not null,
    ID_SEXO int not null,
    ID_NACIONALIDADE int not null,
    FONE varchar(50) not null,
    ID_RACA int not null,
    ID_ESCOLARIDADE int not null,
    constraint foreign key (ID_ESTADO) references STATE (ID_ESTADO),
    constraint foreign key (ID_CIDADE) references CITY(ID_CIDADE),
    constraint foreign key (ID_SEXO) references GENDER(ID_SEXO),
    constraint foreign key (ID_NACIONALIDADE) references NATIONALITY(ID_NACIONALIDADE),
    constraint foreign key (ID_RACA) references RACE(ID_RACA),
    constraint foreign key (ID_ESCOLARIDADE) references SCHOLARITY(ID_ESCOLARIDADE)
);




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


#Cidades do Acre
INSERT CITY (CIDADE) values ('Brasiléia');
INSERT CITY (CIDADE) values ('Feijó');
INSERT CITY (CIDADE) values ('Santa Rosa do Purus');
INSERT CITY (CIDADE) values ('Porto Walter');
INSERT CITY (CIDADE) values ('Tarauacá');

#Cidades do Alagoas
INSERT CITY (CIDADE) values ('Maceió');
INSERT CITY (CIDADE) values ('Piranhas');
INSERT CITY (CIDADE) values ('Campo Alegre');
INSERT CITY (CIDADE) values ('Murici');
INSERT CITY (CIDADE) values ('Porto Calvo');

#Cidades do Amapá
INSERT CITY (CIDADE) values ('Macapá');
INSERT CITY (CIDADE) values ('Porto Grande');
INSERT CITY (CIDADE) values ('Itaubal');
INSERT CITY (CIDADE) values ('Santana');
INSERT CITY (CIDADE) values ('Amapá');

#Cidades do Amazonas
INSERT CITY (CIDADE) values ('Manaus');
INSERT CITY (CIDADE) values ('Tefé');
INSERT CITY (CIDADE) values ('Itacoatiara');
INSERT CITY (CIDADE) values ('Codajás');
INSERT CITY (CIDADE) values ('Maués');

#Cidades da Bahia
INSERT CITY (CIDADE) values ('Vitória da Conquista');
INSERT CITY (CIDADE) values ('Salvador');
INSERT CITY (CIDADE) values ('Irecê');
INSERT CITY (CIDADE) values ('Alagoinhas');
INSERT CITY (CIDADE) values ('Jacobina');

#Cidades do Ceará
INSERT CITY (CIDADE) values ('Fortaleza');
INSERT CITY (CIDADE) values ('Sobral');
INSERT CITY (CIDADE) values ('Itapipoca');
INSERT CITY (CIDADE) values ('Acaraú');
INSERT CITY (CIDADE) values ('Crato');

#Cidades do Distrito Federal
INSERT CITY (CIDADE) values ('Gama');
INSERT CITY (CIDADE) values ('Taguatinga');
INSERT CITY (CIDADE) values ('Brazlândia');
INSERT CITY (CIDADE) values ('Sobradinho');
INSERT CITY (CIDADE) values ('Planaltina');

#Cidades do Espírito Santo
INSERT CITY (CIDADE) values ('Vitória');
INSERT CITY (CIDADE) values ('Guarapari');
INSERT CITY (CIDADE) values ('Zila Velha');
INSERT CITY (CIDADE) values ('Cariacica');
INSERT CITY (CIDADE) values ('Serra');

#Cidades de Goiás
INSERT CITY (CIDADE) values ('Goiás');
INSERT CITY (CIDADE) values ('Goiânea');
INSERT CITY (CIDADE) values ('Anápolis');
INSERT CITY (CIDADE) values ('Aparecida de Goiânea');
INSERT CITY (CIDADE) values ('Jatai');

#Cidades do Maranhão
INSERT CITY (CIDADE) values ('Araioses');
INSERT CITY (CIDADE) values ('Caxias');
INSERT CITY (CIDADE) values ('São Luis');
INSERT CITY (CIDADE) values ('Codó');
INSERT CITY (CIDADE) values ('Santa Inês');

#Cidades do Mato Grosso
INSERT CITY (CIDADE) values ('Cuiabá');
INSERT CITY (CIDADE) values ('Rodonópolis');
INSERT CITY (CIDADE) values ('Cáceres');
INSERT CITY (CIDADE) values ('Poconé');
INSERT CITY (CIDADE) values ('Sinop');

#Cidades do Mato Grosso do Sul
INSERT CITY (CIDADE) values ('Campo Grande');
INSERT CITY (CIDADE) values ('Dourados');
INSERT CITY (CIDADE) values ('Ponta Porã');
INSERT CITY (CIDADE) values ('Corumbá');
INSERT CITY (CIDADE) values ('Bonito');

#Cidades de Minas Gerais
INSERT CITY (CIDADE) values ('Belo Horizonte');
INSERT CITY (CIDADE) values ('Contagem');
INSERT CITY (CIDADE) values ('Betim');
INSERT CITY (CIDADE) values ('Uberaba');
INSERT CITY (CIDADE) values ('Montes Claros');

#Cidades do Pará
INSERT CITY (CIDADE) values ('Breves');
INSERT CITY (CIDADE) values ('Anamindeua');
INSERT CITY (CIDADE) values ('Zltamira');
INSERT CITY (CIDADE) values ('Santarém');
INSERT CITY (CIDADE) values ('Belém');

#Cidades do Paraíba
INSERT CITY (CIDADE) values ('Santa Rita');
INSERT CITY (CIDADE) values ('João Pessoa');
INSERT CITY (CIDADE) values ('Campina Grande');
INSERT CITY (CIDADE) values ('Mamanguape');
INSERT CITY (CIDADE) values ('Pombal');

#Cidades de Pernambuco
INSERT CITY (CIDADE) values ('Petrolina');
INSERT CITY (CIDADE) values ('Moreno');
INSERT CITY (CIDADE) values ('Guaranhuns');
INSERT CITY (CIDADE) values ('Recife');
INSERT CITY (CIDADE) values ('Zrcoverde');

#Cidades do Piauí
INSERT CITY (CIDADE) values ('Teresina');
INSERT CITY (CIDADE) values ('Picos');
INSERT CITY (CIDADE) values ('Floriano');
INSERT CITY (CIDADE) values ('Pedro II');
INSERT CITY (CIDADE) values ('Bom Jesus');

#Cidades do Rio de Janeiro
INSERT CITY (CIDADE) values ('Rio de Janeiro');
INSERT CITY (CIDADE) values ('Santa Maria Madalena');
INSERT CITY (CIDADE) values ('Angra dos Reis');
INSERT CITY (CIDADE) values ('Petrópolis');
INSERT CITY (CIDADE) values ('Araruama');

#Cidades do Rio Grande do Norte
INSERT CITY (CIDADE) values ('Natal');
INSERT CITY (CIDADE) values ('Macau');
INSERT CITY (CIDADE) values ('Mossoró');
INSERT CITY (CIDADE) values ('Parnamirim');
INSERT CITY (CIDADE) values ('Santo Antonio');

#Cidades do Rio Grande do Sul
INSERT CITY (CIDADE) values ('Rio Grande');
INSERT CITY (CIDADE) values ('Porto Alegre');
INSERT CITY (CIDADE) values ('Caxias do Sul');
INSERT CITY (CIDADE) values ('Canoas');
INSERT CITY (CIDADE) values ('Pelotas');

#Cidades de Roraima
INSERT CITY (CIDADE) values ('Boa Vista');
INSERT CITY (CIDADE) values ('Bonfim');
INSERT CITY (CIDADE) values ('São Luiz');
INSERT CITY (CIDADE) values ('Normandia');
INSERT CITY (CIDADE) values ('Mucajaí');

#Cidades de Santa Catarina
INSERT CITY (CIDADE) values ("Florianópolis");
INSERT CITY (CIDADE) values ("Blumenau");
INSERT CITY (CIDADE) values ("São José");
INSERT CITY (CIDADE) values ("Itajaí");
INSERT CITY (CIDADE) values ("São José");

#Cidades de São Paulo 
INSERT CITY (CIDADE) values ("Carapicuíba");
INSERT CITY (CIDADE) values ("Cotia");
INSERT CITY (CIDADE) values ("Barueri");
INSERT CITY (CIDADE) values ("Cajamar");
INSERT CITY (CIDADE) values ("Arujá");

#Cidades de Sergipe 
INSERT CITY (CIDADE) values ("ESTÂNCIA");
INSERT CITY (CIDADE) values ("NOSSA SENHORA DO SOCORRO");
INSERT CITY (CIDADE) values ("LAGARTO");
INSERT CITY (CIDADE) values ("TOBIAS BARRETO");
INSERT CITY (CIDADE) values ("Araguatins");

#Cidades de Tocantins
INSERT CITY (CIDADE) values ("Palmas");
INSERT CITY (CIDADE) values ("Araguaína ");
INSERT CITY (CIDADE) values ("Gurupi");
INSERT CITY (CIDADE) values ("Palmas Porto");
INSERT CITY (CIDADE) values ("Araguatins");

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




INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('12345678911', 'João', '123456789',1,3,1,2,"212113212",1,6);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('21243124212', 'Ana Catarina', '123456789',7,3,2,2,"321322132",2,4);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('31231215412', 'Claudio', '123456789',2,4,1,1,"987654231",1,2);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('13123128911', 'Toninho', '123456789',10,5,1,1,"213126781",3,3);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('19381818911', 'Igor', '123456789',11,2,1,2,"21211312",1,2);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('12318931231', 'Marcelo', '123456789',12,7,1,2,"21211312",2,2);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('21312312321', 'Cristiano Ronaldo', '123456789',3,2,1,1,"21211312",1,6);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('51251276754', 'Jurelina', '123456789',2,3,2,2,"21211312",4,5);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('26138645214', 'Eduardo', '123456789',6,9,2,2,"21211312",2,7);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('61273435634', 'Nicolas', '123456789',14,100,1,2,"21211312",1,7);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('69923131293', 'Pedrinho', '123456789',5,22,1,1,"21211312",3,7);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('24592143123', 'Larissa', '123456789',12,2,2,1,"21211312",3,7);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('15126261321', 'Fernado', '123456789',21,3,1,1,"21211312",2,4);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('61231251231', 'Rodrigo', '123456789',14,10,3,2,"21211312",1,2);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('61431241123', 'Walken', '123456789',12,11,1,2,"21211312",1,3);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('61261231231', 'Beatrix', '123456789',3,12,2,1,"21211312",2,5);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('65645645645', 'Lerindo', '123456789',5,9,1,2,"21211312",3,4);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('74324324324', 'Maria', '123456789',22,8,2,1,"21211312",4,4);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('12321321321', 'Carolina', '123456789',23,3,2,1,"21211312",3,7);
INSERT INTO CLIENTES (CPF, NOME, RG, ID_ESTADO, ID_CIDADE, ID_SEXO, ID_NACIONALIDADE, FONE, ID_RACA, ID_ESCOLARIDADE) values ('41829412213', 'Ederson', '123456789',19,123,1,1,"21211312",1,6);

SELECT * FROM CITY;
SELECT * FROM RACE;
SELECT * FROM SCHOLARITY;
SELECT * FROM NATIONALITY;
SELECT * FROM STATE;
SELECT * FROM GENDER;
SELECT * FROM CLIENTES;


select CLIENTES.nome, CITY.CIDADE from CLIENTES INNER JOIN CITY ON CLIENTES.ID_CIDADE = CITY.ID_CIDADE;
SELECT CLIENTES.nome, STATE.ESTADO FROM CLIENTES INNER JOIN STATE ON CLIENTES.ID_ESTADO = STATE.ID_ESTADO;
SELECT CLIENTES.nome, CLIENTES.CPF, RACE.RACA FROM CLIENTES INNER JOIN RACE ON CLIENTES.ID_RACA = RACE.ID_RACA;
SELECT CLIENTES.nome, NATIONALITY.NACIONALIDADE FROM CLIENTES INNER JOIN NATIONALITY ON CLIENTES.ID_NACIONALIDADE = NATIONALITY.ID_NACIONALIDADE;
SELECT CLIENTES.nome, SCHOLARITY.ESCOLARIDADE FROM CLIENTES INNER JOIN SCHOLARITY ON CLIENTES.ID_ESCOLARIDADE = SCHOLARITY.ID_ESCOLARIDADE;
SELECT CLIENTES.nome, CITY.CIDADE, STATE.ESTADO FROM CLIENTES INNER JOIN CITY ON CLIENTES.ID_CIDADE = CITY.ID_CIDADE INNER JOIN STATE ON CLIENTES.ID_ESTADO = STATE.ID_ESTADO;
SELECT CLIENTES.nome, CITY.CIDADE, STATE.ESTADO , CLIENTES.FONE, CLIENTES.RG, GENDER.SEXO, NATIONALITY.NACIONALIDADE, RACE.RACA, SCHOLARITY.ESCOLARIDADE FROM CLIENTES INNER JOIN CITY ON CLIENTES.ID_CIDADE = CITY.ID_CIDADE INNER JOIN STATE ON CLIENTES.ID_ESTADO = STATE.ID_ESTADO INNER JOIN GENDER ON CLIENTES.ID_SEXO = GENDER.ID_SEXO INNER JOIN NATIONALITY ON CLIENTES.ID_NACIONALIDADE = NATIONALITY.ID_NACIONALIDADE INNER JOIN RACE ON CLIENTES.ID_RACA = RACE.ID_RACA INNER JOIN SCHOLARITY ON CLIENTES.ID_ESCOLARIDADE = SCHOLARITY.ID_ESCOLARIDADE;
SET SQL_SAFE_UPDATES = 0;

UPDATE CITY SET CIDADE = 'MENOR QUE M' WHERE CIDADE >= 'A%' AND CIDADE < "N%";
UPDATE CITY SET CIDADE = 'MAIOR QUE M' WHERE CIDADE > 'N%';


#drop database citizen;
select * FROM CITY;
select * FROM NATIONALITY;




