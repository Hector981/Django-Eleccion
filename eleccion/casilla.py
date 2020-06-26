from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Casilla
from .forms import CasillaForm

def listar(request):
    lista_casilla = Casilla.objects.order_by('id')
    return render(request, 'casilla/casilla_listar.html',context= {'lista_casilla':lista_casilla})

def agregar(request):
    form = CasillaForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('listarCasillas')
    return render(request,'casilla/casilla_form.html', context= {'form': form})

def editar(request, id):
    lista_editar = Casilla.objects.get(id=id)
    form = CasillaForm(request.POST or None, instance=lista_editar)
    if  form.is_valid():
        form.save()
        return redirect('listarCasillas')
    return render(request, 'casilla/casilla_editar.html', context= {'form': form, 'lista_editar': lista_editar})

def eliminar(request,id):
    lista_eliminar = Casilla.objects.get(id=id)
    lista_eliminar.delete()  
    return redirect('listarCasillas')
# listado = Casilla.objects.order_by('ubicacion')
# salida = '<br>'.join([q.ubicacion for q in listado])
# return HttpResponse(salida)
