from django.db import models
from datetime import datetime
from veiculo.consts import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEIS


class Veiculo(models.Model):
    marca = models.PositiveSmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)
    foto = models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')

    def __str__(self):
        return f"{self.get_marca_display()} {self.modelo} {self.ano}"

    @property
    def veiculo_novo(self):
        return self.ano == datetime.now().year
        
    def anos_de_uso(self):
        return datetime.now().year - self.ano
