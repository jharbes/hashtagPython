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


### Acessando o valor de uma tupla
nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]