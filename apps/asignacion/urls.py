from django.urls import path

from apps.asignacion.views import index_asignacion, asignacion_view, asignacion_list, asignacion_detail

app_name = "asignacion"

urlpatterns = [
   path('', index_asignacion, name='index'), 
   path('nuevo', asignacion_view, name='asignacion_crear'),
   path('listar', asignacion_list, name='asignacion_listar'),
   path('detalle/<int:id_asignacion>', asignacion_detail, name='asignacion_detalle'),
]