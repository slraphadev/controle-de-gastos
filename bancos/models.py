# bancos/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Banco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    instituicao = models.CharField(max_length=100)
    limite_credito = models.DecimalField(max_digits=10, decimal_places=2)
    dia_fechamento_fatura = models.IntegerField()
    dia_vencimento_fatura = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instituicao