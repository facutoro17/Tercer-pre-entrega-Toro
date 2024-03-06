from django.shortcuts import render
from .models import *
from .forms import *

def inicio(request):
    return render(request, "AppCerveza/inicio.html")

def cargar_cerveza(request):
    if request.method == "POST":
        formulario = formulario_Cerveza(request.POST)
        if formulario.is_valid():

            info_dicc = formulario.cleaned_data
            nueva_cerveza = Cerveza(marca = info_dicc["marca"],
                                    color = info_dicc["color"],
                                    ibu = info_dicc["ibu"],
                                    alcohol = info_dicc["alcohol"],
                                    cantMl = info_dicc["cantMl"])
            nueva_cerveza.save()

            return render(request, "AppCerveza/inicio.html")
    else:
        formulario = formulario_Cerveza()

    return render(request, "AppCerveza/cargar_cerveza.html", {"form":formulario})

def cargar_ginebra(request):
    if request.method == "POST":
        formulario = formulario_Ginebra(request.POST)
        if formulario.is_valid():

            info_dicc = formulario.cleaned_data
            nueva_ginebra = Ginebra(marca = info_dicc["marca"],
                                    sabor = info_dicc["sabor"],
                                    alcohol = info_dicc["alcohol"],
                                    cantMl = info_dicc["cantMl"])
            nueva_ginebra.save()

            return render(request, "AppCerveza/inicio.html")
    else:
        formulario = formulario_Ginebra()
    return render(request, "AppCerveza/cargar_ginebra.html", {"form":formulario})

def cargar_mezcal(request):
    if request.method == "POST":
        formulario = formulario_Mezcal(request.POST)
        if formulario.is_valid():

            info_dicc = formulario.cleaned_data
            nuevo_mezcal = Mezcal(marca = info_dicc["marca"],
                                    tipoAgave = info_dicc["tipoAgave"],
                                    clasificacion = info_dicc["clasificacion"],
                                    alcohol = info_dicc["alcohol"],
                                    cantMl = info_dicc["cantMl"])
            nuevo_mezcal.save()

            return render(request, "AppCerveza/inicio.html")
    else:
        formulario = formulario_Mezcal()
    return render(request, "AppCerveza/cargar_mezcal.html", {"form":formulario})

def buscar_cervezas(request):
    return render(request, "AppCerveza/buscar_cerveza.html")

def buscar_ginebra(request):
    return render(request, "AppCerveza/buscar_ginebra.html")

def buscar_mezcal(request):
    return render(request, "AppCerveza/buscar_mezcal.html")

def resultado_cervezas(request):
    marca = request.GET["marca"]
    resultado = Cerveza.objects.filter(marca__iexact=marca)
    return render(request, "AppCerveza/resultados_cerveza.html", {"resultado_cerveza":resultado})

def resultado_ginebra(request):
    marca = request.GET["marca"]
    resultado = Ginebra.objects.filter(marca__iexact=marca)
    return render(request, "AppCerveza/resultados_ginebra.html", {"resultado_ginebra":resultado})

def resultado_mezcal(request):
    marca = request.GET["marca"]
    resultado = Mezcal.objects.filter(marca__iexact=marca)
    return render(request, "AppCerveza/resultados_mezcal.html", {"resultado_mezcal":resultado})

