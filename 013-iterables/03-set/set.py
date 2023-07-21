"""
# Set

### Estrutura:

meu_set = {valor, valor, valor, valor,...}

### Observações:

- Não pode ter valores duplicados
- Não tem ordem fixa

"""

set_produtos = {'arroz', 'feijao', 'macarrao', 'atum', 'azeite'}

print(set_produtos) # {'azeite', 'macarrao', 'arroz', 'feijao', 'atum'}

novo_set=set()
print(novo_set)
novo_set.add(1)
print(novo_set)




# - Aplicação bem útil:

    # 1. Quantos clientes tivemos na loja?

cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']
print('Tamanho da lista cpf_clientes: {}'.format(len(cpf_clientes)))


# podemos usar essa estrategia para remover os itens duplicados de uma lista tornado-a um set e depois torna-la de novo uma lista com a funcao list()
cpf_clientes_set=set(cpf_clientes)

print(cpf_clientes_set)

for item in cpf_clientes_set:
    print(item)

print('\nTamanho set cpf_clientes_set: {}'.format(len(cpf_clientes_set)))