"""
# Exercícios

## 1. Calculando % de uma lista

Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.

"""

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]


numero_vendedores_meta=0
maior_venda=0

for item in vendas:
    if item[1]>=10000:
        numero_vendedores_meta+=1
    if item[1]>maior_venda:
        maior_venda=item[1]




## Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?

print(maior_venda)

listaMaiorVendedores=[]

for item in vendas:
    if item[1]>=maior_venda:
        listaMaiorVendedores.append(item[0])

print('O maior vendedor é:\n{}'.format(listaMaiorVendedores))