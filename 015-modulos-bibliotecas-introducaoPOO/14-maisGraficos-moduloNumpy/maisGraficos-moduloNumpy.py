# Mais edições de Gráfico com MatplotLib

# importando o matplotlib
import matplotlib.pyplot as plt


# - Usando o módulo numpy para trabalhar com números

# importando o módulo numpy
import numpy as np




### Outros tipos de Gráfico:

# Linha

# gera numeros aleatorios de 1000 (inclusive) até 3000 (exclusive) na quantidade de 50 numeros, classe numpy.ndarrray
vendas = np.random.randint(1000, 3000, 50)

# gera os numeros de 1 (inclusive) até 51 (exclusive), funciona como um range mas seu retorno é um numpy.ndarray
meses = np.arange(1, 51)


print(vendas)
print(type(vendas))

print(meses)
print(type(meses))