-- Database: ejercicio19_1

-- DROP DATABASE IF EXISTS ejercicio19_1;

CREATE TABLE Lugares (
    id SERIAL PRIMARY KEY,
    direccion VARCHAR(200),
    ciudad VARCHAR(100),
    codigo_postal VARCHAR(10)
);


INSERT INTO Lugares (direccion, ciudad, codigo_postal)
VALUES ('Calle Principal 123', 'Ciudad A', '12345');

INSERT INTO Lugares (direccion, ciudad, codigo_postal)
VALUES ('Avenida Central 456', 'Ciudad B', '67890');

CREATE TABLE Personal (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    cargo VARCHAR(100)
);

INSERT INTO Personal (nombre, cargo)
VALUES ('Juan Pérez', 'Técnico de Reparaciones');

INSERT INTO Personal (nombre, cargo)
VALUES ('María López', 'Encargada de Proyectos');

CREATE TABLE Trabajos (
    id SERIAL PRIMARY KEY,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    fk_id_lugar INT,
    fk_id_personal INT,
    realizado BOOLEAN,
    FOREIGN KEY(fk_id_lugar) REFERENCES Lugares(id),
    FOREIGN KEY(fk_id_personal) REFERENCES Personal(id)
);
DROP TABLE Trabajos;

CREATE TABLE Trabajos (
    id SERIAL PRIMARY KEY,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    fk_id_lugar INT,
    fk_id_personal INT,
    realizado BOOLEAN,
    FOREIGN KEY(fk_id_lugar) REFERENCES Lugares(id),
    FOREIGN KEY(fk_id_personal) REFERENCES Personal(id)
);

INSERT INTO Trabajos (descripcion, fecha_inicio, fecha_fin, fk_id_lugar, fk_id_responsable)
VALUES ('Reparación de fachada', '2024-03-15', '2024-03-30', 1, 1);

INSERT INTO Trabajos (descripcion, fecha_inicio, fecha_fin, fk_id_lugar, fk_id_responsable)
VALUES ('Reemplazo de ventanas', '2024-04-01', '2024-04-10', 2, 2);

CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100)
);

INSERT INTO Clientes (nombre, telefono, email)
VALUES ('Empresa XYZ', '123-456-7890', 'info@empresaxyz.com');

INSERT INTO Clientes (nombre, telefono, email)
VALUES ('Edificio ABC', '987-654-3210', 'contacto@edificioabc.com');

CREATE TABLE Materiales (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio_unitario NUMERIC(10, 2)
);

INSERT INTO Materiales (nombre, descripcion, precio_unitario)
VALUES ('Pintura blanca', 'Pintura de exterior para fachadas', 50.00);

INSERT INTO Materiales (nombre, descripcion, precio_unitario)
VALUES ('Cristales dobles', 'Ventanas de doble acristalamiento', 100.00);

SELECT * FROM Lugares;
SELECT * FROM Personal;
SELECT * FROM Clientes;
SELECT * FROM Materiales;
SELECT * FROM Trabajos;

---- 2. Crea una nueva tabla CitasEvaluacion que sirva para 
-- registrar la primera cita de evaluación de un trabajo para presupuestarlo 
-- debe figurar el lugar, el cliente, el personal, la fecha y el presupuesto al menos

CREATE Table CitasEvaluacion (
	 id SERIAL PRIMARY KEY,
	 fk_id_lugar INT,
	 FOREIGN KEY(fk_id_lugar) REFERENCES Lugares(id),
	 fk_id_cliente INT,
	 FOREIGN KEY(fk_id_cliente) REFERENCES clientes(id),
	 fk_id_personal INT,
	 FOREIGN KEY(fk_id_personal) REFERENCES Personal(id),
	 fecha DATE,
	 presupuesto DECIMAL(6,2)
);

--- 3. Realiza lo necesario para que cuando se inserte una cita se cree un trabajo con realizado a false.


ALTER TABLE Trabajos
RENAME COLUMN fk_id_personal to fk_id_responsable;

DELETE FROM Trabajos
WHERE fk_id_responsable = fk_id_responsable;

ALTER TABLE Trabajos
RENAME COLUMN fk_id_responsable to fk_id_personal;

ALTER TABLE CitasEvaluacion
RENAME COLUMN fk_id_personal to fk_id_responsable;

--- 3. Realiza lo necesario para que cuando se inserte una cita se cree un trabajo con realizado a false.

CREATE OR REPLACE FUNCTION crear_trabajo()
RETURNS TRIGGER AS $$
BEGIN
		INSERT INTO Trabajos (descripcion, fecha_inicio, fk_id_lugar, fk_id_responsable, realizado)
		VALUES ('Trabajo no realizado, cita pactada', NEW.fecha, NEW.fk_id_lugar, NEW.fk_id_responsable, FALSE); 
		RETURN NEW;
END; 
$$ LANGUAGE plpgsql;

CREATE TRIGGER crear_trabajo_automatico
AFTER INSERT ON CitasEvaluacion
FOR EACH ROW EXECUTE FUNCTION crear_trabajo();

SELECT * FROM Trabajos;
SELECT * FROM CitasEvaluacion;

INSERT INTO CitasEvaluacion (fecha, presupuesto, fk_id_lugar, fk_id_responsable, fk_id_cliente)
VALUES ('2025-01-03', 1623.78, 2, 1, 2);

UPDATE Trabajos
SET descripcion = 'PReseupuesto aceptado por el cliente, comienzo proximo'
WHERE id = 3;

UPDATE Trabajos
SET fecha_inicio='2025-01-10', fecha_fin = '2025-03-15'
WHERE id = 3;

--- 4. Configura los ON UPDATE y ON DELETE de las fks, de una manera que te parezca lógica.

SELECT *
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';

-- Borro la restriccion

ALTER TABLE CitasEvaluacion
DROP CONSTRAINT citasevaluacion_fk_id_cliente_fkey;

-- La vuelvo a crear con ON UPDATE y ON DELETE
ALTER TABLE CitasEvaluacion
ADD CONSTRAINT fk_cliente
FOREIGN KEY(fk_id_cliente) REFERENCES Clientes(id)
ON UPDATE CASCADE
ON DELETE SET NULL;

SELECT * FROM CitasEvaluacion;
SELECT * FROM Clientes;

UPDATE Clientes
SET id = 490
WHERE id = 1;

INSERT INTO Clientes (nombre, telefono, email)
VALUES ('Davinia', '600000000', 'info@davinia.com');

INSERT INTO CitasEvaluacion (fecha, presupuesto, fk_id_lugar, fk_id_responsable, fk_id_cliente)
VALUES ('2025-01-03', 1623.78, 2, 1, 3);

DELETE FROM Clientes WHERE id=3;

-- Realiza más relaciones, de manera que se puedan saber los materiales usados en los trabajos realizados.

CREATE TABLE Material_trabajos (
	id SERIAL PRIMARY KEY,
	fk_id_material INT,
	fk_id_trabajo INT,
	FOREIGN KEY(fk_id_material) REFERENCES Materiales(id),
	FOREIGN KEY(fk_id_trabajo) REFERENCES Trabajos(id)
);

-- Realiza todos los cambios que consideres en la BD

ALTER TABLE Trabajos
ADD COLUMN fk_id_cliente INT;

ALTER TABLE Trabajos
ADD CONSTRAINT fk_cliente_trabajos
FOREIGN KEY(fk_id_cliente) REFERENCES Clientes(id)
ON UPDATE CASCADE
ON DELETE NO ACTION; 

ALTER TABLE CitasEvaluacion
ADD COLUMN fk_id_trabajo INT; 

ALTER TABLE CitasEvaluacion
ADD CONSTRAINT fk_trabajo
FOREIGN KEY(fk_id_trabajo) REFERENCES Trabajos(id)
ON UPDATE CASCADE
ON DELETE CASCADE;