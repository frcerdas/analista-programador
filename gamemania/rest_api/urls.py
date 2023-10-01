from django.urls import path
from rest_api.views import lista_categorias

urlpatterns = [
    path('lista_categorias/',lista_categorias,name="lista_categorias")
]