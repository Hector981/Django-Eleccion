from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Eleccion
from .forms import EleccionForm

def listar(request):
    lista_eleccion = Eleccion.objects.order_by('id')
    return render(request, 'eleccion/eleccion_listar.html',context= {'lista_eleccion':lista_eleccion})

def agregar(request):
    form = EleccionForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('listarElecciones')
    return render(request,'eleccion/eleccion_form.html', context= {'form': form})

def editar(request, id):
    lista_editar = Eleccion.objects.get(id=id)
    form = EleccionForm(request.POST or None, instance=lista_editar)
    if  form.is_valid():
        form.save()
        return redirect('listarElecciones')
    return render(request, 'eleccion/eleccion_form.html', context= {'form': form, 'lista_editar': lista_editar})

def eliminar(request,id):
    lista_eliminar = Eleccion.objects.get(id=id)
    lista_eliminar.delete()  
    return redirect('listarElecciones')