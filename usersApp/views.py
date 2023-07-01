from django.shortcuts import render
from .models import Usuario

def index(request):
    listAristas = Usuario.objects.f
    context = {}
    return render(request, 'dashboard.html') 

# def profileUsers(request):
#     context = {}
#     return render(request, 'perfilUsuario.html') 

def contactPage(request):
    context =  {}
    return render(request, 'contactoEmp.html')