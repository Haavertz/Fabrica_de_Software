CREATE DATABASE titanic;
use titanic;

create table PassengerId(
passengerId int not null,
Survived varchar (255),
Pclass varchar (10), 
nome varchar (255),
Sex varchar (255),
Age varchar (255),
SibSp varchar (255),
Parch varchar (255),
Ticket varchar (255),
Fare varchar(255),
Cabin varchar (255),
Embarked varchar (255)
);

select * from PassengerId;

select count(*) from PassengerId;
select count(*) from PassengerId where Survived = '1';

select count(*) from PassengerId where Survived = 1 and age < 12;
select count(*) from PassengerId where Survived = 0 and age < 12;

select count(*) from PassengerId where Survived = 1 and Sex = "Female";
select count(*) from PassengerId where Survived = 0 and Sex = "Female";

select count(*) from PassengerId where Survived = 1 and Sex = "Male";
select count(*) from PassengerId where Survived = 0 and Sex = "Male";

select count(*) from PassengerId where 