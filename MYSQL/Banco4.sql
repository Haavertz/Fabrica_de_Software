create database ExercicioEderson;
use ExercicioEderson;

create table Acct_Typ_Cd_LU(
Acct_Code int auto_increment,
Account_Type varchar (30),
primary key (Acct_Code)
);

create table Customer(
Customer_ID int auto_increment,
Customer_Lname varchar (50) not null,
Customer_Fname varchar (50) not null,
Cust_city varchar (50) not null,
Cust_street varchar (50) not null,
Cust_zip int not null,
Cust_Phone int not null,
Fax_Phone int not null,
primary key (Customer_ID)
); 

create table State_Ikup(
St_code int,
State_name varchar (100)
);

create table Supplier(
Supplier_ID int auto_increment,
Supplier_name varchar (50) not null,
Sup_street varchar (50)not null,
Sup_zip varchar(50)not null,
Sup_phone int not null,
Sup_Fax int not null,
primary key(Supplier_ID) 
);

create table Parts_Invertory (
Bar_Code int auto_increment,
Part_name varchar(50) not null,
Prt_description varchar(50) not null,
Prt_Cost varchar(50) not null,
Prt_Price varchar(50) not null,
Quantlty int not null,
primary key(Bar_Code)
);

create table Trans_Code(
TransCode int, 
Transaction_Description varchar (100) not null,
primary key(TransCode)
);

create table Customer_Accont (
Customer_ID int auto_increment,
Last_Purch_dle varchar(50) not null,
Last_pymt_dte varchar(100) not null,
Last_acct_trans_dle varchar (30) not null,
Acct_Balance varchar(50) not null,
primary key(Customer_ID)
);

create table Custome_acct_hist1(
Customer_ID int auto_increment,
Trans_dle varchar(50) not null,
Old_acct_balance varchar (60) not null,
New_acct_balance varchar(60) not null,
primary key(Customer_ID));

create table Purchase_Order(
Seg_ID int auto_increment,
Purch_dle varchar (30) not null,
Serial_num int not null,
Quatily varchar (20) not null,
Price varchar (50) not null,
primary key(Seg_ID)
);

create table Bike_Descripition(
Model_ID int auto_increment,
model_nome varchar(50)not null,
Inv_price varchar(40) not null,
Description_ varchar(50) not null,
primary key (Model_ID));

create table Bike_Invertory(
Seg_ID int auto_increment,
Serial_Number int not null,
Invertory_dle varchar(50),
primary key(Seg_ID));

