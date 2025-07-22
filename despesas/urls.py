# despesas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_despesas, name='dashboard'),
    path('adicionar/', views.adicionar_despesa, name='adicionar_despesa'),
]