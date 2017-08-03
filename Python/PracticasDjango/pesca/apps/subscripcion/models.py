from django.db import models
from apps.inventario.models import Inventario

# Create your models here.

class Persona(models.Model):
	folio = models.CharField(max_length = 50, primary_key = True)
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	telefono = models.CharField(max_length = 12)
	dinero = models.IntegerField()
	email = models.EmailField()
	domicilio = models.TextField()
	compra = models.ManyToManyField(Inventario, blank = True)
