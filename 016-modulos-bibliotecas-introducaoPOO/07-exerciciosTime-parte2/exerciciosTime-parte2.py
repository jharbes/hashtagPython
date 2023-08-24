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


# essa funcao vai funcionar perfeitamente mesmo com a imprecisao do dado do dia da semana
# nosso primeiro argumento será tempo_atual_struct.tm_year+1 para que o codigo fique dinamico, permitindo que ele funcione independente do ano em que estejamos
proximo_ano_novo_segundos=time.mktime((tempo_atual_struct.tm_year+1,1,1,0,0,0,0,0,0))
print(proximo_ano_novo_segundos) # 1704078000.0

tempo_atual_segundos=time.mktime(tempo_atual_struct)
print(tempo_atual_segundos) # 1691078599.0

diferenca_de_tempo=proximo_ano_novo_segundos-tempo_atual_segundos
print(diferenca_de_tempo) # 12999401.0


print('------INICIO DOS CALCULOS)')

diferenca_de_tempo=int(diferenca_de_tempo)

segundos=diferenca_de_tempo%60
minutos=diferenca_de_tempo//60

print(segundos) # 53
print(minutos) # 216627


horas=minutos//60
minutos=minutos%60

print(minutos) # 27
print(horas) # 3610


dias=horas//24 
horas=horas%24

print(horas) # 10
print(dias) # 150

print('O tempo para o próximo ano novo é de {} dias, {} horas, {} minutos e {} segundos'.format(dias,horas,minutos,segundos)) # O tempo para o próximo ano novo é de 150 dias, 10 horas, 27 minutos e 53 segundos