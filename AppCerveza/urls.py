from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('cargar_cerveza/', cargar_cerveza),
    path('cargar_ginebra', cargar_ginebra),
    path('cargar_mezcal', cargar_mezcal),
    path('buscar_cerveza/', buscar_cervezas),
    path('buscar_ginebra/', buscar_ginebra),
    path('buscar_mezcal/', buscar_mezcal),
    path('resultados_cerveza/', resultado_cervezas),
    path('resultados_ginebra/', resultado_ginebra),
    path('resultados_mezcal/', resultado_mezcal),
]
