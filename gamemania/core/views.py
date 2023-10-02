from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Categoria, Videojuego
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

# @role_required('admin')
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

def list_categoria(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'core/list-categorias.html', context)

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

def list_juego(request):
    videojuegos = Videojuego.objects.all()
    context = {
        'videojuegos': videojuegos
    }
    return render(request, 'core/list-juegos.html', context)

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
                'error' : 'Error, intente nuevamente'
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

def registro(request):
    context = {}
    if request.method == 'POST':
        try:
            nombre = request.POST.get('campo-nombre')
            username = request.POST.get('campo-nickname')
            email = request.POST.get('campo-email')
            password = request.POST.get('campo-password')
            password2 = request.POST.get('campo-password-2')
            nacimiento = request.POST.get('campo-fecha-nacimiento')
            direccion = request.POST.get('campo-direccion')
            
            if exists_user(username):
                raise Exception('El Username ya existe')
            
            User.objects.create_user(username=username, first_name=nombre, last_name='null', email=email, password=password)

            # user = User.objects.create_user(username=username, first_name=nombre, last_name='null', email=email, password=password)
            # role = 'cliente'
            # Usuario.objects.create(user=user, role=role, fecha_nacimiento=nacimiento, direccion=direccion)
            
            return render(request, 'core/index.html')
        except Exception as e:
            context = { 'error': e.__str__() }
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria
    }
    return render(request, 'core/registro.html', context)

@login_required
def addgame(request):
    return addgame(request, 'core/addgame.html')