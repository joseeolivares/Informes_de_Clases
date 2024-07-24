
import psycopg2


try:
	connection = psycopg2.connect(user="postgres",
								password="root",
								host="127.0.0.1",
								port="5432",
								database="ejerciciocrud")
	cursor = connection.cursor()

	postgres_insert_query = """ INSERT INTO clientes(nombre,
     apellidos, dni, direccion, fecha_nacimiento) 
	VALUES (%s,%s,%s,%s,%s)"""
	record_to_insert = [('Juan', 'García', '12345678A', 
                        'Calle Principal 123', '1990-05-15'),
						('María', 'López', '87654321B',
                         'Avenida Central 456', '1985-10-20'),
						('Pedro', 'Martínez', '23456789C', 
                        'Plaza Mayor 789', '1978-03-25')]
	for i in record_to_insert:
		cursor.execute(postgres_insert_query, i)
		connection.commit()
		count = cursor.rowcount
	print(count, "Record inserted successfully \
	into clientes table")

except (Exception, psycopg2.Error) as error:
	print("Failed to insert record into clientes table", error)

finally:
	# closing database connection.
	if connection:
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")
