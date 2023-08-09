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