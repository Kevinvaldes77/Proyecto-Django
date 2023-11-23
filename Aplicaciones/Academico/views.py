from django.shortcuts import render, redirect
from .models import Ficha
from django.contrib import messages

# Create your views here.

def home(request):
    fichas = Ficha.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request, "gestionFichas.html", {"fichas": fichas})

def registrarCurso(request): 
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    ficha=Ficha.objects.create(
    codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Cursos Registrado!')
    return redirect('/')

def edicionFicha(request, codigo): 
    ficha = Ficha.objects.get(codigo=codigo)
    return render(request, "edicionFicha.html", {"ficha":ficha})

def editarFicha(request): 
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    ficha = Ficha.objects.get(codigo=codigo)
    ficha.nombre = nombre
    ficha.creditos = creditos
    ficha.save()
    messages.success(request, '¡Cursos Actualizado!')
    return redirect('/')




def eliminarFicha(request, codigo):
    ficha = Ficha.objects.get(codigo=codigo)
    ficha.delete()

    messages.success(request, '¡Cursos Eliminado!')

    return redirect('/')

    