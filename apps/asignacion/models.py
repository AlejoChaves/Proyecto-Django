from django.db import models

# Create your models here.

from apps.persona.models import Persona
from apps.recurso.models import Recurso


class Asignacion(models.Model):
	codigo =  models.IntegerField(null=True)
	fecha =  models.DateField(null=True)
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE )
	recurso =  models.ManyToManyField(Recurso)


