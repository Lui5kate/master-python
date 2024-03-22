"""
Ejercicio 4. Pedir dos numeros al usuario y hacer todas las
operaciones básicas de una calculadora y mostrarlo por pantalla.
"""

print("###Calculadora básica###")
numero1 = int(input("\n Ingresa el primer numero: "))
numero2 = int(input("\n Ingresa el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
residuo = numero1 % numero2
print(f"\nLa suma es = {suma}")
print(f"La resta es = {resta}")
print(f"La multiplicación es = {multiplicacion}")
print(f"La divison es = {division}")
print(f"El residuo de la division es = {residuo}")