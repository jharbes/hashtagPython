import pandas as pd
import matplotlib.pyplot as plt

# importando os arquivos
vendasDf = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtosDf = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojasDf = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientesDf = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

produtosDf = produtosDf[['ID Produto', 'Nome do Produto']]

vendasDf = vendasDf.merge(produtosDf, on='ID Produto')

produtosVendidos=vendasDf.groupby('Nome do Produto').sum()

produtosVendidos=produtosVendidos.sort_values('Quantidade Vendida')[0:1]['Nome do Produto']

print(produtosVendidos)