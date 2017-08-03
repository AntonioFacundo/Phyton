from tkinter import *

class Interfaz:
	def __init__(self, contenedor):
		self.e1 = Label(contenedor, text = "Etiqueta 1", fg = "black", bg = "white")
		self.e2 = Label(contenedor, text = "Etiqueta 2", fg = "black", bg = "gray")
		self.e3 = Label(contenedor, text = "Etiqueta 3", fg = "black", bg = "green")
		self.e4 = Label(contenedor, text = "Etiqueta 4", fg = "black", bg = "white")
		self.e5 = Label(contenedor, text = "Etiqueta 5", fg = "black", bg = "gray")
		self.e6 = Label(contenedor, text = "Etiqueta 6", fg = "black", bg = "green")

		self.e1.place(x = 20, y = 30, width = 120, height = 25)
		self.e2.place(x = 40, y = 80)

ventana = Tk()

mi_interfaz = Interfaz(ventana)
ventana.mainloop()