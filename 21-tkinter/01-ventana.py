# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = " MC-Traker | Automatizaciones y Analíticos 2024"
        self.icon = './imagenes/imagen_carpeta.ico'
        self.icon_alt = './MC-TRAKER/imagenes/imagen_carpeta.ico'
        self.size = "770x470"
        self.resizable = False
    
    def cargar(self):
        # Crear la ventana raíz
        ventana = Tk()
        self.ventana = ventana

        # Título de ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamñaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

    def addText(self,texto_ingresado):
        texto = Label(self.ventana, text=texto_ingresado)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

# Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addText("Adios")
programa.addText("hey")
programa.mostrar()