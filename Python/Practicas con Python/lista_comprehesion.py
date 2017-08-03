"""
lista = [] #False


for valor in range(0, 101):
	lista.append(valor)
"""

#Lista [Valor a agraguar y un for]
lista = [ valor for valor in range(0, 101) if valor % 2 == 0]

#tupla
tupla = tuple((valor for valor in range(0, 101) if valor % 2 == 0)) 

#diccionario
diccionario = { indice:valor for indice, valor in enumerate(lista) if indice <= 10}

print(diccionario)