import psycopg2
import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
def select_all(id):
    resultado_dic = {}
    try:
        conn = psycopg2.connect(
            database="empleados",
            user='postgres',
            password='root',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        select_query = "select * from empleados"
        if id:
            select_query = "select * from empleados where id="+id
        cursor.execute(select_query)
        empleados_resultado = cursor.fetchall() # Resultado de la consulta 
        for row in empleados_resultado:
            resultado_dic[row[0]] = {} # {'1':{}}
            resultado_dic[row[0]]['nombre'] = row[1] # {'1':{'isbn':'11111'}}
            #resultado_dic[row[0]]['isbn'] = '44444'# {'1':{'isbn':'44444'}}
            resultado_dic[row[0]]['apellidos'] = row[2] # {'1':{'isbn':'11111', 'titulo':'Lo que el viento se llevó' }}
            resultado_dic[row[0]]['trabaja_desde'] = row[3]
        print(resultado_dic)
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL: ", error)
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    return resultado_dic

def empleados_insert(nombre, apellidos, trabaja_desde):
    try:
        conn = psycopg2.connect(
            database="empleados",
            user='postgres',
            password='root',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()

        insert_query = """ INSERT INTO empleados(nombre, apellidos, trabaja_desde) 
        VALUES (%s,%s,%s)"""
        data = (nombre, apellidos, trabaja_desde)
        print(data)
        cursor.execute(insert_query, data)
        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into Empleados table")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into empleados table", error)
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")



app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

@app.route('/all', methods=['GET'])
@cross_origin()
def all():
    resultado_dic = select_all(request.args.get('id'))# id=1 -> {'1':{'isbn':'11111', 'titulo':'Lo que el viento se llevó' }}
    return jsonify(resultado_dic)

#/insert (POST): Inserta un Empleados
@app.route('/insert', methods=['POST'])
@cross_origin()
def insert():
   empleados_insert(request.json.get('nombre'), request.json.get('apellidos'), request.json.get('trabaja_desde'))
   return jsonify({'resultinsert': 'Insertado con Éxito'})


def empleadosIddelete(id):
    try:
        conn = psycopg2.connect(
            database="empleados",
            user='postgres',
            password='root',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()

        # Update single record now
        sql_delete_query = """Delete from empleados where id = %s"""
        cursor.execute(sql_delete_query, (id))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into empleados table", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    

@app.route('/delete/<string:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    print("id")
    empleadosIddelete(id)
    return jsonify({'resultdelete': 'Borrado con Éxito'})

def empleadosIdupdate(id, nombre):
    try:
        conn = psycopg2.connect(
            database="empleados",
            user='postgres',
            password='root',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()

        sql_update_query = """Update empleados set \
		empleados_estd = %s where empleados_id = %s"""
        cursor.execute(sql_update_query, (nombre, empleadosId))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record update successfully ")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into empleados table", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

@app.route('/update/<string:id>/<string:nombre>', methods=['PUT'])
@cross_origin()
def update(id,nombre):
    empleadosIdupdate(id,nombre)
    return jsonify({'resultupdate': 'Actualizado con Éxito'})


app.run()