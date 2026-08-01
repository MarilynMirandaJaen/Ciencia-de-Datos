use db_jardineria
---buscar valores con null
select nombre_cliente,ciudad, region
from cliente
where region is null;


---empleados que no tienen jefe asignado
select nombre,apellido1, codigo_jefe
from empleado
where codigo_jefe is null;

---pedidos que aun no han sido entregados
select codigo_pedido,fecha_pedido, fecha_entrega
from pedido
where fecha_entrega is null;

--clientes que si tienen limite de credito(is not null)
select nombre_cliente,limite_credito
from cliente
where limite_credito is not null;

--oficinas que tienen segunda direccion
select ciudad,linea_direccion2
from oficina
where linea_direccion2 is not null;

---reemplazar valores null con coalesce
--sirve para mostrar otro valor cuando aparece null
select nombre_cliente,
coalesce (region,'sin region') as region
from cliente;

--mostrar 'no toene jefe' cuando el empleado no tiene jefe
select nombre,apellido1,
coalesce (cast(codigo_jefe as varchar),'no tiene jefe ') as jefe
from empleado;

--mostrar comentarios en pedidos
--si el pedido no tiene comentarios, aparece 'sin comentarios'
select codigo_pedido,
coalesce (comentarios,'sin comentarios') as comentarios
from pedido;

---clientes que tienen region y limite de credito
---limite credito is not null
select nombre_cliente,region,limite_credito
from cliente
where region is not null and limite_credito is not null;































