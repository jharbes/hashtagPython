"""
## Exercício

Você é um analista de dados em uma empresa e conduziu uma pesquisa de satisfação do cliente durante uma semana. Você perguntou as clientes para classificar seu nível de satisfação com o serviço ao cliente em uma escala de 0 a 10. Você coletou respostas de 30 clientes por dia durante 7 dias, resultando em um total de 210 respostas.

No entanto, os dados que você recebeu estão em um array 1D de 210 elementos. Reorganize os dados de forma a ter as respostas por dia e faça uma análise descritiva básica, calculando a média geral de satisfação e a média diária.

"""
import numpy as np

# considere os seguintes dados aleatórios como início
rng = np.random.default_rng(seed=42)
respostas = rng.integers(low=0, high=10, size=210, endpoint=True)
print(respostas)
"""
[ 0  8  7  4  4  9  0  7  2  1  5 10  8  8  7  8  5  1  9  4  5  4  2 10
  8  7  4  9  5  4  4  2  1  6  9  0  9  9  3  6  1  8  7  3  0 10  4  9
  7  8  8  2  4  5  5  0  6  1  8  7 10  8  4 10  4  3  9  4  0  5  8  2
  5  1  7  5  3  2  6  7 10  4  1  9  6  7  1  3  8  9  4  8  9  4  9  3
  2  7  7  1  9  2  8  0  8  8  8  7  5  7  3  8  6  5  5  6  0  1  2  1
  4  7  7  5  9  6  0  8  6  6  6  6  0  6  8  3  6  0  3  4 10  2  3  4
 10  9  0  2  9  0  9  3 10  3  4  7  1  6  5  8 10  7  4  4  4  8  3  1
  3  0  1  0  8  7  7  5  7  1  9  5 10  1  5  7  5  4  1  4  2  3  7  6
  6  3 10  0  3  1  3 10  4  9  5  7  5  2  8 10  2  8]
"""




"""
O seguinte modelo pode ser pensado para os dados recebidos:

    dia 1 cliente 1, dia 1 cliente 2, dia 1 cliente 3, ...
    ... dia 7 cliente 28, dia 7 cliente 29, dia 7 cliente 30
    
Assim, podemos fazer um reshape:

"""
respostas_por_dia=respostas.reshape(7,-1)

print(respostas_por_dia)
"""
[[ 0  8  7  4  4  9  0  7  2  1  5 10  8  8  7  8  5  1  9  4  5  4  2 10
   8  7  4  9  5  4]
 [ 4  2  1  6  9  0  9  9  3  6  1  8  7  3  0 10  4  9  7  8  8  2  4  5
   5  0  6  1  8  7]
 [10  8  4 10  4  3  9  4  0  5  8  2  5  1  7  5  3  2  6  7 10  4  1  9
   6  7  1  3  8  9]
 [ 4  8  9  4  9  3  2  7  7  1  9  2  8  0  8  8  8  7  5  7  3  8  6  5
   5  6  0  1  2  1]
 [ 4  7  7  5  9  6  0  8  6  6  6  6  0  6  8  3  6  0  3  4 10  2  3  4
  10  9  0  2  9  0]
 [ 9  3 10  3  4  7  1  6  5  8 10  7  4  4  4  8  3  1  3  0  1  0  8  7
   7  5  7  1  9  5]
 [10  1  5  7  5  4  1  4  2  3  7  6  6  3 10  0  3  1  3 10  4  9  5  7
   5  2  8 10  2  8]]

"""

media_geral_de_satisfacao=respostas_por_dia.mean()

print("A média geral de satisfação foi de {:.2f}".format(media_geral_de_satisfacao)) # A média geral de satisfação foi de 5.15




media_geral_por_dia=respostas_por_dia.mean(axis=1)

print(media_geral_por_dia,end='\n\n') # [5.5        5.06666667 5.36666667 5.1        4.96666667 5. 5.03333333]

for i,resposta in enumerate(media_geral_por_dia):
    print('A média diária para o {}º dia foi de {:.2f}'.format(i+1,resposta))

"""
A média diária para o 1º dia foi de 5.50
A média diária para o 2º dia foi de 5.07
A média diária para o 3º dia foi de 5.37
A média diária para o 4º dia foi de 5.10
A média diária para o 5º dia foi de 4.97
A média diária para o 6º dia foi de 5.00
A média diária para o 7º dia foi de 5.03
"""