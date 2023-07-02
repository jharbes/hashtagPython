"""
# Cuidado com o while -> Loop Infinito

Sempre que for usar o comando while, lembre-se de ter certeza que o programa vai terminar em algum momento

### Exemplo

Digamos que temos uma lista de vendedores e as quantidades vendidas e queremos identificar todos os vendedores que bateram a meta de 50 vendas.

"""

vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]

vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']

meta = 50

vendedores_meta_batida=[]
i=0
while i<len(vendas):
    if vendas[i]>=50:
        vendedores_meta_batida.append(vendedores[i])
    i+=1

print('Os vendedores com meta batida são:\n{}'.format(vendedores_meta_batida))