course = "Curso"
my_string = "Codigo facilito"

result = "{a} de {b}".format(a = course, b = my_string)
result = result.lower()

"""Busqueda"""
#regresa el valor de la cadena donde está 
#localizado el resultado de busqueda
pos = result.find("codigo")
print(pos)
print(result[9])

#contador de letras
count = result.count("c")
print(count)

#remplazar una letra de la cadena por otra letra
new_string = result.replace("c", "x")
print(new_string)

#split sirve para seccionar la cadena
new_string = result.split(" ")
print(new_string)

print(result)