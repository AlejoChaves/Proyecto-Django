from django.urls import path

from apps.persona.views import index, persona_view, persona_list

app_name = "persona"

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', persona_view, name='persona_crear'),
    path('listar', persona_list, name='persona_listar'),
]