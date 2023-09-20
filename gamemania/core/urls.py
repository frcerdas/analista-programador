from django.urls import path
from .views import gamemania

app_name = "core"   


urlpatterns = [
    path('', gamemania, name='inicio'),
]