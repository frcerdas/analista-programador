from django.shortcuts import render, get_object_or_404
from .models import Categoria

# Create your views here.
def gamemania(request):
	categoria = Categoria.objects.all()
	return render(request = request, template_name="main/index.html",context={'categoria':categoria})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

def categoria_detail(request, slug_categoria):
    categoria = get_object_or_404(Categoria, slug_categoria=slug_categoria)
    return render(request, 'page-category.html', {'categoria': categoria})