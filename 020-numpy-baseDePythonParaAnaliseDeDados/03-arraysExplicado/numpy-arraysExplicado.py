"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.


## Instalação

Para instalar o NumPy, você pode usar o pip, que é o gerenciador de pacotes do Python.

```python
pip install numpy
```

## Arrays

Um array é uma estrutura de dados que armazena valores do mesmo tipo. Em Python, isso é uma grande vantagem porque economiza espaço e permite operações mais eficientes. Vamos criar um array.

"""
import numpy as np

# Criação de um array
array = np.array([1, 2, 3, 4, 5])

print(array) # [1 2 3 4 5]

print(array[0]) # 1

print(array[1:4]) # [2 3 4]

print(array[0:-1]) # [1 2 3 4]

print(array[0:-1:2]) # [1 3]

print(array[0::2]) # [1 3 5]

print(array[::2]) # [1 3 5]

print(array[::]) # [1 2 3 4 5]

print(array[::-1]) # [5 4 3 2 1]