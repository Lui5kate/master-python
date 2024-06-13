"""
Proyecto pytho y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la BDD
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login      
""")

hazEl = acciones.Acciones()
accion = input("¿Qué deseas hacer?: ")

if accion == "registro" or accion == "Registro" or accion == "REGISTRO":
    hazEl.registro()
elif accion == "login" or accion == "Login" or accion == "LOGIN":
    hazEl.login()