from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'dashboard.html') 

# def profileUsers(request):
#     context = {}
#     return render(request, 'perfilUsuario.html') 

def contactPage(request):
    context =  {}
    return render(request, 'contactoEmp.html')