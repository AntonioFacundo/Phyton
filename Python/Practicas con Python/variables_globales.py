def palidromo(frase):
	frase_local = frase_global.replace(" ", "") #variable local
	print(frase_local )
	return frase_local == frase_local[::-1]

frase_global = "anita lava la tina"
print(frase_global)
resultado = palidromo(frase_global)
print(frase_global)
print(resultado)

def valor_global():
	global variable_glo
	variable_glo = "cambio"

def mostrar():
	print(variable_glo)

def crear_global():
	global nueva_variable
	nueva_variable = "nueva global"

variable_glo = "sin cambio"

valor_global()
mostrar()