from django.urls import path
from rest_api.views import lista_categorias, lista_videojuegos, modify_categoria
# from rest_api.viewsLogin import login

urlpatterns = [
    path('listar-categorias/',lista_categorias,name="lista_categorias"),
    path('listar-videojuegos/',lista_videojuegos,name="lista_videojuegos"),
    #path('modificar-categoria/<id>',modify_categoria,name="modify_categoria"),
    # path('login/',login,name="login")
]