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




### Vamos tirar as colunas inúteis do clientes_df ou pegar apenas as colunas que quisermos

# .drop([coluna1, coluna2, coluna3]) -> retira as colunas: coluna1, coluna2, coluna3

clientesDf=clientesDf.drop(['Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10'],axis=1) # retirando as colunas com esses nomes , axis=1 é coluna

clientesDf=clientesDf[['ID Cliente','E-mail']] # agora criamos uma nova tabela clientesDf, so que essa só possuira as colunas 'ID Cliente' e 'E-mail'

produtosDf=produtosDf[['ID Produto','Nome do Produto']] # produtosDf agora só tera as colunas 'ID Produto' e 'Nome do Produto'

lojasDf=lojasDf[['ID Loja','Nome da Loja']] # lojasDf agora so possuira as colunas 'ID Loja' e 'Nome da Loja'


print(produtosDf)




### Agora vamos juntar os dataframes para ter 1 único dataframe com tudo "bonito"

# novo_dataframe = dataframe1.merge(dataframe2, on='coluna')

# - Obs: O merge precisa das colunas com o mesmo nome para funcionar. Se não tiver, você precisa alterar o nome da coluna com o .rename

# dataframe.rename(columns={'coluna1': 'novo_coluna_1'})


# juntando os dataframes, observe que no final do arquivo estarao as informacoes 'extras' vindas das tabelas anexadas => nome do produto, nome da loja e email, com a correlacao adequada de id de cada um
vendasDf=vendasDf.merge(produtosDf,on='ID Produto')
vendasDf=vendasDf.merge(lojasDf,on='ID Loja')
vendasDf=vendasDf.merge(clientesDf,on='ID Cliente')


# exibindo o dataframe final
print(vendasDf)


# vamos renomear o e-mail para ficar claro que é do cliente
# dataframe.rename(columns={'coluna1': 'novo_coluna_1'})
vendasDf=vendasDf.rename(columns={'E-mail': 'E-mail do Cliente'})

print(vendasDf)