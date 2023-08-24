"""
# Lambda Expressions

### Objetivo:

- As lambdas expressions são funções anônimas (sem nome mesmo) que tem 1 linha de código e são atribuidas a uma variável, como se a variável virasse uma função.
- Elas normalmente são usadas para fazer uma única ação, mas em Python usamos principalmente dentro de métodos como argumento, para não precisarmos criar uma função só para isso (vamos ver isso na aula que vem)
- Outra aplicação delas está em criar um "gerador de funções" (vamos ver na 3ª Aula dessa Seção)

### Obs

- Não é "obrigatório" usar lambda expression, até porque praticamente tudo o que você faz com elas você consegue fazer com functions normais. Mas, é importante saber entender quando encontrar e saber usar a medida que você for se acostumando e vendo necessidade

### Estrutura:

minha_funcao = lambda parametro: expressão

"""

# - Exemplo mais simples

def minha_funcao(num):
    return num*2

print(minha_funcao(5)) # 10


funcao_lambda=lambda x:x*2

print(funcao_lambda(5)) # 10




# - Exemplo útil: Vamos usar lambda expressions para criar uma função que calcula o preço dos produtos acrescido do imposto

imposto = 0.3

minha_funcao2=lambda preco:preco+preco*imposto

print(minha_funcao2(10)) # 13.0