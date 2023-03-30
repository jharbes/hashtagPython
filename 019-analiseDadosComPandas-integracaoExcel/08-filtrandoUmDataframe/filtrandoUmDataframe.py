"""

# Filtrando informações nos dataframes


## Resumo

Um dos grandes potenciais do pandas é para tratar condições.

E a forma com que analisamos condições no dataframe é diferente do que já fizemos até agora no curso, vamos ver como funciona.

"""

### - Preparando as bases de dados

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