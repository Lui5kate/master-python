"""
DICCIONARIO:
Es un tipo de dato que almacena un conjunto de datos.
En formato de clave valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Luis",
    "apellidos": "Lira",
    "web": "lalg22@oytlook.com"
}

print(persona)
print(type(persona))
print(persona["apellidos"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Paco',
        'email': "paco.web",
    },
    {
        'nombre': 'Luis',
        "email": 'luis.web',
    },
    {
        'nombre': 'José',
        'email': 'jose.web'
    }
]

print(contactos)
contactos[0]['nombre'] = 'Francisco'
print(contactos[0]['nombre'])

print("\nListado de contactos: ")
print("------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("------------------------------------")

