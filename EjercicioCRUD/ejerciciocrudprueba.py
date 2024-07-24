import psycopg2

connection = psycopg2.connect(user="postgres",
								password="root",
								host="127.0.0.1",
								port="5432",
								database="ejerciciocrud1")
cursor = connection.cursor()

# Creamos un menú  

import psycopg2
def conectar():
    conexion = 0
    try:
        conexion = psycopg2.connect(database='ejerciciocrud1', user='postgres', password='root')
    except: 
        print('Error')
    return conexion


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

def insertclientes():
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

def insertproductos():
    postgres_insert_query = """ INSERT INTO productos(codigo, nombre, precio_unitario) VALUES (%s,%s,%s)"""
    codigo = input('Inserta un Codigo: ')
    nombre = input('Inserta un nombre: ')
    precio_unitario = input('Inserta un Precio Unitario: ')
    cursor.execute(postgres_insert_query, (codigo, nombre, precio_unitario))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into productos table")

def insertproveedores():
    postgres_insert_query = """ INSERT INTO proveedores(nif, nombre, direccion) VALUES (%s,%s,%s)"""
    nif = input('Inserta un nif: ')
    nombre = input('Insertar un nombre: ')
    direccion = input('Insertar una Direccion: ')
    cursor.execute(postgres_insert_query, (nif, nombre, direccion))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into proveedores table")

def insertcompras():
    postgres_insert_query = """ INSERT INTO compras (id_cliente, codigo_producto, cantidad, fecha_compra) VALUES (%s,%s,%s,%s)"""
    id = input('Inserta el id del cliente: ')
    codigo_producto = input('Insertar el codigo del Producto: ')
    cantidad = input('Insertar una Cantidad: ')
    fecha_compra = input('Insertar una fecha de Compra: ')
    cursor.execute(postgres_insert_query, (id_cliente, codigo_producto, cantidad, fecha_compra))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into compras table")

def deleteclientes():
    sql_delete_query = """Delete from Clientes\
    where id = (%s)"""
    id = input('Inserte el id que desea Borrar: ')
    cursor.execute(sql_delete_query, (id,))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")

def deleteproductos():
    sql_delete_query = """Delete from Productos\
    where codigo = (%s)"""
    codigo = input('Inserte el codigo del Producto que deseas borrar: ')
    cursor.execute(sql_delete_query, (codigo,))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")

def deleteproveedores():
    sql_delete_query = """Delete from Proveedor\
    where nif = (%s)"""
    nif = input('Inserte el nif del Proveedor que deseas borrar: ')
    cursor.execute(sql_delete_query, (nif,))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")
    
def deletecompras():
    sql_delete_query = """Delete from Compras\
    where id = (%s)"""
    id = input('Inserte el id de la Compra que deseas borrar: ')
    cursor.execute(sql_delete_query, (id,))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")

def updateclientes():
    sql_update_query = """Update Clientes set \3
	(nombre, apellidos, dni, direccion, fecha_nacimiento) = (%s,%s,%s,%s,%s) where id = %s"""
    id = input('Coloque el Id que deseas Actualizar: ')
    nombre = input('Inserta un nombre: ')
    apellidos = input('Insertar apellidos: ')
    dni = input('Insertar DNI: ')
    direccion = input('Insertar Direccion: ')
    fecha_nacimiento = input('Insertar Fecha de Nacimiento: ')
    cursor.execute(sql_update_query,(nombre, apellidos, dni, direccion, fecha_nacimiento,id))
    connection.commit()
    count = cursor.rowcount
    print(count, "Record Updated successfully ")
    
    

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
                insertclientes()
            if opcion2 == 2:
                print('Insert en Productos')
                insertproductos() 
            if opcion2 == 3:
                print('Insert en Proveedores')
                insertproveedores() 
            if opcion2 == 4:
                print('Insert en Compras')
                insertcompras() 
        if opcion == 2:
            if opcion2 == 1:
                print('Borrar en Clientes')
                deleteclientes()
            if opcion2 == 2:
                print('Borrar en Productos') 
                deleteproductos()
            if opcion2 == 3:
                print('Borrar en Proveedores')
                deleteproveedores 
            if opcion2 == 4:
                print('Borrar en Compras')
                deletecompras() 
        if opcion == 3:
            if opcion2 == 1:
                print('Actualizar Clientes')
                updateclientes() 
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