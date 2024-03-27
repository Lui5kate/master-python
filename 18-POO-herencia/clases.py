# Herencia: Es la posibilidad de compartir atributos y metodos. Y que diferentes clases hereden de otros

class Persona:
    """
    nombre
    apellidos
    edad
    altura
    """
    
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def geEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad
    
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"
    
class Informatico(Persona):
    """
    lenguajes
    Experiencia
    """

    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado tu PC"
    
class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()
        self.auditarRedes = 'experto'
        self.experieciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red"