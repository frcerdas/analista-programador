from django.contrib import admin
from .models import UserProfile, Genero, Videojuego

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Genero)
admin.site.register(Videojuego)