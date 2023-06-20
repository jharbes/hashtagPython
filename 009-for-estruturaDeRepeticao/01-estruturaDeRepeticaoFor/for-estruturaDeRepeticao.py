"""
# Estrutura de Repetição: for

### Funcionamento:

for i in range(n):
    repetir código n vezes

"""

for i in range(5):
    print('lira')

"""
lira
lira
lira
lira
lira
"""

for i in range(5):
    print(i)

"""
0
1
2
3
4
"""

# - Imagine que você está construindo uma automação para enviar todo dia por e-mail um resumo da produção de uma fábrica. Construa um código que exiba a quantidade produzida de cada os produto nesse "e-mail"

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

for i in range(len(produtos)):
    print('{} unidades produzidas de {}'.format(producao[i],produtos[i]))

"""
15000 unidades produzidas de coca
12000 unidades produzidas de pepsi
13000 unidades produzidas de guarana
5000 unidades produzidas de sprite
250 unidades produzidas de fanta
"""