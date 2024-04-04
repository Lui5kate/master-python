import mysql.connector

# Conexión
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# Probar la conexión
print(database)

# Crear cursor
cursor = database.cursor(buffered=True)

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Mostrar las BDs
cursor.execute("SHOW DATABASES")
for BD in cursor:
    print(BD)

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id INT(10) auto_increment not null,
    marca VARCHAR(40) not null,
    modelo VARCHAR(40) not null,
    precio FLOAT(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Astra',18500)")
database.commit()

# Insertar varios registros
coches = [
    ('Seat','Ibiza', 5000),
    ('Renault','Clio', 522000),
    ('Chevy','Chevy', 511000),
    ('Mercedes','Clase C', 355000)
]

cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",coches)

# Listar registros
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

print("------------LISTADO COMPLETO----------------")
for coche in result:
    print(coche)

print("------------LISTADO COMPLETO POR INDICE 1 = COLUMNA MARCA----------------")
for coche in result:
    print(coche[1])

# Borrar
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Opel'")
database.commit()
print("---------------------------")
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
for coche in result:
    print(coche)
# Indica cuantos registros se borraron
print(cursor.rowcount,"borrados!!")

# Actualizar
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca= 'Seat'")
database.commit()

print(cursor.rowcount,"actualizados!!")