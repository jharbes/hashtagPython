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