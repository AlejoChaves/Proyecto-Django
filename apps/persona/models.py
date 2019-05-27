from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField( max_length=50)
	direccion = models.CharField(max_length=50, null=True)
	telefono =  models.CharField(max_length=50, null=True)

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)



	

