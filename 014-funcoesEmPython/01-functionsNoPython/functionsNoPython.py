"""
# Function Python

### O que é?

As functions são blocos de código que servem 1 único propósito, fazem uma ação específica.

### Estrutura Básica

def nome_funcao():
    faça alguma coisa
    faça outra coisa
    return valor_final

"""

# - Exemplo: vamos criar uma função de cadastro de um Produto. Essa função deve garantir que o produto cadastrado está em letra minúscula.

def cadastrarProduto(produto):
    if isinstance(produto,str):
        return produto.lower()
    else:
        return produto

print(cadastrarProduto('Cachaça'))
print(cadastrarProduto(1))