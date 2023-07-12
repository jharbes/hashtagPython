"""
# Tuplas

### Estrutura:

tupla = (valor, valor, valor, ...)

### Diferença

Parece uma lista, mas é imutável.

### Vantagens:

- Mais eficiente (em termos de performance)
- Protege a base de dados (por ser imutável)
- Muito usado para dados heterogêneos

### Criando tuplas
"""

vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
print(vendas)




### Acessando o valor de uma tupla

# nome = vendas[0]
# data_contratacao = vendas[1]
# data_nascimento = vendas[2]
# salario = vendas[3]
# cargo = vendas[4]


# acessando a tupla por meio de unpacking:
# lembrando que para acessarmos uma tupla de 5 valores por exemplo, precisamos de 5 variaveis
# unpacking tambem funciona para listas
nome,data_contratacao,data_nascimento,salario,cargo=vendas


print(nome)
print(data_contratacao)
print(data_nascimento)
print(salario)
print(cargo)




# - o enumerate que vínhamos usando até agora, na verdade, cria uma tupla para a gente. Vamos ver na prática:

vendas = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']

for i, venda in enumerate(vendas):
        print('{} vendeu {} unidades'.format(funcionarios[i], venda))


# observe o unpacking em tuplas por meio do enumerate, o resultado serao tuplas
for item in enumerate(vendas):
        print(item)