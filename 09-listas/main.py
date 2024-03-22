"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un único
nombre.
Para acceder a esos valores podemos usar un indice numérico.
"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez')) #tuplas con metodo list
years = list(range(2020, 2250))
variada = ["Luis", 30, 4 , 4.5, True, "Texto"]
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
# Indices
pelicula = "otra cosa"
peliculas[2] = "El hobbit"
peliculas[1] = "Titanic"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])

# Añadir elementos a lista

cantantes.append("kase 0")
cantantes.append("odisseo")
print(cantantes)

# Recorrer lista

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n********Listado Peliculas*****************")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

# Listas multidimensionales
print("\n************Listado de contactos************")

contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

print(contactos)
print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")


