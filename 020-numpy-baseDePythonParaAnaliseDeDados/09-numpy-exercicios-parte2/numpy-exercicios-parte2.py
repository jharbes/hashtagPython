"""
## Exercício

Você é um engenheiro de produção e tem os tempos de ciclo (em minutos) de uma linha de produção em um array NumPy. Seu trabalho é identificar quaisquer tempos de ciclo que estão dois desvios padrão acima ou abaixo da média. Use o seguinte array para sua análise: `tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])`. 

"""
import numpy as np

tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])
media = np.mean(tempos_ciclo) 

print(media) # 5.8


desvio_padrao=np.std(tempos_ciclo)
print(desvio_padrao) # 0.592546294487706

dois_desvio_padrao=2*desvio_padrao
print(dois_desvio_padrao) # 1.185092588975412


tempos_fora=tempos_ciclo[(tempos_ciclo<media-dois_desvio_padrao) | (tempos_ciclo>media+dois_desvio_padrao)]

print(tempos_fora) # [7.2]




### Bônus

condicao = ((tempos_ciclo > media + 2 * desvio_padrao) | (tempos_ciclo < media - 2 * desvio_padrao))

print(condicao) # [False False False False False False False  True False]

print(np.where(condicao)) # [False False False False False False False  True False]


contrario_condicao = ((tempos_ciclo <= media + 2 * desvio_padrao) & (tempos_ciclo >= media - 2 * desvio_padrao))

print(np.where(contrario_condicao)) # (array([0, 1, 2, 3, 4, 5, 6, 8], dtype=int64),)


# observe aqui que a resposta é identico ao exemplo anterior que é o inversao da condicao principal de todo o exercicio, o que queremos mostrar é que podemos negar uma condicao e conseguir o inverso dela apenas utilizando o caractere til (~) na frente dela
print(np.where(~condicao)) # (array([0, 1, 2, 3, 4, 5, 6, 8], dtype=int64),)

print(~condicao) # [ True  True  True  True  True  True  True False  True]


## IMPORTANTE!!
# Lembrar que no Python puro a negação é feita com not
print(not True) # False




### Bônus 2

rng = np.random.default_rng(seed=0)

# a opção de 'normal' utilizada abaixo faz com que os números gerados respeitem uma distribuição normal, onde o 'loc' será o valor da media, o 'scale' será o desvio padrão e o 'size' será o numero de elementos
tempos_gerados = rng.normal(loc=media, scale=desvio_padrao, size=100)

print(tempos_gerados) # array de 100 numeros


# observe que o valor da média não será EXATAMENTE IGUAL, será utilizado apenas como referência pois o algoritmo terá que acomodar todos os dados de maneira a respeitar dados referentes a uma distribuição normal
print(media) # 5.8
print(tempos_gerados.mean()) # 5.848053545223129


# os valores nao sao identicos pelos mesmos motivos explicados acima
print(desvio_padrao) # 0.592546294487706
print(tempos_gerados.std()) # 0.5701068395534514


# utilizando a mesma condicao do exercicio original
condicao = ((tempos_gerados > tempos_gerados.mean() + 2 * tempos_gerados.std()) | (tempos_gerados < tempos_gerados.mean() - 2 * tempos_gerados.std()))

print(np.where(condicao)) # (array([12, 69], dtype=int64),)

print(tempos_gerados[condicao]) # [4.42231163 4.49431839]