from django.db import models


class Produto(models.Model):
    """
    Esse é o 'Model'. Representa um produto na loja.
    """
    nome = models.CharField(
        max_length=100,
        help_text="Nome do produto"
    )
    
    descricao = models.TextField(
        blank=True, null=True,
        help_text="Descrição detalhada do produto"
    )
    
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Preço do produto"
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True, 
        help_text="Data de criação do registro"
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']