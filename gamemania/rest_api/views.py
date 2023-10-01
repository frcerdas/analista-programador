from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Categoria, Videojuego
from .serializers import CategoriaSerializers, VideojuegoSerializers

@csrf_exempt
@api_view(['GET','POST'])
def lista_categorias(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializers(categoria,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializers(data = data)
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)