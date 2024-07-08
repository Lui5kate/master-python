from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
            fg="white",
            bg="#000000",
            padx="520",
            pady="20",
            font=("Consolas",30)
)
texto.pack()

texto = Label(ventana, text="Soy Luis Armando Lira")
texto.config(
    justify=RIGHT,
    width=20,
    height=10,
    bg="orange",
    padx=10,
    pady=10,
    cursor="arrow", #circle,spider,clock
    font=("Consolas",10)
)
texto.pack(anchor=E)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

texto = Label(ventana, text=pruebas(pais="México",apellidos="Lira",nombre="Luis"))
texto.config(
    justify=RIGHT,
    width=50,
    height=50,
    bg="green",
    padx=10,
    pady=10,
    cursor="arrow", #circle,spider,clock
    font=("Consolas",10)
)
texto.pack(anchor=NW)

ventana.mainloop()