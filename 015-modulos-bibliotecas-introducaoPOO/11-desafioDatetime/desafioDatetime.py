"""
## Calculando a idade

Um usuário fornece sua data de nascimento no formato "dd/mm/aaaa". Crie um script Python que calcula a idade do usuário.

"""

import datetime

# data_nascimento='21/11/1983'
# data_nascimento=input('Informe sua data de nascimento no formato "dd/mm/aaaa":')
def retorna_idade(data_nascimento):
    formato='%d/%m/%Y'
    data_nascimento_datetime=datetime.datetime.strptime(data_nascimento,formato)

    data_atual=datetime.datetime.now()

    diferenca_tempo_anos=data_atual.year-data_nascimento_datetime.year

    idade=diferenca_tempo_anos
  
    if data_nascimento_datetime.month>data_atual.month:
        idade-=1
    if data_nascimento_datetime.month==data_atual.month:
        if data_nascimento_datetime.day>data_atual.day:
            idade-=1
    
    return f'Aniversário: {data_nascimento}: {idade=}\n'


print(retorna_idade('15/09/1983'))
print(retorna_idade('10/08/1983'))
print(retorna_idade('09/08/1983'))
print(retorna_idade('08/08/1983'))
print(retorna_idade('07/08/1983'))