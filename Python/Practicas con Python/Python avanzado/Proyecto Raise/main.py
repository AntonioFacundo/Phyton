class TinyIntError(Exception):
	def __init__(self):
		self.message = "El numero no es tiny"

	def __str__(self):
		return self.message

def tiny_int(val):
	return val >= 0 and val <= 255

numero = 400

try:
	if tiny_int(numero):
		print("El numero es correcto")
	else: 
		raise TinyIntError()
except TinyIntError as error:
	print(error)