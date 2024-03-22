cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1, 2, 5, 8, 3 , 4]

# Ordenar
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Babo")
print(cantantes)
cantantes.insert(1, 'Zoe')
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
print(cantantes)
cantantes.remove("Bad Bunny")
print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)

# Contar elementos
print(cantantes)
print(len(cantantes))

# Cuantas veces aparece un elemento
print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes)
print(cantantes.index("Drake"))
print(cantantes.index("2pac"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)

