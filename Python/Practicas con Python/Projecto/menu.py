import sys
import os

def menu():
	elegir = 1

	os.system("cls")
	print("---Seleccione un numero\nRectangulo por defecto 5 x 5")
	print("\n\n")
	print("1.- Dibujar el rectangulo\n")
	print("2.- Obtener su area\n")
	print("3.- Obtener su perimetro\n")
	print("4.- Cambiar dimensiones\n")
	print("5.- Salir\n")

	elegir = int(input("Elegir:\t"))

	while elegir < 1 or elegir > 5:
		elegir = int(input("Elegir un numero entre del 1 al 5:\t"))
	
	return elegir

def dibujar(alto, ancho):

	print("\n\n")

	for valor_1 in range(0, alto):
		for valor_2 in range (0,ancho):
			sys.stdout.write("><")
		sys.stdout.write("\n")
	print("\n")
	input()

def area(valor):
	print("\nEl area del rectangulo es:", valor)
	print("\n")

def perimetro(valor):
	print("\nEl perimetro del rectangulo es:", valor)
	print("\n")