--creacion de una base de datos--

create database clase3
go

use clase3
go

create table produc(
id int not null,
nombre varchar(10) not null,
clase varchar(5)not null
)
go

insert into produc (id, nombre, clase)values
(1, 'Laptop', 'A'),
(2, 'Mouse', 'B'),
(3, 'Teclado', 'A'),
(4, 'Monitor', 'C'),
(5, 'Bocina', 'B'),
(6, 'Camara', 'A'),
(7, 'Disco', 'C'),
(8, 'Memoria', 'B'),
(9, 'Router', 'A'),
(10, 'Switch', 'C');
go

create table ventas(
id int,
nombre varchar(10),
clase varchar(5)
)
go

select * from produc
go