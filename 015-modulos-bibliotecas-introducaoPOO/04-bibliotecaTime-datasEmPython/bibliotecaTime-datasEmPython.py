"""
# Módulo `time` em Python

O módulo `time` em Python fornece uma variedade de funções para trabalhar com tempo. 

## time.time()

A função `time()` retorna o tempo atual em segundos desde a Epoch (1º de janeiro de 1970).  

"""

import time

tempo_atual_segundos = time.time()

print(f"Tempo atual: {tempo_atual_segundos} segundos desde a Epoch") # Tempo atual: 1690983622.1764007 segundos desde a Epoch




tempo_atual_nanosegundos = time.time_ns()

print(f"Tempo atual: {tempo_atual_nanosegundos} nanosegundos desde a Epoch") # Tempo atual: 1690983631820419900 nanosegundos desde a Epoch




inicio = time.time()

for i in range(100_000_000): # 10000000
    pass

fim = time.time()

print(f"Tempo decorrido: {fim - inicio} segundos")




"""
## time.sleep()

A função `sleep()` faz o programa esperar pelo número de segundos especificado.

"""

print("Iniciando a pausa")
time.sleep(5)  # Pausa o programa por 5 segundos
print("Pausa terminada")




"""
## time.ctime()

A função `ctime()` converte um tempo expresso em segundos desde a epoch em uma string representando o tempo local.

"""

tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_em_segundos)
print(f"Tempo local: {tempo_local}") # Tempo local: Wed Aug  2 10:48:02 2023




"""
## time.time() vs time.localtime()

A função `time()` retorna o tempo atual em segundos desde a epoch. A função `localtime()` converte um tempo expresso em segundos desde a epoch em um objeto `struct_time`. Este objeto contém informações sobre o tempo local, como ano, mês, dia, hora, minuto, segundo, etc. A função `localtime()` usa o fuso horário local.

"""

tempo_em_segundos = time.time()
tempo_local = time.localtime(tempo_em_segundos)

print(f"Tempo local: {tempo_local}") # Tempo local: time.struct_time(tm_year=2023, tm_mon=8, tm_mday=2, tm_hour=13, tm_min=51, tm_sec=58, tm_wday=2, tm_yday=214, tm_isdst=0)

print(tempo_local.tm_year) # 2023

print(tempo_local.tm_hour) # 13

print(tempo_local.tm_mday) # 2


# Dia da semana (0-6, 0 é segunda-feira, 6 é domingo). Documentação: https://docs.python.org/3/library/time.html#time.struct_time
print(tempo_local.tm_wday) # 2


# Dia do ano (1-366).
print(tempo_local.tm_yday) # 214


print(tempo_local.tm_zone) # E. South America Standard Time


print(time.time()) # 1690995233.6412516

print(time.ctime(time.time())) # Wed Aug  2 13:53:53 2023

print(time.localtime()) # time.struct_time(tm_year=2023, tm_mon=8, tm_mday=2, tm_hour=13, tm_min=53, tm_sec=53, tm_wday=2, tm_yday=214, tm_isdst=0)