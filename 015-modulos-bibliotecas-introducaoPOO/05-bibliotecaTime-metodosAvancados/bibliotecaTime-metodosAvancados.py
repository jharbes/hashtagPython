"""
# Módulo `time` em Python

O módulo `time` em Python fornece uma variedade de funções para trabalhar com tempo.

## time.strftime()

A função `strftime()` converte um objeto de tempo struct para uma string de acordo com um formato específico.

Os símbolos de formato que podem ser usados estão disponíveis na documentação oficial do Python, [neste link](https://docs.python.org/3/library/time.html#time.strftime).

Por exemplo, podemos querer uma string de tempo no seguinte formato: "Dia da semana, dia do mês de mês do ano, horas:minutos:segundos". Podemos usar o seguinte código para obter o tempo formatado:

"""

import time

tempo_em_struct = time.localtime()
print(tempo_em_struct) # time.struct_time(tm_year=2023, tm_mon=8, tm_mday=3, tm_hour=7, tm_min=16, tm_sec=55, tm_wday=3, tm_yday=215, tm_isdst=0)


print(time.strftime("%d %B %Y", tempo_em_struct)) # 03 August 2023


print(time.strftime("%H:%M:%S", tempo_em_struct)) # 07:16:55


tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S", tempo_em_struct)
print(f"Tempo formatado: {tempo_formatado}") # Tempo formatado: Thursday, 29 de June de 2023, 10:20:00




# Observe que o dia e o mês apareceram em inglês. Para obter o tempo formatado em português, podemos usar o módulo `locale` do Python.

import locale
import time

# Definir a localização para português.
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S", tempo_em_struct)

print(f"Tempo formatado: {tempo_formatado}") # Tempo formatado: quinta-feira, 03 de agosto de 2023, 07:18:42




## time.strptime()

# A função `strptime()` analisa uma string representando um horário de acordo com um formato. O retorno é um objeto `struct_time`.

string_tempo = "30 Junho, 2023"
formato = "%d %B, %Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}") # Tempo em struct: time.struct_time(tm_year=2023, tm_mon=6, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=181, tm_isdst=-1)


# data na forma dia/mês/ano
string_tempo = "06/09/2023"
formato = "%d/%m/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}") # Tempo em struct: time.struct_time(tm_year=2023, tm_mon=9, tm_mday=6, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=249, tm_isdst=-1)


# data na forma mês/dia/ano
string_tempo = "06/09/2023"
formato = "%m/%d/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}") # Tempo em struct: time.struct_time(tm_year=2023, tm_mon=6, tm_mday=9, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=160, tm_isdst=-1)




## time.gmtime()

# A função `gmtime()` converte um tempo expresso em segundos desde a epoch em um objeto struct_time em UTC. UTC significa Coordinated Universal Time, também conhecido como GMT (Greenwich Mean Time). Este é o fuso horário padrão em que as funções `time` operam.

# Tempo em UTC para 0 segundos desde a epoch

time.gmtime(0) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0


gmt_struct = time.gmtime()  # tempo atual em UTC já que não fornecemos nenhum argumento

print(f"Tempo em UTC: {gmt_struct}") # Tempo em UTC: time.struct_time(tm_year=2023, tm_mon=8, tm_mday=3, tm_hour=10, tm_min=36, tm_sec=21, tm_wday=3, tm_yday=215, tm_isdst=0)


# comparando com localtime
print(f"Tempo local: {time.localtime()}") # Tempo local: time.struct_time(tm_year=2023, tm_mon=8, tm_mday=3, tm_hour=7, tm_min=37, tm_sec=20, tm_wday=3, tm_yday=215, tm_isdst=0)


print(f"Tempo em UTC: {time.strftime('%A, %d de %B de %Y, %H:%M:%S', gmt_struct)}") # Tempo em UTC: quinta-feira, 03 de agosto de 2023, 10:36:21


print(gmt_struct.tm_zone) # UTC


gmt_struct_exemplo = time.gmtime(1_234_567_890)

print(f"Tempo em UTC: {gmt_struct_exemplo}") # Tempo em UTC: time.struct_time(tm_year=2009, tm_mon=2, tm_mday=13, tm_hour=23, tm_min=31, tm_sec=30, tm_wday=4, tm_yday=44, tm_isdst=0)

print(f"Tempo em UTC: {time.strftime('%A, %d de %B de %Y, %H:%M:%S', gmt_struct_exemplo)}") # Tempo em UTC: sexta-feira, 13 de fevereiro de 2009, 23:31:30