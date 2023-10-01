from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Videojuego
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
	categoria = Categoria.objects.all()
	return render(request = request, template_name="main/index.html",context={'categoria':categoria})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

def categoria_detail(request, slug_categoria):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, slug_categoria=slug_categoria)
    videojuegos_por_categoria = Videojuego.objects.filter(categoria=categoria)
    return render(request, 'main/page-category.html', {'categoria': categoria, 'categorias': categorias, 'videojuegos_por_categoria': videojuegos_por_categoria})

def inicio_sesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('campo-nickname')
        contraseña = request.POST.get('campo-password')
        user = authenticate(request, username=usuario, password=contraseña)
        if user is not None:
            login(request, user)
            categoria = Categoria.objects.all()
            return render(request = request, template_name="main/index.html",context={'categoria':categoria})
        else:
            context = {
                'error' : 'Error, intente nuevamente'
            }
            return render(request, 'main/auth/login.html', context)
    categoria = Categoria.objects.all()
    return render(request, 'main/auth/login.html',context={'categoria':categoria})

def registro(request):
    categoria = Categoria.objects.all()
    return render(request, 'main/registro.html',context={'categoria':categoria})

@login_required
def addgame(request):
     return addgame(request, 'main/addgame.html')