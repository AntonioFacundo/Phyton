#!/usr/bin/python3

"""
Aqui colocamos todo lo que hace este modulo 
a que contexto le corresponde.
"""

__author__ = "Juan Antonio Facundo Flores"
__copyright__ = "Copyright 2016, Codigo Facilito"
__credits__ = "Codigo Facilito"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Antonio Facundo"
__email__ = "antonio_facundo@outlook.com"
__status__ = "Developer"


def suma(*args):
	resultado = 0
	for valor in args:
		resultado += valor
	return resultado

def resta(*args):
	primero = True
	resultado = 0
	for valor in args:
		if primero == True:
			resultado = valor
			primero = False
		resultado -= valor
	return resultado

def multi(*args):
	resultado = 1
	for valor in args:
		resultado *= valor
	return resultado

def divi(*args):
	primero = True
	contador = 0
	resultado = 0

	for valor in args:

		if primero == True:
			resultado = valor
			primero = False
			continue

		if contador > 0:

			if valor == 0:
				return "no se puede dividir entre 0"

		resultado /= valor
		contador += 1

	return resultado