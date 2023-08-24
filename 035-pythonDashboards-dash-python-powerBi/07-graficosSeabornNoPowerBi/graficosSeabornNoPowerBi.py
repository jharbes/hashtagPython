"""
# Usando outros gráficos no Power BI com Python

### Temos 2 bibliotecas muito usadas no Python para gráficos, além da matplotlib que já conhecemos:

- Plotly
- Seaborn

Você pode usar as duas que são muito boas. Vamos usar nesse exemplo a Seaborn

"""

### Passo 1: Recriando os dataframes que estão no Power BI

import pandas as pd
import os

# importando os arquivos
# sempre usar o caminho COMPLETO para o Power BI, pois inclusive ele se encontra em pasta diferente do que a do script python
caminho_padrao = r'C:\Users\jharbes\Documents\GitHub\hashtagPython\032-pythonDashboards-dash-python-powerBi\06-pythonParaCriarGraficosNoPowerBi'
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
tres_lojas_df['Data da Venda'] = pd.to_datetime(tres_lojas_df['Data da Venda'], format='%d/%m/%Y')
print(tres_lojas_df)



### Passo 2: Vamos agora criar um gráfico de linha para comparar as Vendas das 3 Lojas

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import seaborn as sns

sns.set_theme(style="darkgrid")

# codigo abaixo para usar no PowerBI (podemos usar tambem em outros locais) para aumentar o tamanho do grafico
fig,ax=plt.subplots(figsize=(15,5))


# editando eixo

# vamos alterar a formatacao da data do eixo x para que haja apenas o mes de forma a ficar mais legivel
ax.xaxis.set_major_formatter(DateFormatter('%m')) 

# vamos editar o ax para que o eixo x mostre as datas de forma correta, colocaremos apenas 12 marcadores no eixo x
ax.xaxis.set_major_locator(plt.MaxNLocator(12))

# data = Base de dados
# ax = tamanho setado anteriormente para o grafico
sns.lineplot(x="Data da Venda", y="Quantidade Vendida", hue="Nome da Loja", data=tres_lojas_df ,ax=ax)


plt.show()