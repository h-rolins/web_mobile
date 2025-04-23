from django.db import models
from datetime import datetime
from veiculo.consts import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEIS


class Veiculo(models.Model):
    marca = models.PositiveSmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)