"""
# Usando módulos para ajudar a resolver desafios

### Objetivo

- Muitas vezes algum módulo vai ajudar a gente a resolver um desafio que talvez até conseguíssemos resolver de outra forma.

### Exemplo

- Digamos que você está analisando todas as vendas dos produtos de tecnologia de um e-commerce e quer saber quais foram os 5 produtos que mais venderam (e suas respectivas quantidades de vendas) - ou seja, queremos descobrir um top 3 produtos de forma simples

"""
vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

vendas_tecnologia_sorted=sorted(vendas_tecnologia.items(),key=lambda x:x[1],reverse=True)

print(vendas_tecnologia_sorted[0:3]) # [('notebook dell', 17000), ('iphone', 15000), ('ps5', 14300)]


# outra maneira de resolver:


vendas_tecnologia2 = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

from collections import Counter

vendas_tecnologia2_sorted=Counter(vendas_tecnologia2)

print(vendas_tecnologia2_sorted) # Counter({'notebook dell': 17000, 'iphone': 15000, 'ps5': 14300, 'samsung galaxy': 12000, 'tv samsung': 10000, 'tv philco': 2500, 'notebook asus': 2450, 'tablet': 1720, 'ipad': 1000, 'notebook hp': 1000})

print(vendas_tecnologia2_sorted.most_common(3)) # [('notebook dell', 17000), ('iphone', 15000), ('ps5', 14300)]