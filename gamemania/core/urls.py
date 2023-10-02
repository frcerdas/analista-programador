from django.urls import path
from .views import inicio, categoria_detail, inicio_sesion, registro, add_categoria, list_categoria, modify_categoria, add_juego, list_juego, modify_juego, cerrar_sesion, admin_area

# app_name = "core"   


urlpatterns = [
    path('', inicio, name='inicio'),
    path('categoria/<str:slug_categoria>/', categoria_detail, name='categoria_detail'),
    path('login/', inicio_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('registro/', registro, name='registro'),
    path('agregar-categoria/', add_categoria, name='add_categoria'),
    path('listar-categorias/', list_categoria, name='list_categoria'),
    path('modificar-categoria/<id>', modify_categoria, name='modify_categoria'),
    path('agregar-juego/', add_juego, name='add_juego'),
    path('listar-juegos/', list_juego, name='list_juego'),
    path('modificar-juego/<id>', modify_juego, name='modify_juego'),
    path('area-administracion/', admin_area, name='admin_area'),
]