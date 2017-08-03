my_string = 'hola mundo! "Antonio"'

#string para saltos de linea
my_string = """String con saltos
de linea.\nAdios"""

course = "Python 3"
name = "Eduardo"

#concatenar 1
final_message = course + " " + name

#concatenar 2
final_message = "Nuevo curso de %s por %s" %(course, name)

#contatenar 3 recomendada
final_message = "nuevo curso de {} por {}".format(course, name)

print(final_message)