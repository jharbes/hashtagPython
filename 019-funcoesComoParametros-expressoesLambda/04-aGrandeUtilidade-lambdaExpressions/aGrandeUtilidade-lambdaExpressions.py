"""
# Principal Aplicação de Lambda Expressions

### Usar lambda como argumento de alguma outra função, como map e filter

"""
preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}




### map()
# - Queremos saber o preço de cada produto adicionando o valor do imposto de 30% sobre o valor do produto

# Fazendo por function

def preco_com_imposto(preco):
    return preco*1.3

preco_tecnologia_com_imposto=map(preco_com_imposto,preco_tecnologia.values())

print(list(preco_tecnologia_com_imposto)) # [3185.0, 5850.0, 3900.0, 1300.0, 3900.0, 1300.0, 3900.0, 3900.0, 1040.0, 2210.0]



# fazendo por lambda

preco_tecnologia_com_imposto2=map(lambda x:x*1.3,preco_tecnologia.values())

print(list(preco_tecnologia_com_imposto2)) # [3185.0, 5850.0, 3900.0, 1300.0, 3900.0, 1300.0, 3900.0, 3900.0, 1040.0, 2210.0]