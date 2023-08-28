"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Mas suas capacidades vão muito além disso, como veremos nos nestes vídeos. E ele serve como uma boa base para o Pandas, que é uma das bibliotecas mais populares para análise de dados em Python.

## Instalação

Para instalar o NumPy, você pode usar o comando `pip install numpy` no terminal.

# pip install numpy


## Arrays NumPy

Um array é uma estrutura de dados que armazena valores de um mesmo tipo. Em Python, isso é uma grande vantagem porque economiza espaço e permite operações mais eficientes.


## Resumindo

Aqui estão algumas diferenças chave entre listas e arrays:

1. **Tipo de dados**: As listas podem armazenar elementos de tipos diferentes ao mesmo tempo, enquanto os arrays armazenam elementos do mesmo tipo.

2. **Operações matemáticas**: Você pode realizar operações matemáticas em todos os elementos de um array de uma vez, o que não é possível com listas.

3. **Desempenho**: Arrays são mais eficientes em termos de memória e desempenho do que listas quando se trabalha com grandes quantidades de dados numéricos.

4. **Funcionalidades**: NumPy arrays vêm com várias funções integradas para operações matemáticas e científicas, como média, soma, multiplicação de matrizes, etc., que não estão disponíveis com listas.


"""
import numpy as np

array = np.array([1, 2, 3, 4, 5])

print(array) # [1 2 3 4 5]



"""
É relevante entender a diferença entre uma lista e um array.

Uma **lista** é uma das estruturas de dados mais básicas em Python. Ela pode conter qualquer tipo de elementos, como números, strings, outras listas, e todos eles podem ser de tipos diferentes. Por exemplo:

"""
lista = [1, 'dois', 3.0]

print(lista) # [1, 'dois', 3.0]

print(type(lista)) # <class 'list'>

for elemento in lista:
    print(type(elemento))

"""
output:
<class 'int'>
<class 'str'>
<class 'float'>

"""



# Um **array**, por outro lado, é uma estrutura de dados que também armazena elementos, mas todos os elementos devem ser do mesmo tipo. Se você tentar criar um array com elementos de tipos diferentes, o NumPy irá convertê-los todos para o tipo mais geral. Por exemplo:

import numpy as np

array = np.array(lista)

# observe que se tornou um array de strings
print(array) # ['1' 'dois' '3.0']

print(type(array)) # <class 'numpy.ndarray'>

for elemento in array:
    print(type(elemento))
"""
output:
<class 'numpy.str_'>
<class 'numpy.str_'>
<class 'numpy.str_'>
"""

# <U32 quer dizer que o tipo dos elementos sao caracteres unicode que ocupam 32 bits de memoria
print(array.dtype) # <U32



"""

## Operações Matemáticas

Se você tentar adicionar um número a todos os elementos de uma lista, você receberá um erro.

"""
lista = [1, 2, 3, 4, 5]
# nova_lista = lista + 1  # Isso causará um erro
# print(nova_lista)


nova_lista = []

for numero in lista:
    nova_lista.append(numero + 1)

print(nova_lista) # [2, 3, 4, 5, 6]



# Com um array NumPy, você pode adicionar (ou subtrair, multiplicar, dividir) um número a todos os elementos de uma vez.

import numpy as np

array = np.array([1, 2, 3, 4, 5])
novo_array = array + 1  # Isso adicionará 1 a todos os elementos

print(novo_array) # [2 3 4 5 6]



"""
## Desempenho

Para grandes quantidades de dados, os arrays NumPy são significativamente mais eficientes em termos de memória e desempenho do que as listas Python. Aqui está um exemplo que demonstra isso:

"""
import numpy as np
import time

# Crie uma lista e um array com 10 milhões de números
lista = list(range(1, 10_000_001))
array = np.array(range(1, 10_000_001))

# Calcule a soma de todos os números na lista
inicio = time.time()
soma_lista = sum(lista)
fim = time.time()

print(f"Tempo para somar todos os números na lista: {fim - inicio} segundos") # Tempo para somar todos os números na lista: 0.18758249282836914 segundos


# Calcule a soma de todos os números no array
inicio = time.time()
soma_array = np.sum(array)
fim = time.time()

print(f"Tempo para somar todos os números no array: {fim - inicio} segundos") # Tempo para somar todos os números no array: 0.0051462650299072266 segundos