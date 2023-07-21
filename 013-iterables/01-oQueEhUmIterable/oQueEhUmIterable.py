"""
# O que é um iterable?

### Explicação não programadora

Um iterable é uma estrutura que armazena dados que pode ser "iterada" ou seja, que você pode fazer um loop como um for dentro dela e ir passando de item a item. É como se fosse um tipo de lista de coisas que você pode ir olhando cada um dos elementos dentro dela.

Até agora as principais que vimos foram:

- Vamos falar nesse módulo de algumas outras, mas esse conceito é importante porque várias funções do python usam isso para explicar como as coisas funcionam. Então é importante que quando você ler o termo "iterable" você entenda o que estão falando: "é tipo uma lista de coisas que eu posso percorrer e fazer alguma ação com cada uma das coisas dentro dessa lista"

"""

# Listas

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']

for produto in produtos:
    print(produto)




# Strings

texto = 'lira@gmail.com'

for ch in texto:
    print(ch)




# Tuplas

produtos = ('iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus')

for produto in produtos:
    print(produto)




# Dicionários

vendas_produtos = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

for produto in vendas_produtos:
    print(produto)
    #print('{}: {} unidades'.format(produto, vendas_produtos[produto]))