"""
# DataFrame


## Resumo

É como se fosse uma tabela.

- As colunas funcionam "como chaves de dicionário"
- As linhas funcionam "como listas"

## Funcionamento

Temos um dataframe chamado vendas_df

vendas_df['coluna_x'] -> uma lista com os valores da coluna_x (em formato dataframe, é um dataframe com 1 coluna só)

vendas_df[0] -> NÃO FUNCIONA ASSIM PARA DATAFRAMES

vendas_df[:3] -> pega até a linha de índice 3 do dataframe

vendas_df[['coluna_x', 'coluna_y', 'coluna_z']] -> cria um novo dataframe com as colunas coluna_x, coluna_y e coluna_z

vendas_df['coluna_x'][0] -> pega o item da 1ª linha da coluna coluna_x

"""

# - Vamos ler um arquivo real, com a Base de Dados de Vendas da Empresa "Contoso"

import pandas as pd

vendas_df = pd.read_csv(r'Contoso - Vendas  - 2017.csv', sep=';')

vendas_df


# ## Aplicação

# - O 1º passo de toda Análise de Dados é você entender o que existe na sua base de dados

# Usaremos o .info() para isso

