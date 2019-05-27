from django import forms
from apps.recurso.models import Recurso


class RecursoForm(forms.ModelForm):
	class Meta:
		model = Recurso

		fields = [
			'codigo',
			'categoria',
			'nombre',
			'marca',
			'serie',

		]

		labels = {
			'codigo' : 'Codigo',
			'categoria' : 'Categoria',
			'nombre' : 'Nombre',
			'marca' : 'Marca',
			'serie' : 'Serie',
		}

		widgets = {
			'codigo' : forms.TextInput(attrs={'class' : 'form-control'}),
			'categoria' : forms.Select(attrs={'class':'form-control'}),
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'marca' : forms.TextInput(attrs={'class' : 'form-control'}),
			'serie' : forms.TextInput(attrs={'class' : 'form-control'}),
		}  