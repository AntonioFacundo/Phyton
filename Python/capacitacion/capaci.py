from abc import ABCMeta, abstractmethod

class Persona:
	__metaclass__ = ABCMeta

	@abstractmethod
	def hablar(self): pass

class Deportista(Persona):

	def __init__(self, edad, nombre, deporte):
		self.__edad = edad
		self.nombre = nombre
		self.__deporte = deporte
		print(self.nombre, self.__edad)


	def __ver_deporte(self):
		return self.__deporte

	def hace_deporte(self):
		print(self.nombre, "voy a practicar", self.__ver_deporte())

	def hablar(self,*palabras):
		for frase in palabras:
			print (frase)


luis = Deportista(13, "Luis", "fut")
luis.hablar("ljasdhlaskjd")
luis.hace_deporte()
