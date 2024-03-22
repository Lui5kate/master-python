'''
Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano,
que imprima un mensaje según el tipo de dato de cada variable. Usar funciones.
'''

# Función para traducir tipos de datos a sus nombres en español
def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == int:
        result = "Número"
    elif tipo == bool:
        result = "Booleano"
    else:
        result = "tipo de dato no admitido"
    return result


# Función para comprobar el tipo de dato de una variable y mostrarlo si coincide con el tipo especificado.
def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = f"Este dato es de tipo: {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato es incorrecto"
    return result

# Variables de ejemplo
mi_lista = ["hola mundo", 77]
titulo = "Master de Python"
numero = 100
verdadero = True

# Llamada a la función para comprobar el tipo de dato
print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))