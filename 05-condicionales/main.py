"""
# Condicional IF

SI se cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones  

# Operadores de comparación
== igual
!= diferente
<  menor que
>  mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos

and Y
or O
! negacion
not NO

"""

# Ejemplo 1
print("###### EJEMPLO 1 #####")

#color = input("Adivina cuál es mi color favorito: ")
color = "rojo"

if color == "rojo":
    print("El color es ROJO")
else:
    print("Color incorrecto")

# Ejemplo 2
print("\n###### EJEMPLO 2 #####")

#year = int(input("¿En qué año estamos?: "))
year = 2020

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n###### EJEMPLO 3 #####")

nombre = "Luis Armando Lira"
ciudad = "CDMX"
continente = "America"
edad = 30
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "America":
        print("El usuario NO es Americano ")
    else:
        print(f"Es Americano y de {ciudad}")
        
else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4
print("\n###### EJEMPLO 4 #####")

#dia = int(input("Introduce el numero del día de la semana: "))
dia = 1

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print(" Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

# Ejemplo 5
print("\n###### EJEMPLO 5 #####")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 18

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No está en edad de trabajar")

# Ejemplo 6
print("\n###### EJEMPLO 6 #####")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana" )
else:
    print(f"{pais} NO es un país de habla hispana")

# Ejemplo 7
print("\n###### EJEMPLO 7 #####")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana" )
else:
    print(f"{pais} es un país de habla hispana")

# Ejemplo 8
print("\n###### EJEMPLO 8 #####")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana" )
else:
    print(f"{pais} es un país de habla hispana")