"""
# Exibindo Gráficos no Python

### Importância

- Para exploração e visualização de dados, nada melhor do que usar gráficos para isso. Apesar do Python ser programação, gráficos facilitam d+ em qualquer projeto que trabalhe com dados.

### Estrutura

- Usaremos o módulo Matplotlib.pyplot, que é o módulo mais usado no Python. Existem outros, como o Seaborn e o Plotly, caso queira ver/usar

"""
vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']


# plotar o gráfico da forma mais simples

import matplotlib.pyplot as plt

# utiliza a lista 'vendas_meses' como base de dados para o grafico a ser mostrado
# foi informado apenas o eixo x, o eixo y sera os indices pois foi omitido
plt.plot(vendas_meses)

plt.show()




# - Adicionar um Label no eixo X ou eixo Y

# foi informado apenas o eixo x, o eixo y sera os indices pois foi omitido
plt.plot(vendas_meses)
 
plt.ylabel('Vendas') # coloca o label do eixo y de 'Vendas'
plt.xlabel('Meses') # coloca o label do eixo x de 'Meses'

plt.show()




# - Mudar os nomes dos meses

# foram informados os meses e os valores das vendas dos meses, eixo x e y respectivamente
plt.plot(meses,vendas_meses)

plt.ylabel('Vendas') # coloca o label do eixo y de 'Vendas'
plt.xlabel('Meses') # coloca o label do eixo x de 'Meses'

plt.show()




# - Ajeitando o Eixo

# foram informados os meses e os valores das vendas dos meses, eixo x e y respectivamente
plt.plot(meses,vendas_meses)

plt.ylabel('Vendas') # coloca o label do eixo y de 'Vendas'
plt.xlabel('Meses') # coloca o label do eixo x de 'Meses'

# o metodo axis informa qual sera o dominio e imagem representado no grafico, neste caso o eixo x do grafico ficara compreendido entre 0 e 12 e o eixo y entre 0 e 3000
# plt.axis([0,12,0,3000])

# ou

# plt.axis([0,12,0,max(vendas_meses)])

# ou

plt.axis([0,12,0,max(vendas_meses)+500])


plt.show()