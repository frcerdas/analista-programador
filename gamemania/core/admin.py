from django.contrib import admin
from .models import Categoria, Videojuego, UserProfile, Usuario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Videojuego)
admin.site.register(UserProfile)
admin.site.register(Usuario)