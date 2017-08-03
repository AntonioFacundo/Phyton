def generador(*args):
	"""
	Recibe n cantidad de numeros y regresa el numero 
	ademas de regresar True o False si el numero es mayor
	o menos a 5
	"""
	for valor in args:
		yield valor, True if valor > 5 else False

decumentacion = generador.__doc__
nombre = generador.__name__
print(nombre, ": ")
print(decumentacion)
 
