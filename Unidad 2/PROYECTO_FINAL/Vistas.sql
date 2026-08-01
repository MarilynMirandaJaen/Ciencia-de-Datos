use db_universidad;
go

-- Vista de modalidades con más de cinco cursos
-- Muestra las modalidades que tienen más de cinco cursos
-- Displays delivery modes with more than five courses
create view vista_modalidades_cursos
as
select
    modalidad,
    count(*) as cantidad_cursos
from curso
group by modalidad
having count(*) > 5;
go

-- Vista de capacidad de aulas
-- Muestra las aulas con capacidad mayor a 40
-- Displays classrooms with capacity greater than 40
create view vista_aulas_grandes
as
select
    id_aula,
    numero_aula,
    edificio_aula,
    capacidad
from aula
where capacidad > 40;
go

-- Vista de matrículas pagadas o con costo mayor a 200000
-- Muestra las matrículas pagadas o con costo mayor a 200000
-- Displays paid enrollments or enrollments with a cost greater than 200000
create view vista_matriculas
as
select
    id_matricula,
    nombre_estudiante,
    curso,
    costo,
    pagado
from matricula
where curso is not null
and (pagado = 1 or costo > 200000);
go

-- Vista de cursos matriculados
-- Relaciona los cursos con las matrículas realizadas
-- Matches courses with enrollments
create view vista_cursos_matriculados
as
select
    c.id_curso,
    c.nombre_curso,
    c.creditos,
    c.modalidad,
    m.nombre_estudiante,
    m.fecha_matricula,
    m.costo
from curso as c
inner join matricula as m
on c.nombre_curso = m.curso;
go

-- Consulta la vista de modalidades de cursos
-- Queries the course modalities view
select * from vista_modalidades_cursos;

-- Consulta la vista de aulas grandes
-- Queries the large classrooms view
select * from vista_aulas_grandes;

-- Consulta la vista de matrículas y ordena el costo de mayor a menor
-- Queries the enrollments view and sorts the cost from highest to lowest
select * from vista_matriculas
order by costo desc;

-- Consulta la vista de cursos matriculados y ordena por modalidad
-- Queries the enrolled courses view and sorts by delivery mode
select * from vista_cursos_matriculados
order by modalidad asc;