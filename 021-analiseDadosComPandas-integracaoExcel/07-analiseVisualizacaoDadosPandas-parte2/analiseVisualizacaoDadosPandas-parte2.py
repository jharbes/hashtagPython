"""

# Resumos e um pouco de Visualização no pandas


## Resumo

Vamos ver alguns métodos para analisar nossas tabelas (dataframes)

Além disso, vamos usar os plot de gráfico padrões do pandas, mas no projeto de DataScience veremos outras mais bonitas e também muito práticas.

OBS: O pandas usa o matplotlib (que vimos na seção de "módulos e bibliotecas") para plotar gráficos.<br>
Se quiser personalizar mais do que o padrão do pandas, importe o matplotlib e use os métodos do matplotlib

"""

# - Preparando as bases de dados (o que fizemos na última aula)

import pandas as pd
import matplotlib.pyplot as plt

# importando os arquivos
vendasDf = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtosDf = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojasDf = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientesDf = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

# limpando apenas as colunas que queremos
clientesDf = clientesDf[['ID Cliente', 'E-mail']]
produtosDf = produtosDf[['ID Produto', 'Nome do Produto']]
lojasDf = lojasDf[['ID Loja', 'Nome da Loja']]

# mesclando e renomeando os dataframes
vendasDf = vendasDf.merge(produtosDf, on='ID Produto')
vendasDf = vendasDf.merge(lojasDf, on='ID Loja')
vendasDf = vendasDf.merge(clientesDf, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})
print(vendasDf)




### Qual cliente que comprou mais vezes?

# - Usaremos o método .value_counts() para contar quantas vezes cada valor do Dataframe aparece
# - Usaremos o método .plot() para exibir um gráfico

frequenciaClientes=vendasDf['E-mail do Cliente'].value_counts()
print(frequenciaClientes)
# frequenciaClientes.plot() # grafico completo

# frequenciaClientes[:5].plot() # aqui escolhemos os cinco primeiros clientes da tabela

# frequenciaClientes[:5].plot(figsize=(15,5)) # escolhemos com figsize o tamanho do grafico a ser mostrado

frequenciaClientes[:5].plot(figsize=(15,5),yticks=range(0,100,5)) # aqui colocamos o eixo y para mostrar valores de 0 a 100 de 5 em 5, alem das outras marcacoes ja feitas

# plt.show() # mostra o grafico 




### Qual a Loja que mais vendeu?

# - Usaremos o .groupby para agrupar o nosso dataframe, de acordo com o que queremos (somando as quantidades de vendas, por exemplo)

vendasLojas=vendasDf.groupby('Nome da Loja').sum()

# vendasLojas=vendasLojas['Quantidade Vendida'] # formatacao diferente
# display(vendasLojas)

vendasLojas=vendasLojas[['Quantidade Vendida']] # nao precisamos passar o nome da loja pois ele se tornou o indice no novo dataframe

print(vendasLojas) # importante notar que a tabela mostra o valor vendido de cada loja mas ainda nao esta ordenado de maneira crescente ou decrescente




# - Agora precisamos pegar o maior valor. Temos 2 formas:
#    1. Ordenar o dataframe em ordem decrescente de Quantidade Vendida
#        - Método .sort_values
#    2. Pegar o Maior valor diretamente
#        - Métodos .max() e .idxmax()

# ordenando o dataframe

vendasLojas=vendasLojas.sort_values('Quantidade Vendida', ascending=False) # ascending=False para que ele ordene de forma decrescente

# podemos plotar em um gráfico

vendasLojas[:5].plot(figsize=(15,5),kind='bar') # figsize ajusta o tamanho do grafico, kind ajusta para um grafico de barra em vez de linha

plt.show() # mostra todos os graficos gerados pelo codigo


print(vendasLojas)


# pegando o maior valor e se índice

maiorValor=vendasLojas['Quantidade Vendida'].max()

melhorLoja=vendasLojas['Quantidade Vendida'].idxmax()

print(f'{melhorLoja=} {maiorValor=}')




### Qual produto que menos vendeu?

#- Já temos uma lista criada para isso, basta verificarmos o final da lista (já que ela está ordenada) ou então usarmos os métodos:
#    1. min()
#    2. idxmin()

print(vendasLojas[-1:]) # nao funciona so com o -1 pois os dataframes nao aceitam apenas o indice, aceitam apenas ranges

# ou

print(vendasLojas['Quantidade Vendida'].idxmin())