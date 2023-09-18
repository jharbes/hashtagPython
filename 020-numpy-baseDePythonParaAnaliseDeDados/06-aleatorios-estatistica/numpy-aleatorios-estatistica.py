"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.

"""

## Números aleatórios e estatística básica  

import numpy as np

# Crie um gerador de números aleatórios.
rng = np.random.default_rng()

numero_aleatorio = rng.random()
print(numero_aleatorio) # 0.016581514099106687


array_aleatorio = rng.random(3)
print(array_aleatorio) # [0.81672889 0.64768309 0.71536078]


print(array_aleatorio * 10) # [4.04164911 6.61453945 6.36450206]




"""
Vamos criar um cenário onde esses dados aleatórios podem ser úteis para uma análise de vendas.

Suponha que você seja um analista de vendas em uma empresa e queira entender melhor o desempenho das vendas de um produto específico. No entanto, você não tem acesso aos dados reais de vendas, então você decide gerar alguns dados de vendas aleatórios para realizar sua análise.

"""
# Gere dados de vendas falsos para 30 dias
# Vamos supor que as vendas de um produto podem variar de 50 a 200 por dia 

rng = np.random.default_rng(seed=42)
dados_vendas = rng.integers(low=50, high=200, size=30)

print(dados_vendas) # [ 63 166 148 115 114 178  62 154  80  64 128 196 160 164 157 167 126  69 175 117 125 105  77 189 167 146 110 173 131 116]



# Agora, você pode usar esses dados para realizar várias análises. Por exemplo, você pode querer saber qual foi o dia com as vendas mais altas, as vendas mais baixas, ou a média de vendas durante o mês. Aqui está como você pode fazer isso:

print(np.max(dados_vendas)) # 196

print(np.argmax(dados_vendas)) # 11

# Dia com as vendas mais altas
vendas_maximas = np.max(dados_vendas)
dia_vendas_maximas = np.argmax(dados_vendas) + 1

print(f"O dia com as vendas mais altas foi o dia {dia_vendas_maximas} com {vendas_maximas} vendas.") # O dia com as vendas mais altas foi o dia 12 com 196 vendas.


# Dia com as vendas mais baixas
vendas_minimas = np.min(dados_vendas)
dia_vendas_minimas = np.argmin(dados_vendas) + 1

print(f"O dia com as vendas mais baixas foi o dia {dia_vendas_minimas} com {vendas_minimas} vendas.") # O dia com as vendas mais baixas foi o dia 7 com 62 vendas.


# Média de vendas durante o mês
media_vendas = np.mean(dados_vendas)
print(f"A média de vendas durante o mês foi de {media_vendas} vendas por dia.") # A média de vendas durante o mês foi de 131.4 vendas por dia.


print(np.median(dados_vendas)) # 129.5


print(np.percentile(dados_vendas, 50)) # 129.5