from django.urls import path

from apps.recurso.views import index_recurso, recurso_view, recurso_list

app_name = "recurso"

urlpatterns = [
    path('', index_recurso, name='index'),
    path('nuevo', recurso_view, name='recurso_crear'),
    path('listar', recurso_list, name='recurso_listar'),
]