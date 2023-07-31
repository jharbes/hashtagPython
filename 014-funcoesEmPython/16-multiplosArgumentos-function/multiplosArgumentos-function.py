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

def minha_soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma




def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra'] 
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco