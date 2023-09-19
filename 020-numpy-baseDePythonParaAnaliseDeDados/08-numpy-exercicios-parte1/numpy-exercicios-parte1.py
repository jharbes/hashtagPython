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
# observe que a soma de True sempre será 1 e False sempre será zero (True == 1) (False == 0)
print(salarios>media_salarios) # [False False  True  True False  True False  True  True]
print(np.sum(salarios>media_salarios)) # 5




##### Observe abaixo que o somatório de Booleanos também funciona para listas simples do Python e não apenas para Arrays do Numpy

lista=[True, False, True, False]

# observe que a soma de True sempre será 1 e False sempre será zero (True == 1) (False == 0)
print(sum(lista)) # 2



lista2=[2<5,not True,5!=5,6==6]

# observe que a soma de True sempre será 1 e False sempre será zero (True == 1) (False == 0)
print(sum(lista2)) # 2




### Bônus

# Outras formas de fazer contagem
# IMPORTANTE***: Lembrar que salarios > media_salario é um array do Numpy

print(salarios>media_salarios) # [False False  True  True False  True False  True  True]


# A funcao np.count_nonzero() conta o numero de elementos que seja DIFERENTES do valor zero
print(np.count_nonzero(salarios > media_salarios)) # 5


# A funcao np.unique() retorna um array apenas com os valores ÚNICOS, ou seja, não repetidos
print(np.unique(salarios > media_salarios)) # [False  True]


# Agora com o argumento 'return_counts' ele retorna um tupla onde o primeiro elemento é o array numpy em si COM OS ELEMENTOS UNICOS e o segundo elemento será a contagem de cada um dos elementos quantas vezes se repete no array original, na mesma ordem que os elementos se encontram no aray resultante
print(np.unique(salarios > media_salarios, return_counts=True))

# fazendo o unpacking da tupla:
valores_unicos, contagem = np.unique(salarios > media_salarios, return_counts=True)

print(valores_unicos) # [False  True]
print(contagem) # [4 5]




### Bônus 2

# Criando 20 valores fictícios de salários com a mesma faixa anterior, tomando cuidado de outras pessoas gerarem os mesmos valores:

rng = np.random.default_rng(seed=42)

salarios_gerados = rng.integers(low=np.min(salarios), high=np.max(salarios), size=20)

print(salarios_gerados) # [2249 4167 3832 3228 3212 4404 2240 3952 2564 2263 3474 4731 4060 4131 4008 4200 3437 2358 4351 3261]




rng = np.random.default_rng(seed=42)

# agora estamos fazendo exatamente como o exemplo anterior, porem com o argumento 'endpoint=True' o que significa que o valor setado para o argumento 'high' será incluido entre os numeros aleatorios gerados, porque por default o valor de 'high' fica de fora do conjunto de numeros aptos a aleatoriedade
salarios_gerados = rng.integers(low=np.min(salarios), high=np.max(salarios), size=20, endpoint=True)

print(salarios_gerados) # [2249 4167 3833 3229 3212 4404 2240 3953 2564 2263 3474 4732 4060 4131 4009 4201 3437 2358 4352 3261]


print(np.mean(salarios_gerados)) # 3506.45


# as funções estatísticas também podem ser chamadas como métodos dos arrays, observe que a SINTAXE ESTÁ DIFERENTE
print(salarios_gerados.min()) # 2240
print(salarios_gerados.max()) # 4732
print(salarios_gerados.mean()) # 3506.45