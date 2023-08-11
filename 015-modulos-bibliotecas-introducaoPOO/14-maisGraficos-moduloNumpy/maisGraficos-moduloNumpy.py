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
print(type(vendas)) # <class 'numpy.ndarray'>

print(meses)
print(type(meses)) # <class 'numpy.ndarray'>



plt.plot(meses,vendas) # define meses no eixo x e vendas no eixo y

plt.axis([0,50,0,max(vendas)+200]) # define o dominio de x entre 0 e 50 e a imagem em 0 a numero maximo de vendas +200

plt.xlabel('Meses') # ajusta o label do eixo x para 'Meses'

plt.ylabel('Vendas') # ajusta o label do eixo y para 'Vendas'

plt.show()




# Editando o grafico de linha

# mudando a linha para apenas os marcadores (sem a continuidade da linha, apenas os pontos existentes)

plt.plot(meses,vendas,'ro') # define meses no eixo x e vendas no eixo y, o parametro 'ro' define o gradico como marcadores conforme explicado acima

plt.axis([0,50,0,max(vendas)+200]) # define o dominio de x entre 0 e 50 e a imagem em 0 a numero maximo de vendas +200

plt.xlabel('Meses') # ajusta o label do eixo x para 'Meses'

plt.ylabel('Vendas') # ajusta o label do eixo y para 'Vendas'

plt.show()