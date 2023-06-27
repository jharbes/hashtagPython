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




"""
## 2. Análise de Vendas

Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.

Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

"""

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

print('Vendedores que bateram as metas com seu respectivo valor em vendas:')
for vendedor in vendas:
    if vendedor[1]>10000:
        print('Vendedor {} com R${} em vendas'.format(vendedor[0],vendedor[1]))




"""
## 3. Comparação com Ano Anterior

Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)

Dica: lembre do enumerate, ele pode facilitar seu "for"

"""

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
#seu código aqui

print('Seguem abaixo os produtos que tiveram aumento de vendas em 2020 comparados ao ano de 2019:\n')
for i,produto in enumerate(produtos):
    if vendas2020[i]>vendas2019[i]:
        print('Produto {}\nValor vendas 2019: R$ {}\nValor vendas 2020: R$ {}\nPercentual de crescimento: {}%\n'.format(produto,vendas2019[i],vendas2020[i],round((vendas2020[i]/vendas2019[i]-1)*100,2)))