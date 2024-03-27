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
cursor = database.cursor()

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