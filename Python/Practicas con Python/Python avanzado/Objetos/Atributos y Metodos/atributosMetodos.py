class Lapiz:
	

	#Metodos
	color = "amarillo"
	contiene_borrador = False
	usa_grafito = True 

	#metodo __init__

	def __init__(self, color = "verde", contiene_borrador = False, usa_grafito = False): #valores por default
		#Atributos
		self.color = color
		self.contiene_borrador = contiene_borrador
		self.susa_grafito = usa_grafito 

	def dibujar(self):
		print("el lapiz esta dibujando")

	def borrar(self):
		if self.es_valido_para_borrar():
			print("El lapiz esta borrando")
		else:
			print("no es posible borrar")
		

	def es_valido_para_borrar(self):
		return self.contiene_borrador #para acceder a un atributo en una funcion
