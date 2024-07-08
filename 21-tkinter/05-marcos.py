from tkinter import *

ventana = Tk()
ventana.title("Marcos en python con Tkinter")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250,height=250)
marco_padre.pack(side=BOTTOM,fill=X,expand=YES,anchor=S)

marco = Frame(marco_padre, width=250,height=250)
marco.config(bg="red",bd=6,relief="solid")
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(bg="red",fg="white",font=("Arial",20))
texto.pack(anchor=CENTER,fill=Y,expand=YES)

marco = Frame(marco_padre, width=250,height=250)
marco.config(bg="green",bd=6,relief="solid")
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250,height=250)
marco_padre.pack(side=TOP,fill=X,expand=YES,anchor=N)

marco = Frame(marco_padre, width=250,height=250)
marco.config(bg="blue",bd=6,relief="solid")
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=250,height=250)
marco.config(bg="orange",bd=6,relief="solid")
marco.pack(side=RIGHT)

ventana.mainloop()