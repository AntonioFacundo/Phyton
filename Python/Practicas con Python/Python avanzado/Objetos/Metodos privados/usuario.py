#se agrega doble guion bajo para 
#hacer un atributo privado __password

class Usuario:
	def __init__ (self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password)
		self.email = email

	def __generar_password(self, password):
		return password.upper()


	#decorador
	@property
	def password(self):
		return self.__password
	
	@password.setter
	def n_password(self, valor):
		self.__password = self.__generar_password(valor)
