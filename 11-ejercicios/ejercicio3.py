'''
Programa que compruebe si una variable está vacía, 
y si lo está, rellenarla con texto en minúsculas y 
mostrarlo en mayúsculas.
'''

texto = " "

if len(texto.strip()) <= 0:
    texto = "hola soy un texto en minúsculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")