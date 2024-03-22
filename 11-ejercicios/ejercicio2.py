'''
Escribir un programa que añada valores a una lista mientras su longitud sea menor a 120 y luego mostrar la lista.
Plus: Usar While y For
'''

coleccion = []
'''
for contador in range(0,120):
    coleccion.append(f"elemento - {contador}")
    print("Mostrando el: " + coleccion[contador])

#print(coleccion)
print(coleccion[115])
'''
x = 0

while x < 120:
    coleccion.append(f"elemento - {x}")
    print("Mostrando el: " + coleccion[x])
    x+=1

print(coleccion)