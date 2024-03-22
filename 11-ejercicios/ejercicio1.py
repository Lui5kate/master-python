"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer función que recorre listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algún elemento (que el usuario pida por teclado)
"""
# Crear lista
numeros = [5, 1, 3, 1, 12, 78, 30, 190]
print(numeros)

# Crear función que recorra y devuelva string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += f"Elemento {lista.index(elemento)+1}: " + str(elemento)
        resultado += "\n"
    return resultado


# Recorrer y mostrar
print("#####Recorrer y mostrar#####")
for conteo in numeros:
    print(conteo)

# Crear función que recorra y devuelva string
print(mostrarLista(numeros))
print(mostrarLista(["Luis", "Manuel"]))

# Ordenar y mostrar
print("#####Ordenar y mostrar#####")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar su longitud
print("#####Mostrar su longitud#####")
print(len(numeros))

# Buscar algún elemento (que el usuario pida por teclado)
try:
    print("#####Busqueda en la lista#####")

    busqueda = int(input("Elemento a buscar: "))

    while not isinstance(busqueda, int) or busqueda <= 0:
        busqueda = int(input("Elemento a buscar: "))
    else:
        print(f"Has introducido el numero {busqueda}")

        search = numeros.index(busqueda)
        print(f"El numero buscado existe en la lista con indice: {search}")
except:
    print("El numero no está en la lista")

