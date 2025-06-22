from rest_framework import serializers
from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    """
    Este é o 'View' para a API. Define quais campos do Model serão 
    convertidos para JSON.
    """
    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'descricao',
            'preco',
            'data_criacao'
        ]