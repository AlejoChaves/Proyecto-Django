from django import forms
from apps.persona.models import Persona

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona

		fields = [
			'nombre',
			'apellido',
			'direccion',
			'telefono',

		]

		labels = {
			'nombre' : 'Nombre',
			'apellido': 'Apellido',
			'direccion': 'Dirección',
			'telefono': 'Telefono',
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
			'direccion' : forms.TextInput(attrs={'class' : 'form-control'}),
			'telefono' : forms.TextInput(attrs={'class' : 'form-control'}),
		}  
