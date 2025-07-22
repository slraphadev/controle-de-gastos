# despesas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rota para a dashboard (lista de despesas)
    path('', views.listar_despesas, name='dashboard'),

    # Rota para o formulário de adicionar
    path('adicionar/', views.adicionar_despesa, name='adicionar_despesa'),

    # NOVAS ROTAS:
    path('<int:pk>/editar/', views.editar_despesa, name='editar_despesa'),
    path('<int:pk>/deletar/', views.deletar_despesa, name='deletar_despesa'),
]