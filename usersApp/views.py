from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Usuario,Producto,CategoriaProducto

def validacionesProd(producto):
    try:
        int(producto.precio)
        int(producto.stock)
        str(producto.nombre)
        return True
    except Exception:
        return False


def index(request):
    listAristas = Usuario.objects.exclude(id_prof = None)[:6]
    listCategs = CategoriaProducto.objects.all()

    context = {
        'listArtists': listAristas,
        'listCategs' : listCategs,
    }
    return render(request, 'general/dashboard.html', context) 

# def profileUsers(request):
#     context = {}
#     return render(request, 'perfilUsuario.html') 

def contactPage(request):
    listCategs = CategoriaProducto.objects.all()

    context = {
        'listCategs' : listCategs,
    }
    return render(request, 'contactoEmp.html', context)

def verPerfil(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    listCategs = CategoriaProducto.objects.all()

    context = {
        'listCategs' : listCategs,
        'user':usuario
    }
    return render(request, 'perfilUsuario.html',context)

def productPage(request, categ):
    categ = CategoriaProducto.objects.get(nombre = categ)

    try:
        listProds = Producto.objects.get(id_categ_prod = categ.id_categ_prod)
    except Exception:
        print("error en query no existe registros")
        listProds = None

    listCategs = CategoriaProducto.objects.all()

    context = {
        'listCategs' : listCategs,
        'listProds' : listProds,
        'categoria' : categ,
    }

    return render(request,'product/listProduct.html', context)

@login_required
def regProduct(request):
    listCategs = CategoriaProducto.objects.all()
    curUser = User.objects.get(username = request.user)

    context = {
        'listCategs' : listCategs,
        'userSession' : curUser,
    }

    if request.method == 'POST':
        nombreProd = request.POST['nombre']
        precioProd = request.POST['precio']
        stockProd = request.POST['stock']
        imgProd = request.POST['idCategProd']
        idCategProd = request.POST['imgPicker']
        idUser = curUser.id_usuario

        newProduct = Producto.objects.create(
            nombre = nombreProd,
            precio = precioProd,
            stock = stockProd,
            img_producto = imgProd,
            id_categ_prod = idCategProd,
            id_usuario = idUser
        )

        if validacionesProd(newProduct):
            newProduct.save()
            context += {
                'msgResultadoInsert':'Se ha ingresado correctamente!'
            }
            return render(request, 'product/addProduct.html',context)    
        else:
            context += {
                'msgResultadoInsert' : 'No se ha podido ingresar correctamente'
            }
            return render(request, 'product/addProduct.html',context)
    else:
        return render(request, 'product/addProduct.html', context)

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
        else:
            context = {
                'msgLogin' : 'Error al iniciar sesión, intenta nuevamente'
            }
            return render(request, 'general/sessionPage.html', context)
    else:
        return render(request,'general/sessionPage.html')
    
def logoutSession(request):
    context = {}

    logout(request)
    return redirect('dashboard')

def registerUser(request):
    context = {}
    username = request.POST["username"]
    first_name = request.POST["firstName"]
    last_name = request.POST["lastName"]
    email = request.POST["email"]
    password = request.POST["password"]
    confPassword = request.POST["confPassword"]

    if password != confPassword:
        context = {
            'msgErrorPass' : '¡Las contraseñas deben coincidir!' 
        }
        return render(request,'general/sessionPage.html',context)

    user = User.objects.create (
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,  
            is_active = True
        )

    user.save()        
    # userLogin = authenticate(username = username, password = password)
    # login(request, userLogin)
    return redirect('dashboard')