# -*- coding: utf-8 -*-
"""06.06 Exercícios String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tKRJ7IEmMke0hfwmm7fHG3TGMsodwv2z

# Exercícios

## 1. Cadastro de CPF

Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.

Ex: 'Insira seu CPF (digite apenas números)'

Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"
"""

cpf=input('Digite o CPF apenas com números: ')

if not (cpf.isdigit() and len(cpf)==11):
    print('Digite seu CPF corretamente e digite apenas números')
else:
    print('CPF ok')




"""## 2. Melhorando nosso Cadastro de CPF

Agora, além das validações anteriores, vamos criar um input que permita que o usuário insira pontos, traços e inclusive espaços vazios.

Nosso programa deve "tratar" o que o usuário inserir para padronizar o CPF dele em apenas números.

A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços do CPF que o cliente inserir e, uma vez retirados pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.

No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF correto já só com número.
"""

cpf=input('Digite o CPF apenas com números: ')

cpf=cpf.strip().replace('.','').replace('-','')
print(cpf)
if not (cpf.isdigit() and len(cpf)==11):
    print('Digite seu CPF corretamente e digite apenas números')
else:
    print('CPF ok')




"""## 3. Cadastro de e-mails

- A Hashtag sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em cada página um cadastro de nome e e-mail. Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail válido, verificando se ele tem '@' e se depois do '@' tem algum ponto, afinal:

- liragmail.com NÃO é um e-mail válido
- lira@gmail NÃO é um e-mail válido
- lira@gmail.com é um e-mail válido

Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:
1. Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
2. Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido

Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String. Você pode testar o que ele dá como resposta caso ele não encontre um item dentro da string
"""

