-- Usa la base de datos / Uses the database
use db_universidad;
go

-- Inserta un nuevo registro en la tabla estudiante / Inserts a new record into the student table
insert into estudiante (
    tipo_ident_est,              -- Tipo de identificación / Identification type (ID card, Passport, etc.)
    ident_estudiante,            -- Número de identificación / Student identification number
    nombre_estudiante,           -- Nombre del estudiante / Student first name
    apellido1_estudiante,        -- Primer apellido / First last name
    apellido2_estudiante,        -- Segundo apellido / Second last name
    fecha_naci_est,              -- Fecha de nacimiento / Date of birth
    genero,                      -- Género (M/F) / Gender (M/F)
    telefono_estudiante,         -- Número de teléfono / Phone number
    email_estudiante,            -- Correo electrónico / Email address
    promedio,                    -- Promedio académico / Grade point average (GPA)
    activo_estudiante            -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
)
values
('Cedula','301010101','Juan','Perez','Lopez','2003-01-15','M','88881111','juan1@gmail.com',85.5,1),
('Cedula','102350102','Maria','Rodriguez','Soto','2002-03-21','F','65897412','maria2@gmail.com',90.2,1),
('Pasaporte','C45678901','Carlos','Ramirez','Vega','2001-05-18','M','88881113','carlos3@gmail.com',78.9,1),
('Cedula','309540104','Ana','Jimenez','Mora','2004-07-11','F','75844556','ana4@gmail.com',88.0,1),
('Cedula','601120905','Luis','Fernandez','Rojas','2003-09-30','M','88562541','luis5@gmail.com',72.4,0),
('Cedula','101010106','Laura','Castro','Perez','2002-11-12','F','88881116','laura6@gmail.com',95.8,1),
('Pasaporte','P1002457','Jose','Hernandez','Diaz','2000-12-05','M','74589632','jose7@gmail.com',81.3,1),
('Cedula','501010587','Sofia','Alvarado','Ruiz','2003-06-19','F','89541236','sofia8@gmail.com',89.7,1),
('Cedula','101010109','Miguel','Vargas','Mendez','2004-02-10','M','88881119','miguel9@gmail.com',76.2,0),
('Cedula','508950110','Valeria','Araya','Solis','2001-04-22','F','65897415','valeria10@gmail.com',91.4,1),
('Cedula','801330111','Andres','Chaves','Campos','2002-08-17','M','88881121','andres11@gmail.com',84.6,1),
('Cedula','101010652','Daniela','Quesada','Cordero','2003-10-03','F','82564179','daniela12@gmail.com',87.8,1),
('Pasaporte','B98765432','Kevin','Navarro','Rojas','2000-01-28','M','88881123','kevin13@gmail.com',68.5,0),
('Cedula','507890114','Paula','Salas','Mora','2002-02-15','F','77552387','paula14@gmail.com',94.0,1),
('Cedula','706512354','Diego','Arias','Lopez','2001-03-08','M','88881125','diego15@gmail.com',79.3,1),
('Cedula','301010116','Natalia','Monge','Vega','2004-05-09','F','85263147','natalia16@gmail.com',92.6,1),
('Cedula','501890287','Jorge','Rojas','Perez','2003-06-25','M','88881127','jorge17@gmail.com',74.1,1),
('Pasaporte','P1256004','Camila','Mora','Castro','2002-07-14','F','88881128','camila18@gmail.com',88.4,1),
('Cedula','101010119','Ricardo','Solis','Diaz','2001-08-18','M','63258974','ricardo19@gmail.com',82.0,0),
('Cedula','201010120','Gabriela','Acosta','Jimenez','2004-09-27','F','65230145','gabriela20@gmail.com',97.5,1),
('Cedula','105740121','Fernando','Ureña','Campos','2000-10-06','M','88881131','fernando21@gmail.com',69.9,1),
('Cedula','401010199','Melissa','Porras','Vargas','2003-12-11','F','85263145','melissa22@gmail.com',86.8,1),
('Pasaporte','A12345678','Esteban','Bonilla','Rojas','2002-01-13','M','84123659','esteban23@gmail.com',80.5,1),
('Cedula','101010124','Andrea','Villalobos','Mendez','2004-02-20','F','74123698','andrea24@gmail.com',93.2,1),
('Cedula','101010874','Oscar','Segura','Lopez','2001-04-16','M','88881135','oscar25@gmail.com',77.6,0),
('Cedula','102140126','Monica','Guillen','Ruiz','2002-06-08','F','82541000','monica26@gmail.com',89.9,1),
('Cedula','202540178','Pablo','Leiva','Soto','2003-07-02','M','88881137','pablo27@gmail.com',71.8,1),
('Pasaporte','P1204006','Karen','Madrigal','Perez','2000-08-23','F','62310457','karen28@gmail.com',90.7,1),
('Cedula','501010129','Adrian','Molina','Chaves','2004-09-05','M','88881139','adrian29@gmail.com',83.6,1),
('Cedula','104120145','Daniel','Calvo','Rojas','2002-10-29','M','87410235','daniel30@gmail.com',75.0,0);


-- Inserta un nuevo registro en la tabla profesores / Inserts a new record into the professors table
insert into profesores (
    tipo_ident_prof,             -- Tipo de identificación / Identification type (ID card, Passport, etc.)
    ident_profesor,              -- Número de identificación / Professor identification number
    nombre_profesor,             -- Nombre del profesor / Professor first name
    apellido1_profesor,          -- Primer apellido / First last name
    apellido2_profesor,          -- Segundo apellido / Second last name
    fecha_naci_prof,             -- Fecha de nacimiento / Date of birth
    telefono_profesor,           -- Número de teléfono / Phone number
    email_profesor,              -- Correo electrónico / Email address
    materia,                     -- Materia que imparte / Subject taught
    salario,                     -- Salario del profesor / Professor salary
    genero,                      -- Género (M/F) / Gender (M/F)
    fecha_ingreso,               -- Fecha de ingreso / Hiring date
    activo_profesor              -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
)
values
('Cedula','508810101','Carlos','Ramirez','Lopez','1980-01-15','74102354','carlos@gmail.com','Matematicas',900.00,'M','2015-02-01',1),
('Cedula','201810104','Maria','Perez','Soto','1982-03-20','88882002','maria@gmail.com','Español',700.00,'F','2016-03-10',1),
('Pasaporte','A12345678','John','Smith','Brown','1978-05-18','88882003','john@gmail.com','Ingles',980.00,'M','2014-01-15',1),
('Cedula','801010104','Ana','Jimenez','Mora','1985-07-22','88882004','ana@gmail.com','Historia',500.25,'F','2018-04-20',1),
('Cedula','101710205','Luis','Fernandez','Rojas','1979-09-11','88882005','luis@gmail.com','Fisica',900.00,'M','2013-08-01',1),
('Cedula','201010106','Laura','Castro','Perez','1988-10-30','88882006','laura@gmail.com','Quimica',855.00,'F','2019-02-11',1),
('Pasaporte','B98765432','Michael','Johnson','White','1981-12-05','88882007','michael@gmail.com','Biologia',600.00,'M','2017-06-05',1),
('Cedula','601010108','Sofia','Alvarado','Ruiz','1984-04-18','88882008','sofia@gmail.com','Arte',400.00,'F','2020-01-15',1),
('Cedula','209870128','Miguel','Vargas','Mendez','1977-06-27','88882009','miguel@gmail.com','Musica',450.00,'M','2012-11-01',1),
('Cedula','401010110','Valeria','Araya','Solis','1986-08-13','62147841','valeria@gmail.com','Computacion',990.00,'F','2021-03-08',1),
('Cedula','301010151','Andres','Chaves','Campos','1983-02-14','88882011','andres@gmail.com','Programacion',985.00,'M','2016-05-09',0),
('Cedula','201440112','Daniela','Quesada','Cordero','1989-11-09','78521456','daniela@gmail.com','Base de Datos',950.90,'F','2022-02-14',1),
('Pasaporte','C45678901','Emily','Taylor','Green','1987-01-19','88882013','emily@gmail.com','Ingles',800.75,'F','2018-07-01',1),
('Cedula','401010114','Paula','Salas','Mora','1990-05-16','65210141','paula@gmail.com','Contabilidad',755.10,'F','2023-01-10',1),
('Cedula','601410117','Diego','Arias','Lopez','1981-03-28','74568712','diego@gmail.com','Administracion',658.35,'M','2015-09-20',1),
('Cedula','201250111','Natalia','Monge','Vega','1984-06-21','88882016','natalia@gmail.com','Derecho',877.80,'F','2017-10-15',1),
('Cedula','107410178','Jorge','Rojas','Perez','1976-07-30','87410236','jorge@gmail.com','Economia',895.00,'M','2011-04-11',1),
('Cedula','108960247','Camila','Mora','Castro','1991-08-17','88882018','camila@gmail.com','Mercadeo',665.65,'F','2024-02-03',1),
('Cedula','501010119','Ricardo','Solis','Diaz','1982-10-12','88882019','ricardo@gmail.com','Estadistica',765.90,'M','2016-08-18',0),
('Cedula','205110741','Gabriela','Acosta','Jimenez','1988-12-02','65100021','gabriela@gmail.com','Psicologia',568.25,'F','2019-11-25',1);

-- Inserta un nuevo registro en la tabla curso / Inserts a new record into the course table
insert into curso (
    nombre_curso,    -- Nombre del curso / Course name
    creditos,        -- Cantidad de créditos / Number of credits
    duracion,        -- Duración del curso / Course duration
    modalidad,       -- Modalidad (Presencial, Virtual o Híbrido) / Delivery mode (In-person, Virtual, or Hybrid)
    estado           -- Estado (1=Activo, 0=Inactivo) / Status (1=Active, 0=Inactive)
)
values
('Matematicas I',4,4,'Presencial',1),
('Matematicas II',4,4,'Presencial',1),
('Programacion I',5,5,'Virtual',1),
('Programacion II',5,5,'Virtual',1),
('Base de Datos',4,4.5,'Hibrido',1),
('Redes',4,4,'Presencial',1),
('Sistemas Operativos',4,4.5,'Virtual',1),
('Ingenieria de Software',5,5,'Hibrido',1),
('Seguridad Informatica',4,4,'Virtual',1),
('Desarrollo Web',5,5,'Hibrido',1),
('Fisica General',4,4,'Presencial',1),
('Quimica General',4,4,'Presencial',1),
('Biologia',3,3.5,'Virtual',1),
('Historia Universal',3,3,'Presencial',1),
('Español',3,3,'Virtual',1),
('Ingles I',3,3,'Hibrido',1),
('Ingles II',3,3,'Hibrido',1),
('Contabilidad',4,4,'Presencial',1),
('Administracion',4,4,'Virtual',1),
('Economia',2,4,'Hibrido',1),
('Mercadeo',3,3.5,'Presencial',1),
('Estadistica',4,4.5,'Virtual',1),
('Calculo I',5,5,'Presencial',1),
('Calculo II',5,5,'Presencial',1),
('Algebra Lineal',4,4,'Virtual',1),
('Inteligencia Artificial',5,5.5,'Hibrido',1),
('Analisis de Datos',4,4.5,'Virtual',1),
('Computacion en la Nube',4,4,'Hibrido',1),
('Arquitectura de Computadoras',4,4,'Presencial',1),
('Etica Profesional',2,4,'Virtual',1);

-- Inserta un nuevo registro en la tabla facultad / Inserts a new record into the faculty table
insert into facultad (
    nombre,       -- Nombre de la facultad / Faculty name
    encargado,    -- Nombre del encargado / Person in charge
    edificio,     -- Edificio donde se ubica / Building location
    telefono,     -- Número de teléfono / Contact phone number
    activo        -- Estado (1=Activa, 0=Inactiva) / Status (1=Active, 0=Inactive)
)
values
('Arquitectura','Andrea Mora','Bloque A','87456123',1),
('Odontologia','Mario Salazar','Torre Norte','63217845',1),
('Enfermeria','Patricia Rojas','Pabellon 1','89124567',1),
('Medicina','Roberto Jimenez','Modulo A','74563218',1),
('Psicologia','Diana Castro','Edificio Central','85673412',1),
('Turismo','Fernando Vargas','Bloque B','67891234',1),
('Idiomas','Viviana Solis','Torre Sur','88234561',1),
('Trabajo Social','Oscar Mendez','Pabellon 2','72341895',1),
('Ciencias Politicas','Paola Herrera','Modulo B','86542137',1),
('Diseño Grafico','Mauricio Araya','Anexo C','69457821',1),
('Veterinaria','Alejandro Ruiz','Campus Norte','81234567',1),
('Farmacia','Silvia Campos','Campus Sur','65437891',1),
('Ingenieria Civil','Ernesto Vega','Bloque C','89765432',1),
('Ingenieria Industrial','Karen Jimenez','Bloque D','72345618',1),
('Ingenieria Electrica','Hector Solis','Torre Este','84561237',1),
('Ingenieria Mecanica','Melissa Rojas','Torre Oeste','67894512',1),
('Comunicacion','David Murillo','Pabellon 3','88971234',1),
('Relaciones Internacionales','Paola Vargas','Pabellon 4','73456128',1),
('Ciencias Ambientales','Luis Arce','Edificio Omega','85612349',1),
('Nutricion','Carolina Salazar','Centro Academico','69234781',1);

-- Inserta un nuevo registro en la tabla aula / Inserts a new record into the classroom table
insert into aula (
    numero_aula,     -- Número o código del aula / Classroom number or code
    edificio_aula,   -- Edificio donde se encuentra / Building where the classroom is located
    capacidad        -- Capacidad máxima de estudiantes / Maximum student capacity
)
values
('A-101','Bloque A',30),
('A-102','Bloque A',35),
('A-201','Bloque A',40),
('A-202','Bloque A',45),
('B-101','Bloque B',25),
('B-102','Bloque B',30),
('B-201','Bloque B',40),
('B-202','Bloque B',50),
('C-101','Bloque C',35),
('C-102','Bloque C',40),
('C-201','Bloque C',45),
('D-101','Bloque D',30),
('D-201','Bloque D',20),
('TN-101','Torre Norte',40),
('TN-201','Torre Norte',55),
('TS-101','Torre Sur',35),
('P1-101','Pabellon 1',40),
('P2-201','Pabellon 2',45),
('M-A01','Modulo A',25),
('M-B01','Modulo B',30),
('EC-101','Edificio Central',40),
('CA-201','Centro Academico',55),
('AN-101','Anexo Norte',50),
('AS-102','Anexo Sur',45),
('LAB-01','Laboratorio 1',35),
('LAB-02','Laboratorio 2',40),
('AUD-01','Auditorio',200),
('S-101','Sector Este',30),
('S-201','Sector Oeste',35),
('V-101','Villa Academica',40);

-- Inserta un nuevo registro en la tabla matrícula / Inserts a new record into the enrollment table
insert into matricula (
    nombre_estudiante,   -- Nombre del estudiante matriculado / Enrolled student name
    curso,               -- Nombre del curso matriculado / Enrolled course name
    fecha_matricula,     -- Fecha de la matrícula / Enrollment date
    costo,               -- Costo de la matrícula / Enrollment cost
    pagado               -- Estado del pago (1=Pagado, 0=Pendiente) / Payment status (1=Paid, 0=Pending)
)
values
('Juan Perez','Matematicas I','2026-01-10',185000,1),
('Maria Rodriguez','Programacion I','2026-01-11',210000,1),
('Carlos Ramirez','Base de Datos','2026-01-12',225000,0),
('Ana Jimenez','Fisica General','2026-01-12',180000,1),
('Luis Fernandez','Quimica General','2026-01-13',190000,1),
('Laura Castro','Ingles I','2026-01-14',150000,0),
('Jose Hernandez','Estadistica','2026-01-15',205000,1),
('Sofia Alvarado','Calculo I','2026-01-16',230000,1),
('Miguel Vargas','Redes','2026-01-17',215000,0),
('Valeria Araya','Ingenieria de Software','2026-01-18',250000,1),
('Andres Chaves','Administracion','2026-01-19',175000,1),
('Daniela Quesada','Economia','2026-01-20',180000,0),
('Kevin Navarro','Historia Universal','2026-01-21',160000,1),
('Paula Salas','Biologia','2026-01-22',170000,1),
('Diego Arias','Desarrollo Web','2026-01-23',245000,0),
('Natalia Monge','Programacion II','2026-01-24',220000,1),
('Jorge Rojas','Contabilidad','2026-01-25',200000,1),
('Camila Mora','Mercadeo','2026-01-26',195000,0),
('Ricardo Solis','Calculo II','2026-01-27',235000,1),
('Gabriela Acosta','Algebra Lineal','2026-01-28',210000,1),
('Fernando Ureña','Inteligencia Artificial','2026-01-29',280000,0),
('Melissa Porras','Analisis de Datos','2026-01-30',260000,1),
('Esteban Bonilla','Computacion en la Nube','2026-02-01',255000,1),
('Andrea Villalobos','Arquitectura de Computadoras','2026-02-02',240000,0),
('Oscar Segura','Etica Profesional','2026-02-03',140000,1),
('Monica Guillen','Español','2026-02-04',150000,1),
('Pablo Leiva','Ingles II','2026-02-05',155000,0),
('Karen Madrigal','Seguridad Informatica','2026-02-06',235000,1),
('Adrian Molina','Sistemas Operativos','2026-02-07',225000,1),
('Daniel Calvo','Matematicas II','2026-02-08',190000,0),
('Isabel Rivas','Programacion I','2026-02-09',220000,1),
('Brayan Campos','Matematicas I','2026-02-10',185000,0),
('Tatiana Aguilar','Base de Datos','2026-02-11',225000,1),
('Cristian Herrera','Redes','2026-02-12',210000,1),
('Lucia Fuentes','Ingenieria de Software','2026-02-13',250000,0),
('Marco Mendez','Quimica General','2026-02-14',190000,1),
('Elena Murillo','Biologia','2026-02-15',175000,1),
('Samuel Rojas','Calculo I','2026-02-16',235000,0),
('Carolina Zamora','Contabilidad','2026-02-17',200000,1),
('Alberto Vega','Administracion','2026-02-18',180000,1),
('Nicole Chacon','Mercadeo','2026-02-19',195000,1),
('Sebastian Mora','Estadistica','2026-02-20',205000,0),
('Juliana Solis','Ingles II','2026-02-21',160000,1),
('Fabricio Ruiz','Computacion en la Nube','2026-02-22',255000,1),
('Cindy Araya','Analisis de Datos','2026-02-23',260000,0),
('Bryan Villalobos','Arquitectura de Computadoras','2026-02-24',245000,1),
('Viviana Salazar','Seguridad Informatica','2026-02-25',230000,1),
('Mauricio Herrera','Fisica General','2026-02-26',180000,0),
('Katherine Castro','Programacion II','2026-02-27',220000,1),
('Kevin Rojas','Inteligencia Artificial','2026-02-28',280000,1);