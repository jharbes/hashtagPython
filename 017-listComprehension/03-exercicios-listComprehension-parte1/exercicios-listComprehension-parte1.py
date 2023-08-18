"""
# Exercícios

## 1. Tirando informações de listas e dicionários

Digamos que você está analisando as vendas de produtos de uma empresa de varejo.

Essa lista tem: (produto, vendas de 2019, vendas de 2020) para cada produto.

Crie uma lista com as vendas de 2019.

"""
vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

vendas_2019=[venda_2019 for produto,venda_2019,venda_2020 in vendas_produtos]

print(vendas_2019) # [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467, 489705, 328311, 591120]



# - Agora, qual o maior valor de vendas de 2019?
vendas_2019.sort(reverse=True)

print(vendas_2019) # [973139, 892292, 887061, 718654, 712350, 591120, 573823, 558147, 531580, 489705, 438508, 422760, 405252, 328311, 237467, 154753]

print(vendas_2019[0]) # 973139



# - E se eu quisesse descobrir o produto que mais vendeu em 2019?
# Temos 2 formas de fazer, refazendo o list comprehension ou consultando a lista original

vendas_produtos_2019=[(vendas_2019,produto) for produto,vendas_2019,vendas_2020 in vendas_produtos]

print(vendas_produtos_2019) # [(558147, 'iphone'), (712350, 'galaxy'), (573823, 'ipad'), (405252, 'tv'), (718654, 'máquina de café'), (531580, 'kindle'), (973139, 'geladeira'), (892292, 'adega'), (422760, 'notebook dell'), (154753, 'notebook hp'), (887061, 'notebook asus'), (438508, 'microsoft surface'), (237467, 'webcam'), (489705, 'caixa de som'), (328311, 'microfone'), (591120, 'câmera canon')]

vendas_produtos_2019.sort(reverse=True)

print(vendas_produtos_2019) # [(973139, 'geladeira'), (892292, 'adega'), (887061, 'notebook asus'), (718654, 'máquina de café'), (712350, 'galaxy'), (591120, 'câmera canon'), (573823, 'ipad'), (558147, 'iphone'), (531580, 'kindle'), (489705, 'caixa de som'), (438508, 'microsoft surface'), (422760, 'notebook dell'), (405252, 'tv'), (328311, 'microfone'), (237467, 'webcam'), (154753, 'notebook hp')]

print(vendas_produtos_2019[0][1]) # geladeira