# bancos/models.py

from django.db import models
from django.contrib.auth.models import User
# Importa os validadores
from django.core.validators import MinValueValidator, MaxValueValidator

class Banco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    instituicao = models.CharField(max_length=100)
    
    # Adiciona um validador para garantir que o limite não seja negativo
    limite_credito = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.00)]
    )
    
    # Adiciona validadores para o dia ficar entre 1 e 31
    dia_fechamento_fatura = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)]
    )
    dia_vencimento_fatura = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)]
    )
    
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instituicao