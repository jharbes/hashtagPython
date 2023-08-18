"""
# Um exemplo prático de List Comprehension

### O que faríamos se quisermos ordenar 2 listas "relacionadas"

"""
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

lista_aux = list(zip(vendas_produtos, produtos))
lista_aux.sort(reverse=True)
produtos = [produto for vendas, produto in lista_aux]

print(produtos) # ['microondas', 'iphone', 'vinho', 'cafeiteira']