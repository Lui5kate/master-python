# POO

# definir una clase (molde para crear mas objetos de ese tipo
#  (Coche) conc aracterísticas similares)

class Coche:
    
    # Atributos o propiedades (variables)
    # Características del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

# fin defiición clase

# Crear objetos / Instanciar la clase
coche = Coche()

print("Coche 1:")

coche.setColor("amarillo")
coche.setModelo("murcielago")

print(coche.marca, coche.getModelo(),  coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad actual: ", coche.getVelocidad())

# Crear mas objetos

print("-------------------")
print("Coche 2:")

coche2 = Coche()
coche2.setColor("Verde")
coche2.setModelo("Gallardo")
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))