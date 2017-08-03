mi_funcion = lambda numero_1, numero_2: numero_1 + numero_2

formato = lambda sentencia: '¿{}?'.format(sentencia)

pregunta = formato("Puedes hacer esto una pregunta")

resultado = mi_funcion(10, 30)
print(resultado)
print(pregunta)
input()