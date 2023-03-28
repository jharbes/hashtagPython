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

# importando os arquivos
vendasDf = pd.read_csv(r'Contoso - Vendas  - 2017.csv', sep=';')
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