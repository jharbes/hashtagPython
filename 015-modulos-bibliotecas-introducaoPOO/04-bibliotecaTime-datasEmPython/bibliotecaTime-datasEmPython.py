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