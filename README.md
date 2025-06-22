# Exercício API RESTful - Loja Online (domínio Produtos)

Este projeto é uma API RESTful desenvolvida em Django e Django REST Framework como parte de um exercício. A API implementa operações CRUD para gerenciar produtos de uma loja online.

## Funcionalidades

*   **CRUD completo** para a entidade `Produto`.
*   Endpoints para **contagem** de registros e **busca por nome**.
*   Estrutura MVC (Model-View-Controller) bem definida.
*   Gerenciamento de segredos com arquivo `.env`.
*   Testes unitários para garantir a funcionalidade da API.
*   Comando customizado para popular o banco de dados com dados de teste.

## Pré-requisitos

*   Python 3.8+
*   `pip` (gerenciador de pacotes do Python)
*   Git

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Clone o Repositório

```bash
git clone https://github.com/pedropuppin/desafio_final.git
cd desafio_final
```

### 2. Crie e Ative um Ambiente Virtual

Use um ambiente virtual para isolar as dependências do projeto.

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

Instale todas as bibliotecas necessárias a partir do arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto (na mesma pasta que `manage.py`). Este arquivo guardará sua `SECRET_KEY`.

Copie o conteúdo abaixo para o seu arquivo `.env`:

```env
# filepath: .env
SECRET_KEY='coloque-aqui-uma-nova-secret-key-gerada'
DEBUG=True
```
> **Importante:** Para gerar uma nova `SECRET_KEY`, você pode usar um gerador online ou executar um comando do Django.

### 5. Aplique as Migrações do Banco de Dados

Este comando criará o banco de dados SQLite e as tabelas necessárias.

```bash
python manage.py migrate
```

### 6. (Opcional) Popule o Banco de Dados

Para facilitar os testes, você pode popular o banco de dados com produtos de exemplo usando o comando customizado.

```bash
# Cria 50 produtos de exemplo
python manage.py seed_produtos --numero 50
```

### 7. Inicie o Servidor de Desenvolvimento

Agora, seu projeto está pronto para ser executado!

```bash
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`.

## Documentação da API

A API de produtos está disponível sob o prefixo `/api_v1/`.

**Base URL:** `http://127.0.0.1:8000/api_v1/`

### Endpoints de Produtos (`/produtos/`)

| Método | Endpoint                               | Descrição                                      |
| :----- | :------------------------------------- | :--------------------------------------------- |
| `GET`    | `/api/produtos/`                       | Retorna uma lista de todos os produtos.          |
| `POST`   | `/api/produtos/`                       | Cria um novo produto.                          |
| `GET`    | `/api/produtos/{id}/`                  | Retorna os detalhes de um produto específico.  |
| `PUT`    | `/api/produtos/{id}/`                  | Atualiza completamente um produto específico.  |
| `PATCH`  | `/api/produtos/{id}/`                  | Atualiza parcialmente um produto específico.   |
| `DELETE` | `/api/produtos/{id}/`                  | Exclui um produto específico.                  |
| `GET`    | `/api/produtos/contar/`                | Retorna o número total de produtos.            |
| `GET`    | `/api/produtos/buscar/?nome={termo}`   | Busca produtos cujo nome contenha o `{termo}`. |

**Exemplo de corpo para `POST` e `PUT`:**
```json
{
    "nome": "Monitor 4K",
    "descricao": "Monitor de 27 polegadas.",
    "preco": "1899.99"
}
```

### Coleção do Postman

Para facilitar os testes da API, uma coleção do Postman (`API_Desafio_final.postman_collection.json`) está incluída na raiz do projeto. Você pode importá-la diretamente no seu Postman.

## Como Rodar os Testes

Para garantir que tudo está funcionando como esperado, você pode executar a suíte de testes automatizados.

```bash
python manage.py test produtos
```
