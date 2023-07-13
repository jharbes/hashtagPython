"""
# Métodos úteis em dicionários

## items() dos dicionários

### Estrutura:

itens_dicionario = dicionario.items()

ou então:

for item in dicionario.items()
    cada item do dicionario em formato de tupla

"""

vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}


# .items() transforma os itens do dicionario em uma lista de tuplas
vendas_tecnologia_items=vendas_tecnologia.items()


print(vendas_tecnologia_items) # dict_items([('notebook asus', 2450), ('iphone', 15000), ('samsung galaxy', 12000), ('tv samsung', 10000), ('ps5', 14300), ('tablet', 1720), ('notebook dell', 17000), ('ipad', 1000), ('tv philco', 2500), ('notebook hp', 1000)])




# - Quais produtos venderam mais de 5000 unidades?

#forma 1 -> usando apenas o dicionario e as chaves

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave]>5000:
        print(chave)

print('\n')

#forma 2 -> usando o dicionario.items()

for item in vendas_tecnologia_items:
    if item[1]>5000:
        print(item[0])




"""
# Listas importantes a partir do Dicionário

### Métodos importantes:

.keys() -> uma "lista" com todas as chaves do dicionario

.values() -> uma "lista" com todos os valores do dicionario

Obs: Se o dicionario for modificado, automaticamente essas variáveis são modificadas, mesmo tendo sido criadas anteriormente

"""

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()

print(chaves) # dict_keys(['notebook asus', 'iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'notebook dell', 'ipad', 'tv philco', 'notebook hp'])


print(valores) # dict_values([2450, 15000, 12000, 10000, 14300, 1720, 17000, 1000, 2500, 1000])




vendas_tecnologia['liraphone'] = 10

print(chaves) # dict_keys(['notebook asus', 'iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'notebook dell', 'ipad', 'tv philco', 'notebook hp', 'liraphone'])

print(valores) # dict_values([2450, 15000, 12000, 10000, 14300, 1720, 17000, 1000, 2500, 1000, 10])

print(list(chaves)) # ['notebook asus', 'iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'notebook dell', 'ipad', 'tv philco', 'notebook hp', 'liraphone']

print(list(valores)) # [2450, 15000, 12000, 10000, 14300, 1720, 17000, 1000, 2500, 1000, 10]



