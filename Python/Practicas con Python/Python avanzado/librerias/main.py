from librerias import *

"""Random"""
valor = random.randint(0,10) #el 0 y el 10 se toman

print(valor)

lista = [True, "string", 23, False]

print(lista)

random.shuffle(lista)#intercambia los valores de posicion en la tabla

print(lista)


"""libreria datetime"""
print(datetime.datetime.now())

"""libreria sys"""
for i in range(100):
	time.sleep(0.5)
	sys.stdout.write("\r%d %%" % i)
	sys.stdout.flush()