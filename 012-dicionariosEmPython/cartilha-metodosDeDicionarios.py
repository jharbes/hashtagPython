# Métodos Específicos de Dicionário

# - clear() -> Deleta todos os elementos do Dicionário (semelhante ao que aprendemos em listas)

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_mes.clear()
print(vendas_mes) # {}




# - copy() -> Cria uma cópia do dicionário (semelhante ao que aprendemos em listas)

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas2_mes = vendas_mes.copy()
print(vendas2_mes) # {'jan': 150, 'fev': 100, 'mar': 190}




# - fromkeys(chaves, valor_padrao) -> Cria um dicionário com as chaves e o mesmo valor padrão para todas as chaves

chaves = ('jan', 'fev', 'mar')
vendas = 100
vendas_mes = dict.fromkeys(chaves, vendas)
print(vendas_mes) # {'jan': 100, 'fev': 100, 'mar': 100}




# - get(chave) -> 	Retorna o valor especificado pela chave (Semelhante a fazer dictionario[chave]

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(vendas_mes.get('mar')) # 190




# - items() -> Retorna uma lista em que cada item é uma tupla com (chave, valor)

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}

print(list(vendas_mes.items())) # [('jan', 150), ('fev', 100), ('mar', 190)]
print(vendas_mes.items()) # dict_items([('jan', 150), ('fev', 100), ('mar', 190)])




# - keys() -> Retorna uma lista com todas as chaves do dicionário
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}

print(list(vendas_mes.keys())) # ['jan', 'fev', 'mar']
print(vendas_mes.keys()) # dict_keys(['jan', 'fev', 'mar'])




# - pop(chave) -> Retira o item do dicionário e retorna o valor dele para ser usado

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.pop('fev') #retira o fevereiro do dicionário ao mesmo tempo que armazena o valor dele na variável
print(vendas_mes) # {'jan': 150, 'mar': 190}
print(vendas_fev) # 100




# - popitem() -> Retira o último item adicionado ao dicionário

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
#retira o último item adicionado no dicionário ao mesmo tempo que armazena o item(chave, valor) dele na variável
vendas_ult = vendas_mes.popitem() 
print(vendas_mes) # {'jan': 150, 'fev': 100}
print(vendas_ult) # {'jan': 150, 'fev': 100}




# - setdefault(chave, valor) -> Retorna o valor da chave passada, mas caso a chave não exista, cria no dicionário o item com a chave e valor passados.

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.setdefault('fev', 500)
print(vendas_fev) # 100
#repare que como fevereiro existe na lista, ele procura pelo valor de fevereiro e ignora o 500 passado
#agora quando não existe na lista:
vendas_abr = vendas_mes.setdefault('abr', 600)
#repare que agora além de vendas_abr retornar o 600 como valor, ele adicionou um item no dicionario
print(vendas_abr) # 600
print(vendas_mes) # {'jan': 150, 'fev': 100, 'mar': 190, 'abr': 600}




# - update(dicionario) -> Adiciona o dicionário passado como parâmetro ao dicionário original

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_2tri = {'abr': 400, 'mai': 600, 'jun': 500}
vendas_mes.update(vendas_2tri)
print(vendas_mes) # {'jan': 150, 'fev': 100, 'mar': 190, 'abr': 400, 'mai': 600, 'jun': 500}




# - values() -> Retorna uma lista com todos os valores do dicionários

vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(vendas_mes.values()) # dict_values([150, 100, 190])
print(list(vendas_mes.values())) # [150, 100, 190]