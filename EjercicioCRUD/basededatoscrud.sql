-- Crear la base de datos
--CREATE DATABASE prueba;

-- Conectarse a la base de datos
--\c prueba;

-- Crear la tabla Clientes
CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    dni VARCHAR(20) UNIQUE,
    direccion TEXT,
    fecha_nacimiento DATE
);

-- Crear la tabla Productos
CREATE TABLE Productos (
    codigo SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE,
    precio_unitario DECIMAL(10, 2)
);

-- Crear la tabla Proveedores
CREATE TABLE Proveedores (
    nif VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    direccion TEXT
);

-- Crear la tabla Compras para la relación muchos a muchos entre Clientes y Productos
CREATE TABLE Compras (
    id SERIAL PRIMARY KEY,
    id_cliente INT REFERENCES Clientes(id),
    codigo_producto INT REFERENCES Productos(codigo),
    cantidad INT,
    fecha_compra DATE,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id),
    FOREIGN KEY (codigo_producto) REFERENCES Productos(codigo)
);

-- Crear la tabla Suministros para la relación muchos a muchos entre Productos y Proveedores
CREATE TABLE Suministros (
    id SERIAL PRIMARY KEY,
    codigo_producto INT REFERENCES Productos(codigo),
    nif_proveedor VARCHAR(20) REFERENCES Proveedores(nif),
    FOREIGN KEY (codigo_producto) REFERENCES Productos(codigo),
    FOREIGN KEY (nif_proveedor) REFERENCES Proveedores(nif)
);

SELECT * FROM clientes;