import datetime as dt

from django.db import models

__all__ = [
    "Categoriaproduto", "Produto", "Unidademedida",
    "Pessoa", "Endereco", "Telefone",
    "Formulaproduto", "Formulamateria", "Materiaprima",
    "Pedidofabricacao", "Statusfabricacao"
]


class Categoriaproduto(models.Model):
    pkid_categoria = models.AutoField(primary_key=True)
    nomecategoria = models.CharField(
        'Nome da Categoria', unique=True, max_length=100)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.nomecategoria

    class Meta:
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias (Produto)'


class Cotacaocompra(models.Model):
    pkid_cotacao = models.AutoField(primary_key=True)
    fornecedor = models.CharField(max_length=100, blank=True, null=True)
    dt_cotacao = models.DateTimeField(blank=True, null=True)
    dt_entrega = models.DateTimeField(blank=True, null=True)
    formapamento = models.CharField(max_length=45, blank=True, null=True)
    pedidocompra_pkid_compra = models.IntegerField()
    statuscotacao_pkid_status = models.IntegerField()
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.TextField(default=0, blank=True, null=True)

    class Meta:
        managed = True


class Endereco(models.Model):
    pkid_endereco = models.AutoField(primary_key=True)
    fkid_pessoa = models.ForeignKey(
        'Pessoa', models.CASCADE,
        blank=True, null=True,
        verbose_name='Pessoa')
    logradouro = models.CharField('Endereço', max_length=100)
    numero = models.CharField('Número', max_length=7, null=True, blank=True)
    complemento = models.CharField(
        'Complemento', max_length=45, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=150)
    uf = models.CharField('Estado', max_length=2)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return f'{self.fkid_pessoa.nomecompleto_razaosocial} : {self.cep}'

    class Meta:
        managed = True
        verbose_name = 'Endereço (Pessoa : CEP)'
        verbose_name_plural = 'Endereços'


class Entrega(models.Model):
    pkid_entrega = models.AutoField(primary_key=True)
    dataentrega = models.DateTimeField(blank=True, null=True)
    formaentrega = models.CharField(max_length=100, blank=True, null=True)
    valorfrete = models.TextField(blank=True, null=True)
    nomecontarecebimento = models.CharField(
        max_length=100, blank=True, null=True)
    fkid_usuario_alteracao = models.IntegerField()
    dt_cadastro = models.DateTimeField()
    dt_alteracao = models.DateTimeField()
    hide = models.TextField(default=0)

    class Meta:
        managed = True


class Formapagamento(models.Model):
    pkid_formapag = models.AutoField(primary_key=True)
    formapagamento = models.CharField(max_length=50)
    fkid_usuario_alteracao = models.IntegerField()
    dt_cadastro = models.DateTimeField()
    dt_alteracao = models.DateTimeField()
    hide = models.TextField(default=0)

    class Meta:
        managed = True


class Formulaproduto(models.Model):
    pkid_formula = models.AutoField(primary_key=True)
    fkid_produto = models.OneToOneField(
        'Produto', on_delete=models.CASCADE,
        unique=True,
        verbose_name='Produto')
    tempomaturacao = models.TimeField('Tempo de Maturação')
    hide = models.BooleanField(default=0)

    def __str__(self):
        return f'Fórmula {self.fkid_produto.nomeproduto}'

    class Meta:
        managed = True
        verbose_name = 'Fórmula Produto'
        verbose_name_plural = 'Fórmulas (Produto)'


class Itemcompra(models.Model):
    pkid_item = models.AutoField(primary_key=True)
    produto = models.CharField(max_length=45, blank=True, null=True)
    descricaoproduto = models.CharField(max_length=45, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    precounitario = models.TextField(blank=True, null=True)
    totalvenda = models.TextField(blank=True, null=True)
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.TextField(default=0, blank=True, null=True)
    pedidocompra_pkid_compra = models.IntegerField()
    statuscompra_pkid_status = models.IntegerField()
    unidademedidacompra_pkid_unidademedida = models.IntegerField()

    class Meta:
        managed = True
        unique_together = (('pkid_item', 'pedidocompra_pkid_compra'),)


class Itemcotacao(models.Model):
    pkid_item = models.AutoField(primary_key=True)
    produto = models.CharField(max_length=45, blank=True, null=True)
    descricaoproduto = models.CharField(max_length=100, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    precounitario = models.TextField(blank=True, null=True)
    totalvenda = models.TextField(blank=True, null=True)
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.TextField(default=0, blank=True, null=True)
    cotacaocompra_pkid_cotacao = models.IntegerField()

    class Meta:
        managed = True
        unique_together = (('pkid_item', 'cotacaocompra_pkid_cotacao'),)


class Itemvenda(models.Model):
    pkid_item = models.AutoField(primary_key=True, max_length=45)
    pedido_venda_idpedido_venda = models.IntegerField()
    produto = models.CharField(max_length=45, blank=True, null=True)
    descricaoproduto = models.CharField(max_length=45, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    unidademedida_pkid_unidademedida = models.IntegerField()
    precounitario = models.TextField(blank=True, null=True)
    totalvenda = models.TextField(blank=True, null=True)
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.TextField(default=0, blank=True, null=True)
    produtos_idprodutos = models.IntegerField()
    usuario_pkid_usuario = models.IntegerField()

    class Meta:
        managed = True
        unique_together = (('pkid_item', 'pedido_venda_idpedido_venda'),)


class Linhavenda(models.Model):
    pkid_linhavenda = models.AutoField(primary_key=True)
    pedidovenda_pkid_venda = models.IntegerField()
    fkid_produto = models.IntegerField()
    quantidade = models.IntegerField()
    precovenda = models.TextField()
    fkid_usuario_alteracao = models.IntegerField()
    dt_alteracao = models.DateTimeField()
    dt_cadastro = models.DateTimeField()
    hide = models.TextField(default=0)

    class Meta:
        managed = True
        unique_together = (('pkid_linhavenda', 'pedidovenda_pkid_venda'),)


class Materiaprima(models.Model):
    pkid_materiaprima = models.AutoField(primary_key=True)
    materiaprima = models.CharField('Matéria Prima', max_length=60)
    marca = models.CharField('Marca', max_length=50, blank=True, null=True)
    totalestoque = models.IntegerField('Qtd. em Estoque')
    unidade = models.ForeignKey(
        'Unidademedida', on_delete=models.CASCADE, verbose_name='Unidade')
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.materiaprima

    class Meta:
        managed = True
        verbose_name = 'Matéria Prima'
        verbose_name_plural = 'Matérias Primas'


class Formulamateria(models.Model):
    pkid_formula_materia = models.AutoField(primary_key=True)
    fkid_formulaproduto = models.ForeignKey(
        "Formulaproduto",
        on_delete=models.CASCADE,
        verbose_name='Fórmula')
    fkid_materiaprima = models.ForeignKey(
        "Materiaprima",
        on_delete=models.CASCADE,
        verbose_name='Matéria Prima')
    quantidade = models.FloatField('Quantidade')
    unidade = models.ForeignKey(
        "Unidademedida",
        on_delete=models.CASCADE,
        verbose_name='Unidade')

    def __str__(self):
        return f'{self.fkid_materiaprima.materiaprima} : {self.fkid_formulaproduto}'

    class Meta:
        verbose_name = 'Matéria Prima : Fórmula'
        verbose_name_plural = 'Matérias Fórmulas (Relação)'


class Movimentacao(models.Model):
    pkid_movimentacao = models.AutoField(primary_key=True)
    fkid_produto = models.IntegerField()
    tipomovimentacao = models.TextField()
    numentradas = models.IntegerField()
    numsaidas = models.IntegerField()
    dt_cadastro = models.DateTimeField()
    dt_alteracao = models.DateTimeField()
    hide = models.TextField(default=0)
    fkid_linhavenda1 = models.IntegerField(blank=True, null=True)
    fkid_venda = models.IntegerField(blank=True, null=True)
    fkid_pedidofabri = models.IntegerField(blank=True, null=True)
    fkid_estoque = models.IntegerField()

    class Meta:
        managed = True


class Pedidocompra(models.Model):
    pkid_compra = models.AutoField(primary_key=True)
    fornecedor = models.CharField(max_length=100, blank=True, null=True)
    dt_pedido = models.DateTimeField(blank=True, null=True)
    dt_compra = models.DateTimeField(blank=True, null=True)
    dt_pagamento = models.DateTimeField(blank=True, null=True)
    dt_recebimento = models.DateTimeField(blank=True, null=True)
    cotacaocompra_pkid_cotacao = models.IntegerField()
    dt_cadastro = models.DateTimeField(blank=True, null=True)
    dt_alteracao = models.DateTimeField(blank=True, null=True)
    hide = models.TextField(default=0, blank=True, null=True)
    statuscompra_pkid_status = models.IntegerField()

    class Meta:
        managed = True


class Pedidofabricacao(models.Model):
    pkid_pedidofabricacao = models.AutoField(primary_key=True)
    fkid_formula = models.ForeignKey(
        "Formulaproduto", on_delete=models.CASCADE)
    fkid_statusfabricacao = models.ForeignKey(
        "Statusfabricacao", on_delete=models.CASCADE)
    quantidade = models.FloatField("Quantidade")
    dt_fim_maturacao = models.DateTimeField()
    hide = models.BooleanField(default=0)

    def is_ready(self):
        return dt.datetime.now(dt.timezone.utc) >= self.dt_fim_maturacao

    def materias(self):
        lista = []
        for materia in Formulamateria.objects.filter(fkid_formulaproduto=self.fkid_formula).values():

            id_materia = materia['fkid_materiaprima_id']
            unidade = materia['unidade_id']

            materia['fkid_materiaprima_id'] = Materiaprima.objects.get(
                pkid_materiaprima=id_materia
            ).materiaprima

            materia['unidade_id'] = Unidademedida.objects.get(
                pkid_unidademedida=unidade
            ).unidademedida

            lista.append((materia, id_materia))
        return lista

    def name(self):
        return f'Pedido nº{self.pkid_pedidofabricacao}'

    def __str__(self):
        return f'Pedido nº{self.pkid_pedidofabricacao}'

    class Meta:
        verbose_name = 'Pedido de Fabricação'
        verbose_name_plural = 'Pedidos de Fabricação'


class Pedidovenda(models.Model):
    pkid_venda = models.AutoField(primary_key=True)
    fkid_pessoa = models.IntegerField()
    fkid_usuario = models.IntegerField()
    dt_pedido = models.DateTimeField(blank=True, null=True)
    dt_pagamento = models.DateTimeField(blank=True, null=True)
    dt_entrega = models.DateTimeField(blank=True, null=True)
    fkid_usuarioalteracao = models.IntegerField()
    fkid_formapag = models.IntegerField()
    fkid_entrega = models.IntegerField()
    dt_cadastro = models.DateTimeField()
    dt_alteracao = models.DateTimeField()
    hide = models.TextField(default=0)
    fkid_status = models.IntegerField()

    class Meta:
        managed = True


class Pessoa(models.Model):
    pkid_pessoa = models.AutoField(primary_key=True, )
    nomecompleto_razaosocial = models.CharField(
        'Nome / Razão Social', max_length=100)
    apelido_nomefantasia = models.CharField(
        'Apelido / Nome Fantasia', max_length=100, blank=True, null=True)
    email = models.CharField('E-mail', unique=True,
                             max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(
        'CPF / CNPJ', unique=True, max_length=19, blank=True, null=True)
    rg_ie = models.CharField('RG / IE', max_length=50, blank=True, null=True)
    genero = models.CharField('Gênero', max_length=1)
    dt_nascimento = models.DateField(
        'Data de Nascimento', blank=True, null=True)
    st_pessoajuridica = models.BooleanField(
        'Pessoa Jurídica', max_length=1, default=0)
    tipopessoa = models.CharField(
        'Tipo da Pessoa', max_length=15, null=False, blank=False)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.nomecompleto_razaosocial

    class Meta:
        managed = True
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Produto(models.Model):
    pkid_produto = models.AutoField(primary_key=True, )
    fkid_categoria = models.ForeignKey(
        'Categoriaproduto',
        on_delete=models.CASCADE,
        verbose_name='Categoria')
    fkid_unidademedida = models.ForeignKey(
        'Unidademedida',
        on_delete=models.CASCADE,
        verbose_name='Unidade de Medida')
    codproduto = models.CharField('Código', unique=True, max_length=8)
    nomeproduto = models.CharField('Nome do Produto', max_length=50)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    precocusto = models.DecimalField(
        'Preço de Custo', max_digits=10, decimal_places=2, blank=True, null=True)
    totalestoque = models.IntegerField('Qtd. em Estoque', default=0)
    descricao = models.CharField(
        'Descrição', max_length=300, blank=True, null=True)
    sabor = models.CharField('Sabor', max_length=45, blank=True, null=True)
    marca = models.CharField('Marca', max_length=50, blank=True, null=True)
    altura = models.IntegerField('Altura')
    largura = models.IntegerField('Largura')
    profundidade = models.IntegerField('Profundidade')
    peso = models.DecimalField('Peso', max_digits=10, decimal_places=3, )
    fotoproduto = models.FileField(
        'Foto do Produto', upload_to='uploads/%Y/%m', max_length=1000, blank=True, null=True)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.nomeproduto

    class Meta:
        managed = True
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Statuscompra(models.Model):
    pkid_status = models.AutoField(primary_key=True)
    descricaostatus = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True


class Statusfabricacao(models.Model):
    pkid_status = models.AutoField(primary_key=True)
    order = models.IntegerField("Ordem")
    status = models.CharField("Estado", max_length=45, blank=True, null=True)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.status

    class Meta:
        managed = True
        verbose_name = 'Status de Fabricação'
        verbose_name_plural = 'Status de Fabricação'


class Statusvenda(models.Model):
    pkid_status = models.AutoField(primary_key=True)
    descricaostatus = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True


class Telefone(models.Model):
    pkid_telefone = models.AutoField(primary_key=True)
    fkid_pessoa = models.ForeignKey(
        'Pessoa', on_delete=models.CASCADE,
        verbose_name='Pessoa')
    ddi = models.CharField('DDI', max_length=2, default=55)
    ddd = models.CharField('DDD', max_length=2)
    numero = models.CharField('Número', max_length=15)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return f'{self.fkid_pessoa.nomecompleto_razaosocial} ({self.ddd}){self.numero}'

    class Meta:
        managed = True
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'


class Unidademedida(models.Model):
    pkid_unidademedida = models.AutoField(primary_key=True)
    unidademedida = models.CharField('Unidade', max_length=50)
    hide = models.BooleanField(default=0)

    def __str__(self):
        return self.unidademedida

    class Meta:
        managed = True
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'


class Usuario(models.Model):
    pkid_usuario = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(max_length=45)
    login = models.CharField(unique=True, max_length=45)
    senha = models.CharField(max_length=45)
    dt_importacao = models.DateTimeField()
    dt_alteracao = models.DateTimeField()
    hide = models.TextField(default=0)

    class Meta:
        managed = True


class Usuarioalteracao(models.Model):
    pkid_usuario_alteracao = models.AutoField(primary_key=True)
    dt_alteracao = models.DateTimeField()
    tipo_alteracao = models.TextField()

    class Meta:
        managed = True
