from django import forms
from django.forms import ModelForm
from .models import Categoria, Videojuego
from django.contrib.auth.models import User


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria','imagen','slug_categoria']

class VideojuegoForm(ModelForm):
    class Meta:
        model = Videojuego
        fields = ['idVideojuego','nombreVideojuego','descripcion','fechaLanzamiento','precio','imagen','categoria']

class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')