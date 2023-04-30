### Puxar base de dados

import pandas as pd

# drop -> joga colunas fora
# sort -> ordena as linhas
# loc -> filtra as linhas

tabelaDf=pd.read_csv('exportacoes_franca.csv')

# filtrando a tabela pois todas as linhas estao duplicadas pois a franca aparece como Economic Block = Europe e European Union
tabelaDf=tabelaDf.loc[tabelaDf['Economic Block']=='Europe',:]
print(tabelaDf)




### Informações Gerais

print(tabelaDf.head())

print(tabelaDf.info())

print(tabelaDf.describe())




### Como foi a evolução das exportações para a frança ao longo dos anos em dólar?

avaliacaoDolarDf=tabelaDf.groupby('Year').sum()
avaliacaoDolarDf=avaliacaoDolarDf[['US$ FOB','Net Weight']]

# criar uma funcao de formatacao para uma saida mais amigavel dos valores em dolares:
def formatar(valor):
    return f'{valor:,.2f}'

# aplicar a formatacao
avaliacaoDolarDf['US$ FOB']=avaliacaoDolarDf['US$ FOB'].map(formatar)

print(avaliacaoDolarDf)




### Quais os produtos mais exportados em dólar ao longo de todo o período?

avaliacaoProdutosDf=tabelaDf.groupby('SH4 Description').sum()
avaliacaoProdutosDf=avaliacaoProdutosDf[['US$ FOB']]
avaliacaoProdutosDf=avaliacaoProdutosDf.sort_values('US$ FOB',ascending=False)

print(avaliacaoProdutosDf['US$ FOB'].map(formatar))




### Em 2020 qual cidade mais exportou para a França em dólares?

avaliacaoExportacao2020Cidade=tabelaDf.loc[tabelaDf['Year']==2020,:]
avaliacaoExportacao2020Cidade=avaliacaoExportacao2020Cidade.groupby('City').sum()[['US$ FOB']].sort_values('US$ FOB',ascending=False)

print(avaliacaoExportacao2020Cidade['US$ FOB'].map(formatar))