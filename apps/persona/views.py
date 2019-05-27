from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.persona.forms import PersonaForm
from apps.persona.models import Persona

# Create your views here.
def index(request):
	return render(request, 'index.html')

def persona_view(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('persona:index')
	else:
		form = PersonaForm()
	return render(request, 'persona/persona_form.html', {'form' : form})


def persona_list(request):
	persona = Persona.objects.all()
	contexto = {'personas' : persona}
	return render(request, 'persona/persona_list.html', contexto)

			
