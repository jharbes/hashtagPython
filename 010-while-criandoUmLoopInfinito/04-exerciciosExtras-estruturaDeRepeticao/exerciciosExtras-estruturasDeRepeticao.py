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

nome=input('Digite o seu nome: ')
while len(nome)<=3:
    print('\nNOME INVÁLIDO! Deve ter mais de três caracteres')
    nome=input('Digite o seu nome: ')


while True:
    idade=input('Digite sua idade: ')
    try:
        idade=int(idade)
        if idade>=0 and idade<=150:
            break
        else:
            print('\nVALOR INVÁLIDO! Idade deve ser entre 0 e 150 anos!')
            continue
    except:
        print('\nVALOR INVÁLIDO! Idade deve ser entre 0 e 150 anos!')


while True:
    salario=input('Digite seu salário: ')
    try:
        salario=float(salario)
        if salario>0:
            break
        else:
            print('\nVALOR INVÁLIDO! Salário deve ser numérico e maior que zero!')
            continue
    except:
        print('\nVALOR INVÁLIDO! Salário deve ser numérico e maior que zero!')


sexo=input('Informe seu sexo (m ou f): ')
sexo=sexo.lower()
while sexo!='m' and sexo!='f':
    print('\nSEXO INVÁLIDO, preencha com m ou f.')
    sexo=input('Informe seu sexo (m ou f): ')


estado_civil=input('Informe seu estado civil (s, c, v ou d): ')
estado_civil=estado_civil.lower()
while estado_civil!='s' and estado_civil!='c' and estado_civil!='v' and estado_civil!='d':
    print('\nESTADO CIVIL INVÁLIDO, preencha com s, c, v ou d.')
    estado_civil=input('Informe seu estado civil (s, c, v ou d): ')




#### 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_A=80000
populacao_B=200000

numero_anos=0

while populacao_A<=populacao_B:
    populacao_A*=1.03
    populacao_B*=1.015
    numero_anos+=1

print('O número de anos necessários serão de {}.'.format(numero_anos))




#### 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    populacao_X=input('Digite a população do país X: ')
    try:
        populacao_X=int(populacao_X)
        if populacao_X>=0:
            break
        else:
            print('\nVALOR INVÁLIDO!')
            continue
    except:
        print('\nVALOR INVÁLIDO!')

while True:
    populacao_Y=input('Digite a população do país Y: ')
    try:
        populacao_Y=int(populacao_Y)
        if populacao_Y>=0:
            break
        else:
            print('\nVALOR INVÁLIDO!')
            continue
    except:
        print('\nVALOR INVÁLIDO!')


while True:
    taxa_X=input('Digite a taxa de crescimento do país X: (em %) ')
    try:
        taxa_X=float(taxa_X)
        if taxa_X>=0:
            break
        else:
            print('\nVALOR INVÁLIDO!')
            continue
    except:
        print('\nVALOR INVÁLIDO!')

while True:
    taxa_Y=input('Digite a taxa de crescimento do país Y: (em %) ')
    try:
        taxa_Y=float(taxa_Y)
        if taxa_Y>=0:
            break
        else:
            print('\nVALOR INVÁLIDO!')
            continue
    except:
        print('\nVALOR INVÁLIDO!')

taxa_X=taxa_X/100+1
taxa_Y=taxa_Y/100+1

numero_anos_xy=0

if populacao_X>populacao_Y and taxa_X<taxa_Y:
    while populacao_X<=populacao_B:
        populacao_X*=taxa_X
        populacao_Y*=taxa_Y
        numero_anos_xy+=1
    print('O número de anos necessários serão de {}.'.format(numero_anos_xy))
elif populacao_X>populacao_Y and taxa_X>=taxa_Y:
    print('Nunca ultrapassará a população')
elif populacao_Y>populacao_X and taxa_Y<taxa_X:
    while populacao_Y<=populacao_X:
        populacao_X*=taxa_X
        populacao_Y*=taxa_Y
        numero_anos_xy+=1
    print('O número de anos necessários serão de {}.'.format(numero_anos_xy))
elif populacao_Y>populacao_X and taxa_Y>=taxa_X:
    print('Nunca ultrapassará a população')
elif populacao_Y==populacao_X:
    print('Populações já são iguais')




#### 6. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento

