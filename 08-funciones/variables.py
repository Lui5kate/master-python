"""
Variables locales: Se definen dentro de la función y no
se puede usar fuera de ella, solo están disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función
y están disponibles dentro y fuera de ellas.
"""

#Variable global
frase = "Mejor afuera que adentro"
print(frase)

def holaMundo():
    frase = "Hola mundo!!"
    print("Dentro de la función: ")
    print(frase)

    year = 2021
    print(year)
    
    global website
    website = "lalg22@outlook.com"
    print("Dentro de función: ", website)

    return "Dato devuelto " + str(year)

print(holaMundo())
print("Fuera: ", website)
