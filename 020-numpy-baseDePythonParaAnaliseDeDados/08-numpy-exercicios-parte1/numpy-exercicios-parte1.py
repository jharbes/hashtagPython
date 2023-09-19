"""
## Exercício

Você é um analista de RH e tem os salários de todos os funcionários da sua empresa em um array NumPy. Seu trabalho é identificar quantos funcionários ganham acima da média. Use o seguinte array para sua análise: `salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])`.

"""
import numpy as np

salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])


media_salarios=np.mean(salarios)

print(media_salarios) # 3455.5555555555557

acima_media=np.where(salarios>media_salarios)

print(type(acima_media)) # <class 'tuple'>
print(acima_media) # (array([2, 3, 5, 7, 8], dtype=int64),)


salarios_acima_media=salarios[salarios>media_salarios]
print(salarios_acima_media) # [3500 4000 4500 3800 4800]
print(type(salarios_acima_media)) # <class 'numpy.ndarray'>



# Faremos de três maneiras:

# length da lista salarios[acima_media]
print(len(salarios[acima_media])) # 5

# size do primeiro elemento da tupla resultante do where acima
print(acima_media[0].size) # 5

# somando as condicoes True do array
print(salarios>media_salarios) # [False False  True  True False  True False  True  True]
print(np.sum(salarios>media_salarios)) # 5