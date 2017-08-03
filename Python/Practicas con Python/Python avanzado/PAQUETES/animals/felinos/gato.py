from ..animal import Animal

class Gato(Animal):

	#def __new__(cls, nombre):
	#	cls.nombre = nombre
	#	return super().__new__(cls)

	def __init__ (self, nombre):
		self.nombre = nombre