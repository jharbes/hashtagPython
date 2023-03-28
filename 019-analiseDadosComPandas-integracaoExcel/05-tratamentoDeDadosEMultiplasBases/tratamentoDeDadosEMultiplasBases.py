"""

# Comparando, Tratando e Mesclando DataFrames

## Objetivo

Vamos modificar os IDs para os nomes dos produtos, dos clientes e das lojas, para nossas análises ficarem mais intuitivas futuramente. Para isso, vamos criar um data frame com todos os detalhes.

- Usaremos o método merge para isso e, depois se quisermos, podemos pegar apenas as colunas que queremos do dataframe final.

"""

### Criando nossos dataframes


import pandas as pd

# **** as vezes precisaremos mudar o encoding. Possiveis valores para testar:
# encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'

vendasDf = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')

produtosDf=pd.read_csv(r'Contoso - Cadastro Produtos.csv',sep=';')

lojasDf=pd.read_csv(r'Contoso - Lojas.csv',sep=';')

clientesDf=pd.read_csv(r'Contoso - Clientes.csv',sep=';')


# usaremos o display/print para ver todos os dataframes
print(vendasDf)
print(produtosDf)
print(lojasDf)
print(clientesDf)

