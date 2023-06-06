"""
# Integração de Python com Power BI

### 2 Formas de Fazer:

1. Usar o Python para fazer os tratamentos de bases de dados, criar colunas, etc. para importar para o Power BI depois -> biblioteca pandas -> exatamente como aprendemos no módulo de pandas

2. (O que vamos focar aqui). Usar scripts em Python diretamente dentro do Power BI



### O que conseguimos fazer?

Basicamente, tudo o que temos feito no Python você consegue jogar para dentro do Power BI. Isso porque o Power BI tem um executor de scripts em Python, o que significa que ele roda nossos códigos lá dentro.

- Um dos maiores usos para Python no Power BI é a biblioteca do pandas, dado que ela trabalha com tabelas e o Power BI também.
- Além disso, as bibliotecas de visuais/gráficos também são muito úteis

### Como usar o Python no Power BI - 3 opções:

    1 - Como fonte de Dados
    2 - Para editar uma tabela no Editor de Consultas (Power Query)
    3 - Para criar um visual


### Antes de começar, configurações importantes

Arquivo -> Opções -> Scripts do Python:
- Verificar se o campo "Diretório base do Python" está onde você instalou o python no ambiente virtual
- Se não estiver (provavelmente não vai estar), ajeitar manualmente

"""

### Pequeno teste

import pandas as pd

vendas_df = pd.read_csv(r'C:\Users\jharbes\Documents\GitHub\hashtagPython\032-pythonDashboards-dash-python-powerBi\03-configuracoesImportantes-python-powerBi\Contoso - Vendas - 2017.csv', sep=';')
print(vendas_df)