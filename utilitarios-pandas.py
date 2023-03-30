### UTILITARIOS PANDAS:

# percorrendo linhas em tabelas:

for linha in tabela.index:
    print(tabela.loc[linha, "Cliente"])
    print(tabela.loc[linha, "Endereço"])
    print(tabela.loc[linha, "Bairro"])
    
    
    
# - Para isso, vamos precisar filtrar. A forma de filtrar nos dataframes é uma "simples" comparação

quantidadeVendidaLoja1=0
quantidadeDevolvidaLoja1=0

for linha in vendas_df.index:
    if vendas_df.loc[linha,'Nome da Loja']=='Loja Contoso Europe Online ':
        quantidadeDevolvidaLoja1+=vendas_df.loc[linha,'Quantidade Devolvida']
        quantidadeVendidaLoja1+=vendas_df.loc[linha,'Quantidade Vendida']

if quantidadeVendidaLoja1>0:
    percentualDevolvidoLoja1=(quantidadeDevolvidaLoja1/quantidadeVendidaLoja1)*100
    print(f'{percentualDevolvidoLoja1=:.2f}%')
else:
    print('Sem vendas para essa loja\n')


# ou

# filtrando a tabela para que ela so tenha loja contoso europe online, podemos tambem usar o ID da loja (o nome da loja na tabela esta com um erro , possui um espaco no final do nome)
vendasLojaContosoEuropeOnline=vendas_df[vendas_df['Nome da Loja']=='Loja Contoso Europe Online ']
print(vendasLojaContosoEuropeOnline)

if vendasLojaContosoEuropeOnline['Quantidade Vendida'].sum()>0:
    percentualDevolvidoLojaContosoEuropeOnline=(vendasLojaContosoEuropeOnline['Quantidade Devolvida'].sum()/vendasLojaContosoEuropeOnline['Quantidade Vendida'].sum())*100

    print(f'{percentualDevolvidoLojaContosoEuropeOnline=:.2f}%\n')
else:
    print('Sem vendas para essa loja\n')