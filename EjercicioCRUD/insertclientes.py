import psycopg2


try:
	connection = psycopg2.connect(user="postgres",
								password="root",
								host="127.0.0.1",
								port="5432",
								database="ejerciciocrud1")
	cursor = connection.cursor()
	postgres_insert_query = """ INSERT INTO clientes(nombre, apellidos, dni, direccion, fecha_nacimiento) VALUES (%s,%s,%s,%s,%s)"""
	nombre = input('Inserta un nombre: ')
	apellidos = input('Insertar apellidos: ')
	dni = input('Insertar DNI: ')
	direccion = input('Insertar Direccion: ')
	fecha_nacimiento = input('Insertar Fecha de Nacimiento: ')
	cursor.execute(postgres_insert_query, (nombre, apellidos, dni, direccion, fecha_nacimiento))
	connection.commit()
	count = cursor.rowcount
	print(count, "Record inserted successfully into clientes table")

except (Exception, psycopg2.Error) as error:
	print("Failed to insert record into clientes table", error)

finally:
	# closing database connection.
	if connection:
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")

