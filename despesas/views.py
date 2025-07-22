# despesas/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Despesa

@login_required
def listar_despesas(request):
    # Filtra as despesas para pegar apenas as do usuário logado
    # e ordena pela data da compra, da mais nova para a mais antiga
    despesas_do_usuario = Despesa.objects.filter(usuario=request.user).order_by('-data_compra')

    contexto = {
        'despesas': despesas_do_usuario
    }
    return render(request, 'despesas/dashboard.html', contexto)