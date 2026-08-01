

---creacion de vistas
create view vista_cliente
as
select nombre_cliente, ciudad, pais
from cliente;
go
-----------------------

select * from vista_cliente;

----vista de productos caros

create view productos_caros
as
select nombre, precio_venta
from producto
where precio_venta > 100;

select * from productos_caros;

-----vista con join
create view pedidos_clientes
as
select p.codigo_pedido,
c.nombre_cliente,
p.fecha_pedido
from pedido p
inner join cliente c
on p.codigo_cliente = c.codigo_cliente;
select * from pedidos_clientes;


---vista con funciones de agregacion
create view total_pagos_cliente_max
as
select codigo_cliente,
sum(total)
as total_pagado
from pago
group by codigo_cliente;

select * from total_pagos_cliente_max;

--eliminar una vista
drop view pedidos_clientes;
go

-- con CTE
with promedio as (
select avg (precio_venta) as precio_promedio
from producto)
SELECT nombre, precio_venta
FROM producto, promedio
WHERE precio_venta > promedio.precio_promedio;






















