USE db_universidad;
GO


-- Vista de modalidades con más de cinco cursos
-- Muestra las modalidades que tienen más de cinco cursos
-- Displays delivery modes with more than five courses
CREATE VIEW vista_modalidades_cursos
AS
SELECT
    modalidad,
    COUNT(*) AS cantidad_cursos
FROM curso
GROUP BY modalidad
HAVING COUNT(*) > 5;
GO

-- Vista de capacidad de aulas
-- Muestra las aulas con capacidad mayor a 40
-- Displays classrooms with capacity greater than 40
CREATE VIEW vista_aulas_grandes
AS
SELECT
    id_aula,
    numero_aula,
    edificio_aula,
    capacidad
FROM aula
WHERE capacidad > 40;
GO

-- Vista de matrículas pagadas o con costo mayor a 200000
-- Muestra las matrículas pagadas o con costo mayor a 200000
-- Displays paid enrollments or enrollments with a cost greater than 200000
CREATE VIEW vista_matriculas
AS
SELECT
    id_matricula,
    nombre_estudiante,
    curso,
    costo,
    pagado
FROM matricula
WHERE curso IS NOT NULL
AND (pagado = 1 OR costo > 200000);
GO

-- Vista de cursos matriculados
-- Relaciona los cursos con las matrículas realizadas.
-- Matches courses with enrollments.

CREATE VIEW vista_cursos_matriculados
AS
SELECT
    c.id_curso,
    c.nombre_curso,
    c.creditos,
    c.modalidad,
    m.nombre_estudiante,
    m.fecha_matricula,
    m.costo
FROM curso AS c
INNER JOIN matricula AS m
ON c.nombre_curso = m.curso;
GO


-- Consulta la vista de modalidades de cursos
-- Queries the course modalities view
SELECT *
FROM vista_modalidades_cursos;

-- Consulta la vista de aulas grandes
-- Queries the large classrooms view
SELECT *
FROM vista_aulas_grandes;

-- Consulta la vista de matrículas y ordena el costo de mayor a menor
-- Queries the enrollments view and sorts the cost from highest to lowest
SELECT *
FROM vista_matriculas
ORDER BY costo DESC;

-- Consulta la vista de cursos matriculados y ordena por modalidad
-- Queries the enrolled courses view and sorts by delivery mode
SELECT *
FROM vista_cursos_matriculados
ORDER BY modalidad ASC;