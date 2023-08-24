"""
# pandas e csv

## Resumo

Quase sempre quando formos "ler" um arquivo csv, vamos usar o pandas. É prático e bem eficiente.

DATAFRAME:
Objeto do pandas que se constitui por uma tabela, onde podemos manipular os dados com a biblioteca pandas
"""

## Funcionamento

# Forma mais básica: (muitas vezes não usaremos a forma mais básica)
# dataframe = pd.read_csv('arquivo_com_extensao')

import pandas as pd


# - Vamos ler um arquivo real, com a Base de Dados de Vendas da Empresa "Contoso"

vendasDf=pd.read_csv('Contoso - Cadastro Produtos.csv')
print(vendasDf)
vendasDf # tambem exibe o arquivo csv (jupyter)

vendasDf2=pd.read_csv('Contoso - Vendas - 2017.csv')
print(vendasDf2)
vendasDf2 # tambem exibe o arquivo csv (jupyter)

# nesse caso o arquivo está com a separacao de colunas feitas com (;) ponto e virgula, porem o padrao do csv é a separacao por (,) virgula, logo teremos que indicar esse separador para que a leitura seja feita adequadamente.

vendasDf=pd.read_csv('Contoso - Cadastro Produtos.csv',sep=';')
print(vendasDf)
vendasDf # tambem exibe o arquivo csv (jupyter)

vendasDf2=pd.read_csv('Contoso - Vendas - 2017.csv',sep=';')
print(vendasDf2)
vendasDf2 # tambem exibe o arquivo csv (jupyter)