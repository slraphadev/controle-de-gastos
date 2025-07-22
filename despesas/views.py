# despesas/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Despesa
from .forms import DespesaForm
from bancos.models import Banco


@login_required
def listar_despesas(request):
    # --- Lógica de Despesas (já tínhamos) ---
    despesas = Despesa.objects.filter(usuario=request.user)
    soma_despesas = despesas.aggregate(Sum('valor_total'))
    total_em_uso = soma_despesas['valor_total__sum'] if soma_despesas['valor_total__sum'] else 0

    # --- Lógica de Limites (NOVO) ---
    # 1. Busca todos os bancos do usuário
    bancos = Banco.objects.filter(usuario=request.user)
    
    # 2. Calcula o limite de crédito total somando o limite de cada banco
    soma_limites = bancos.aggregate(Sum('limite_credito'))
    limite_total = soma_limites['limite_credito__sum'] if soma_limites['limite_credito__sum'] else 0
    
    # 3. Calcula o limite disponível
    limite_disponivel = limite_total - total_em_uso

    # --- Enviando tudo para o template ---
    contexto = {
        'despesas': despesas.order_by('-data_compra'),
        'total_em_uso': total_em_uso,
        'limite_total': limite_total,
        'limite_disponivel': limite_disponivel,
    }
    return render(request, 'despesas/dashboard.html', contexto)


@login_required
def adicionar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST, user=request.user)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            
            # --- LÓGICA DE CATEGORIZAÇÃO AUTOMÁTICA (NOVO) ---
            nome_despesa_lower = despesa.nome.lower()
            if any(palavra in nome_despesa_lower for palavra in ['comida', 'almoço', 'janta', 'restaurante', 'mercado', 'ifood']):
                despesa.categoria = 'ALIMENTACAO'
            elif any(palavra in nome_despesa_lower for palavra in ['uber', '99', 'gasolina', 'transporte', 'onibus']):
                despesa.categoria = 'TRANSPORTE'
            elif any(palavra in nome_despesa_lower for palavra in ['aluguel', 'condominio', 'luz', 'internet']):
                despesa.categoria = 'MORADIA'
            elif any(palavra in nome_despesa_lower for palavra in ['cinema', 'show', 'bar', 'streaming', 'spotify']):
                despesa.categoria = 'LAZER'
            elif any(palavra in nome_despesa_lower for palavra in ['farmacia', 'remedio', 'medico', 'consulta']):
                despesa.categoria = 'SAUDE'
            else:
                despesa.categoria = 'OUTROS'
            # --- FIM DA LÓGICA ---
            
            despesa.save()
            return redirect('dashboard')
    else:
        form = DespesaForm(user=request.user)
    
    contexto = {'form': form}
    return render(request, 'despesas/adicionar_despesa.html', contexto)


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


@login_required
def deletar_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        despesa.delete()
        return redirect('dashboard')
    return render(request, 'despesas/deletar_despesa.html', {'despesa': despesa})