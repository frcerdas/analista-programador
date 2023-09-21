from django.urls import path
from .views import inicio, categoria_detail, login, registro, addgame

# app_name = "core"   


urlpatterns = [
    path('', inicio, name='inicio'),
    path('categoria/<str:slug_categoria>/', categoria_detail, name='categoria_detail'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('agregar-juego', addgame, name='addgame'),
]