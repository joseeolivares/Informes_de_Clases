import psycopg2

def delete():
	try:
		connection = psycopg2.connect(user="postgres",
									password="root",
									host="127.0.0.1",
									port="5432",
									database="ejerciciocrud")
		cursor = connection.cursor()

		# Update single record now
		sql_delete_query = """Delete from id_cliente\
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


id_cliente = 1
delete()
def conectar():
    conexion = 0
def opciones1():
    opcion = 0
    print('Elige una opcion:')
    print('1. Insertar en una tabla')
    print('2. Borrar en una tabla')
    print('3. Actualizar datos en una tabla')
    print('4. Buscar en una tabla')
    print('5. Salir')
    opcion = int(input('')) 
    return opcion

def opciones2():
    opcion = 0
    print('Elige una tabla:')
    print('1. Clientes')
    print('2. Productos')
    print('3. Proveedores')
    print('4. Compras')
    print('5. Salir')
    opcion = int(input('')) 
    return opcion

def menu():
    opcion = 0
    opcion2 = 0
    while opcion != 5:
        opcion = opciones1()
        if opcion != 5:
            opcion2 = opciones2()
        if opcion == 1:
            if opcion2 == 1:
                print('Insert en Clientes') 
            if opcion2 == 2:
                print('Insert en Productos') 
            if opcion2 == 3:
                print('Insert en Proveedores') 
            if opcion2 == 4:
                print('Insert en Compras') 
        if opcion == 2:
            if opcion2 == 1:
                delete()
            if opcion2 == 2:
                print('Borrar en Productos') 
            if opcion2 == 3:
                print('Borrar en Proveedores') 
            if opcion2 == 4:
                print('Borrar en Compras') 
        if opcion == 3:
            if opcion2 == 1:
                print('Actualizar Clientes') 
            if opcion2 == 2:
                print('Actualizar Productos') 
            if opcion2 == 3:
                print('Actualizar Proveedores') 
            if opcion2 == 4:
                print('Actualizar Compras')
        if opcion == 4:
            if opcion2 == 1:
                print('Buscar en Clientes') 
            if opcion2 == 2:
                print('Buscar en Productos') 
            if opcion2 == 3:
                print('Buscar en Proveedores') 
            if opcion2 == 4:
                print('Buscar en Compras')
    
conexion = conectar()
menu()