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

#limpando apenas as colunas que queremos
clientesDf = clientesDf[['ID Cliente', 'E-mail']]
produtosDf = produtosDf[['ID Produto', 'Nome do Produto']]
lojasDf = lojasDf[['ID Loja', 'Nome da Loja']]

#mesclando e renomeando os dataframes
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

plt.show() # mostra o grafico 