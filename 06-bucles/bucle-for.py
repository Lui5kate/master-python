"""
# FOR

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range(0, 5):
    print("Voy por el " + str(contador))
    #resultado = resultado + contador
    resultado += contador

print(f"El resultado es: {resultado}")

# Ejemplo tablas de multiplicar
print("\n#### EJEMPLO 1 #####")

numero_usuario = int(input("¿De qué número quieres la tabla?: "))

print(f"\n#### Tabla de multiplicar del numero {numero_usuario} ####")

for numero_tabla in range(1, 11):
    if numero_usuario > 99:
        print("No se puede mostrar la tabla de números mayores a 99")
        break
    elif numero_usuario < 1:
        print("No se puede mostrar la tabla de números menores a 1")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")
