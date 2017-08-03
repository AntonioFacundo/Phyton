import sqlite3

def insertar():
	db1 = sqlite3.connect('novelas.db')

	print("Estas en la funcion insertar")

	nombre1 = str(input("Escribe el titulo"))
	autor1 = input("Escribe el autor")
	year1 = str( input("Digita el anio de la novela"))

	consulta = db1.cursor()

	str_consulta = ('INSERT INTO tabla (nombre, autor, year) VALUES (?,?,?)', (+nombre1+), (+autor1+), (+year1+))


	

	print(str_consulta)
	consulta.execute(str_consulta)
	consulta.close()
	db1.commit()
	db1.close()

insertar()
input()