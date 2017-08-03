class Circulo:

	#variable de clase
	#las variables de clase no pueden hacerse privadas
	#estan propensas a cambios
	#se les agrega un guion bajo para que nadie las cambie
	_pi = 3.1416

	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return self.radio * self.radio * self._pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(circulo_uno.radio)
print(circulo_dos.radio)
print(circulo_uno.area())
Circulo._pi = 2
print(Circulo._pi)

#muestra todos los atributos del objeto
#no los de la clase
#print(circulo_uno.__dict__)

#property
def foo(self):
    return self._foo
@foo.setter
def foo(self, value):
    self._foo = value
