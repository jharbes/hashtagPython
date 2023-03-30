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




### E agora, caso a gente queira modificar 1 valor específico, como fazemos? Vamos importar novamente a base de produtos

novo_produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
print(novo_produtos_df.head())
# repare no .head() para pegar apenas os primeiros valores do dataframe (geralmente as primeiro 5 linhas), é bem comum esse uso para ter uma visão do que são os dados

print(novo_produtos_df.tail()) # igual ao .head() porem retornara os cinco ultimos items do dataframe




"""
### Antes de entrar no próximo exemplo, precisamos falar de 2 métodos:

    *** SE BASEIA NO VALOR DO INDICE E NAO DA POSICAO ***
    1. loc - permite pegar uma linha de acordo com o índice dela. Ele dá erro caso não encontre o índice. Isso é interessante principalmente quando o índice é uma informação relevante ao invés só do número do índice ou quando queremos pegar alguma linha específica do dataframe (ao invés de ir do início do dataframe até a linha 5, por exemplo).

        Também podemos usar como loc[índice_linha, índice_coluna] para acessar um valor específico e modificá-lo.


    *** SE BASEIA NA POSICAO DO ELEMENTO E NAO VALOR DO INDICE***
    2. iloc - enxerga o dataframe como linhas e colunas e consegue pegar o valor com um número de linha e um número de coluna. Repara que ele não analisa o valor do índice da linha e da coluna, apenas a posição importa.

        Uso: iloc[num_linha, num_coluna]
        
"""

# - Vendo na prática

# com esse comando transformamos a coluna 'Nome do Produto' no índice do dataframe
novo_produtos_df = novo_produtos_df.set_index('Nome do Produto')
print(novo_produtos_df.head())



# vamos pegar o preço produto Contoso Optical Wheel OEM PS/2 Mouse E60 Black

# por loc (valor do indice)
print(novo_produtos_df.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Black'])
print(novo_produtos_df.loc[['Contoso Optical Wheel OEM PS/2 Mouse E60 Black']])
print(novo_produtos_df.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Black', 'Preco Unitario'])

# por iloc (posica do indice)
print(novo_produtos_df.iloc[0])
print(novo_produtos_df.iloc[2, 5])
print(novo_produtos_df.iloc[2,0])
# print(novo_produtos_df.iloc[2,0].index())


print('\n--------EXERCICIO--------\n')

novo_produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')

### A empresa decidiu aumentar o preço do produto ID 873 (Contoso Wireless Laser Mouse E50 Grey) para 23 reais. Como fazemos, para modificar isso na nossa base?

novo_produtos_df=novo_produtos_df.set_index('ID Produto')
novo_produtos_df.loc[873,'Preco Unitario']=23

print(novo_produtos_df.loc[873,'Preco Unitario'])


print(novo_produtos_df.head())


# ou
print('------------------------')

novo_produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')

novo_produtos_df.loc[novo_produtos_df['ID Produto']==873, 'Preco Unitario']=23

print(novo_produtos_df.head())