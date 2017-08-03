#import calculadora
#from calculadora import *
from calculadora import (suma as sumita, 
						resta, 
						multi, 
						divi)


#respuesta = calculadora.suma(10,10,10,10)
respuesta_s = sumita(20,40)
respuesta_r = resta(1,3,4,5)
respuesta_m = multi(2,3,2)
respuesta_d = divi(20,2,2)

print(respuesta_s)
print(respuesta_r)
print(respuesta_m)
print(respuesta_d)

from calculadora import __name__ as __name__calcu__

print(__name__)
print(__name__calcu__)

"""sirve para evitar que funciones se ejecuten
en un modulo importado si estan en el primer nivel
de identacion
"""
#if __name__ == '__main__': #Es este el script princpipal?

