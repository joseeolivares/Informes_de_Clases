import psycopg2


def updateTable(id_cliente, nombre2):
	try:
		connection = psycopg2.connect(user="postgres",
									password="root",
									host="127.0.0.1",
									port="5432",
									database="ejerciciocrud1")
		cursor = connection.cursor()

		# Update single record now
		sql_update_query = """Update Clientes set \
		nombre = %s where id_cliente = %s"""
		cursor.execute(sql_update_query,
					(nombre2,
						id_cliente))
		connection.commit()
		count = cursor.rowcount
		print(count, "Record Updated successfully ")

	except (Exception, psycopg2.Error) as error:
		print("Error in update operation", error)

	finally:
		# closing database connection.
		if connection:
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")


# call the update function
id_cliente = 3
nombre2 = "Alex"
updateTable(id_cliente, nombre2)