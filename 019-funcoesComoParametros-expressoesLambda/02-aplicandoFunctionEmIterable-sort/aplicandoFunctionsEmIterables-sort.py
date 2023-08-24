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