"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y cada una tenga un dato distinto.
"""
# Crear variables y asignarles un valor
texto = "Máster en Python"
texto2 = "Luis Armando Lira González"
numero = 45
decimal = 7.9

#Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("---------------------------------------")

#Sustituir el valor de algunas variables /reasugnado valores
numero = 77
decimal = 8.0

print(numero)
print(decimal)

print("---------------------------------------")

# Concatenación

nombre= "Luis"
apellidos = "Lira"
web = "luislira.com"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print(nombre, apellidos, web)