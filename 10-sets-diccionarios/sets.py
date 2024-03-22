"""
SET es un tipo de dato, para tener una colección de valores,
pero no tiene ni índice ni órden.
"""

personas =  {
    "Victor",
    "Manuel",
    "Paco"
}

personas.add("Luis")
personas.remove("Manuel")


print(personas)
print(type(personas))
