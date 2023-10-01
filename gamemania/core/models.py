from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
# añadimos el usuario profile
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES, verbose_name='Rol')
    
    def __str__(self):
        return self.user.username + ' - ' + self.role

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoría')
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    slug_categoria = models.SlugField(unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug_categoria:
            self.slug_categoria = slugify(self.nombreCategoria)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombreCategoria
    
class Videojuego(models.Model):
    idVideojuego = models.AutoField(primary_key=True)
    nombreVideojuego = models.CharField(max_length=50, verbose_name='Nombre del videojuego')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripcion del videojuego')
    fechaLanzamiento = models.DateField(null=True, blank=True, verbose_name='Fecha de lanzamiento del videojuego')
    precio = models.IntegerField(verbose_name='Precio del videojuego')
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreVideojuego