from django.shortcuts import render, redirect

# Create your views here.

from ordenamiento.models import *
from ordenamiento.forms import *

def index(request):
    parroquias = Parroquia.objects.all()
    informacion_template = {'parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'index.html', informacion_template)

def ver_barrios(request):
    barrios = Barrio.objects.all()
    informacion_template = {'barrios': barrios}
    return render(request, 'view_barrios.html', informacion_template)

def crear_parroquia(request):
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_parroquia.html', diccionario)


def crear_barrio(request):
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(ver_barrios)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_barrio.html', diccionario)

def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_parroquia.html', diccionario)


def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(ver_barrios)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_barrio.html', diccionario)



