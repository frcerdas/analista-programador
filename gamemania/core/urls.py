from django.urls import path
from .views import gamemania, categorias, categoria_detail

app_name = "core"   


urlpatterns = [
    path('', gamemania, name='inicio'),
    path('categoria/<str:nombre_categoria>/', categoria_detail, name='categoria_detail'),
]