"""
# Retornar um valor na Function Python

### Estrutura Básica

def nome_funcao():
    return valor_final

"""

# - Exemplo: vamos criar uma função de cadastro de um Produto. Essa função deve garantir que o produto cadastrado está em letra minúscula.

def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar')
    produto = produto.casefold()
    produto = produto.strip()
    return produto



produto=cadastrar_produto()

print(produto)