import psycopg2

def selectcliente():
	try:
		connection = psycopg2.connect(user="postgres",
									password="root",
									host="127.0.0.1",
									port="5432",
									database="ejerciciocrud1")
		cursor = connection.cursor()
		
		sql_update_query = "select * from Clientes"
		
		cursor.execute(sql_update_query,)
		print("Selecting rows from publisher table using cursor.fetchall")
		cliente_2 = cursor.fetchall()
		
		print("Print each row and it's columns values")
		for row in cliente_2:
			print("id_cliente = ", row[0], )
			print("nombre = ", row[1])
			print("apellidos = ", row[2])
			print("dni = ", row[3])
			print("direccion = ", row[4], "\n")
			print("fecha_nacimiento = ", row[5],"\n")
	except (Exception, psycopg2.Error) as error:
			print("Error while fetching data from PostgreSQL", error)

	finally:
		# closing database connection.
		if connection:
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

selectcliente()