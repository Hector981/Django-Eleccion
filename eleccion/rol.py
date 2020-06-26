from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Rol
from .forms import RolForm

def listar(request):
    lista_rol = Rol.objects.order_by('id')
    return render(request, 'rol/rol_listar.html',context= {'lista_rol':lista_rol})

def agregar(request):
    form = RolForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('listarRoles')
    return render(request,'rol/rol_form.html', context= {'form': form})

def editar(request, id):
    lista_editar = Rol.objects.get(id=id)
    form = RolForm(request.POST or None, instance=lista_editar)
    if  form.is_valid():
        form.save()
        return redirect('listarRoles')
    return render(request, 'rol/rol_form.html', context= {'form': form, 'lista_editar': lista_editar})

def eliminar(request,id):
    lista_eliminar = Rol.objects.get(id=id)
    lista_eliminar.delete()  
    return redirect('listarRoles')
# listado = Rol.objects.order_by('descripcion')
# salida = '<br>'.join([q.ubicacion for q in listado])
# return HttpResponse(salida)
