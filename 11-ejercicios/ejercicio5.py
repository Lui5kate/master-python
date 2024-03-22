'''
Crear una lista con el contenido de este tabla:
Accion    Aventura              Deportes
GTA         MARIO               FIFA 21
COD         CRASH               PRO 21
PUBG        PRINCE OF PERSIA    FORZA

Mostrar este información ordenada
'''

tabla = [
    {
        "categoria": "Accion",
        "juegos": ["GTA", "COD", "PUBG"]
    },
    {
        "categoria": "Aventura",
        "juegos": ["Mario", "Crash", "Prince of persia"]
    },
    {
        "categoria": "Deportes",
        "juegos": ["FIFA 21", "PRO 21", "FORZA"]
    }
]

for categoria in tabla:
    print(f"---------{categoria['categoria']}---------")
    for juego in categoria['juegos']:
        print(juego)