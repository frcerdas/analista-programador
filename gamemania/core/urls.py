from django.urls import path
from .views import inicio, fps, deportes, aventura, ingenio, rpg, login, registro, addgame

urlpatterns = [
    path('',inicio,name="inicio"),
    path('fps',fps,name="fps"),
    path('deportes',deportes,name="deportes"),
    path('aventura',aventura,name="aventura"),
    path('ingenio',ingenio,name="ingenio"),
    path('rpg',rpg,name="rpg"),
    path('login',login,name="login"),
    path('registro',registro,name="registro"),
    path('agregar-juego',addgame,name="addgame")
]