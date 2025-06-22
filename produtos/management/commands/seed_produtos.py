import random
from django.core.management.base import BaseCommand
from faker import Faker
from produtos.models import Produto

class Command(BaseCommand):
    help = 'Cria N produtos aleatórios no banco de dados'

    def add_arguments(self, parser):
        """Define um argumento para o comando, que será o número de produtos a criar."""
        parser.add_argument(
            '--numero',
            type=int,
            help='Número de produtos a serem criados',
            default=1
        )

    def handle(self, *args, **options):
        numero_de_produtos = options['numero']
        fake = Faker('pt_BR') 

        self.stdout.write('Limpando produtos antigos...')
        Produto.objects.all().delete()
        
        self.stdout.write(f'Criando {numero_de_produtos} produtos...')

        for i in range(numero_de_produtos):
            nome_produto = f"{fake.word().capitalize()} {fake.word().capitalize()}"
            descricao_produto = fake.sentence(nb_words=10)
            preco_produto = round(random.uniform(10.50, 999.99), 2)
            
            Produto.objects.create(
                nome=nome_produto,
                descricao=descricao_produto,
                preco=preco_produto
            )
            self.stdout.write(f'  -> Criado produto {i + 1}: "{nome_produto}"')

        self.stdout.write(self.style.SUCCESS(f'Sucesso! {numero_de_produtos} produtos foram criados.'))
