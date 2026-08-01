-- Crea la base de datos / Creates the database
CREATE DATABASE db_universidad;
GO

-- Usa la base de datos / Uses the database
USE db_universidad;
GO

-- Tabla estudiante / Student table
CREATE TABLE estudiante (
    id_estudiante INT IDENTITY(1,1) PRIMARY KEY,      -- Identificador único del estudiante / Unique student identifier
    tipo_ident_est CHAR(30) NOT NULL,                 -- Tipo de identificación / Identification type
    ident_estudiante CHAR(30) NOT NULL,               -- Número de identificación / Identification number
    nombre_estudiante VARCHAR(20) NOT NULL,           -- Nombre del estudiante / Student first name
    apellido1_estudiante VARCHAR(20) NOT NULL,        -- Primer apellido / First last name
    apellido2_estudiante VARCHAR(20) NOT NULL,        -- Segundo apellido / Second last name
    fecha_naci_est DATE NOT NULL,                     -- Fecha de nacimiento / Date of birth
    genero VARCHAR(1) NOT NULL,                       -- Género (M/F) / Gender (M/F)
    telefono_estudiante VARCHAR(8) NOT NULL,          -- Teléfono / Phone number
    email_estudiante CHAR(30) NOT NULL,               -- Correo electrónico / Email address
    promedio FLOAT NOT NULL,                          -- Promedio académico / Grade point average
    activo_estudiante BIT NOT NULL                    -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
);

-- Tabla profesores / Professors table
CREATE TABLE profesores (
    id_profesor INT IDENTITY(1,1) PRIMARY KEY,        -- Identificador único / Unique professor identifier
    tipo_ident_prof CHAR(30) NOT NULL,                -- Tipo de identificación / Identification type
    ident_profesor CHAR(30) NOT NULL,                 -- Número de identificación / Identification number
    nombre_profesor CHAR(20) NOT NULL,                -- Nombre / First name
    apellido1_profesor CHAR(20) NOT NULL,             -- Primer apellido / First last name
    apellido2_profesor CHAR(20) NOT NULL,             -- Segundo apellido / Second last name
    fecha_naci_prof DATE NOT NULL,                    -- Fecha de nacimiento / Date of birth
    telefono_profesor VARCHAR(8) NOT NULL,            -- Teléfono / Phone number
    email_profesor CHAR(30) NOT NULL,                 -- Correo electrónico / Email address
    materia CHAR(30) NOT NULL,                        -- Materia que imparte / Subject taught
    salario FLOAT NOT NULL,                           -- Salario / Salary
    genero VARCHAR(1) NOT NULL,                       -- Género (M/F) / Gender (M/F)
    fecha_ingreso DATE NOT NULL,                      -- Fecha de ingreso / Hiring date
    activo_profesor BIT NOT NULL                      -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
);

-- Tabla curso / Course table
CREATE TABLE curso (
    id_curso INT IDENTITY(1,1) PRIMARY KEY,           -- Identificador único / Unique course identifier
    nombre_curso CHAR(50) NOT NULL,                   -- Nombre del curso / Course name
    creditos INT NOT NULL,                            -- Créditos / Credits
    duracion FLOAT NOT NULL,                          -- Duración / Duration
    modalidad CHAR(15) NOT NULL,                      -- Modalidad / Delivery mode
    estado BIT NOT NULL                               -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
);

-- Tabla facultad / Faculty table
CREATE TABLE facultad (
    id_facultad INT IDENTITY(1,1) PRIMARY KEY,        -- Identificador único / Unique faculty identifier
    nombre CHAR(40) NOT NULL,                         -- Nombre de la facultad / Faculty name
    encargado CHAR(40) NOT NULL,                      -- Encargado / Person in charge
    edificio CHAR(20) NOT NULL,                       -- Edificio / Building
    telefono CHAR(8) NOT NULL,                        -- Teléfono / Phone number
    activo BIT NOT NULL                               -- Estado (1=Activa, 0=Inactiva) / Status (1=Active, 0=Inactive)
);

-- Tabla aula / Classroom table
CREATE TABLE aula (
    id_aula INT IDENTITY(1,1) PRIMARY KEY,            -- Identificador único / Unique classroom identifier
    numero_aula CHAR(10) NOT NULL,                    -- Número del aula / Classroom number
    edificio_aula CHAR(20) NOT NULL,                  -- Edificio / Building
    capacidad INT NOT NULL                            -- Capacidad máxima / Maximum capacity
);

-- Tabla matrícula / Enrollment table
CREATE TABLE matricula (
    id_matricula INT IDENTITY(1,1) PRIMARY KEY,       -- Identificador único / Unique enrollment identifier
    nombre_estudiante VARCHAR(40) NOT NULL,           -- Nombre del estudiante / Student name
    curso CHAR(40) NOT NULL,                          -- Curso matriculado / Enrolled course
    fecha_matricula DATE NOT NULL,                    -- Fecha de matrícula / Enrollment date
    costo FLOAT NOT NULL,                             -- Costo / Cost
    pagado BIT NOT NULL                               -- Estado del pago (1=Pagado, 0=Pendiente) / Payment status (1=Paid, 0=Pending)
);