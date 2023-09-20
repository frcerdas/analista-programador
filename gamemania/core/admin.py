from django.contrib import admin
from .models import Genero, Videojuego, UserProfile

# Register your models here.
admin.site.register(Genero)
admin.site.register(Videojuego)
admin.site.register(UserProfile)