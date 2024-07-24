-- Database: ejercicio23_04_practico

-- DROP DATABASE IF EXISTS ejercicio23_04_practico;

CREATE TABLE presidentes (
	id SERIAL PRIMARY KEY,
	dni INT UNIQUE,
	nombre VARCHAR(50),
	apellidos VARCHAR(100),
	equipo VARCHAR(50),
	año_elegido_presidente VARCHAR(4),
	fecha_nacimiento DATE
);

CREATE TABLE equipos (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	estadio_juega VARCHAR(100),
	aforo VARCHAR(100),
	año_fundado VARCHAR(4),
	ciudad_equipo TEXT,
	codigo_indentifica INT UNIQUE,
	fk_id_presidente INT,
	FOREIGN KEY (fk_id_presidente) REFERENCES presidentes(id)
);

CREATE TABLE jugadores(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	fecha_nacimiento DATE,
	posicion_juego VARCHAR(50),
	codigo_jugador INT UNIQUE,
	fk_id_equipo INT,
	FOREIGN KEY (fk_id_equipo) REFERENCES equipos(id)
);

CREATE TABLE partidos (
	id SERIAL PRIMARY KEY,
	nombre_equipo VARCHAR(50),
	nombre_estadio VARCHAR(50),
	goles_metidos_equipo_casa VARCHAR(4),
	goles_metidos_equipo_fuera VARCHAR(4),
	codigo_numerico INT UNIQUE
);

CREATE TABLE goles (
	id SERIAL PRIMARY KEY,
	numero_goles VARCHAR(4),
	minuto_gol VARCHAR(20),
	descripcion TEXT
);

CREATE TABLE goles_jugadores_partidos (
	id SERIAL PRIMARY KEY,
	fk_id_jugador INT,
	FOREIGN KEY (fk_id_jugador) REFERENCES jugadores(id),
	fk_id_partido INT,
	FOREIGN KEY (fk_id_partido) REFERENCES partidos(id),
	fk_id_gol INT,
	FOREIGN KEY (fk_id_gol) REFERENCES goles(id)
);


INSERT INTO presidentes (dni, nombre, apellidos, equipo, año_elegido_presidente, fecha_nacimiento)
VALUES ('123456', 'nombre1', 'apellido1', 'equipo1', '2005', '2000-05-25')

INSERT INTO presidentes (dni, nombre, apellidos, equipo, año_elegido_presidente, fecha_nacimiento)
VALUES ('1234564', 'nombre2', 'apellido2', 'equipo2', '2003', '2000-05-28')

INSERT INTO equipos (nombre, estadio_juega, aforo , año_fundado, ciudad_equipo, codigo_indentifica, fk_id_presidente)
VALUES ('equipo1', 'estadio1', '1500', '2001', 'ciudad1', '1234', '1')

INSERT INTO equipos (nombre, estadio_juega, aforo , año_fundado, ciudad_equipo, codigo_indentifica, fk_id_presidente)
VALUES ('equipo2', 'estadio2', '1600', '2000', 'ciudad2', '12345', '2')

INSERT INTO jugadores (nombre, fecha_nacimiento, posicion_juego, codigo_jugador, fk_id_equipo)
VALUES ('jugador 1', '2003-02-25', 'posicion1', '2545', '1')

INSERT INTO jugadores (nombre, fecha_nacimiento, posicion_juego, codigo_jugador, fk_id_equipo)
VALUES ('jugador 2', '2004-02-25', 'posicion2', '2546', '2')

INSERT INTO partidos (nombre_equipo, nombre_estadio, goles_metidos_equipo_casa, goles_metidos_equipo_fuera, codigo_numerico)
VALUES ('nombre1', 'estadio1', '25', '26', '4567')

INSERT INTO partidos (nombre_equipo, nombre_estadio, goles_metidos_equipo_casa, goles_metidos_equipo_fuera, codigo_numerico)
VALUES ('nombre2', 'estadio2', '26', '25', '45678')

INSERT INTO goles (numero_goles, minuto_gol,descripcion)
VALUES ('2', '89', 'descripcion1')

INSERT INTO goles (numero_goles, minuto_gol,descripcion)
VALUES ('4', '90', 'descripcion2')

INSERT INTO goles_jugadores_partidos (fk_id_jugador, fk_id_partido, fk_id_gol)
VALUES ('1', '1', '1')

INSERT INTO goles_jugadores_partidos (fk_id_jugador, fk_id_partido, fk_id_gol)
VALUES ('1', '2', '2')

SELECT * FROM jugadores;
SELECT * FROM presidentes
SELECT * FROM equipos
SELECT * FROM partidos
SELECT * FROM goles
SELECT * FROM goles_jugadores_partidos

ALTER TABLE goles_jugadores_partidos
ADD CONSTRAINT fk_jugador
FOREIGN KEY(fk_id_jugador) REFERENCES jugadores(id)
ON UPDATE CASCADE
ON DELETE SET NULL;

SELECT * FROM goles_jugadores_partidos

