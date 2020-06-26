from django.conf.urls import url
from django.urls import path
from . import views
from . import casilla
from . import candidato
from . import funcionario
from . import eleccion
from . import rol
urlpatterns = [
     path('', views.index, name='index'),

     path('casilla/listar', casilla.listar, name='listarCasillas'),
     path('casilla/agregar',casilla.agregar, name='agregarCasillas'),
     path('casilla/editar/<int:id>',casilla.editar, name='editarCasillas'),
     path('casilla/eliminar/<int:id>',casilla.eliminar, name='eliminarCasillas'),

     path('candidato/listar',candidato.listar, name='listarCandidatos'),
     path('candidato/agregar',candidato.agregar, name='agregarCandidatos'),
     path('candidato/editar/<int:id>',candidato.editar, name='editarCandidatos'),
     path('candidato/eliminar/<int:id>',candidato.eliminar, name='eliminarCandidatos'),

     path('funcionario/listar',funcionario.listar, name='listarFuncionarios'),
     path('funcionario/agregar',funcionario.agregar, name='agregarFuncionarios'),
     path('funcionario/editar/<int:id>',funcionario.editar, name='editarFuncionarios'),
     path('funcionario/eliminar/<int:id>',funcionario.eliminar, name='eliminarFuncionarios'),


     path('eleccion/listar',eleccion.listar, name='listarElecciones'),
     path('eleccion/agregar',eleccion.agregar, name='agregarElecciones'),
     path('eleccion/editar/<int:id>',eleccion.editar, name='editarElecciones'),
     path('eleccion/eliminar/<int:id>',eleccion.eliminar, name='eliminarElecciones'),

     path('rol/listar',rol.listar, name='listarRoles'),
     path('rol/agregar',rol.agregar, name='agregarRoles'),
     path('rol/editar/<int:id>',rol.editar, name='editarRoles'),
     path('rol/eliminar/<int:id>',rol.eliminar, name='eliminarRoles'),
]





































