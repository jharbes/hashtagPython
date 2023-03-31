"""

# Exportando do DataFrame para um csv

### Depois de modificar um DataFrame, ou até criar um, muitas vezes podemos exportar esse dataframe para um csv

No pandas, isso é bem simples:

dataframe.to_csv('nome_do_arquivo.csv', sep=',')

"""

### Lendo um DataFrame, modificando ele e exportando

import pandas as pd

# importando os arquivos

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

# limpando apenas as colunas que queremos

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# mesclando e renomeando os dataframes

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})

print(vendas_df)




# agora vamos criar o csv

# comentando pois o arquivo gerado tem mais de 100mb
# vendas_df.to_csv('Novo Vendas 2017.csv',sep=';')



### Criando um dicionário, transformando o dicionário em um DataFrame e Exportando para csv

vendas_produtos = {'iphone': [558147, 951642], 'galaxy': [712350, 244295], 'ipad': [573823, 26964], 'tv': [405252, 787604], 'máquina de café': [718654, 867660], 'kindle': [531580, 78830], 'geladeira': [973139, 710331], 'adega': [892292, 646016], 'notebook dell': [422760, 694913], 'notebook hp': [154753, 539704], 'notebook asus': [887061, 324831], 'microsoft surface': [438508, 667179], 'webcam': [237467, 295633], 'caixa de som': [489705, 725316], 'microfone': [328311, 644622], 'câmera canon': [591120, 994303]}


vendasProdutosDf=pd.DataFrame.from_dict(vendas_produtos)

# observe que as chaves do dicionario viram colunas e os valores do dicionario viram as linhas
print(vendasProdutosDf)


# com o orient='index' alteramos o dataframe fazendo com que as chaves sejam os indices e nao as colunas
vendasProdutosDf=pd.DataFrame.from_dict(vendas_produtos,orient='index')

print(vendasProdutosDf)


# vamos alterar os nomes das colunas para que nao fique 0 e 1
vendasProdutosDf=vendasProdutosDf.rename(columns={0:'Vendas 2019',1:'Vendas 2020'})
print(vendasProdutosDf)

# encoding para utilizacao correta de caracteres especiais
vendasProdutosDf.to_csv(r'Novo Vendas Produtos.csv',sep=',',encoding='latin1')