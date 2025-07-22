# despesas/forms.py
from django import forms
from .models import Despesa
from bancos.models import Banco

class DespesaForm(forms.ModelForm):
    # Novidade aqui! Sobrescrevemos o método __init__ do formulário.
    def __init__(self, *args, **kwargs):
        # Pegamos o 'user' que será passado pela view.
        user = kwargs.pop('user', None)
        super(DespesaForm, self).__init__(*args, **kwargs)

        # Se um usuário foi passado, filtramos o queryset do campo 'banco'.
        if user:
            self.fields['banco'].queryset = Banco.objects.filter(usuario=user)

    class Meta:
        model = Despesa
        # Definimos os campos que aparecerão no formulário.
        fields = ['nome', 'banco', 'valor_total', 'numero_parcelas', 'data_compra']
        # Adicionamos 'widgets' para melhorar a experiência do usuário.
        widgets = {
            'data_compra': forms.DateInput(attrs={'type': 'date'}),
        }