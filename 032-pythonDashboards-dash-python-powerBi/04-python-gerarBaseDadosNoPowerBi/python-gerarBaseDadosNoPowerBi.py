"""
# Integração Parte 1 - Python para "Criar" Bases de Dados


### Qual arquivo vamos importar?

- Vamos usar o mesmo exemplo que usamos da empresa Contoso no módulo de Análise de Dados

Temos 4 arquivos diferentes:
- Vendas
- Lojas
- Clientes
- Produtos

E vamos integrar eles em 1 arquivo único apenas com as informações relevantes. Depois, vamos importar essa base tratada para o Power BI

"""

import pandas as pd
import os

# importando os arquivos
# sempre usar o caminho COMPLETO para o Power BI, pois inclusive ele se encontra em pasta diferente do que a do script python
caminho_padrao = r'C:\Users\jharbes\Documents\GitHub\hashtagPython\032-pythonDashboards-dash-python-powerBi\04-python-gerarBaseDadosNoPowerBi'
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