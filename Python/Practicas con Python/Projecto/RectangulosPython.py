from clases import Rectangulo
from menu import *

rec = Rectangulo()
elegir = 0

while elegir != 5:
	elegir = menu()

	if elegir == 1:
		dibujar(rec.ob_alto, rec.ob_ancho)
	elif elegir == 2:
		area(rec.ob_area)
		input()
	elif elegir == 3:
		perimetro(rec.ob_perimetro)
		input()
	elif elegir == 4:
		rec.cambiar_todo(int(input("Nuevo largo: \t")), int(input("\nNuevo ancho:\t")))

input()