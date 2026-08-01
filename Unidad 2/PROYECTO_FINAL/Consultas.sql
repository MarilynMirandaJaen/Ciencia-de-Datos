USE db_universidad;
GO

-- 1. SELECT
-- Muestra todos los estudiantes
-- Displays all students
SELECT *
FROM estudiante;

-- 2. WHERE
-- Muestra los profesores activos
-- Displays active professors
SELECT *
FROM profesores
WHERE activo_profesor = 1;

-- 3. ORDER BY
-- Ordena los cursos por cantidad de créditos
-- Sorts courses by number of credits
SELECT
    nombre_curso,
    creditos,
    modalidad
FROM curso
ORDER BY creditos DESC;

-- 4. DISTINCT
-- Muestra los edificios de las facultades sin repetir
-- Displays faculty buildings without duplicates
SELECT DISTINCT edificio
FROM facultad;

-- 5. LIKE
-- Busca aulas cuyo número comienza con A
-- Searches for classrooms whose number starts with A
SELECT *
FROM aula
WHERE numero_aula LIKE 'A%';

-- 6. BETWEEN
-- Muestra matrículas con costo entre 180000 y 230000
-- Displays enrollments costing between 180000 and 230000
SELECT
    nombre_estudiante,
    curso,
    costo
FROM matricula
WHERE costo BETWEEN 180000 AND 230000;

-- 7. IN
-- Muestra cursos virtuales o híbridos
-- Displays virtual or hybrid courses
SELECT *
FROM curso
WHERE modalidad IN ('Virtual', 'Hibrido');

-- 8. NOT
-- Muestra estudiantes que no están activos
-- Displays students who are not active
SELECT *
FROM estudiante
WHERE NOT activo_estudiante = 1;

-- 9. IS NULL
-- Muestra profesores que no tienen correo registrado
-- Displays professors without a registered email
SELECT *
FROM profesores
WHERE email_profesor IS NULL;

-- 10. IS NOT NULL
-- Muestra facultades que tienen teléfono registrado
-- Displays faculties with a registered phone number
SELECT *
FROM facultad
WHERE telefono IS NOT NULL;

-- 11. AND
-- Muestra aulas con capacidad mayor a 35 en Bloque A
-- Displays classrooms with capacity greater than 35 in Block A
SELECT *
FROM aula
WHERE edificio_aula = 'Bloque A'
  AND capacidad > 35;

-- 12. OR
-- Muestra matrículas pagadas o con costo menor a 180000
-- Displays paid enrollments or enrollments costing less than 180000
SELECT *
FROM matricula
WHERE pagado = 1
   OR costo < 180000;

-- 13. GROUP BY
-- Agrupa los estudiantes por género
-- Groups students by gender
SELECT
    genero,
    COUNT(*) AS cantidad_estudiantes
FROM estudiante
GROUP BY genero;

-- 14. HAVING
-- Muestra modalidades que tienen más de cinco cursos
-- Displays delivery modes with more than five courses
SELECT
    modalidad,
    COUNT(*) AS cantidad_cursos
FROM curso
GROUP BY modalidad
HAVING COUNT(*) > 5;

-- 15. COUNT
-- Cuenta la cantidad total de profesores
-- Counts the total number of professors
SELECT COUNT(*) AS total_profesores
FROM profesores;

-- 16. SUM
-- Suma el costo de todas las matrículas
-- Adds the cost of all enrollments
SELECT SUM(costo) AS costo_total_matriculas
FROM matricula;

-- 17. AVG
-- Calcula la capacidad promedio de las aulas
-- Calculates the average classroom capacity
SELECT AVG(capacidad) AS capacidad_promedio
FROM aula;

-- 18. MIN
-- Muestra el promedio académico más bajo
-- Displays the lowest academic average
SELECT MIN(promedio) AS promedio_minimo
FROM estudiante;

-- 19. MAX
-- Muestra el salario más alto de los profesores
-- Displays the highest professor salary
SELECT MAX(salario) AS salario_maximo
FROM profesores;

-- 20. INNER JOIN
-- Relaciona estudiantes con sus matrículas
-- Matches students with their enrollments
SELECT
    e.id_estudiante,
    e.nombre_estudiante,
    e.apellido1_estudiante,
    m.curso,
    m.fecha_matricula,
    m.costo,
    m.pagado
FROM estudiante e
INNER JOIN matricula m
ON CONCAT(e.nombre_estudiante, ' ', e.apellido1_estudiante) = m.nombre_estudiante;


-- 21. LEFT JOIN
-- Muestra todos los cursos y, si existe coincidencia,el profesor que imparte ese curso.
-- Si un curso no tiene profesor asignado, igualmente aparecerá en el resultado con valores NULL.
--
-- Displays all courses and, if there is a match, the professor who teaches that course.
-- If a course has no assigned professor, it will still appear with NULL values.

SELECT
    c.nombre_curso,
    c.modalidad,
    p.nombre_profesor,
    p.apellido1_profesor
FROM curso c
LEFT JOIN profesores p
ON c.nombre_curso = p.materia;

-- 22. RIGHT JOIN
-- Muestra todas las facultades y, si existe coincidencia,las aulas ubicadas en el mismo edificio.
-- Displays all faculties and, if there is a match, the classrooms located in the same building.

SELECT
    f.nombre AS facultad,
    f.edificio,
    a.numero_aula,
    a.capacidad
FROM aula a
RIGHT JOIN facultad f
ON a.edificio_aula = f.edificio;