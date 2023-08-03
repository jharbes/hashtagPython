"""
## Tempo até o próximo ano

Crie um script Python que calcula quantos dias, horas, minutos e segundos faltam até o próximo Ano Novo.

Lembrar da tupla de struct_time: https://docs.python.org/3/library/time.html#time.struct_time

"""

# lembrando

segundos_por_minuto = 60
segundos_por_hora = 60 * 60
segundos_por_dia = 24 * 60 * 60

print(f"Segundos em um minuto: {segundos_por_minuto} s") # 60

print(f"Segundos em uma hora: {segundos_por_hora} s") # 3600
print(f"Segundos em um dia: {segundos_por_dia} s") # 86400




import time

tempo_atual_struct=time.localtime()
print(tempo_atual_struct) # time.struct_time(tm_year=2023, tm_mon=8, tm_mday=3, tm_hour=13, tm_min=3, tm_sec=19, tm_wday=3, tm_yday=215, tm_isdst=0)

proximo_ano_novo_segundos=time.mktime((2024,1,1,0,0,0,0,0,0))
print(proximo_ano_novo_segundos) # 1704078000.0

tempo_atual_segundos=time.mktime(tempo_atual_struct)
print(tempo_atual_segundos) # 1691078599.0

diferenca_de_tempo=proximo_ano_novo_segundos-tempo_atual_segundos
print(diferenca_de_tempo) # 12999401.0