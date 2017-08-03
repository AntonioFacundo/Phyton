from django.db import models

# Create your models here.

class Usuario(models.Model):

	nombre = models.CharField(max_length = 50, primary_key = True)
	apellido = models.CharField(max_length = 50)
	edad = models.IntegerField()
	email = models.EmailField()