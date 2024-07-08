from tkinter import *

ventana = Tk()
#ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
            fg="white",
            bg="#000000",
            padx="320",
            pady="20",
            font=("Consolas",30)
)
texto.pack(side=TOP)

texto = Label(ventana, text="Soy Luis Armando Lira")
texto.config(
    justify=RIGHT,
    width=10,
    height=10,
    bg="orange",
    padx=10,
    pady=10,
    cursor="arrow", #circle,spider,clock
    font=("Consolas",10)
)
texto.pack(side=TOP,fill=X,expand=YES)


texto = Label(ventana, text="Hola")
texto.config(
    justify=RIGHT,
    width=10,
    height=10,
    bg="green",
    padx=10,
    pady=10,
    cursor="arrow", #circle,spider,clock
    font=("Consolas",10)
)
texto.pack(side=LEFT,fill=X,expand=YES)

texto = Label(ventana, text="Hola 2")
texto.config(
    justify=RIGHT,
    width=10,
    height=10,
    bg="red",
    padx=10,
    pady=10,
    cursor="arrow", #circle,spider,clock
    font=("Consolas",10)
)
texto.pack(side=LEFT,fill=X,expand=YES)

texto = Label(ventana, text="Hola 3")
texto.config(
    justify=RIGHT,
    width=10,
    height=10,
    bg="blue",
    padx=10,
    pady=10,
    cursor="arrow", #circle,spider,clock
    font=("Consolas",10)
)
texto.pack(side=LEFT,fill=X,expand=YES)

ventana.mainloop()