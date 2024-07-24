-- Database: ejercicio3

-- DROP DATABASE IF EXISTS ejercicio3;

CREATE TABLE profesores(
	id SERIAL PRIMARY KEY,
	DNI VARCHAR(20) UNIQUE,
	nombre VARCHAR(100),
	direccion TEXT,
	telefono VARCHAR(20)
);

CREATE TABLE modulo(
	id SERIAL PRIMARY KEY,
	codigo VARCHAR(50),
	nombre VARCHAR(100),
	fk_id_profesores INT REFERENCES profesores id,
	FOREIGN KEY (fk_id_profesores) REFERENCES profesores id
);


