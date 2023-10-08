from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Videojuego
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CategoriaForm, VideojuegoForm
from .decorators import role_required
from .forms import CategoriaForm



# Create your views here.
def inicio(request):
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria
    }
    return render(request,'core/index.html',context)

@staff_member_required
def admin_area(request):
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria
    }
    return render(request,'core/admin-area.html',context)

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

@staff_member_required
def list_categoria(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'core/list-categorias.html', context)

@staff_member_required
def add_categoria(request):
    alert_class = ""
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            alert_class = "success"
            messages.success(request,'La categoría se ha agregado con éxito.')
        else:
            alert_class = "warning"
            messages.error(request, 'Hubo un error al agregar la categoría. Por favor, corrige los errores en el formulario.')
    else:
        form = CategoriaForm()
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'form': form,
        'alert_class': alert_class
    }
    return render(request,'core/add-categoria.html', context)

@staff_member_required
def modify_categoria(request, id):
    categoria = Categoria.objects.get(idCategoria=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría modificada con éxito.')
        else:
            messages.error(request, 'Hubo un error al modificar la categoría. Corrige los errores en el formulario.')
    else:
        form = CategoriaForm(instance=categoria)

    context = {
        'form': form,
        'categoria': categoria,
    }
    return render(request, 'core/update-categoria.html', context)

@staff_member_required
def list_juego(request):
    videojuegos = Videojuego.objects.all()
    context = {
        'videojuegos': videojuegos
    }
    return render(request, 'core/list-juegos.html', context)

@staff_member_required
def add_juego(request):
    alert_class = ""
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            alert_class = "success"
            messages.success(request,'El videojuego ha sido agregada con éxito.')
        else:
            alert_class = "warning"
            messages.error(request, 'Hubo un error al agregar el videojuego. Por favor, corrige los errores en el formulario.')
    else:
        form = VideojuegoForm()
    categorias = Videojuego.objects.all()
    context = {
        'categorias': categorias,
        'form': form,
        'alert_class': alert_class
    }
    return render(request,'core/add-juego.html', context)

@staff_member_required
def modify_juego(request, id):
    videojuego = Videojuego.objects.get(idVideojuego=id)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
            messages.success(request, 'Videojuego modificado con éxito.')
        else:
            messages.error(request, 'Hubo un error al modificar el videojuego. Corrige los errores en el formulario.')
    else:
        form = VideojuegoForm(instance=videojuego)

    context = {
        'form': form,
        'categorias': categorias,
    }
    return render(request, 'core/update-juego.html', context)

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
                'error' : 'Error, intente nuevamente.'
            }
            return render(request,'core/auth/login.html',context)
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

def exists_user(username):
    try:
        User.objects.get(username=username)     
        return True
    except User.DoesNotExist:
        return False

def exists_email(email):
    try:
        User.objects.get(email=email)     
        return True
    except User.DoesNotExist:
        return False

def registro(request):
    if request.user.is_authenticated:
        categoria = Categoria.objects.all()
        context = {
        'categoria': categoria
        }
        return render(request,'core/index.html',context)
    else:
        context = {}
        if request.method == 'POST':
            nombre = request.POST.get('campo-nombre')
            username = request.POST.get('campo-nickname')
            email = request.POST.get('campo-email')
            password = request.POST.get('campo-password')
            password2 = request.POST.get('campo-password-2')
            nacimiento = request.POST.get('campo-fecha-nacimiento')
            direccion = request.POST.get('campo-direccion')
            
            if exists_user(username):
                context = {
                'error' : 'Error, el nombre de usuario ya se encuentra en uso.'
                }
                
            if exists_email(email):
                context = {
                'error' : 'Error, el correo registrado ya se encuentra en uso.'
                }
                return render(request,'core/registro.html',context)
            
            User.objects.create_user(username=username, first_name=nombre, last_name='null', email=email, password=password)
                
            context = {
                    'register' : 'Registro Exitoso! inicie sesión a continuación:'
                }
            return render(request,'core/auth/login.html',context)
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria
    }
    return render(request, 'core/registro.html', context)

@staff_member_required
def addgame(request):
    return addgame(request, 'core/addgame.html')