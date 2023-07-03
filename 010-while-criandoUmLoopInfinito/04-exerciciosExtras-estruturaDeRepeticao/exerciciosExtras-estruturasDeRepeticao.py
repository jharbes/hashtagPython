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




#### 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

login=input('Digite o nome de usuário: ')
senha=input('Digite a senha desejada: ')

while login==senha:
    print('\nUSUÁRIO NÃO PODE SER IGUAL A SENHA!')
    login=input('Digite o nome de usuário: ')
    senha=input('Digite a senha desejada: ')




#### 3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
##### Nome: maior que 3 caracteres;
##### Idade: entre 0 e 150;
##### Salário: maior que zero;
##### Sexo: 'f' ou 'm';
##### Estado Civil: 's', 'c', 'v', 'd';

