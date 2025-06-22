from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Produto

class ProdutoAPITests(APITestCase):
    """
    Testes para a API de Produtos.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Dados iniciais para todos os testes da classe.
        """
        cls.produto1 = Produto.objects.create(
            nome="Begônia Rex",
            descricao="Planta ornamental de folhas coloridas",
            preco=5500.00
        )
        cls.produto2 = Produto.objects.create(
            nome="Mouse sem fio",
            descricao="Mouse ergonômico",
            preco=150.00
        )

    def test_list_produtos(self):
        """
        Eendpoint de listagem de todos os produtos (Find All).
        """
        url = reverse('produto-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_produto(self):
        """
        Endpoint de busca por ID (Find By ID).
        """
        url = reverse('produto-detail', args=[self.produto1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.produto1.nome)

    def test_create_produto(self):
        """
        Endpoint de criação de um novo produto (Create).
        """
        url = reverse('produto-list')
        data = {'nome': 'Carregador UGreen', 'descricao': 'Carregador para IPhone', 'preco': '350.75'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 3)

    def test_update_produto(self):
        """
        Endpoint de atualização de um produto (Update).
        """
        url = reverse('produto-detail', args=[self.produto1.id])
        data = {'nome': 'Jiboia Verde', 'descricao': 'Planta pendurada', 'preco': '45.00'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.produto1.refresh_from_db()
        self.assertEqual(self.produto1.nome, 'Jiboia Verde')

    def test_delete_produto(self):
        """
        Endpoint de exclusão de um produto (Delete).
        """
        url = reverse('produto-detail', args=[self.produto2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Produto.objects.count(), 1)

    def test_contar_produtos(self):
        """
        Endpoint de contagem de produtos.
        """
        url = reverse('produto-contar')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total'], 2)

    def test_buscar_por_nome(self):
        """
        Endpoint de busca por nome (Find By Name).
        """
        url = reverse('produto-buscar-por-nome')
        response = self.client.get(url, {'nome': 'Rex'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Begônia Rex')

    def test_buscar_por_nome_sem_parametro_retorna_erro(self):
        """
        Testa se a busca por nome retorna erro 400 sem o parâmetro 'nome'.
        """
        url = reverse('produto-buscar-por-nome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)