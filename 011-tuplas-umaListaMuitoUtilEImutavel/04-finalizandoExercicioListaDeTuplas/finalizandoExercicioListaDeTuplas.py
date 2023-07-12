"""
# Aplicação de Tupla - Lista de Tuplas

### Estrutura:

Além de casos como o do enumerate, em que usamos uma função para transformar itens em tuplas porque isso ajuda o nosso código, temos também listas de tuplas como algo comum dentro do Python.

lista = [
    tupla1,
    tupla2,
    tupla3,
    ]
    
ou seja

lista = [
    (valor1, valor2, valor3),
    (valor4, valor5, valor6),
    (valor7, valor8, valor9),
    ]

"""

### Exemplo:

# Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.

# Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:

vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]




# - Qual foi o faturamento de IPhone no dia 20/08/2020?
# - Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?

# faturamento_iphone_200820=vendas[0][4]*vendas[0][5]+vendas[0][4]*vendas[1][5]
# print(faturamento_iphone_200820)

# ou

faturamento_iphone_200820=0
for item in vendas:
    data,produto,cor,capacidade,unidades,valor_unitario=item
    if data=='20/08/2020' and produto=='iphone x':
        faturamento_iphone_200820+=unidades*valor_unitario

print(faturamento_iphone_200820)




# vendas_21082020=[item for item in vendas if item[0]=='21/08/2020']
# print(vendas_21082020)

# unidades=-1
# produto_maior_venda=''
# for venda in vendas_21082020:
#     if venda[4]>unidades:
#         produto_maior_venda='{} {} {}'.format(venda[1],venda[2],venda[3])

# print(produto_maior_venda)

# ou

maior_unidades=-1
produto_mais_vendido=[]
for item in vendas:
    data,produto,cor,capacidade,unidades,valor_unitario=item
    if data=='21/08/2020' and unidades>maior_unidades:
        maior_unidades=unidades
        produto_mais_vendido=[]
        produto_mais_vendido.append(item)
    elif data=='21/08/2020' and unidades==maior_unidades:
        produto_mais_vendido.append(item)


for item in produto_mais_vendido:
    data,produto,cor,capacidade,unidades,valor_unitario=item
    print('{} {} {}'.format(produto,cor,capacidade))