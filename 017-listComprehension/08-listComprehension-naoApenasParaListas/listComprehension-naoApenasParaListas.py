"""
# List Comprehension não serve só para criar uma lista, serve para qualquer ação em iterable

### Exemplo:

"""
# - Vamos calcular quantos % das vendas o meu top 5 produtos representa das vendas totais

produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']


# - Fazendo por for

total_top5=0
for i,produto in enumerate(produtos):
    if produto in top5:
        total_top5+=vendas[i]


print(total_top5) # 8461

print('Top 5 representou {:0.1%} das vendas'.format(total_top5/sum(vendas))) # Top 5 representou 50.6% das vendas




# - Fazendo por list comprehension

total_top5=sum([vendas[i] for i,produto in enumerate(produtos) if produto in top5])

print(total_top5) # 8461

print('Top 5 representou {:0.1%} das vendas'.format(total_top5/sum(vendas))) # # Top 5 representou 50.6% das vendas