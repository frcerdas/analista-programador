from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Videojuego
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    categoria = Categoria.objects.all()
    context = {
         'categoria': categoria
    }
    return render(request,'core/index.html',context)

def categorias(request):
    categorias = Categoria.objects.all()
    context = {
         'categorias': categorias
    }
    return render(request,'core/categorias.html',context)

def categoria_detail(request, slug_categoria):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, slug_categoria=slug_categoria)
    videojuegos_por_categoria = Videojuego.objects.filter(categoria=categoria)
    context = {
        'categoria': categoria,
        'categorias': categorias,
        'videojuegos_por_categoria': videojuegos_por_categoria
    }
    return render(request,'core/page-category.html',context)

def add_categoria(request):
    categorias = Categoria.objects.all()
    context = {
         'categorias': categorias
    }
    return render(request,'core/add-categoria.html', context)

def inicio_sesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('campo-nickname')
        contraseña = request.POST.get('campo-password')
        user = authenticate(request, username=usuario, password=contraseña)
        if user is not None:
            login(request, user)
            categoria = Categoria.objects.all()
            context = {
                'categoria': categoria
            }
            return render(request, 'core/index.html',context)
        else:
            context = {
                'error' : 'Error, intente nuevamente'
            }
            return render(request,'core/index.html',context)
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria
        }
    return render(request, 'core/auth/login.html',context)

def cerrar_sesion(request):
    logout(request)
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria
        }
    return render(request, 'core/auth/login.html', context)

def registro(request):
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria
    }
    return render(request, 'core/registro.html', context)

@login_required
def addgame(request):
    return addgame(request, 'core/addgame.html')