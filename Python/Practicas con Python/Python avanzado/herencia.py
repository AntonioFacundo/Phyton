class Animal:
	@property 
	def terrestre(self):
		return True

class Felino(Animal): #Clase padre
	@property 
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El felino esta cazando")

class Mascota:
	nombre = '' #Las mascotas necesitan nombre

	def mostrar_nombre(self):
		print(self.nombre)
 	
class Gato(Felino, Mascota):
	def mostrar_nombre(self):
		print("El nombre es: {}".format(self.nombre))

class Jaguar(Felino):
	pass

gato = Gato()
gato.nombre = "Gato 1"

print(gato.mostrar_nombre())