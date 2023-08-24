"""
# List Comprehensions com if para "filtrar" itens

### Estrutura:

lista = [expressão for item in iterable if condicao]

"""
# - Digamos que eu queira criar uma lista de produtos que bateram a meta.

meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']




# Fazendo por For tradicional

vendas_produtos_meta_batida=[]
for i,produto in enumerate(produtos):
    if vendas_produtos[i]>=1000:
        vendas_produtos_meta_batida.append(produto)

print(vendas_produtos_meta_batida) # ['vinho', 'microondas', 'iphone']




# Fazendo por list comprehension

vendas_produtos_meta_batida2=[produto for i,produto in enumerate(produtos) if vendas_produtos[i]>=1000]

print(vendas_produtos_meta_batida2) # ['vinho', 'microondas', 'iphone']