from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.asignacion.forms import AsignacionForm
from apps.asignacion.models import Asignacion

# Create your views here.
def index_asignacion(request):
	return render(request, 'index.html')

def asignacion_view(request):
	if request.method == 'POST':
		form = AsignacionForm(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('asignacion:index')
	else:
		form = AsignacionForm()
	return render(request, 'asignacion/asignacion_form.html', {'form' : form})	


def asignacion_list(request):
	asignacion = Asignacion.objects.order_by('fecha')
	contexto = {'asignaciones' : asignacion}
	return render(request, 'asignacion/asignacion_list.html', contexto)	


def asignacion_detail(request, id_asignacion):
	asignacion = Asignacion.objects.get(id=id_asignacion)
	context = {'asignacion' : asignacion}
	return render(request, 'asignacion/detalleasignacion.html', context)	


