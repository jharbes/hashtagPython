"""
# Transformando Listas em Dicionários e Function zip

### Estrutura:

- Dicionário com valores padrões:

dicionario = dict.fromkeys(lista_chaves, valor_padrao)

- Dicionário a partir de listas de tuplas:

dicionario = dict(lista_tuplas)

- Dicionário a partir de 2 listas:

Passo 1: Transformar listas em lista de tuplas com o método zip<br>
Passo 2: Transformar em dicionario

lista_tuplas = zip(lista1, lista2)<br>
dicionario = dict(lista_tuplas)

"""

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

lista_tuplas=zip(produtos,vendas)

print(lista_tuplas) # <zip object at 0x0000021AFB9DF2C0>
# print(list(lista_tuplas))

dicionario_produtos=dict(lista_tuplas)

print(dicionario_produtos) # {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}




# - Quanto vendemos de ipad?

# fazendo por listas

for i, produto in enumerate(produtos):
    if produto=='ipad':
        print(vendas[i])

# fazendo por dicionario

for chave in dicionario_produtos:
    if chave=='ipad':
        print(dicionario_produtos[chave])