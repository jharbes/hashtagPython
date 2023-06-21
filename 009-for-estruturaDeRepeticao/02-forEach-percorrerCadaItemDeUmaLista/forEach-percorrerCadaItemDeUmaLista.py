# For "each"

### Estrutura:

# O for no Python consegue percorrer uma lista e a cada "loop" retornar o valor do item.


"""
for i in range(5):
    print(i)
    
range(5) é na verdade uma lista do tipo: [0, 1, 2, 3, 4]

"""

"""
for item in lista:
    print(item)
    
ou então para string:

# onde ch seria cada caractere
for ch in texto:
    print(ch)

"""

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
texto = 'lira@gmail.com'


for produto in produtos:
    print(produto)
# coca
# pepsi
# guarana
# sprite
# fanta



for caractere in texto:
    print(caractere)
# l
# i
# r
# a
# @
# g
# m
# a
# i
# l
# .
# c
# o
# m