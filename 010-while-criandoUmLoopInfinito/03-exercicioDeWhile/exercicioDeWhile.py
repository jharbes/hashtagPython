"""
# Exercícios

## 1. Input até o usuário parar

Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em uma lista.

O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum produto ou quantidade.

Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

Obs: Caso queira, para o print ficar mais visual, pode usar o join para cada item ser printado em uma linha.
Sugestão para sua lista de produtos vendidos:

"""

# vendas = [
#     ['maçã', 5],
#     ['banana', 15],
#     ['azeite', 1],
#     ['vinho', 3],
# ]

# seu código aqui

vendas=[]
numero_produto=1
print('SISTEMA DE VENDAS\n')
print('Para finalizar deixe o nome do produto ou a quantidade em branco.\n')

produto='x'
quantidade_produto='1'
while produto!='' and quantidade_produto!='':
    produto=input('Digite o produto de número {}: '.format(numero_produto))
    quantidade_produto=input('Digite a quantidade do produto de número {}: '.format(numero_produto))
    if produto and quantidade_produto:
        vendas.append([produto,quantidade_produto])
    numero_produto+=1


print('LISTA DE VENDAS:\n')
for venda in vendas:
    print(venda[0],' - ',venda[1])




"""
### Obs: Podemos fazer o While de 2 maneiras:

1. While com a condição que finalize o programa
2. While rodando para sempre, mas com uma condição dentro do while que dê um break no código.

Vamos mostrar as 2 opções

"""