from rest_framework import serializers
from veiculo.models import Veiculo

class SerializadorVeiculo (serializers.ModelSerializer):

    marca_display = serializers.SerializerMethodField()
    cor_display = serializers.SerializerMethodField()
    combustivel_display = serializers.SerializerMethodField()

    def get_marca_display (self, instancia):
        return instancia.get_marca_display()

    def get_cor_display (self, instancia):
        return instancia.get_cor_display()

    def get_combustivel_display (self, instancia):
        return instancia.get_combustivel_display()
    class Meta:
        model = Veiculo
        exclude = []