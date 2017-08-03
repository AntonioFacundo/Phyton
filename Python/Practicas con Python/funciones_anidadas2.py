#CLosure
#funciones que crea funciones 
def crear_funcion(numero_1, numero_2):

	# anidada: tareas complejas pero solo la llama otra funcion
	def validacion():
		print("se ejecuta validacion")
		return numero_1 > 0 and numero_2 > 0

	return validacion


def aplicar_funcion(func):
	func()

nueva_funcion = crear_funcion(10, 10)

aplicar_funcion(nueva_funcion)
#algoritmo

print(aplicar_funcion)
input()