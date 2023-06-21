# for + if

### Estrutura:

"""
for item in lista:
    if condicao:
        faça alguma coisa
    else:
        outra coisa

"""


"""
Digamos que a gente esteja analisando a meta de vendas de vários funcionários de uma empresa. A meta de vendas é de 1000 reais em 1 dia.

Temos uma lista com as vendas de todos os funcionários e quero calcular qual o % de pessoas que bateram a meta.

"""
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000



# formatando percentual
def formatacaoPercentual(valor):
    valor*=100
    return '{}%'.format(round(valor,2))



numero_funcionario_meta=0
for venda_funcionario in vendas:
    if venda_funcionario>=meta:
        numero_funcionario_meta+=1

percentual_meta=numero_funcionario_meta/len(vendas)

print(formatacaoPercentual(percentual_meta)) # 26.09%