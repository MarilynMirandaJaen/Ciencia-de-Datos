

select count(*)
as total_clientes from cliente;

select count(limite_credito)
as clientes_con_credito from cliente;

select avg(limite_credito)
as promedio_credito from cliente;

-----min---
select min(limite_credito)
as clientes_menos from cliente;

---max--
select max(limite_credito)
as clientes_menos from cliente;


select 
count(*) as total_cientes,
sum(limite_credito) as total_credito,
avg(limite_credito) as promedio_credito,
min(limite_credito) as credito_minimo,
max(limite_credito) as credito_maximo
from cliente;


select 
count(*) as total_pedidos,
sum(fecha_pedido) as primer_pedido,
sum(fecha_pedido) as ultimo_pedido
from pedido;

-----total de pedido por cliente (solo los que tienen mas de 5 pedidos)

select codigo_cliente,
count(*) as total_pedidos
from pedido
group by codigo_cliente
having count (*) > 5

---promedio de precio de productos por gama (solo caras)

select gama , avg(precio_venta) as promedio_precio
from producto
group by gama 
having avg(precio_venta) > 10;

----total pagado por cada cliente 8-solo los que han pagado mucho)

select codigo_cliente,
sum(total)
from pago
group by codigo_cliente
having sum(total) < 10000;

---cantidad de emplados por oficina(solo oficinas grandes)
select codigo_oficina,
count (codigo_empleado) as total_empleados
from empleado
group by codigo_oficina
having count(codigo_empleado) > 5

---total de productos vendidos por pedido(solo pedidos grandes)
select codigo_pedido,
sum (cantidad) as total_productos
from detalle_pedido
group by codigo_pedido
having sum(cantidad) > 100

----clientes por pais (solo paises con muchos clientes)

select pais,
count (*) as total_clientes
from cliente
group by pais
having count(*) > 3

-----iner join----
select
c.nombre_cliente,
p.codigo_pedido,
p.fecha_pedido
from cliente c
inner join pedido p
on c.codigo_cliente=p.codigo_cliente


select
c.nombre_cliente,
p.codigo_pedido,
pr.nombre as producto,
dp.cantidad
from cliente c
inner join pedido p on c.codigo_cliente = p.codigo_cliente
inner join detalle_pedido dp on p.codigo_pedido = dp.codigo_pedido
inner join producto pr on dp.codigo_producto= pr.codigo_producto;


SELECT 
    c.nombre_cliente,
    p.codigo_pedido
FROM cliente c
LEFT JOIN pedido p
ON c.codigo_cliente = p.codigo_cliente;

SELECT c.nombre_cliente
FROM cliente c
LEFT JOIN pedido p 
ON c.codigo_cliente = p.codigo_cliente
WHERE p.codigo_pedido IS NULL;

SELECT 
    c.nombre_cliente,
    p.codigo_pedido
FROM cliente c
RIGHT JOIN pedido p
ON c.codigo_cliente = p.codigo_cliente;

SELECT 
    p.codigo_pedido,
    pr.nombre,
    dp.cantidad
FROM producto pr
RIGHT JOIN detalle_pedido dp 
ON pr.codigo_producto = dp.codigo_producto
RIGHT JOIN pedido p 
ON dp.codigo_pedido = p.codigo_pedido;






































































