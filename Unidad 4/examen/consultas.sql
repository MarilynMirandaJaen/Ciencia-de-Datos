create database Farmacia_DT;
go

use Farmacia_DT;
go

use Farmacia_DT;
go

select * from Sucursales;
select * from Medicamentos;
select * from Clientes;
select * from Ventas;

/******** verificar columnas con valor 0 *******/
select *
from Ventas
where Cliente_ID not in (
    select Cliente_ID
    from Clientes
);

select *
from Ventas
where Sucursal_ID not in (
    select Sucursal_ID
    from Sucursales
);

select *
from Ventas
where Medicamento_ID not in (
    select Medicamento_ID
    from Medicamentos
);
/******* modificar a permitir valores null en columnas *********/
alter table Ventas
alter column Cliente_ID int null;

alter table Ventas
alter column Sucursal_ID int null;

/********** convertir valores en 0 a NULL para crear relaciones *********/
update Ventas
set Cliente_ID = null
where Venta_ID = 149;

update Ventas
set Sucursal_ID = null
where Venta_ID = 249;

/******** se crea relaciones entre tablas ***********/
alter table Ventas
add constraint FK_Ventas_Sucursales
foreign key (Sucursal_ID)
references Sucursales(Sucursal_ID);

alter table Ventas
add constraint FK_Ventas_Clientes
foreign key (Cliente_ID)
references Clientes(Cliente_ID);

alter table Ventas
add constraint FK_Ventas_Medicamentos
foreign key (Medicamento_ID)
references Medicamentos(Medicamento_ID);