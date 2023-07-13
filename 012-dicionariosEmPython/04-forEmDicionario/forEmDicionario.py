"""
# For nos Dicionarios

### Estrutura:

for chave in dicionario:
    faça alguma coisa

"""

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# demonstrando o for

for chave in vendas_tecnologia:
    print('{} : {}'.format(chave,vendas_tecnologia[chave]))

# output:

# iphone : 15000
# samsung galaxy : 12000
# tv samsung : 10000
# ps5 : 14300
# tablet : 1720
# ipad : 1000
# tv philco : 2500
# notebook hp : 1000
# notebook dell : 17000
# notebook asus : 2450




# - Qual o total de notebooks vendidos?

total_notebooks_vendidos=0

for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_notebooks_vendidos+=vendas_tecnologia[chave]

print('Total de notebooks vendidos foi de {}'.format(total_notebooks_vendidos)) # Total de notebooks vendidos foi de 20450