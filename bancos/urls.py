# bancos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rota para a lista de bancos
    path('', views.listar_bancos, name='listar_bancos'),
    
    # Rota para o formulário de adicionar
    path('adicionar/', views.adicionar_banco, name='adicionar_banco'),
    
    # Rota para o formulário de editar (com o 'name' que estava faltando)
    path('<int:pk>/editar/', views.editar_banco, name='editar_banco'),
    
    # Rota para a página de confirmação de deletar
    path('<int:pk>/deletar/', views.deletar_banco, name='deletar_banco'),
]