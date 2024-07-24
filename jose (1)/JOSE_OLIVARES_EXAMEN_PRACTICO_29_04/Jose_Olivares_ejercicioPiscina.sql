-- Database: Jose_Olivares_ejercicioPiscinas

-- DROP DATABASE IF EXISTS "Jose_Olivares_ejercicioPiscinas";

-- Crear la tabla de Piscinas
CREATE TABLE Piscinas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(255),
    capacidad FLOAT,
    fecha_construccion DATE
);

-- Crear la tabla de ProductosQuimicos
CREATE TABLE ProductosQuimicos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(100),
    cantidad FLOAT,
    fecha_vencimiento DATE
);

-- Crear la tabla de Empleados
CREATE TABLE Empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    cargo VARCHAR(100)
);

-- Crear la tabla de Mantenimiento
CREATE TABLE Mantenimiento (
    id SERIAL PRIMARY KEY,
    fk_id_piscina INT,
    fk_id_producto INT,
    fk_id_empleado INT,
    fecha DATE,
    descripcion TEXT,
    costo FLOAT,
    FOREIGN KEY(fk_id_piscina) REFERENCES Piscinas(id),
    FOREIGN KEY(fk_id_producto) REFERENCES ProductosQuimicos(id),
    FOREIGN KEY(fk_id_empleado) REFERENCES Empleados(id)
);

SELECT * FROM piscinas
SELECT * FROM ProductosQuimicos
SELECT * FROM Empleados
SELECT * FROM Mantenimiento

INSERT INTO Piscinas (nombre, ubicacion, capacidad, fecha_construccion)
VALUES ('Pedro', 'Madrid, Madrid', '20.5', '2024-03-25')

INSERT INTO ProductosQuimicos (nombre, tipo, cantidad, fecha_vencimiento)
VALUES ('Detergente', 'Liquido', '1.5', '2026-05-25')

INSERT INTO Empleados (nombre, apellido, cargo)
VALUES ('Alejandro', 'Garcia', 'Encargado')

INSERT INTO Mantenimiento (fk_id_piscina, fk_id_producto, fk_id_empleado, fecha, descripcion, costo)
VALUES ('1', '1', '1', '2024-04-25', 'Lavado, pintado y limpieza', 1500)