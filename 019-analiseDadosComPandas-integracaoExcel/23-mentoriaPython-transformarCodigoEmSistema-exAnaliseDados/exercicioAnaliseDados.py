### Puxar base de dados

import pandas as pd

tabelaDf=pd.read_csv('exportacoes_franca.csv')
print(tabelaDf)



### Informações Gerais

print(tabelaDf.head())

print(tabelaDf.info())

print(tabelaDf.describe())



### Como foi a evolução das exportações para a frança ao longo dos anos?
