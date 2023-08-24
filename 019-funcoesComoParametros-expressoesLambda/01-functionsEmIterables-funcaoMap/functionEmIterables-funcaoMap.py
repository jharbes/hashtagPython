"""
# Function em iterables

### Segue a mesma lógica de list comprehension, mas é mais simples

Basicamente alguns métodos e funções que já existem no Python podem rodar uma function para cada item, da mesma forma que fizemos com list comprehension.

Isso pode ajudar a gente a resolver alguns desafios de forma mais simples

Uma função que permite que a gente faça isso é a map function

### map function

lista = list(map(função, iterable_original))


### Olhando assim pode não parecer tão útil, mas a lógica de executar uma função para cada item é bem útil para outras funções que já existem no Python. Veremos na próxima aula

"""
# - Exemplo: digamos que eu tenha uma function que corrige um código de um produto (semelhante ao que fizemos na seção de function aqui do curso)

def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto


# - Agora queremos padronizar uma lista de códigos:

produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']


# - Usando o for, temos que percorrer a lista toda e para cada item executar a function

for i,item in enumerate(produtos):
    produtos[i]=padronizar_texto(item)

print(produtos) # ['abc12', 'abc34', 'abc37', 'beb12', 'bsa151', 'beb23']




# - Usando o map, apenas chamamos a função e ela já faz isso para a gente

# map aplica uma function (primeiro parametro da funcao) em cada um dos itens do enumerate (nesse caso uma lista)
# a resposta sera um map object, por isso envolvemos na funcao list() para termos como resposta uma lista
produtos3=list(map(padronizar_texto,produtos))

print(produtos3)