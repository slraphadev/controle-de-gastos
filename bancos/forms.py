# bancos/forms.py
from django import forms
from .models import Banco

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['instituicao', 'limite_credito', 'dia_fechamento_fatura', 'dia_vencimento_fatura']