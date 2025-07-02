# bancos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_bancos, name='listar_bancos'),
    path('adicionar/', views.adicionar_banco, name='adicionar_banco'),
]