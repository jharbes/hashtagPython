"""
# Um exemplo prático de List Comprehension

### O que faríamos se quisermos ordenar 2 listas "relacionadas"

"""
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

# funcao zip une cada item das duas listas em uma tupla de dois elementos (venda_produto, produto) e formara um objeto zip, por isso vamos envolver na funcao list() para transformar esse objeto zip em uma lista
lista_aux = list(zip(vendas_produtos, produtos))
print(type(lista_aux)) # <class 'list'>


print(lista_aux) # [(1500, 'vinho'), (150, 'cafeiteira'), (2100, 'microondas'), (1950, 'iphone')]


# o sort fara a ordenacao de acordo com o PRIMEIRO item da tupla em questao, por isso colocamos o valor das vendas em primeiro lugar da tupla
lista_aux.sort(reverse=True)

print(lista_aux) # [(2100, 'microondas'), (1950, 'iphone'), (1500, 'vinho'), (150, 'cafeiteira')]


produtos = [produto for vendas, produto in lista_aux]

print(produtos) # ['microondas', 'iphone', 'vinho', 'cafeiteira']