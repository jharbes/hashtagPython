"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.

"""
"""
## np.reshape() - detalhes

A função `reshape()` é usada para alterar a forma de um array. Por exemplo, se você tem dados de vendas para 2 semanas e quer reorganizá-los em uma matriz de 2x7 (2 semanas, 7 dias por semana).

"""
import numpy as np

# Vendas diárias para 2 semanas
vendas = np.array([200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

# Reorganizar os dados em uma matriz de 2x7
vendas_reshaped = np.reshape(vendas, (2, 7))

print(vendas_reshaped) # [[200 220 250 210 300 280 230] [210 220 240 230 210 280 220]]


# observe que o reshaped nao altera o array antigo
print(vendas) # [200 220 250 210 300 280 230 210 220 240 230 210 280 220]


# o atributo ndim informa o NUMERO DE DIMENSOES do array
print(vendas.ndim) # 1

# informa a forma do array, nesse caso 14 de comprimento
# leia-se: a primeira dimensao do array tem tamanho 14
print(vendas.shape) # (14,)


# AXIS = EIXO
# axis=0 (coluna), axis=1 (linha)
print(vendas_reshaped.sum(axis=0)) # [410 440 490 440 510 560 450]


print(vendas_reshaped.sum(axis=1)) # # [1690 1610]


"""
## Exemplo

Considere que uma loja funciona de segunda a sábado, independentemente de feriados. Nos últimos 30 dias, teve o menor volume de vendas sendo 20 e o maior sendo 200. Crie uma simulação das vendas desses últimos 30 dias, separando por semanas. Calcule:

- o total de vendas por semana
- a média de vendas por semana
- a média de vendas por dia da semana

"""
rng = np.random.default_rng(seed=42)
vendas = rng.integers(low=20, high=200, size=30, endpoint=True)

print(vendas) # [ 36 160 138  99  98 175  35 146  56  37 115 196 153 157 149 162 112  43 171 101 110  87  53 187 161 136  92 168 118 100]