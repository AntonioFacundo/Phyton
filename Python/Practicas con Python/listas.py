#se igualan a parentecis cuadrados
my_list = ["strings", 15, 15.7, True]

#agregar al final
#el parametro es lo que se agregara
my_list.append(6)

#insertar 
#resive 2 parametros 
#el primero para el lugar y el segundo lo que insertamos
my_list.insert(3, "insertar")
print(my_list[3])

#remover de la lista
my_list.remove(15)

#pop sirve para tomar el ultimo valor y eliminarlo
last_value = my_list.pop()
print(last_value)

print(my_list)


my_list_number = [10, 8, 9, 4, 5, 3, 1, 2]
my_list_number2 = [22, 25]

print(my_list_number)
my_list_number.sort()
print(my_list_number)

my_list_number.sort(reverse = True)
print(my_list_number)

#si se utiliza append se almacena una lista dentro 
#de la lista
my_list_number.extend(my_list_number2)

print(my_list_number)

