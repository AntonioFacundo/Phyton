#metodos magicos

class Usuario:
	def __new__(cls):#Primero
		print("Este es el primero")
		return super().__new__(cls)

	def __init__(self):#Segundo
		print("este es el segundo")

	def __str__(self):
		print("se imprime cuando intento mostrar el objeto")

	def __getattr__(self, nombre):
		print("Aqui mostramos que no se encontro el atributo")
		self.otros_metodos()

	def otros_metodos(self):
		print("otro metodo")

usuario = Usuario()
print(usuario.apellido)