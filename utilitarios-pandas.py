### UTILITARIOS PANDAS:

# percorrendo linhas em tabelas:

for linha in tabela.index:
    print(tabela.loc[linha, "Cliente"])
    print(tabela.loc[linha, "Endereço"])
    print(tabela.loc[linha, "Bairro"])