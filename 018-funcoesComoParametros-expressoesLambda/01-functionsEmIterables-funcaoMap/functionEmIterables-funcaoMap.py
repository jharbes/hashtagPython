"""
# Function em iterables

### Segue a mesma lógica de list comprehension, mas é mais simples

Basicamente alguns métodos e funções que já existem no Python podem rodar uma function para cada item, da mesma forma que fizemos com list comprehension.

Isso pode ajudar a gente a resolver alguns desafios de forma mais simples

Uma função que permite que a gente faça isso é a map function

### map function

lista = list(map(função, iterable_original))

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


print(produtos)