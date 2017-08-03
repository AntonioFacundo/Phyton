from django.db import models


# Create your models here.

class Inventario(models.Model):
	nombre = models.CharField(max_length = 50)
	numero = models.IntegerField()
	precio = models.IntegerField()
