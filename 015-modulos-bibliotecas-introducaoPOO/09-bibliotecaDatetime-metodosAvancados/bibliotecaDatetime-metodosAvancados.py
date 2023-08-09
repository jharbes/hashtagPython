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


print(agora.strftime('%a')) # Wed
print(agora.strftime("%A, %d de %B")) # Thursday, 29 de June


data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")

print(f"Data formatada: {data_formatada}") # Data formatada: Wednesday, 09 de August de 2023, 11:07:21

print(type(data_formatada)) # <class 'str'>




import locale
from datetime import datetime

# Definir a localização para português.
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

agora = datetime.now()
data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")

print(f"Data formatada: {data_formatada}") # Data formatada: quarta-feira, 09 de agosto de 2023, 11:10:24




"""
## datetime.datetime.strptime()

A função `strptime()` analisa uma string representando uma data e hora de acordo com um formato. O retorno é um objeto datetime.

"""
from datetime import datetime

string_data = "30 Junho, 2023, 15:30:20"
formato = "%d %B, %Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)

print(f"Data: {data}") # Data: 2023-06-30 15:30:20

print(type(data)) # <class 'datetime.datetime'>



# formato DD/MM/YYYY
string_data = "09/06/2023, 15:30:20"
formato = "%d/%m/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)

print(f"Data: {data}") # Data: 2023-06-09 15:30:20



# formato MM/DD/YYYY
string_data = "09/06/2023, 15:30:20"
formato = "%m/%d/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)

print(f"Data: {data}") # Data: 2023-09-06 15:30:20




"""
## Trabalhando com fuso horário

Podemos criar um objeto datetime usando a classe `datetime`. O construtor da classe aceita os seguintes argumentos:

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

data_hora = datetime(2023, 6, 26, 15, 30, 20)
print(f"Data/hora: {data_hora}") # Data/hora: 2023-06-26 15:30:20




"""
Os horários que vimos até o momento são os que chamamos de ingênuos (*naive*). Eles não possuem informações sobre o fuso horário. Para criar um horário consciente (*aware*), precisamos passar um objeto `tzinfo` para o construtor da classe `datetime`. O módulo `datetime` fornece uma classe `timezone` que pode ser usada para criar um objeto `tzinfo`. No exemplo abaixo, usamos UTC como fuso horário. UTC significa Tempo Universal Coordenado, que é o fuso horário de referência a partir do qual todos os outros fusos horários são calculados.

![UTC](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/World_Time_Zones_Map.png/800px-World_Time_Zones_Map.png)

"""
# exemplo com fuso horário
from datetime import datetime, timezone

fuso_horario = timezone.utc
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario)
print(f"Data/hora: {data_hora}") # Data/hora: 2023-06-26 15:30:20+00:00




# Podemos passar um objeto `timedelta` para o construtor da classe `timezone` para criar um fuso horário com um deslocamento específico. Por exemplo, o código abaixo cria um fuso horário com um deslocamento de 3 horas em relação ao UTC (o que significa que o horário apresentado está enquandrado no fuso horário -3):

# exemplo com fuso horário de São Paulo
from datetime import datetime, timezone, timedelta

fuso_horario_sao_paulo = timezone(timedelta(hours=-3))
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario_sao_paulo)

print(f"Data/hora: {data_hora}") # Data/hora: 2023-06-26 15:30:20-03:00




# Como alternativa, podemos usar o módulo `zoneinfo` para criar um objeto `tzinfo`. O módulo `zoneinfo` está disponível na biblioteca padrão do Python desde a versão 3.9. O módulo `zoneinfo` fornece uma classe `ZoneInfo` que pode ser usada para criar um objeto `tzinfo`. No exemplo abaixo, usamos o fuso horário de São Paulo. Observe que não precisamos passar um objeto `timedelta` para o construtor da classe `ZoneInfo`.

# exemplo com fuso horário de São Paulo sem necessidade de timedelta (o que significa que o horário apresentado está enquandrado no fuso horário -3)
from datetime import datetime
from zoneinfo import ZoneInfo

fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario_sao_paulo)

print(f"Data/hora: {data_hora}") # Data/hora: 2023-06-26 15:30:20-03:00




"""
### Conversão entre fusos horários

Podemos converter um objeto datetime de um fuso horário para outro usando o método `astimezone()`.

"""
from datetime import datetime
from zoneinfo import ZoneInfo


import zoneinfo

# listando todas as ZoneInfo disponiveis
zoneinfo.available_timezones()


 
data_hora_atual = datetime.now()

print(f"Data/hora atual (fuso horário local): {data_hora_atual}") # Data/hora atual (fuso horário local): 2023-08-09 12:58:36.005368


fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)

print(f"Data/hora atual em São Paulo: {data_hora_sao_paulo}") # Data/hora atual em São Paulo: 2023-08-09 12:58:36.005368-03:00


fuso_horario_ny = ZoneInfo('America/New_York')
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)

print(f"Data/hora atual em Nova York: {data_hora_ny}") # Data/hora atual em Nova York: 2023-08-09 11:58:36.005368-04:00