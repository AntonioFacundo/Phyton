def suma(numero_1, numero_2, numero_3):
	return numero_1 + numero_2 + numero_3

def division(numero_1, numero_2):
	if numero_2 == 0:
		return "no se puede dividir entre 0"
	else:
		return numero_1 / numero_2

def multiplicacion(numero_1, numero_2 = 100):
	return numero_1 * numero_2

def multiples_valores():
	return "string", 3, 3.4, True

def mostrar_resultado(funcion):
	print(funcion(5,6))

a = int(input("Valor 1:\t"))
b = int(input("Valor 2:\t"))
c = int(input("Valor 3:\t"))

resultado = suma(a, b, c)

print(resultado)

resultado = division(a, b)

print(resultado)

resultado = multiplicacion(a, b)

print(resultado)

string, entero, flotante, booleano = multiples_valores()

print(string)
print(entero)
print(flotante)
print(booleano)

mi_variable = multiplicacion
mostrar_resultado(mi_variable)

input()