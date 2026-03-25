from django.db import models

# Create your models here.
class SimulacaoEmprestimo(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    juros = models.DecimalField(max_digits=10, decimal_places=2)
    prazo = models.IntegerField()
    parcela = models.DecimalField(max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)
    data_simulacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Simulação de R$ {self.valor} em {self.prazo} meses"
    
