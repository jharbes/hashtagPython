"""

# Integração Python + Excel

### 2 formas:

1. Pandas
    - Mais usada no geral
    - Trata o Excel como uma base de dados
    - Faz o que quiser com o arquivo
    - Pode desfazer a estrutura original do arquivo, caso queira editar
    
2. Openpyxl
    - Trata o Excel como uma planilha mesmo que pode ter várias coisas
    - Edita "como se fosse um VBA"
    - Menos eficiente
    - Mantém mais a estrutura original do arquivo, mas cuidado porque não necessariamente tudo, então tem que testar

"""

### Desafio

# - Temos uma planilha de produtos e serviços. Com o aumento de imposto sobre os serviços, temos que atualizar o preço dos produtos impactados pela mudança.

# Novo Multiplicador Imposto: 1.5

# pandas

import pandas as pd

tabela=pd.read_excel('Produtos.xlsx')
print(tabela)


# atualizando a cotação e as colunas seguintes

# autualizar o multiplicador
tabela.loc[tabela['Tipo']=='Serviço','Multiplicador Imposto']=1.5

# fazer a conta do preço base reais
tabela['Preço Base Reais']=tabela['Multiplicador Imposto']*tabela['Preço Base Original']

# utilizamos o index=False para que a nova tabela gerada nao venha com os indices gerados pelos pandas de 0 até o (n-1) itens da tabela
tabela.to_excel('ProdutosPandas.xlsx',index=False)