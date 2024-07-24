-- Database: ejerciciopractico

-- DROP DATABASE IF EXISTS ejerciciopractico;

CREATE TABLE vehiculo (
	id SERIAL PRIMARY KEY,
	propietario VARCHAR(100) NOT NULL,
	matricula VARCHAR(50) NOT NULL
);

CREATE TABLE reparacion (
	id SERIAL,
	descripcion TEXT,
	PRIMARY KEY(id)
);
	
CREATE TABLE vehiculo_reparacion (
	id SERIAL PRIMARY KEY,
	fk_id_vehiculo INT,
	fk_id_reparacion INT,
	FOREIGN KEY (fk_id_vehiculo) REFERENCES vehiculo (id),
	FOREIGN KEY (fk_id_reparacion) REFERENCES reparacion (id)
);

SELECT * FROM vehiculo
SELECT * FROM reparacion
SELECT * FROM vehiculo_reparacion

INSERT INTO vehiculo (propietario, matricula)
VALUES ('Armando Figueroa', '123ABC');
INSERT INTO vehiculo (propietario, matricula)
VALUES ('Maria Lopez', '456DEF');
INSERT INTO vehiculo (propietario, matricula)
VALUES ('Alex Suarez', '789GHI') 

INSERT INTO reparacion (descripcion)
VALUES ('Cambio de Neumaticos');
INSERT INTO reparacion (descripcion)
VALUES ('Lavado');
INSERT INTO reparacion (descripcion)
VALUES ('Cambio de Aceite y Neumaticos')

INSERT INTO vehiculo_reparacion (fk_id_vehiculo, fk_id_reparacion)
VALUES (1,2);
INSERT INTO vehiculo_reparacion (fk_id_vehiculo, fk_id_reparacion)
VALUES (2,1);
INSERT INTO vehiculo_reparacion (fk_id_vehiculo, fk_id_reparacion)
VALUES (3,3)
