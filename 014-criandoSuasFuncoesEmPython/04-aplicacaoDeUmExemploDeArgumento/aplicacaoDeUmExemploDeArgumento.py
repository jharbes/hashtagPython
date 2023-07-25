"""
# Argumentos/Parâmetros da Função

### Estrutura:

def minha_funcao(parametro1, parametro2, parametro3):
    return parametro1 + parametro2 + parametro3

"""

# - Exemplo: nosso famoso print

vendas = 50
print('Produto', 'Iphone', 'Vendas', vendas)




# - Só para mostrar o funcionamento, vamos criar uma função de soma

def minha_soma(num1, num2, num3):
    return num1 + num2 + num3

soma = minha_soma(10, 20, 0)
print(soma)


def soma2(*args):
    return sum(args)

print(soma2(1,2,3,4,5,6))