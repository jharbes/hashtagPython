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

# criando formatacao para os valores (em reais)
import locale

locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')

def formatacaoMoeda(valor):
    return locale.currency(valor,grouping=True)

faturamento=[]

for i in range(5):
    while True:
        faturamento_mes=input('Entre com o faturamento do mês {}: '.format(i+1))
        try:
            faturamento_mes=float(faturamento_mes)
            if faturamento_mes>=0:
                faturamento.append(faturamento_mes)
                break
            else:
                print('\nVALOR INVÁLIDO! Faturamento deve ser numérico e ser igual ou maior que zero!')
                continue
        except:
            print('\nVALOR INVÁLIDO! Faturamento deve ser numérico e ser igual ou maior que zero!')

print(faturamento)

print('O maior faturamento foi de {} no mês de número {}.'.format(formatacaoMoeda(max(faturamento)),faturamento.index(max(faturamento))+1))




#### 7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o faturamento total (soma) e o faturamento médio por mês (média).

from statistics import mean

print('O faturamento total foi de {} e o faturamento médio mensal foi de {}.'.format(formatacaoMoeda(sum(faturamento)),formatacaoMoeda(mean(faturamento))))




#### 8. Faça um programa que consiga categorizar a idade das equipes de uma empresa. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da equipe varia entre 0 e 25 (jovem) ,26 e 60 (sênior) e maior que 60 (idosa); e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada.

while True:
        numero_funcionarios=input('Entre com o número de funcionários: ')
        try:
            numero_funcionarios=int(numero_funcionarios)
            if numero_funcionarios>=1:
                break
            else:
                print('\nVALOR INVÁLIDO! Número de funcionários deve ser numérico e igual ou maior que zero!')
                continue
        except:
            print('\nVALOR INVÁLIDO! Número de funcionários deve ser numérico e igual ou maior que zero!')

idade_funcionarios=[]
for i in range(numero_funcionarios):
     while True:
        idade=input('Digite a idade do funcionário de número {}: '.format(i+1))
        try:
            idade=int(idade)
            if idade>=0:
                idade_funcionarios.append(idade)
                break
            else:
                print('\nVALOR INVÁLIDO! Idade do funcionário deve ser numérico e igual ou maior que zero!')
                continue
        except:
            print('\nVALOR INVÁLIDO! Idade do funcionário deve ser numérico e igual ou maior que zero!')

media_idade=round(mean(idade_funcionarios),0)

if media_idade<=25:
    print('A equipe é jovem e a média de idade é de {}'.format(media_idade))
elif media_idade<=60:
    print('A equipe é sênior e a média de idade é de {}'.format(media_idade))
else:
    print('A equipe é idosa e a média de idade é de {}'.format(media_idade))




    #### 9. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

    while True:
        numero_eleitores=input('Entre com o número de eleitores: ')
        try:
            numero_eleitores=int(numero_eleitores)
            if numero_eleitores>=1:
                break
            else:
                print('\nVALOR INVÁLIDO! Número de eleitores deve ser numérico e igual ou maior que zero!')
                continue
        except:
            print('\nVALOR INVÁLIDO! Número de eleitores deve ser numérico e igual ou maior que zero!')


votos_computados=[0,0,0]

for i in range(numero_eleitores):
    voto=input('Escolha o candidato 0, 1 ou 2 (valores diferentes anulam o voto): ')
    if voto=='0':
        votos_computados[0]+=1
        print('Voto computado para o candidato 0.')
    elif voto=='1':
        votos_computados[1]+=1
        print('Voto computado para o candidato 1.')
    elif voto=='2':
        votos_computados[2]+=1
        print('Voto computado para o candidato 2.')
    else:
        print('Voto anulado')

print("""
Os votos computados são:
Candidato 0: {} votos,
Candidato 1: {} votos,
Candidato 2: {} votos
""".format(votos_computados[0],votos_computados[1],votos_computados[2]))




#### 10. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

while True:
        numero_cds=input('Entre com o número de CDs: ')
        try:
            numero_cds=int(numero_cds)
            if numero_cds>=1:
                break
            else:
                print('\nVALOR INVÁLIDO! Número de CDs deve ser numérico e igual ou maior que zero!')
                continue
        except:
            print('\nVALOR INVÁLIDO! Número de CDs deve ser numérico e igual ou maior que zero!')

valor_cds=[0 in range(numero_cds)]



for i in range(numero_cds):
    while True:
        valor_cd=input('Entre com o valor do CD de número {}: '.format(i))
        try:
            valor_cd=float(valor_cd)
            if valor_cd>=0:
                valor_cds.append(valor_cd)
                break
            else:
                print('\nVALOR INVÁLIDO! Valor do CD deve ser numérico e igual ou maior que zero!')
                continue
        except:
            print('\nVALOR INVÁLIDO! Valor do CD deve ser numérico e igual ou maior que zero!')

import statistics

print("""
O valor total investido na coleção de CDS foi de {}.
A média de valor gasta em cada um deles foi de {}.
""".format(formatacaoMoeda(sum(valor_cds)),formatacaoMoeda(mean(valor_cds))))




#### 11. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

print('Loja Quase Dois - Tabela de preços')

preco_item=1.99
for i in range(50):
    print(i+1,' - R$',preco_item*(i+1))




#### 12. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário desse funcionário em 2003. 

salario_inicial=1000
aumento=0.015
ano_inicial=1995
ano_final=2003
numero_anos_aumento=ano_final-ano_inicial
salario_final=salario_inicial

for i in range(numero_anos_aumento):
    salario_final=salario_final*(1+aumento)
    aumento*=2

print('R$',round(salario_final,2))




#### 13. O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

