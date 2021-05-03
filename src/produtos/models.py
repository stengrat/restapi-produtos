from django.db import models
from uuid import uuid4


class Estabelecimento(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nm_fan = models.CharField(max_length=250, null=True, blank=True)
    nm_emp = models.CharField(max_length=200, null=True, blank=True)
    tp_logr = models.CharField(max_length=50, null=True, blank=True)
    nm_logr = models.CharField(max_length=200, null=True, blank=True)
    nr_logr = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=250, null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    mun = models.CharField(max_length=250, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):  
        return self.nm_fan + ' ' + self.bairro

class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    local = models.CharField(max_length=12, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_tabela = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    datahora = models.DateTimeField(auto_now_add=True)
    tempo = models.CharField(max_length=200, null=True, blank=True)
    estabelecimento = models.ForeignKey(Estabelecimento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):  
        return self.desc