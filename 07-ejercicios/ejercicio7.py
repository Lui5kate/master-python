"""
Ejercicio 7. Hacer un programa que muestre todos los numeros
impares entre dos numeros que decida el usuario.
"""

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 < numero2:
    for conteo in range(numero1, (numero2+1)):
        if conteo%2 != 0:
            print(conteo)
else:
    print("El numero 1 debe ser mayor al numero 2")
