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

print(f"Ano: {agora.year}") # Ano: 2023
print(f"Mês: {agora.month}") # Mês: 8
print(f"Dia: {agora.day}") # Dia: 7
print(f"Hora: {agora.hour}") # Hora: 10
print(f"Minuto: {agora.minute}") # Minuto: 17
print(f"Segundo: {agora.second}") # Segundo: 4




## datetime.date.today()

# A função `today()` retorna a data atual.

from datetime import date

hoje = date.today()
print(f"Data atual: {hoje}") # Data atual: 2023-08-07

print(f"Ano: {hoje.year}") # Ano: 2023
print(f"Mês: {hoje.month}") # Mês: 8
print(f"Dia: {hoje.day}") # Dia: 7




## datetime.timedelta()

# A classe `timedelta` é usada para realizar operações com datas (adição e subtração).

from datetime import datetime, timedelta

data_atual = datetime.now()
print(f"Data atual: {data_atual}") # Data atual: 2023-08-07 10:23:47.549034

data_futura = data_atual + timedelta(days=10)
print(f"Data 10 dias no futuro: {data_futura}") # Data 10 dias no futuro: 2023-08-17 10:23:47.549034

data_passada = data_atual - timedelta(days=10)
print(f"Data 10 dias no passado: {data_passada}") # Data 10 dias no passado: 2023-07-28 10:23:47.549034


dez_horas_adiante = data_atual + timedelta(hours=10)
print(f"10 horas adiante: {dez_horas_adiante}") # 10 horas adiante: 2023-08-07 20:23:47.549034




"""
## Criação de um objeto datetime

Podemos criar um objeto datetime usando a classe `datetime`. O construtor da classe possui como principais argumentos:

- `year`: ano (por exemplo, 2023)
- `month`: mês (1-12)
- `day`: dia (1-31)
- `hour`: hora (0-23)
- `minute`: minuto (0-59)
- `second`: segundo (0-59)
- `microsecond`: microssegundo (0-999999)
- `tzinfo`: fuso horário

"""
from datetime import datetime

data = datetime(2023, 7, 20, 8, 30, 20)
print(f"Data: {data}") # Data: 2023-07-20 08:30:20


data = datetime(2023, 7, 20)
print(f"Data: {data}") # Data: 2023-07-20 00:00:00


data = datetime(2023, 7, 20, 8, 30, 20, 100000)
print(f"Data: {data}") # Data: 2023-07-20 08:30:20.100000



# `fromisoformat()` é um método de classe que converte uma string em um objeto datetime.

data_hora_iso = datetime.fromisoformat("2023-06-26 15:30:20")
print(f"Data/hora: {data_hora_iso}") # Data/hora: 2023-06-26 15:30:20




"""
## Calcular a diferença entre duas datas

Podemos calcular a diferença entre duas datas subtraindo uma da outra. O resultado será um objeto timedelta.

"""
from datetime import datetime

data1 = datetime(2023, 6, 25)
data2 = datetime(2023, 7, 25)

diferenca = data2 - data1
print(f"A diferença entre as duas datas é de {diferenca.days} dias.") # A diferença entre as duas datas é de 30 dias.


type(diferenca) # datetime.timedelta

diferenca.days # 30




"""
## Comparação entre datas

Podemos comparar datas usando os operadores de comparação padrão.

Segue uma lógica intuitiva:

    passado < presente < futuro

"""
from datetime import datetime

data1 = datetime(2023, 7, 25)
data2 = datetime(2023, 7, 25)

if data1 > data2:
    print("A data1 é posterior à data2")
elif data1 < data2:
    print("A data1 é anterior à data2")
else:
    print("As datas são iguais")

# As datas são iguais


data1 = datetime(2023, 7, 25, 8, 30, 30)
data2 = datetime(2023, 7, 25, 8, 30, 20)

if data1 > data2:
    print("A data1 é posterior à data2")
elif data1 < data2:
    print("A data1 é anterior à data2")
else:
    print("As datas são iguais")

# A data1 é posterior à data2




"""
## Ordenando uma lista de datas

Podemos usar a função `sorted` para ordenar uma lista de datas.

"""
from datetime import datetime

datas = [
    datetime(2023, 6, 28),
    datetime(2023, 5, 28),
    datetime(2023, 7, 28),
    datetime(2023, 6, 18),
]

datas_ordenadas = sorted(datas)

print(datas_ordenadas) # [datetime.datetime(2023, 5, 28, 0, 0), datetime.datetime(2023, 6, 18, 0, 0), datetime.datetime(2023, 6, 28, 0, 0), datetime.datetime(2023, 7, 28, 0, 0)]


for data in datas_ordenadas:
    print(data.date())

# 2023-05-28
# 2023-06-18
# 2023-06-28
# 2023-07-28