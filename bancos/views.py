# bancos/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Banco

@login_required
def listar_bancos(request):
    # Filtra os bancos para pegar apenas os que pertencem ao usuário logado
    bancos_do_usuario = Banco.objects.filter(usuario=request.user)

    # Envia os dados para o template
    contexto = {
        'bancos': bancos_do_usuario
    }
    return render(request, 'bancos/listar_bancos.html', contexto)