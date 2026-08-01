use db_jardineria
go

--comando para buscar un nombre <> diferente e = igual a 
select * from cliente where nombre_contacto = 'Jose';
select * from cliente where nombre_contacto <> 'Jose';


--% parecido
select nombre_contacto  from cliente where  nombre_contacto
LIKE 'luis%';

--% que terminen en %an
select nombre_contacto  from cliente where  nombre_contacto
LIKE '%an';


----empiecen con Ju%
select nombre_contacto, apellido_contacto, telefono from cliente where  nombre_contacto
LIKE 'Ju%';


----empiecen con J%
select nombre_contacto, apellido_contacto, telefono from cliente where  nombre_contacto
LIKE 'J%';


----algun lugar tengan la %b%
select nombre_contacto from cliente where  nombre_contacto
LIKE '%b%';

----limite mayor o menor
----nombe del cont=xxx y AND > 1000
select * from cliente where  nombre_contacto = 'Anne'
AND  limite_credito > 1000


select * from cliente where  nombre_contacto = 'Anne'
AND  limite_credito > 3000

select * from cliente where  ciudad like '%lo%'
AND  limite_credito > 3000

------or----------
select * from cliente where  ciudad  ='Miami'
OR  limite_credito > 3000

select * from cliente where  ciudad  ='Miami'
OR  limite_credito > 3000


-----algun espacio en NULL
select nombre_cliente,linea_direccion2  from cliente where linea_direccion1 is NULL or linea_direccion2 is NULL 

select * from cliente where  not ciudad  ='San Francisco'

select * from cliente where  ciudad  in ('Miami','Madrid') 
and codigo_empleado_rep_ventas between 5 and 8 and nombre_cliente like 'D%'











