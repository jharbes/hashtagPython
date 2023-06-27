"""
# Exercícios

## 1. Criando um Registro de Hóspedes

Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:

quarto = [
    ['João', 'cpf:00000000000'],
    ['Julia', 'cpf:11111111111'],
    ['Marcus', 'cpf:22222222222'],
    ['Maria', 'cpf:33333333333'],
]

- Para simplificar, não vamos nos preocupar com possibilidades de "tentar colocar mais de 1 hóspede, digitar o cpf errado, etc. Nosso objetivo é treinar a criação de uma rotina de cadastro

"""

numero_hospedes=input('Digite o número de hospedes: ')

registroHospedes=[]
try:
    numero_hospedes=int(numero_hospedes)
    for i in range(numero_hospedes):
        nome_hospede=input('Digite o nome do hospede de número '+str(i+1)+':')
        cpf_hospede=input('Digite o cpf do hospede de número '+str(i+1)+':')
        registroHospedes.append([nome_hospede,'cpf:'+cpf_hospede])
    for hospede in registroHospedes:
        print(hospede)
except:
    print('Número de hóspedes inválido')




