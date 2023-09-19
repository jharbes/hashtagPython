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