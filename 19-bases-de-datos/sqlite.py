import sqlite3

# Crear conexión
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio int(255)
);
""")

# Guardar cambios
conexion.commit()

# Insertar datos
cursor.execute("""
INSERT INTO productos VALUES (
    NULL,'Primer Producto', 'Descripción de mi producto', 550
)
""")
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)

print("----------")

for producto in productos:
    print(producto)

print("----------")

for producto in productos:
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])

print("----------")

cursor.execute("SELECT * FROM productos")
producto = cursor.fetchone()
print(producto)

print("---------")

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)

print("---------")

# Insertar muchos registros de golpe
productos = [
    ("producto 1", "descripción 1", 100),
    ("producto 2", "descripción 2", 200),
    ("producto 3", "descripción 3", 300),
    ("producto 4", "descripción 4", 400)
]

cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ? )", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio=678 WHERE precio=200")

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)

print("---------")

# Cerrar conexión
conexion.close()

