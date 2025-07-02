# bancos/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Banco
from .forms import BancoForm

@login_required
def listar_bancos(request):
    # Filtra os bancos para pegar apenas os que pertencem ao usuário logado
    bancos_do_usuario = Banco.objects.filter(usuario=request.user)

    # Envia os dados para o template
    contexto = {
        'bancos': bancos_do_usuario
    }
    return render(request, 'bancos/listar_bancos.html', contexto)

@login_required
def adicionar_banco(request):
    if request.method == 'POST':
        # Se o formulário foi enviado, processa os dados
        form = BancoForm(request.POST)
        if form.is_valid():
            banco = form.save(commit=False) # Não salva no banco ainda
            banco.usuario = request.user    # Associa ao usuário logado
            banco.save()                    # Agora salva no banco
            return redirect('listar_bancos') # Redireciona para a lista
    else:
        # Se for o primeiro acesso, mostra um formulário em branco
        form = BancoForm()

    contexto = {
        'form': form
    }
    return render(request, 'bancos/adicionar_banco.html', contexto)