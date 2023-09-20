from django.shortcuts import render
from .models import Genero

# Create your views here.
def gamemania(request):
	genero = Genero.objects.all()
	return render(request = request, template_name="main/index.html",context={'genero':genero})
