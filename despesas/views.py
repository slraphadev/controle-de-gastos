# despesas/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Despesa
from .forms import DespesaForm
from bancos.models import Banco


@login_required
def listar_despesas(request):
    despesas_do_usuario = Despesa.objects.filter(usuario=request.user).order_by('-data_compra')
    soma_despesas = despesas_do_usuario.aggregate(Sum('valor_total'))
    total_gasto = soma_despesas['valor_total__sum'] if soma_despesas['valor_total__sum'] else 0
    contexto = {
        'despesas': despesas_do_usuario,
        'total_gasto': total_gasto,
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


# --- NOVA VIEW DE EDITAR ---
@login_required
def editar_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = DespesaForm(request.POST, user=request.user, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DespesaForm(user=request.user, instance=despesa)
    return render(request, 'despesas/editar_despesa.html', {'form': form, 'despesa': despesa})


# --- NOVA VIEW DE DELETAR ---
@login_required
def deletar_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        despesa.delete()
        return redirect('dashboard')
    return render(request, 'despesas/deletar_despesa.html', {'despesa': despesa})