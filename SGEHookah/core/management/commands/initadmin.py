from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import *

class Command(BaseCommand):
	def handle(cls, *args, **options):
		if User.objects.count() == 0:
			admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
			admin.is_active = True
			admin.is_admin = True
			admin.save()
			print('Admin created. \nUser: admin\nPass:admin123')
		else:
			print('Admin exists, skipping ...')

		if cls.make_unidade():
			print('Unidade Criada')

		if cls.make_categoria():
			print('Categoria Criada')
		
		if cls.make_materia():
			print('Matéria Criada')
		
		if cls.make_product():
			print('Produto Criado')

		if cls.make_status_craft():
			print('Status de Fabricação Criados')

	def make_unidade(cls):
		if Unidademedida.objects.count() == 0:
			Unidademedida.objects.create(unidademedida='ml')
			return True
		return False

	def make_categoria(cls):
		if Categoriaproduto.objects.count() == 0:
			Categoriaproduto.objects.create(nomecategoria='Juice')
			return True
		return False

	def make_materia(cls):
		if Materiaprima.objects.count() == 0:
			Materiaprima.objects.create(
				materiaprima='VG', 
				totalestoque=0, 
				unidade=Unidademedida.objects.first()
				)
			Materiaprima.objects.create(
				materiaprima='PG', 
				totalestoque=0, 
				unidade=Unidademedida.objects.first()
				)
			return True
		return False

	def make_product(cls):
		if Produto.objects.count() == 0:
			produto = Produto(
				fkid_categoria= Categoriaproduto.objects.first(),
				fkid_unidademedida= Unidademedida.objects.first(),
				codproduto= '1001',
				nomeproduto= 'Juice Morango',
				preco= 10.00,
				sabor= 'Morango',
				altura= 20,
				largura= 20,
				profundidade= 20,
				peso= 0.200,
				fotoproduto= 'default_product.png'
			)
			produto.save()
			return True
		return False

	def make_status_craft(cls):
		if Statusfabricacao.objects.count() == 0:
			status1 = Statusfabricacao(order=0, status='Pedido Criado')
			status2 = Statusfabricacao(order=1, status='Maturação')
			status3 = Statusfabricacao(order=2, status='Finalização')
			status4 = Statusfabricacao(order=3, status='Produção Encerrada')

			status1.save()
			status2.save()
			status3.save()
			status4.save()
			return True
		return False