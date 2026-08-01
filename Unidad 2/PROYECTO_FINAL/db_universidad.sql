-- Crea la base de datos / Creates the database
create database db_universidad;
go

-- Usa la base de datos / Uses the database
use db_universidad;
go

-- Tabla estudiante / Student table
create table estudiante (
    id_estudiante int identity(1,1) primary key,      -- Identificador único del estudiante / Unique student identifier
    tipo_ident_est char(30) not null,                 -- Tipo de identificación / Identification type
    ident_estudiante char(30) not null,               -- Número de identificación / Identification number
    nombre_estudiante varchar(20) not null,           -- Nombre del estudiante / Student first name
    apellido1_estudiante varchar(20) not null,        -- Primer apellido / First last name
    apellido2_estudiante varchar(20) not null,        -- Segundo apellido / Second last name
    fecha_naci_est date not null,                     -- Fecha de nacimiento / Date of birth
    genero varchar(1) not null,                       -- Género (M/F) / Gender (M/F)
    telefono_estudiante varchar(8) not null,          -- Teléfono / Phone number
    email_estudiante char(30) not null,               -- Correo electrónico / Email address
    promedio float not null,                          -- Promedio académico / Grade point average
    activo_estudiante bit not null                    -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
);

-- Tabla profesores / Professors table
create table profesores (
    id_profesor int identity(1,1) primary key,        -- Identificador único / Unique professor identifier
    tipo_ident_prof char(30) not null,                -- Tipo de identificación / Identification type
    ident_profesor char(30) not null,                 -- Número de identificación / Identification number
    nombre_profesor char(20) not null,                -- Nombre / First name
    apellido1_profesor char(20) not null,             -- Primer apellido / First last name
    apellido2_profesor char(20) not null,             -- Segundo apellido / Second last name
    fecha_naci_prof date not null,                    -- Fecha de nacimiento / Date of birth
    telefono_profesor varchar(8) not null,            -- Teléfono / Phone number
    email_profesor char(30) not null,                 -- Correo electrónico / Email address
    materia char(30) not null,                        -- Materia que imparte / Subject taught
    salario float not null,                           -- Salario / Salary
    genero varchar(1) not null,                       -- Género (M/F) / Gender (M/F)
    fecha_ingreso date not null,                      -- Fecha de ingreso / Hiring date
    activo_profesor bit not null                      -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
);

-- Tabla curso / Course table
create table curso (
    id_curso int identity(1,1) primary key,           -- Identificador único / Unique course identifier
    nombre_curso char(50) not null,                   -- Nombre del curso / Course name
    creditos int not null,                            -- Créditos / Credits
    duracion float not null,                          -- Duración / Duration
    modalidad char(15) not null,                      -- Modalidad / Delivery mode
    estado bit not null                               -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
);

-- Tabla facultad / Faculty table
create table facultad (
    id_facultad int identity(1,1) primary key,        -- Identificador único / Unique faculty identifier
    nombre char(40) not null,                         -- Nombre de la facultad / Faculty name
    encargado char(40) not null,                      -- Encargado / Person in charge
    edificio char(20) not null,                       -- Edificio / Building
    telefono char(8) not null,                        -- Teléfono / Phone number
    activo bit not null                               -- Estado (1=Activa, 0=Inactiva) / Status (1=Active, 0=Inactive)
);

-- Tabla aula / Classroom table
create table aula (
    id_aula int identity(1,1) primary key,            -- Identificador único / Unique classroom identifier
    numero_aula char(10) not null,                    -- Número del aula / Classroom number
    edificio_aula char(20) not null,                  -- Edificio / Building
    capacidad int not null                            -- Capacidad máxima / Maximum capacity
);

-- Tabla matrícula / Enrollment table
create table matricula (
    id_matricula int identity(1,1) primary key,       -- Identificador único / Unique enrollment identifier
    nombre_estudiante varchar(40) not null,           -- Nombre del estudiante / Student name
    curso char(40) not null,                          -- Curso matriculado / Enrolled course
    fecha_matricula date not null,                    -- Fecha de matrícula / Enrollment date
    costo float not null,                             -- Costo / Cost
    pagado bit not null                               -- Estado del pago (1=Pagado, 0=Pendiente) / Payment status (1=Paid, 0=Pending)
);