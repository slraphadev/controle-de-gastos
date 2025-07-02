# bancos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_bancos, name='listar_bancos'),
]