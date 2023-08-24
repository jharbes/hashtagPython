"""
# Adicionando Colunas, Modificando Colunas e Valores
"""

### Vamos pegar o nosso dataframe novamente

import pandas as pd
import numpy as np


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
vendas_df.info()




### Agora, e se quisermos acrescentar uma coluna com o mês, o dia e o ano de cada venda (e não só a data completa)

# transformando a data da venda no formato object (texto) para o formato datetime, com o formato mostramos o que cada elemento é e separamos de acordo com as barras que ja estao nas informacoes do dataframe (poderia ser diferente)
vendas_df['Data da Venda']=pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y')

print(vendas_df)
vendas_df.info()

# Conforme os dicionarios em python, caso uma coluna nao exista ele cria a coluna
vendas_df['Ano da Venda']=vendas_df['Data da Venda'].dt.year
vendas_df['Mes da Venda']=vendas_df['Data da Venda'].dt.month
vendas_df['Dia da Venda']=vendas_df['Data da Venda'].dt.day

print(vendas_df)