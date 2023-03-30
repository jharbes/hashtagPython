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
print(f'{percentualDevolvido=:.2f}%')




### Agora, se quisermos fazer a mesma análise apenas para 1 loja. Queremos filtrar apenas os itens da Loja Contoso Europe Online e saber o % de devolução dessa loja.

# - Para isso, vamos precisar filtrar. A forma de filtrar nos dataframes é uma "simples" comparação

