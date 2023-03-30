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


# mesclando e renomeando os dataframes, observe que as novas colunas serao incluidas no fim da tabela e as informacoes pertinentes serao vinculadas ao ID da tabela antiga conforme mostra abaixo: exemplo, a tabela vai ler o ID produto e adicionar o nome do produto correspondente no fim da tabela

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})

print(vendas_df)




### Primeiro, vamos aplicar uma função normalmente. Qual o % das vendas que foi devolvido?

# - Para isso vamos somar as quantidades nas colunas correspondentes. Lembrando, o % vai ser: Total Devolvido / Total Vendido.

quantidadeVendida=vendas_df['Quantidade Vendida'].sum()
print(quantidadeVendida)

quantidadeDevolvida=vendas_df['Quantidade Devolvida'].sum()
print(quantidadeDevolvida)

percentualDevolvido=(quantidadeDevolvida/quantidadeVendida)*100
print(f'{percentualDevolvido=:.2f}%\n')




### Agora, se quisermos fazer a mesma análise apenas para 1 loja. Queremos filtrar apenas os itens da Loja Contoso Europe Online e saber o % de devolução dessa loja.

# - Para isso, vamos precisar filtrar. A forma de filtrar nos dataframes é uma "simples" comparação

quantidadeVendidaLoja1=0
quantidadeDevolvidaLoja1=0

for linha in vendas_df.index:
    if vendas_df.loc[linha,'Nome da Loja']=='Loja Contoso Europe Online ':
        quantidadeDevolvidaLoja1+=vendas_df.loc[linha,'Quantidade Devolvida']
        quantidadeVendidaLoja1+=vendas_df.loc[linha,'Quantidade Vendida']

if quantidadeVendidaLoja1>0:
    percentualDevolvidoLoja1=(quantidadeDevolvidaLoja1/quantidadeVendidaLoja1)*100
    print(f'{percentualDevolvidoLoja1=:.2f}%\n')
else:
    print('Sem vendas para essa loja\n')


# ou

# filtrando a tabela para que ela so tenha loja contoso europe online, podemos tambem usar o ID da loja (o nome da loja na tabela esta com um erro , possui um espaco no final do nome)
vendasLojaContosoEuropeOnline=vendas_df[vendas_df['Nome da Loja']=='Loja Contoso Europe Online ']
print(vendasLojaContosoEuropeOnline)

if vendasLojaContosoEuropeOnline['Quantidade Vendida'].sum()>0:
    percentualDevolvidoLojaContosoEuropeOnline=(vendasLojaContosoEuropeOnline['Quantidade Devolvida'].sum()/vendasLojaContosoEuropeOnline['Quantidade Vendida'].sum())*100

    print(f'{percentualDevolvidoLojaContosoEuropeOnline=:.2f}%\n')
else:
    print('Sem vendas para essa loja\n')




### Vamos fazer em 2 passos para entender certinho o que está acontecendo.

# vendasLojaContosoEuropeOnline=vendas_df[vendas_df['Nome da Loja']=='Loja Contoso Europe Online ']
# vendasLojaContosoEuropeOnline=vendas_df[vendas_df['ID Loja']==306]

# lista a tabela apenas com vendas da loja ID 306
todasLojasId306=vendas_df[vendas_df['ID Loja']==306]
print(todasLojasId306)

# informa se a venda eh loja ID 306 ou nao
ehLoja306= vendas_df['ID Loja']==306
print(ehLoja306)




### Desafio: e se eu quisesse criar uma tabela apenas com as vendas da Loja Contoso Europe Online e que não tiveram nenhuma devolução. Quero criar essa tabela e saber quantas vendas são.

# - Repare que nesse caso são 2 condições, como fazemos isso?

# tudo junto

import numpy as np

vendasLoja306SemDevolucao=vendas_df[np.logical_and(vendas_df['ID Loja']==306, vendas_df['Quantidade Devolvida']==0)]

# ou

# o parenteses em cada condicao eh obrigatorio
# vendasLoja306SemDevolucao=vendas_df[(vendas_df['ID Loja']==306) & (vendas_df['Quantidade Devolvida']==0)]

print(vendasLoja306SemDevolucao)
print(vendasLoja306SemDevolucao['Quantidade Vendida'].sum())


# separado

vendasLoja306SemDevolucao = vendas_df[vendas_df['ID Loja']==306]
vendasLoja306SemDevolucao = vendasLoja306SemDevolucao[vendas_df['Quantidade Devolvida']==0]

print(vendasLoja306SemDevolucao)
print(vendasLoja306SemDevolucao['Quantidade Vendida'].sum())
