"""
# Como "retornar" mais de um objeto

- É possível retornar 2 "coisas"? 2 listas, 2 strings, 2 números...
    - Sim, basta retornar como uma tupla com 2 itens (vamos fazer um exemplo)
    
"""

# observe que ambos returns funcionarao de maneira identica retornando uma tupla
# logo o padrao de retorno de multiplos valores, e também recomendada é uma tupla
def operacoes_basicas(num1, num2):
    soma = num1 + num2
    diferenca = num1 - num2
    mult = num1 * num2
    divisao = num1 / num2
    # return (soma, diferenca, mult, divisao)
    return soma, diferenca, mult, divisao


print(operacoes_basicas(1,2)) # (3, -1, 2, 0.5)




"""
### Aplicação

- Data Science e Inteligência Artificial usa MUITO isso.

    1. Quando criamos um modelo de previsão, precisamos treinar esse modelo e testar para ver se ele sendo um bom modelo ou não.
    2. Temos então que pegar os nossos dados e dividir em 2 pedaços, uma lista de treino e uma lista de teste.
    3. Vamos então pensar no exemplo de um modelo que tenta identificar qual o valor justo de um imóvel de acordo com o tamanho do imóvel. Temos então 2 listas:
        - Lista 1: Preços Reais dos Imóveis
        - Lista 2: Tamanho do imóvel.
    4. Vamos criar então uma função que recebe 2 listas como entrada e que divide cada uma dessas listas em 2, um pedaço de treino e um pedaço de teste. O percentual que a lista vai ser dividida é definida por um fator (que também vai ser um parâmetro da função)

"""

# exemplo mais simples para facilitar a visualização
precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147]

# Vamos definir qual o fator que vamos dividir as listas (ou seja, quantos % da lista vai ficar pra teste. O resto fica pra treino)
#Vamos usar 0.1 (10%)

# Isso significa que a lista de teste tem quantos itens?

# Agora vamos entender qual conta temos que fazer para dividir a lista em 2 listas. Uma com 90% dos valores e outra com 10%