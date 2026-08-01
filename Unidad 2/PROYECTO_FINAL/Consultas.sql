use db_universidad;
go

-- 1. SELECT
-- Muestra todos los estudiantes
-- Displays all students
select *
from estudiante;

-- 2. WHERE
-- Muestra los profesores activos
-- Displays active professors
select *
from profesores
where activo_profesor = 1;

-- 3. ORDER BY
-- Ordena los cursos por cantidad de créditos
-- Sorts courses by number of credits
select
    nombre_curso,
    creditos,
    modalidad
from curso
order by creditos desc;

-- 4. DISTINCT
-- Muestra los edificios de las facultades sin repetir
-- Displays faculty buildings without duplicates
select distinct edificio
from facultad;

-- 5. LIKE
-- Busca aulas cuyo número comienza con A
-- Searches for classrooms whose number starts with A
select *
from aula
where numero_aula like 'A%';

-- 6. BETWEEN
-- Muestra matrículas con costo entre 180000 y 230000
-- Displays enrollments costing between 180000 and 230000
select
    nombre_estudiante,
    curso,
    costo
from matricula
where costo between 180000 and 230000;

-- 7. IN
-- Muestra cursos virtuales o híbridos
-- Displays virtual or hybrid courses
select *
from curso
where modalidad in ('Virtual', 'Hibrido');

-- 8. NOT
-- Muestra estudiantes que no están activos
-- Displays students who are not active
select *
from estudiante
where not activo_estudiante = 1;

-- 9. IS NULL
-- Muestra profesores que no tienen correo registrado
-- Displays professors without a registered email
select *
from profesores
where email_profesor is null;

-- 10. IS NOT NULL
-- Muestra facultades que tienen teléfono registrado
-- Displays faculties with a registered phone number
select *
from facultad
where telefono is not null;

-- 11. AND
-- Muestra aulas con capacidad mayor a 35 en Bloque A
-- Displays classrooms with capacity greater than 35 in Block A
select *
from aula
where edificio_aula = 'Bloque A'
  and capacidad > 35;

-- 12. OR
-- Muestra matrículas pagadas o con costo menor a 180000
-- Displays paid enrollments or enrollments costing less than 180000
select *
from matricula
where pagado = 1
   or costo < 180000;

-- 13. GROUP BY
-- Agrupa los estudiantes por género
-- Groups students by gender
select
    genero,
    count(*) as cantidad_estudiantes
from estudiante
group by genero;

-- 14. HAVING
-- Muestra modalidades que tienen más de cinco cursos
-- Displays delivery modes with more than five courses
select
    modalidad,
    count(*) as cantidad_cursos
from curso
group by modalidad
having count(*) > 5;

-- 15. COUNT
-- Cuenta la cantidad total de profesores
-- Counts the total number of professors
select count(*) as total_profesores
from profesores;

-- 16. SUM
-- Suma el costo de todas las matrículas
-- Adds the cost of all enrollments
select sum(costo) as costo_total_matriculas
from matricula;

-- 17. AVG
-- Calcula la capacidad promedio de las aulas
-- Calculates the average classroom capacity
select avg(capacidad) as capacidad_promedio
from aula;

-- 18. MIN
-- Muestra el promedio académico más bajo
-- Displays the lowest academic average
select min(promedio) as promedio_minimo
from estudiante;

-- 19. MAX
-- Muestra el salario más alto de los profesores
-- Displays the highest professor salary
select max(salario) as salario_maximo
from profesores;

-- 20. INNER JOIN
-- Relaciona estudiantes con sus matrículas
-- Matches students with their enrollments
select
    e.id_estudiante,
    e.nombre_estudiante,
    e.apellido1_estudiante,
    m.curso,
    m.fecha_matricula,
    m.costo,
    m.pagado
from estudiante e
inner join matricula m
    on concat(e.nombre_estudiante, ' ', e.apellido1_estudiante) = m.nombre_estudiante;

-- 21. LEFT JOIN
-- Muestra todos los cursos y, si existe coincidencia, el profesor que imparte ese curso.
-- Si un curso no tiene profesor asignado, igualmente aparecerá en el resultado con valores NULL.
--
-- Displays all courses and, if there is a match, the professor who teaches that course.
-- If a course has no assigned professor, it will still appear with NULL values.
select
    c.nombre_curso,
    c.modalidad,
    p.nombre_profesor,
    p.apellido1_profesor
from curso c
left join profesores p
    on c.nombre_curso = p.materia;

-- 22. RIGHT JOIN
-- Muestra todas las facultades y, si existe coincidencia, las aulas ubicadas en el mismo edificio.
-- Displays all faculties and, if there is a match, the classrooms located in the same building.
select
    f.nombre as facultad,
    f.edificio,
    a.numero_aula,
    a.capacidad
from aula a
right join facultad f
    on a.edificio_aula = f.edificio;