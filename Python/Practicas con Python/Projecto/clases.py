class Rectangulo:

	def __init__(self, largo = 5, ancho = 5):
		self.__largo = largo
		self.__ancho = ancho

	#Propiedades
	@property
	def ob_alto(self):
		return self.__largo 

	@property
	def ob_ancho(self):
		return self.__ancho
	
	@property
	def ob_area(self):
		return self.__largo * self.__ancho
		

	@property 
	def ob_perimetro(self):
		if self.__largo == 0 or self.__ancho == 0:
			return 0
		else:
			return (self.__largo * 2) + (self.__ancho * 2)

	@ob_alto.setter
	def cambiar_alto(self, valor):
		self.__largo = valor

	@ob_ancho.setter
	def cambiar_ancho(self, valor):
		self.__ancho = valor

	def cambiar_todo(self,alto,ancho):
		self.cambiar_alto = alto
		self.cambiar_ancho = ancho