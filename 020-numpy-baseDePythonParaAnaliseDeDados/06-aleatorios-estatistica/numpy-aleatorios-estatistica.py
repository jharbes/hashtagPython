"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.

"""

## Números aleatórios e estatística básica  

import numpy as np

# Crie um gerador de números aleatórios.
rng = np.random.default_rng()

numero_aleatorio = rng.random()
print(numero_aleatorio)