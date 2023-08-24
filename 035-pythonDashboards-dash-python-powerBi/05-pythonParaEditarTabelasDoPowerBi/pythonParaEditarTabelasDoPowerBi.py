"""
Integração Parte 2 - Python para editar as Bases de Dados (de qualquer origem)

Nesse caso, abriremos o Editor de Consultas do Power BI (Power Query) e rodaremos um script na base de dados que quisermos

"""

import pandas as pd
import os

# importando os arquivos
# sempre usar o caminho COMPLETO para o Power BI, pois inclusive ele se encontra em pasta diferente do que a do script python
caminho_padrao = r'C:\Users\Jorge\Desktop\hashtag\hashtagPython\032-pythonDashboards-dash-python-powerBi\05-pythonParaEditarTabelasDoPowerBi'
vendas_df = pd.read_csv(os.path.join(caminho_padrao, r'Contoso - Vendas - 2017.csv'), sep=';')
produtos_df = pd.read_csv(os.path.join(caminho_padrao, r'Contoso - Cadastro Produtos.csv'), sep=';')
lojas_df = pd.read_csv(os.path.join(caminho_padrao, r'Contoso - Lojas.csv'), sep=';')
clientes_df = pd.read_csv(os.path.join(caminho_padrao, r'Contoso - Clientes.csv'), sep=';')

# limpando apenas as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome da Marca']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})

# atentar que o comando display NAO existe para o Power BI
print(vendas_df)

# todos os dataframes presentes (clientes_df, produtos_df, lojas_df e vendas_df estarao presentes no Power BI e lá poderemos decidir quais delas vamos importar)



# estamos filtrando tres lojas de toda a tabela, apenas as lojas que tiverem o 'ID Loja' =86 306 e 172
# ao transferir para o PowerBI o script teremos que a tabela vendas_df estara com o nome 'dataset' que foi colocado pelo PowerBI

# Caso haja problema na data na hora de execução do script python provavelmente teremos que converte-la para texto e depois retornarmos o tipo dela para data
tres_lojas_df=vendas_df[vendas_df['ID Loja'].isin([86,306,172])]
print(tres_lojas_df)

