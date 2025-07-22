# bancos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Banco
from .forms import BancoForm

@login_required
def listar_bancos(request):
    # Esta view busca os bancos do usuário logado e os envia para o template.
    bancos_do_usuario = Banco.objects.filter(usuario=request.user)
    
    # O dicionário 'contexto' é o que leva os dados para o template.
    contexto = {
        'bancos': bancos_do_usuario
    }
    
    # A função 'render' é responsável por processar o HTML com os dados do contexto.
    return render(request, 'bancos/listar_bancos.html', contexto)

@login_required
def adicionar_banco(request):
    if request.method == 'POST':
        form = BancoForm(request.POST)
        if form.is_valid():
            banco = form.save(commit=False)
            banco.usuario = request.user
            banco.save()
            return redirect('listar_bancos')
    else:
        form = BancoForm()
    return render(request, 'bancos/adicionar_banco.html', {'form': form})

@login_required
def editar_banco(request, pk):
    banco = get_object_or_404(Banco, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = BancoForm(request.POST, instance=banco)
        if form.is_valid():
            form.save()
            return redirect('listar_bancos')
    else:
        form = BancoForm(instance=banco)
    return render(request, 'bancos/editar_banco.html', {'form': form, 'banco': banco})

@login_required
def deletar_banco(request, pk):
    banco = get_object_or_404(Banco, pk=pk, usuario=request.user)
    if request.method == 'POST':
        banco.delete()
        return redirect('listar_bancos')
    return render(request, 'bancos/deletar_banco.html', {'banco': banco})