from django.contrib import admin
from produtos.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    """
    Configurações do admin para o modelo Produto.
    """
    list_display = (
        'id',
        'nome',
        'preco',
        'data_criacao'
    )
    
    search_fields = (
        'nome',
    )
    
    list_filter = (
        'data_criacao',
    )
    
    ordering = (
        '-id',
    )