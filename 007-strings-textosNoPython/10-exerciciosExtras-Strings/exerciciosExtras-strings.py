"""
# Strings

Todos os exercícios são feitos partindo-se do pressuposto de que todas as entradas são dadas de forma correta. Casos limite não mencionados no enunciado não são abordados porque não fazem parte do exercício.

"""
#### 1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

string1=input('Informe a primeira string: ')
string2=input('Informe a segunda string: ')

print('\nTamanho de "'+string1+'": '+str(len(string1))+' caracteres')
print('Tamanho de "'+string2+'": '+str(len(string2))+' caracteres')
print('As duas strings são de tamanhos diferentes.' if len(string1)!=len(string2) else 'As duas strings são de tamanho igual.')
print('As duas strings possuem conteúdo diferente.' if string1!=string2 else 'As duas strings possuem conteúdo igual.')




#### 2. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

telefone=input('Digite o número do telefone: ')

print('Telefone: '+telefone)

telefone=telefone.replace('-','').strip()

if len(telefone)<7:
    print('Número inválido, favor preencher novamente.')
elif len(telefone)==7:
    print('Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.')
    telefone='3'+telefone
    print('Telefone corrigido sem formatação: '+telefone)
    print('Telefone corrigido com formatação: '+telefone[:4]+'-'+telefone[4:])
elif len(telefone)==8:
    print('Telefone ok')
    pass
else:
    print('Número inválido, favor preencher novamente.')