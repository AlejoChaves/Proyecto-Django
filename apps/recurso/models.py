from django.db import models

# Create your models here.

class Recurso(models.Model):


	CATEGORIA_CHOICE = (
	 ('AC', 'Accesorios de computo'),
     ('AS', 'Accesorios de seguridad'),
    )



	codigo = models.CharField(max_length=50)
	categoria = models.CharField( max_length=50, choices=CATEGORIA_CHOICE)
	nombre = models.CharField( max_length=50)
	marca = models.CharField( max_length=50)
	serie = models.CharField( max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)
	

	

