"""
## Exercício 1

Você é um gerente de vendas e tem os dados de vendas de um produto para os últimos 7 dias em uma lista: `[127, 90, 201, 150, 210, 220, 115]`. Calcule a média de vendas durante a semana.

"""
import numpy as np

dados = [127, 90, 201, 150, 210, 220, 115]

dados=np.array(dados)
media=np.mean(dados)
print('A média das vendas do produto foi {:.2f}'.format(media))




"""
## Exercício 2

Você é um analista financeiro e tem os preços de fechamento diário de uma ação para a última semana em um array NumPy: `precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])`. Calcule o preço máximo, mínimo e a variação de preço durante a semana.

"""
precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])

preco_maximo=np.max(precos)
preco_minimo=np.min(precos)
variacao_preco=preco_maximo-preco_minimo

print('O preço máximo foi de R$ {}, o preço mínimo foi de R$ {} e a variação entre os dois foi de R$ {:.2f}}'.format(preco_maximo,preco_minimo,variacao_preco))




"""
## Exercício 3

Sua loja vendeu em um dia 5 unidades do *Produto A*, 3 unidades do *Produto B* e 2 unidades do *Produto C*. Os preços dos produtos são, respectivamente, 100, 200 e 50 reais. Calcule o total de vendas do dia.

"""
quantidades = np.array([5, 3, 2])
precos = np.array([100, 200, 50])