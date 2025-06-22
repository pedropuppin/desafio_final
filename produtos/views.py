from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Esse é o 'Controller'. Ele lida com as requisições HTTP
    e implementa todos os endpoints para o CRUD.
    
    O Django REST Framework já implementa as operações básicas de CRUD
    como o 'Find All' e o 'Find By ID' como requisitado no exercício.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @action(detail=False, methods=['get'], url_path='contar')
    def contar(self, request):
        """Endpoint para retornar o número total de produtos."""
        count = self.get_queryset().count()
        return Response({'total': count})

    @action(detail=False, methods=['get'], url_path='buscar')
    def buscar_por_nome(self, request):
        """Endpoint para retornar registros que correspondam a um nome."""
        nome = request.query_params.get('nome', None)
        if nome is not None:
            produtos = self.get_queryset().filter(nome__icontains=nome)
            serializer = self.get_serializer(produtos, many=True)
            return Response(serializer.data)
        return Response(
            {"detalhe": "Parâmetro 'nome' é obrigatório."},
            status=status.HTTP_400_BAD_REQUEST
        )