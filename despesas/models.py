# despesas/models.py

from django.db import models
from django.contrib.auth.models import User
from bancos.models import Banco # Importamos o modelo do outro app

class Despesa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    numero_parcelas = models.IntegerField(default=1)
    data_compra = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.banco.instituicao}"