from django import forms
from apps.asignacion.models import Asignacion

class AsignacionForm(forms.ModelForm):
	class Meta:
		model = Asignacion

		fields = [
			'codigo',
			'fecha',
			'persona',
			'recurso',

		]

		labels = {
			'codigo' : 'Codigo',
			'fecha' : 'Fecha',
			'persona' : 'Persona',
			'recurso' : 'Recurso',
		}

		widgets = {
			'codigo' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha' : forms.TextInput(attrs={'class':'form-control'}),
			'persona' : forms.Select(attrs={'class':'form-control'}),
			'recurso' : forms.CheckboxSelectMultiple(),
		}  
