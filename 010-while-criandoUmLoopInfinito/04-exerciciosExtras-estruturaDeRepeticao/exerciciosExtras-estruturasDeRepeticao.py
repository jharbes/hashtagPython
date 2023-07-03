"""
# Estruturas de repetição

Todos os exercícios são feitos partindo-se do pressuposto de que todas as entradas são dadas de forma correta. Casos limite não mencionados no enunciado não são abordados porque não fazem parte do exercício.

"""

#### 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota=input('Digite uma nota entre 0 e 10: ')
    try:
        nota=int(nota)
        if nota>=0 and nota<=10:
            print('\nNota {} válida!'.format(nota))
            break
        else:
            print('\nVALOR INVÁLIDO!')
            continue
    except:
        print('\nVALOR INVÁLIDO!')