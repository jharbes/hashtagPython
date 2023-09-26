"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.

"""
"""
## np.reshape()

A função `reshape()` é usada para alterar a forma de um array. Por exemplo, se você tem dados de vendas para 2 semanas e quer reorganizá-los em uma matriz de 2x7 (2 semanas, 7 dias por semana).

"""
import numpy as np

# Vendas diárias para 2 semanas
vendas = np.array([200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

# Reorganizar os dados em uma matriz de 2x7
vendas_reshaped = np.reshape(vendas, (2, 7))

print(vendas_reshaped) # [[200 220 250 210 300 280 230] [210 220 240 230 210 280 220]]


print(vendas.ndim) # 1

print(vendas.shape) # (14,)

print(vendas_reshaped.ndim) # 2

print(vendas_reshaped.shape) # (2, 7)

print(vendas_reshaped) # [[200 220 250 210 300 280 230] [210 220 240 230 210 280 220]]

print(vendas_reshaped[0]) # [200 220 250 210 300 280 230]

print(vendas_reshaped[1]) # [210 220 240 230 210 280 220]

print(vendas_reshaped[0][0]) # 200

print(vendas_reshaped[1][0]) # 210

print(vendas_reshaped.sum()) # 3300

print(vendas_reshaped.shape) # (2, 7)

print(vendas_reshaped) # [[200 220 250 210 300 280 230] [210 220 240 230 210 280 220]]


# axis=0 colunas, axis=1 linhas
print(vendas_reshaped.sum(axis=0)) # [410 440 490 440 510 560 450]

print(vendas_reshaped.sum(axis=1)) # [1690 1610]

print(vendas_reshaped.mean(axis=1)) # [241.42857143 230.        ]