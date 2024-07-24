import psycopg2

# Establishing the connection
conn = psycopg2.connect(
	database="examenpracticopg-",
	user='postgres',
	password='root',
	host='127.0.0.1',
	port='5432'
)

# Creating a cursor object using the 
# cursor() method
cursor = conn.cursor()

# Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS libros")

# Creating table as per requirement
sql = '''CREATE TABLE libros(
				codigo SERIAL,
				titulo VARCHAR(40) NOT NULL,
				codigoautor INT not null,
				codigoeditorial smallint not null,
                precio decimal(5,2),
				primary key(codigo)
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()

# Closing the connection
conn.close()
