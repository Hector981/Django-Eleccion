from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Funcionario
from .forms import FuncionarioForm

def listar(request):    
    lista_funcionario= Funcionario.objects.order_by('id')    
    return render(request, 'funcionario/funcionario_listar.html',context= {'lista_funcionario':lista_funcionario}) 

def agregar(request):
    form = FuncionarioForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('listarFuncionarios')
    return render(request,'funcionario/funcionario_form.html', context= {'form': form})

def editar(request, id):
    lista_editar = Funcionario.objects.get(id=id)
    form = FuncionarioForm(request.POST or None, instance=lista_editar)
    if  form.is_valid():
        form.save()
        return redirect('listarFuncionarios')
    return render(request, 'funcionario/funcionario_editar.html', context= {'form': form, 'lista_editar': lista_editar})

def eliminar(request,id):
    lista_eliminar = Funcionario.objects.get(id=id)
    lista_eliminar.delete()  
    return redirect('listarFuncionarios')

# listado = Funcionario.objects.order_by('nombrecompleto')    
# salida = '<br>'.join([q.nombrecompleto for q in listado])    
# return HttpResponse(salida)