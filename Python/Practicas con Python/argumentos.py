#cuando no sabemos cuantos argumentos necesitaremos

#para muchos argumentos
def suma (*args):
	resultado = 0
	for valor in args:
		resultado += valor
	return resultado

#para poner muchos argumentos de parametros
def suma_shida (**kwargs):
	valor = kwargs.get('valor', 'No contiene valor')
	print(valor)

resultado = suma(10, 10, 10, 10)
print(resultado)

suma_shida(10,10)

# * -> n valores -> tuplas
# ** -> n valores -> diccionarios