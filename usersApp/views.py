from django.shortcuts import render
from .models import Usuario

def index(request):
    listAristas = Usuario.objects.exclude(id_prof = None)[:6]
    context = {
        'listArtists': listAristas,
    }
    return render(request, 'dashboard.html', context) 

# def profileUsers(request):
#     context = {}
#     return render(request, 'perfilUsuario.html') 

def contactPage(request):
    context =  {}
    return render(request, 'contactoEmp.html')

def verPerfil(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    context = {
        'user':usuario
    }
    return render(request, 'perfilUsuario.html',context)