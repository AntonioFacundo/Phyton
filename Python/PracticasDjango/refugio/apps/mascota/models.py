from django.db import models

from apps.adopcion.models import Persona

# Create your models here.
#argumentos del la funcion foreignKey(tabla relacionada, valores nulos, permite guardar sin ingresar ningun dato
#	en ese campo, al eliminar una campo de la tabla relacionada elimina todo lo que tenga relacion con esta tabla)
#foreignKey se utiliza para un campo que se relaciona a muchos de una segunda tabla

#Para poder hacer que solo tenga relacion con un solo objeto de la segunda tabla
#se utiliza la funcion OneToOneField y tiene los mismos argumentos

#relaciones de muchos a muchos 
#cada campo de cada tabla puede tener muchas relaciones entre ellas
#se utiliza la tabla ManyToManyField de argumento solo la tabla relacionada

class Vacuna(models.Model):
	nombre = models.CharField(max_length = 50)

class Mascota(models.Model):
	nombre = models.CharField(max_length = 50)
	sexo = models.CharField(max_length = 10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	persona = models.ForeignKey(Persona, null = True, blank = True, on_delete = models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna, blank=True)


