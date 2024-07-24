
import psycopg2


try:
	connection = psycopg2.connect(user="postgres",
								password="root",
								host="127.0.0.1",
								port="5432",
								database="examenpracticopg-")
	cursor = connection.cursor()

	postgres_insert_query = """ INSERT INTO libros(codigo,
	titulo, codigoautor, codigoeditorial, precio) 
	VALUES (%s,%s,%s,%s,%s)"""
	record_to_insert = [(1, 'Las ventajas de ser un Invisible', 1,
						500, '25.5')]
	for i in record_to_insert:
		cursor.execute(postgres_insert_query, i)
		connection.commit()
		count = cursor.rowcount
	print(count, "Record inserted successfully \
	into libros table")

except (Exception, psycopg2.Error) as error:
	print("Failed to insert record into libros table", error)

finally:
	# closing database connection.
	if connection:
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")
