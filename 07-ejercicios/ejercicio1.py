"""
EJERCICIO 1.
    - Crear 2 variables, una "pais" y otra "continente"
    - Mostrar su valor por pantalla (imprimir)
    - Poner un comentario diciendo el tipo de dato
"""

pais = "Mexico"                     #string
continente = "Americano"            #string
pais2 = str(type(pais))             #type convertido a string
continente2 = str(type(continente)) #type convertido a string

print(f"Tu país es {pais} y tu continente es {continente}")
print(f"{pais} es de tipo " + pais2)
print(f"{continente} es de tipo " + continente2)