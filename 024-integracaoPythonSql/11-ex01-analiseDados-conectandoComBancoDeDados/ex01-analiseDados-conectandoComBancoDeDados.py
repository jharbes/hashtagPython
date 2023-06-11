"""
## Exercício Desafio

- Digamos que seu chefe pediu para você um relatório da análise dos salários da unidade de San Francisco da empresa. O objetivo dele é entender:

1. Qual foi a evolução do salário médio ao longo dos anos (TotalPay e TotalPayBenefits)

2. Quantos funcionários tivemos ao longo dos anos

3. Qual foi a evolução do total gasto com salário ao longo dos anos (TotalPayBenefits)

- Base de Dados a ser usada: salarios.sqlite

"""

### Importação da Base de Dados


# Com SQLITE

import pandas as pd
import sqlite3

conexao=sqlite3.connect('salarios.sqlite')

tabela_salarios_sqlite=pd.read_sql('SELECT * FROM Salaries',conexao)

conexao.close()

print(tabela_salarios_sqlite)




# Com PYODBC

import pyodbc

print(pyodbc.drivers())

dados_conexao=('Driver={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite')

conexao=pyodbc.connect(dados_conexao)
cursor=conexao.cursor()

cursor.execute('SELECT * FROM Salaries')

valores_tabela_pyodbc=cursor.fetchall() # cursor.fetchall() resgata os valores da tabela (sem o cabeçalho)

descricao_tabela_pyodbc=cursor.description # cursos.description() resgata o cabeçalho da tabela (sem os valores)

print(descricao_tabela_pyodbc)
print(valores_tabela_pyodbc)

cursor.close()
conexao.close()


# gerando uma lista do cabeçalho por meio de list comprehension onde percorre a descricao_tabela_pyodbc, cada linha dela (que eh uma tupla) e seu primeiro item
colunas=[tupla[0] for tupla in descricao_tabela_pyodbc]

# podemos tambem fazer assim:
"""
colunas=[]
for tupla in descricao_tabela_pyodbc:
    colunas.append(tupla[0])
"""

tabela_salarios_pyodbc=pd.DataFrame.from_records(valores_tabela_pyodbc, columns=colunas)

print(tabela_salarios_pyodbc)




### Análise de Dados

# garantindo que estamos só com San Francisco

tabela_salarios_pyodbc=tabela_salarios_pyodbc.loc[tabela_salarios_pyodbc['Agency']=='San Francisco']

tabela_salarios_sqlite=tabela_salarios_sqlite.loc[tabela_salarios_sqlite['Agency']=='San Francisco']

print(tabela_salarios_pyodbc)
print(tabela_salarios_sqlite)

# a partir de agora utilizaremos apenas uma das tabelas pois elas sao iguais e darao os mesmos resultados




##### 1. Qual foi a evolução do salário médio ao longo dos anos

#### MINHA RESOLUCAO

# observe que após fazer o comando que calcula as médias ele manterá apenas as colunas numericas
evolucao_salario=tabela_salarios_sqlite.groupby('Year').mean()

evolucao_salario=evolucao_salario.drop(columns=['Id'])

evolucao_salario['TotalPayment']=evolucao_salario['TotalPay']+evolucao_salario['TotalPayBenefits']

evolucao_salario=evolucao_salario.drop(['TotalPay','TotalPayBenefits'],axis=1)

print(evolucao_salario)


#### RESOLUCAO PROFESSOR

#### RESOLUCAO PROFESSOR

tabela_salario_medio=tabela_salarios_sqlite.groupby('Year').mean()

print(tabela_salario_medio[['TotalPay','TotalPayBenefits']])