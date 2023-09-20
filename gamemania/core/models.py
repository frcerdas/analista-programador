from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
# añadimos el usuario profile
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES, verbose_name='Rol')
    
    def __str__(self):
        return self.user.username + ' - ' + self.role

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True)
    nombreGenero = models.CharField(max_length=50, verbose_name='Nombre del Género')
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    
    def __str__(self):
        return self.nombreGenero
    
class Videojuego(models.Model):
    idVideojuego = models.AutoField(primary_key=True)
    nombreVideojuego = models.CharField(max_length=50, verbose_name='Nombre del videojuego')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripcion del videojuego')
    fechalanzamiento = models.DateField(null=True, blank=True, verbose_name='Fecha de lanzamiento del videojuego')
    precio = models.IntegerField(verbose_name='Precio del videojuego')
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreVideojuego