from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.recurso.forms import RecursoForm
from apps.recurso.models import Recurso

# Create your views here.
def index_recurso(request):
	return render(request, 'index.html')

def recurso_view(request):
	if request.method == 'POST':
		form = RecursoForm(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('recurso:index')
	else:
		form = RecursoForm()
	return render(request, 'recurso/recurso_form.html', {'form' : form})

def recurso_list(request):
	recurso = Recurso.objects.all()
	contexto = {'recursos' : recurso}
	return render(request, 'recurso/recurso_list.html', contexto)		