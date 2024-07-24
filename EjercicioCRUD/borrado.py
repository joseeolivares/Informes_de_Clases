import psycopg2

def delete():
	try:
		connection = psycopg2.connect(user="postgres",
									password="root",
									host="127.0.0.1",
									port="5432",
									database="ejerciciocrud1")
		cursor = connection.cursor()

		# Update single record now
		sql_delete_query = """Delete from Clientes\
		where id_cliente = %s"""
		cursor.execute(sql_delete_query, (id_cliente,))
		connection.commit()
		count = cursor.rowcount
		print(count, "Record deleted successfully ")

	except (Exception, psycopg2.Error) as error:
		print("Error in Delete operation", error)

	finally:
		# closing database connection.
		if connection:
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")


id_cliente = 3
delete()