

def division(numero_1, numero_2):

	# anidada: tareas complejas pero solo la llama otra funcion
	def validacion():
		return numero_1 > 0 and numero_2 > 0

	if validacion():
		return numero_1 / numero_2

resultado = division(10,0)
print(resultado)