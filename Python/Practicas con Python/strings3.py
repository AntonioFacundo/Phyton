#metodos de string
course = "curso"
my_string = "Codigo facilito"

result = "{a} de {b}".format( b = course, a =my_string)

#dejar todo en string y minusculas 
#y retorna un string diferente al original
result = result.lower()

#lo mismo pero en mayusculas
#result = result.upper()

#metodo title pone el string como un titulo
#sirve para dar formato
result = result.title()

print(result)