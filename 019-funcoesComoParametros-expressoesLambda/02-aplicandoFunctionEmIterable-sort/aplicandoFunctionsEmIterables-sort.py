"""
# sort (ou sorted) com function

### Descrição:

Até agora no programa, usamos várias vezes o .sort() para ordenar listas

Mas o método sort tem um parâmetro que nunca usamos e que agora sabemos usar.


Diferença entre .sort() e sorted() :

lista.sort() ordena a lista alterando a lista original

sorted() nao altera a lista original, logo tem que ser atribuido a uma variavel para que tenha efeito pratico

"""
produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos.sort()

print(produtos) # ['IPad', 'IPhone 11', 'IPhone x', 'airpods', 'apple tv', 'apple watch', 'mac', 'mac book']



# - Como faríamos para ordenar corretamente?

produtos2=['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos2.sort(key=str.lower)

print(produtos2) # ['airpods', 'apple tv', 'apple watch', 'IPad', 'IPhone 11', 'IPhone x', 'mac', 'mac book']




### Outro exemplo: como ordenar um dicionário de acordo com o valor

vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

vendas_produtos_list=[(vendas_produtos[produto],produto) for produto in vendas_produtos]

vendas_produtos_list.sort(reverse=True)

print(vendas_produtos_list) # [(5500, 'iphone'), (300, 'microondas'), (150, 'cafeiteira'), (100, 'vinho')]

lista_vendas=[(quantidade,produto) for produto,quantidade in vendas_produtos_list]

print(lista_vendas) # [('iphone', 5500), ('microondas', 300), ('cafeiteira', 150), ('vinho', 100)]



# - Queremos listar da maior quantidade de vendas para a menor, para enviar como report para o diretor, por exemplo

print(dict(lista_vendas)) # {'iphone': 5500, 'microondas': 300, 'cafeiteira': 150, 'vinho': 100}