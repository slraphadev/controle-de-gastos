# despesas/models.py

from django.db import models
from django.contrib.auth.models import User
from bancos.models import Banco

# --- NOVO: Definimos as opções de categoria ---
CATEGORIAS_CHOICES = [
    ('ALIMENTACAO', 'Alimentação'),
    ('TRANSPORTE', 'Transporte'),
    ('MORADIA', 'Moradia'),
    ('LAZER', 'Lazer'),
    ('SAUDE', 'Saúde'),
    ('OUTROS', 'Outros'),
]

class Despesa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    numero_parcelas = models.IntegerField(default=1)
    data_compra = models.DateField()

    # --- NOVO CAMPO ---
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS_CHOICES,
        default='OUTROS' # Define um padrão
    )

    def __str__(self):
        return f"{self.nome} - {self.banco.instituicao}"