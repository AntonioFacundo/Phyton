class Circulo:

	@staticmethod
	def pi ():
	return 3.1416

	#metodo estatico no lleva la palabra self

	def __init__ (self, radio):
		self.radio = radio

	def area(self):
		return self.radio * self.radio * Circulo.pi()

circulo_uno = Circulo(3)

print(circulo_uno.area())