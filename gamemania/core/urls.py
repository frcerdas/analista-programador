from django.urls import path
from .views import inicio, categoria_detail, inicio_sesion, registro, addgame, cerrar_sesion

# app_name = "core"   


urlpatterns = [
    path('', inicio, name='inicio'),
    path('categoria/<str:slug_categoria>/', categoria_detail, name='categoria_detail'),
    path('login/', inicio_sesion, name='login'),
    path('logout', cerrar_sesion, name='logout'),
    path('registro/', registro, name='registro'),
    path('agregar-juego', addgame, name='addgame'),
]