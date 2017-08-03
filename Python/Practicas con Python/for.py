lista = (1,2,3,4,5,6,7,8,9,10)


for indice, valor in enumerate(lista):
	print(valor, "tiene el incide", indice)

for valor in range(0, len(lista)):
	print(valor)


diccionario ={'a': 10, 'b': 20, 'c': 30}
for llave, valor in diccionario.items():
	print('la llave', llave, 'tiene el valor de', valor)