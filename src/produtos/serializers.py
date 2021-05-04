from rest_framework import serializers
from .models import Estabelecimento, Produto


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    estabelecimento = EstabelecimentoSerializer(required=False, read_only=True)
    class Meta:
        model = Produto
        fields = '__all__'
