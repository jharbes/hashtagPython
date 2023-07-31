"""
# Quantidade Indefinidas de Argumentos

### Utilidade:

Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

### Estrutura:

*args para positional arguments -> argumentos vêm em formato de tupla

def minha_funcao(*args):
    ...


**kwargs para keyword arguments -> argumentos vêm em formato de dicionário

def minha_funcao(**kwargs):

"""

# quando passamos os argumentos com packing eles vao como uma tupla, observe a saida do print dos argumentos
def minha_soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


print(minha_soma(1,2,3,4,5))
# (1, 2, 3, 4, 5)
# 15




# observe que os argumentos nomeados (keyword arguments ou kwargs) sao recebidos como um dicionario, observe a saida do print dos argumentos
def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra'] 
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco



print(preco_final(1000,desconto=0.2,imposto=0.1,garantia_extra=100))
# {'desconto': 0.2, 'imposto': 0.1, 'garantia_extra': 100}
# 990.0000000000001


print(preco_final(100,imposto=0.2))
# {'imposto': 0.2}
# 120.0


print(preco_final(desconto=0.2,preco=1000))
# {'desconto': 0.2}
# 800.0