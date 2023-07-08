from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Usuario,Producto

def index(request):
    listAristas = Usuario.objects.exclude(id_prof = None)[:6]
    context = {
        'listArtists': listAristas,
    }
    return render(request, 'general/dashboard.html', context) 

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

def producPage(request):
    productList = Producto.objects.all()
    context = {
        'productList': productList,
    }
    return render(request,'productDash.html')

# def sessionPage(request):
#     context = {}
#     return render(request,'general/sessionPage.html')

def loginPage(request):
    context = {}

    if request.method == 'POST':

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
            # ...
        else:
            # Return an 'invalid login' error message.
            messages.success(request,('Error al iniciar sesión, intenta nuevamente'))
            return redirect('loginPage')
            # ...
    else:
        return render(request,'general/sessionPage.html')
    
def logoutSession(request):
    context = {}
    
    logout(request)
    return redirect('dashboard')
