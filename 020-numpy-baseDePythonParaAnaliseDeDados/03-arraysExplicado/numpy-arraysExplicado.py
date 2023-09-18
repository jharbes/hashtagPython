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

# lembrar que o primeiro indice colocado é incluido, o segundo é excluido
print(array[1:4]) # [2 3 4]

# lembrar que a ultima posicao(-1) nao é incluido, logo o elemento 5 nao sera incluido
print(array[0:-1]) # [1 2 3 4]

# do primeiro elemento ate o ultimo(-1 que nao sera incluido conforme dito antes), porem andando de 2 em 2 
print(array[0:-1:2]) # [1 3]

# ao deixar em branco a posicao do ultimo elemento estamos informando que desejamos que o ultimo elemento do array SEJA INCLUIDO
print(array[0::2]) # [1 3 5]

# tambem nao somos obrigados a colocar o ZERO no inicio para informar que queremos o vetor desde o inicio, podemos suprimir essa informacao e ele continuara a comecar desde o inicio do vetor
print(array[::2]) # [1 3 5]

# a ausencia do ultimo elemento usará o valor DEFAULT para o PASSO que é 1
print(array[::]) # [1 2 3 4 5]

# nesse caso apenas informamos que o PASSO será de -1, ou seja, andará de trás pra frente
print(array[::-1]) # [5 4 3 2 1]