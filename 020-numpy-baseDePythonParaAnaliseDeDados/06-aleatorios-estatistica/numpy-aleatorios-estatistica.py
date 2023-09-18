"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.

"""
"""
Breve resumo e conceitos simplificados das funções estatísticas citadas:

1. Mediana:
A mediana é um valor que divide um conjunto de dados em duas partes iguais. Para encontrá-la, você deve organizar os dados em ordem crescente ou decrescente e escolher o valor do meio. Se houver um número ímpar de dados, a mediana será exatamente o valor central. Se houver um número par de dados, a mediana será a média dos dois valores do meio.

2. Percentil:
O percentil é uma medida estatística que indica a posição relativa de um dado dentro de um conjunto de dados. Ele informa a porcentagem de valores que estão abaixo desse dado. Por exemplo, o percentil 50 (também conhecido como mediana) divide os dados em duas partes iguais, com 50% dos valores abaixo dele e 50% acima.

3. Desvio padrão:
O desvio padrão é uma medida que indica o quão dispersos os valores de um conjunto de dados estão em relação à média. Ele mostra a variabilidade dos dados em relação ao valor médio. Um desvio padrão maior indica que os dados estão mais espalhados, enquanto um desvio padrão menor indica que os dados estão mais próximos da média.

4. Variância:
A variância é outra medida de dispersão que indica o quão distantes os valores de um conjunto de dados estão da média. Ela é calculada como a média dos quadrados das diferenças entre cada valor e a média. A variância fornece uma medida da dispersão total dos dados, independentemente de serem maiores ou menores que a média.

Essas medidas são amplamente utilizadas na estatística para resumir e analisar conjuntos de dados. Elas fornecem informações valiosas sobre a distribuição, a variabilidade e a posição dos dados, permitindo uma compreensão mais completa dos mesmos.

"""
## Números aleatórios e estatística básica  

import numpy as np

# Crie um objeto gerador de números aleatórios. (recomendação dos criadores da biblioteca), nesse caso o gerador PADRÃO do numpy (default_rng())
rng = np.random.default_rng()


# o random, por padrao, sempre gera numeros entre 0 e 1
numero_aleatorio = rng.random()
print(numero_aleatorio) # 0.016581514099106687

numero_aleatorio2=rng.random()*10
print(numero_aleatorio2) # 6.567096646996188


array_aleatorio = rng.random(3)
print(type(array_aleatorio)) # <class 'numpy.ndarray'>
print(array_aleatorio) # [0.81672889 0.64768309 0.71536078]


print(array_aleatorio * 10) # [4.04164911 6.61453945 6.36450206]




"""
Vamos criar um cenário onde esses dados aleatórios podem ser úteis para uma análise de vendas.

Suponha que você seja um analista de vendas em uma empresa e queira entender melhor o desempenho das vendas de um produto específico. No entanto, você não tem acesso aos dados reais de vendas, então você decide gerar alguns dados de vendas aleatórios para realizar sua análise.

"""
# Gere dados de vendas falsos para 30 dias
# Vamos supor que as vendas de um produto podem variar de 50 a 200 por dia 

rng = np.random.default_rng(seed=42)


# .integers() define que serao numeros inteiros, low=numero minimo, high=numero maximo, size= tamanho do array
dados_vendas = rng.integers(low=50, high=200, size=30)

print(type(dados_vendas)) # <class 'numpy.ndarray'>
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


print(np.std(dados_vendas)) # 39.305300745149715


print(np.var(dados_vendas)) # 1544.9066666666665