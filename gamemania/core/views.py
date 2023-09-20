from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'index.html')

def fps(request):
    return render(request,'fps.html')

def deportes(request):
    return render(request,'deportes.html')

def aventura(request):
    return render(request,'aventura.html')

def ingenio(request):
    return render(request,'ingenio.html')

def rpg(request):
    return render(request,'rpg.html')

def login(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'registro.html')

def addgame(request):
    return render(request,'add-game.html')