"""
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.

"""
"""
## Filtros e np.where()

A função `np.where()` é muito útil para fazer uma seleção condicional de elementos de um array (FUNCIONANDO COMO UM FILTRO). Por exemplo, em uma empresa, você pode querer identificar quais funcionários têm salários acima da média.

"""
import numpy as np

# Salários dos funcionários
salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

# Calcular a média salarial
media_salarial = np.mean(salarios)

print(media_salarial) # 3714.285714285714



# Identificar funcionários com salários acima da média
# retorna um array do numpy com os indices onde a condicao é verdadeira, o dtype=int64 mostra que os elementos sao do tipo int (inteiros de 64 bits)
funcionarios_acima_media = np.where(salarios > media_salarial)

print(funcionarios_acima_media) # (array([2, 4, 5, 6], dtype=int64),)


print(salarios[funcionarios_acima_media]) # [4000 4500 4000 5000]


print(salarios[salarios > media_salarial]) # [4000 4500 4000 5000]


print(salarios[salarios >= 4000]) # [4000 4500 4000 5000]


print(np.where(salarios > media_salarial, 'acima da média', 'abaixo da média')) # ['abaixo da média' 'abaixo da média' 'acima da média' 'abaixo da média' 'acima da média' 'acima da média' 'acima da média']



# dar bônus de 10% para os funcionários com salários abaixo da média
salarios_bonus = np.where(salarios < media_salarial, salarios * 1.1, salarios)

print(salarios) # [3000 3500 4000 2000 4500 4000 5000]

print(salarios_bonus) # [3300. 3850. 4000. 2200. 4500. 4000. 5000.]



# considerando novamente nossos salários originais
print(salarios) # [3000 3500 4000 2000 4500 4000 5000]


# filtrar os salários entre 3000 e 4500 com where
print(np.where((salarios >= 3000) & (salarios <= 4500))) # (array([0, 1, 2, 4, 5], dtype=int64),)



salarios_ajustados = np.where((salarios >= 3000) & (salarios <= 4500), salarios * 1.05, salarios)
print(salarios_ajustados) # [3150. 3675. 4200. 2000. 4725. 4200. 5000.]


# filtrar os salários abaixo de 3000 ou acima de 4500 com where
print(np.where((salarios_ajustados < 3000) | (salarios_ajustados > 4500))) # (array([3, 4, 6], dtype=int64),)



salarios_ajustados = np.where((salarios_ajustados < 3000) | (salarios_ajustados > 4500), salarios_ajustados * 1.1, salarios_ajustados)
print(salarios_ajustados) # [3150.  3675.  4200.  2200.  5197.5 4200.  5500. ]