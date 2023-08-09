"""
## Oferecendo desconto para cliente com base na última compra

Suponha que você está trabalhando para uma empresa que deseja rastrear a atividade do cliente. Uma métrica que eles estão interessados é o tempo que passou desde a última transação do cliente. Se for muito tempo, eles podem oferecer um desconto para o cliente. Crie um script Python que mostra quanto tempo se passou desde a última compra do cliente. Se faz mais de 30 dias, mostre uma mensagem oferecendo um desconto para o cliente.

"""
from datetime import datetime, timedelta

def oferecer_desconto(obj_datetime):
    data_atual=datetime.now()
    if data_atual>obj_datetime+timedelta(days=30):
        return 'Oferecer desconto'
    else:
        return 'Não oferecer desconto'

print(oferecer_desconto(datetime(2022,6,10)))
print(oferecer_desconto(datetime(2023,8,5)))




"""
## Data e hora em diferentes fusos horários

Uma empresa tem escritórios em São Paulo, Nova York e Tóquio. Crie um script Python que mostra a data e hora atuais nesses três fusos horários. Exiba, também, se estes escritórios estão abertos ou fechados (9h às 17h).

"""
from datetime import datetime
from zoneinfo import ZoneInfo


def status_escritorios():
    data_hora_atual=datetime.now()

    data_hora_sao_paulo=data_hora_atual.astimezone(ZoneInfo('America/Sao_Paulo'))
    situacao_sao_paulo='Aberto' if data_hora_sao_paulo.hour>=9 and data_hora_sao_paulo.hour<17 else 'Fechado'
    print('Horário escritório de São Paulo:\nEstado atual: {} - {}\n'.format(situacao_sao_paulo,data_hora_sao_paulo))

    data_hora_new_york=data_hora_atual.astimezone(ZoneInfo('America/New_York'))
    situacao_new_york='Aberto' if data_hora_new_york.hour>=9 and data_hora_new_york.hour<17 else 'Fechado'
    print('Horário escritório de Nova York:\nEstado atual: {} - {}\n'.format(situacao_new_york,data_hora_new_york))

    data_hora_tokyo=data_hora_atual.astimezone(ZoneInfo('Japan'))
    situacao_tokyo='Aberto' if data_hora_tokyo.hour>=9 and data_hora_tokyo.hour<17 else 'Fechado'
    print('Horário escritório de Tokyo:\nEstado atual: {} - {}\n'.format(situacao_tokyo,data_hora_tokyo))

status_escritorios()








import zoneinfo

# listando todas as ZoneInfo disponiveis
zoneinfo.available_timezones()