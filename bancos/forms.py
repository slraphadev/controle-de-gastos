# bancos/forms.py

from django import forms
from .models import Banco

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['instituicao', 'limite_credito', 'dia_fechamento_fatura', 'dia_vencimento_fatura']
        
        # Adiciona 'labels' para customizar os nomes dos campos no formulário
        labels = {
            'instituicao': 'Instituição (ex: Nubank, Banco do Brasil)',
            'limite_credito': 'Limite de Crédito (R$)',
            'dia_fechamento_fatura': 'Dia do Fechamento da Fatura',
            'dia_vencimento_fatura': 'Dia do Vencimento da Fatura',
        }