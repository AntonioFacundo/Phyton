def factorial_numero(numero):
	factorial = 1

	while numero > 0:
		factorial *= numero
		numero -= 1
	return factorial

a = int(input("Ingrese un numero:\t"))

result = factorial_numero(a)
print(result)
input()