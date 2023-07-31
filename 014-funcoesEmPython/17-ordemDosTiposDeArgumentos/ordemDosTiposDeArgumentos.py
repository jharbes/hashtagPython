"""
# Ordem dos Argumentos

### Estrutura:

- Sempre os positional arguments vêm antes e depois os keywords arguments.
- Sempre os argumentos individuais vêm antes e depois os "múltiplos"

def minha_funcao(arg1, arg2, arg3, arg4, *args, k = kwarg1, k2 = kwarg2, k3 = kwarg3, **kwargs):
    ...

"""

def minha_soma(*numeros,num1):
    soma=0
    for soma in numeros:
        soma+=0
    soma+=num1
    return soma



print(minha_soma(2,5,num1=1)) # 6

print(minha_soma(2,num1=1)) # 3