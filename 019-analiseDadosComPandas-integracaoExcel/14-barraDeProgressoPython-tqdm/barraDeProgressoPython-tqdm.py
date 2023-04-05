"""

# E quando o nosso código demora muito? Será que travou? Quanto tempo vai demorar?

### Biblioteca/Módulo tqdm

- Vamos importar os arquivos csv da Empresa Contoso e tratar como fizemos ao longo desse módulo

"""

import pandas as pd

# importando os arquivos
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

# limpando apenas as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})
print(vendas_df)




### Agora, imagina que a Loja Contoso Roma (ID 222), para tentar burlar o sistema de metas, diminuiu 1 da quantidade devolvida de todas as vendas que ela teve. Descobrindo isso, precisamos ajeitar a base

# - Farei com um for, principalmente por motivos didáticos, mas teríamos outras formas de fazer isso também.

from tqdm import tqdm

# total é o que a barra vai percorrer, position e leave farao com que a barra fique em apenas uma linha
pbar=tqdm(total=len(vendas_df['ID Loja']),position=0,leave=True)

for index,idLoja in enumerate(vendas_df['ID Loja']):
    pbar.update()
    if idLoja==222:
        vendas_df.loc[index,'Quantidade Devolvida']+=1

print(vendas_df)