from tkinter import *
from PIL import ImageTk, Image

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy Luis!!").pack(anchor=W)

imagen = Image.open('./imagenes/portada_linkedin_1.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()