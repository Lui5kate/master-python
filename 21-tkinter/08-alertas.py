from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    # MessageBox.showinfo("Alerta", "Hola soy Luis Armando Lira")
    MessageBox.showerror("Alerta", "Hola soy Luis Armando Lira")
    # MessageBox.showwarning("Alerta", "Hola soy Luis Armando Lira")


Button(ventana, text="Mostrar alerta!!!",command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Realmente quieres salir?")
    
    if resultado != "no":
        MessageBox.showinfo("Hasta Luego!",f"Adios {nombre}")
        ventana.destroy()

    
Button(ventana, text="Salir",command=lambda: salir("Luis")).pack()

ventana.mainloop()