# despesas/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Despesa
from .forms import DespesaForm

@login_required
def listar_despesas(request):
    despesas_do_usuario = Despesa.objects.filter(usuario=request.user).order_by('-data_compra')
    contexto = {
        'despesas': despesas_do_usuario
    }
    return render(request, 'despesas/dashboard.html', contexto)

@login_required
def adicionar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST, user=request.user)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            despesa.save()
            return redirect('dashboard')
    else:
        form = DespesaForm(user=request.user)

    contexto = {'form': form}
    return render(request, 'despesas/adicionar_despesa.html', contexto)