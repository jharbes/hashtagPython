"""
# Exercícios

## 1. Exercício "menos prático" para treinar manipulação de dicionário

Dessa vez, vamos apenas treinar a manipulação de dicionário. Transforme as listas abaixo em 1 único dicionário no formato:

dicionario = {
    produto: [vendas2019, vendas2020],
    produto2: [vendas2019, vendas2020],
    produto3: [vendas2019, vendas2020],
    ...
}

- Apesar de parecer "menos prático" esse é um procedimento que precisamos nos acostumar a fazer, visto que algumas funções (tema dos próximos módulos) precisam de dicionários para funcionar e saber transformar listas em dicionários (e vice-versa) é uma habilidade muito útil

Obs: Lembre do zip para juntar listas.

Obs2: Repare que cada item das vendas é na verdade uma lista. Então é provável que você precise fazer esse código em 2 etapas

"""

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

# seu código aqui

vendas2019e2020=zip(vendas2019,vendas2020)

produtos_vendas=zip(produtos,vendas2019e2020)

dict_produtos_vendas=dict(produtos_vendas)

print(dict_produtos_vendas) # {'iphone': (558147, 951642), 'galaxy': (712350, 244295), 'ipad': (573823, 26964), 'tv': (405252, 787604), 'máquina de café': (718654, 867660), 'kindle': (531580, 78830), 'geladeira': (973139, 710331), 'adega': (892292, 646016), 'notebook dell': (422760, 694913), 'notebook hp': (154753, 539704), 'notebook asus': (887061, 324831), 'microsoft surface': (438508, 667179), 'webcam': (237467, 295633), 'caixa de som': (489705, 725316), 'microfone': (328311, 644622), 'câmera canon': (591120, 994303)}