#Decoradores 
#	aumentar la funcionalidad
#	A, B, C son funciones
#	A reciba como parametro B para poder crear C

def decorador(is_valid = False):

	def _decorador(func): #A, B

		def before_func():
			#Agregue código
			print("Antes de funcion")

		def after_func():
			#Agregue código
			print("despues de funcion")

		def nueva_funcion(*args, **kwargs):
			if is_valid == True:
				before_func()
			result = func(*args, **kwargs)
			after_func()

			return result 
		return nueva_funcion #C

	return _decorador



@decorador()
def suma(numero_1, numero_2):
	return numero_1 + numero_2

@decorador()
def saluda():
	print("Hola Mundo")

saluda()

resultado = suma(10,10)
print(resultado)
input()