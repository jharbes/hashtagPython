"""
# Guia para o módulo `datetime` em Python

O módulo `datetime` em Python fornece classes para manipulação de datas e horas. Aqui está um guia simples para algumas das funções mais úteis deste módulo.

"""

## datetime.datetime.now()

# A função `now()` retorna a data e a hora atuais.

from datetime import datetime

agora = datetime.now()
print(f"Agora: {agora}") # Agora: 2023-08-07 10:17:04.114486

print(f"Data: {agora.date()}") # Data: 2023-08-07
print(f"Horário: {agora.time()}") # Horário: 10:17:04.114486