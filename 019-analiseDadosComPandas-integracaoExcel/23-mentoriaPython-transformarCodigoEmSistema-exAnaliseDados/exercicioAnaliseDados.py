### Puxar base de dados

import pandas as pd

tabelaDf=pd.read_csv('exportacoes_franca.csv')
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