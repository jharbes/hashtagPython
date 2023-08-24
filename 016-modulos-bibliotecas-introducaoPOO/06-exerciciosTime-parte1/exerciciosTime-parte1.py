"""
## Contagem regressiva

Um evento especial está programado para começar em 10 segundos. Crie uma contagem regressiva que começa em 10 e vai até 0, com uma pausa de um segundo entre cada número.

"""

import time

for i in range(11):
    time.sleep(1)
    print(10-i,end=' \r')




"""
## Formatação de tempo

Uma empresa quer exibir a data e a hora atual em seu site no formato "Dia da semana, dia do mês de mês de ano, horas:minutos". Crie um script Python que mostra a data e a hora atuais neste formato.

"""

import locale
import time

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


def formataTempo(objeto_structime):
    return time.strftime('%A, %d de %B de %Y, %H:%M',objeto_structime)


tempo_atual=time.localtime()

print(formataTempo(tempo_atual)) # quinta-feira, 03 de agosto de 2023, 10:20