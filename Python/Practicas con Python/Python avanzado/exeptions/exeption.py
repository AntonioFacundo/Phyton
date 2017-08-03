try:#intenta
	print(2/0)
except ZeroDivisionError as ex:#si no se puede
	print(ex)
	print("No se puede dividir entre 0")
finally:#siempre se ejecuta
	print("finally")

print("\n\n")

try:
	lista = [1,2]
	print(lista [9])
except Exception as e:
	print(e)

print("se termino el script")