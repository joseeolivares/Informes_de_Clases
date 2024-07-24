
import psycopg2


try:
    conn = psycopg2.connect(database="ClientesProveedores",user='postgres',password='root',host='127.0.0.1',port='5432')
    cursor = conn.cursor()
    postgres_insert_query = """INSERT INTO clientes(nombre) VALUES (%s)"""
    nombre = input('Inserte el nombre del cliente: ')
    cursor.execute(postgres_insert_query, (nombre))
    conn.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into publisher table")
except (Exception, psycopg2.Error) as error:
	print("Failed to insert record into publisher table", error)
