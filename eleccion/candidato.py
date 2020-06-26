from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Candidato
from .forms import CandidatoForm

def listar(request):
    lista_candidato = Candidato.objects.order_by('id')
    return render(request, 'candidato/candidato_listar.html',context= {'lista_candidato':lista_candidato})

def agregar(request):
    form = CandidatoForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect('listarCandidatos')
    return render(request,'candidato/candidato_form.html', context= {'form': form})

def editar(request, id):
    lista_editar = Candidato.objects.get(id=id)
    form = CandidatoForm(request.POST or None, instance=lista_editar)
    if  form.is_valid():
        form.save()
        return redirect('listarCandidatos')
    return render(request, 'candidato/candidato_editar.html', context= {'form': form, 'lista_editar': lista_editar})

def eliminar(request,id):
    lista_eliminar = Candidato.objects.get(id=id)
    lista_eliminar.delete()  
    return redirect('listarCandidatos')

# listado = Candidato.objects.order_by('nombrecompleto')
# salida = '<br>'.join([q.ubicacion for q in listado])
# return HttpResponse(salida)
