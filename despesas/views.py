# despesas/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Despesa
from .forms import DespesaForm
from bancos.models import Banco


@login_required
def listar_despesas(request):
    # 1. Busca as despesas do usuário, ordenadas
    despesas_do_usuario = Despesa.objects.filter(usuario=request.user).order_by('-data_compra')

    # 2. Calcula o total gasto
    soma_despesas = despesas_do_usuario.aggregate(Sum('valor_total'))
    
    # 3. Pega o valor da soma ou define como 0 se não houver despesas
    total_gasto = soma_despesas['valor_total__sum'] if soma_despesas['valor_total__sum'] else 0

    # 4. Adiciona tudo ao contexto para ser usado no template
    contexto = {
        'despesas': despesas_do_usuario,
        'total_gasto': total_gasto,
    }
    return render(request, 'despesas/dashboard.html', contexto)


@login_required
def adicionar_despesa(request):
    if request.method == 'POST':
        # Passa os dados do formulário e o usuário logado
        form = DespesaForm(request.POST, user=request.user)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            despesa.save()
            return redirect('dashboard')
    else:
        # Mostra um formulário em branco, passando o usuário
        form = DespesaForm(user=request.user)
    
    contexto = {'form': form}
    return render(request, 'despesas/adicionar_despesa.html', contexto)