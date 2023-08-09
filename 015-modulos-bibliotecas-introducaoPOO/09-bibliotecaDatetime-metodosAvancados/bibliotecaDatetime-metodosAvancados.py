"""
# Guia para o módulo `datetime` em Python

O módulo `datetime` em Python fornece classes para manipulação de datas e horas. Aqui está um guia simples para algumas das funções mais úteis deste módulo.

"""

"""
## datetime.datetime.strftime()

A função `strftime()` converte um objeto datetime para uma string de acordo com um formato específico.

Símbolos que podem ser usados para formatar datas podem ser achados [aqui](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

"""
from datetime import datetime

agora = datetime.now()
print(agora) # 2023-08-09 11:07:21.283169


print(type(agora)) # <class 'datetime.datetime'>


print(agora.strftime("%A, %d de %B")) # Thursday, 29 de June


data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")

print(f"Data formatada: {data_formatada}") # Data formatada: Wednesday, 09 de August de 2023, 11:07:21




import locale
from datetime import datetime

# Definir a localização para português.
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

agora = datetime.now()
data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")

print(f"Data formatada: {data_formatada}") # Data formatada: quarta-feira, 09 de agosto de 2023, 11:10:24




