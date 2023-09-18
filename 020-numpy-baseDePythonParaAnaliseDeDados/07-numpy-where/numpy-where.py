"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.

"""
"""
## Filtros e np.where()

A função `np.where()` é muito útil para fazer uma seleção condicional de elementos de um array. Por exemplo, em uma empresa, você pode querer identificar quais funcionários têm salários acima da média.

"""
import numpy as np

# Salários dos funcionários
salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

# Calcular a média salarial
media_salarial = np.mean(salarios)

print(media_salarial) # 3714.285714285714



# Identificar funcionários com salários acima da média
funcionarios_acima_media = np.where(salarios > media_salarial)

print(funcionarios_acima_media) # (array([2, 4, 5, 6], dtype=int64),)



print(salarios[funcionarios_acima_media]) # [4000 4500 4000 5000]



print(salarios[salarios > media_salarial]) # [4000 4500 4000 5000]