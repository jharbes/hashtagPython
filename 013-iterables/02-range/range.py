"""
# Range

### Estrutura:

- range(tamanho)

ou 

- range(inicio, fim)

ou

- range(inicio, fim, passo)

"""

# uso mais comum no for:
produtos = ['arroz', 'feijao', 'macarrao', 'atum', 'azeite']
estoque = [50, 100, 20, 5, 80]

for i in range(0,len(produtos)):
    print('{} : {}'.format(produtos[i],estoque[i]))


# range com inicio e fim
print(range(1, 10))

# vamos olhar no for para entender
for i in range(1,10):
    print(i)




# - Exemplo: Modelo Jack Welch da G&E

#     1. Classe A: 10% melhor
#     2. Classe B: 80% mantém/busca melhorar
#     3. Classe C: 10% pior
    
# Quem são os funcionários classe B?

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo']
vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]

print('Funcionários Classe B\n')
for i in range(3,18):
    print('Funcionário {}'.format(funcionarios[i]))


# range com passo
print(range(0, 1000, 10))

for i in range(0, 1000, 10):
    print(i)