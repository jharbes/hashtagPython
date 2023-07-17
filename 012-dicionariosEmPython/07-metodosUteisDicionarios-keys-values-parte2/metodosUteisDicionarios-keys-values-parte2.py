"""
# Métodos úteis em dicionários

## items() dos dicionários

### Estrutura:

itens_dicionario = dicionario.items()

ou então:

for item in dicionario.items()
    cada item do dicionario em formato de tupla

"""

vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

vendas_tecnologia_items=vendas_tecnologia.items()


# - Quais produtos venderam mais de 5000 unidades?

# forma 1 -> usando apenas o dicionario e as chaves

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave]>5000:
        print(chave)

print('\n')

# forma 2 -> usando o dicionario.items()

for item in vendas_tecnologia_items:
    if item[1]>5000:
        print(item[0])

print('\n')
# ou

for produto,numero_itens in vendas_tecnologia_items:
    if numero_itens>5000:
        print(produto)