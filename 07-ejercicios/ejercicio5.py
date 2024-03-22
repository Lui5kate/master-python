"""
Ejecicio 5. Hacer un programa que muestre todos los números entre
dos numeros que diga el usuario.
"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 <= 0 or numero2 <= 0:
    print("Ingrese números mayores a 0")
elif numero2 < numero1:
    print("El segundo número debe ser mayor al primero")
else:
    for conteo in range(numero1, (numero2+1)):
        print(conteo)