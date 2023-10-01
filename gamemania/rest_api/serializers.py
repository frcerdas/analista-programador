from rest_framework import serializers
from core.models import Categoria, Videojuego

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria','imagen','slug_categoria']

class VideojuegoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = ['idVideojuego','nombreVideojuego','descripcion','fechaLanzamiento','precio','imagen','categoria']