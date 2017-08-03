def escritura(datoa, datob, datoc):
	prueba = open('datos.py','w')
	prueba.write(datoa)
	prueba.write(datob)
	prueba.write(datoc)
	print("\nescritura\n")

	prueba.close

escritura( "hola",
			'Mundo',
			'shido'
	)

def lectura():
	prueba = open("datos.py", 'r')
	print(prueba.read())
	prueba.close()
lectura()