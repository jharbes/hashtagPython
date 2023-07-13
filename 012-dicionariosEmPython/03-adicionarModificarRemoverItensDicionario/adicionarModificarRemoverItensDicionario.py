"""
# Adicionar, Remover e Modificar Itens no Dicionário

### Estrutura:

- Adicionar itens:

dicionario = {}
dicionario = dict()

dicionario[chave] = valor

outra opção:

dicionario.update({chave: valor, chave: valor})

"""

lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}

# adicionando 1 item
lucro_2tri['julho']=56000
print(lucro_2tri) # {'abril': 88000, 'maio': 89000, 'junho': 120000, 'julho': 56000}


# adicionando vários itens ou um dicionário a outro
lucro_2tri.update({'agosto':24000,'setembro':86000})
print(lucro_2tri) # {'abril': 88000, 'maio': 89000, 'junho': 120000, 'julho': 56000, 'agosto': 24000, 'setembro': 86000}


lucro_1tri.update(lucro_2tri)
print(lucro_1tri) # {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000, 'abril': 88000, 'maio': 89000, 'junho': 120000, 'julho': 56000, 'agosto': 24000, 'setembro': 86000}


# adicionando um item já existente (manualmente ou pelo update)





# - Modificar itens:

# Da mesma forma que adicionamos 1 valor, caso essa chave já exista o item é apenas modificado.

# dicionario[chave] = valor

# Vamos modificar o lucro de fevereiro:<br>
# (Lembrando: caso o item não exista, ele vai criar o item no dicionário)

lucro_fev = 85000

lucro_1tri['fevereiro']=lucro_fev
print(lucro_1tri) # {'janeiro': 100000, 'fevereiro': 85000, 'março': 90000, 'abril': 88000, 'maio': 89000, 'junho': 120000, 'julho': 56000, 'agosto': 24000, 'setembro': 86000}




# - Remover itens:

# del dicionario[chave]

# ou então

# valor = dicionario.pop(chave)

# mas cuidado com:

# del dicionario   ->    que é diferente de dicionario.clear()

# removendo o mês de junho
del lucro_1tri['junho']
print(lucro_1tri) # {'janeiro': 100000, 'fevereiro': 85000, 'março': 90000, 'abril': 88000, 'maio': 89000, 'julho': 56000, 'agosto': 24000, 'setembro': 86000}

valor=lucro_1tri.pop('julho')
print(lucro_1tri) # {'janeiro': 100000, 'fevereiro': 85000, 'março': 90000, 'abril': 88000, 'maio': 89000, 'agosto': 24000, 'setembro': 86000}
print(valor) # 56000


# obs: o del também funciona para listas, caso queira usar
# del lista[i]
funcionarios = ['João', 'Lira', 'Maria', 'Ana', 'Paula']

del funcionarios[0]
print(funcionarios) # ['Lira', 'Maria', 'Ana', 'Paula']