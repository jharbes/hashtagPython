"""
## Exercício

Você é um gerente de vendas e tem os dados de vendas de três produtos diferentes (Produto A, Produto B, Produto C) para os últimos 5 dias em um array 2D NumPy. Cada linha do array representa um produto e cada coluna representa um dia. Seu trabalho é calcular as vendas totais para cada produto e para cada dia.

Use o seguinte array para sua análise:

```python
vendas = np.array([[50, 60, 70, 65, 80],
                   [85, 90, 78, 92, 88],
                   [72, 75, 68, 77, 76]])
```

**Solução:**

"""
import numpy as np

lista_produtos=np.array(['Produto A','Produto B','Produto C'])

vendas = np.array([[50, 60, 70, 65, 80],
                   [85, 90, 78, 92, 88],
                   [72, 75, 68, 77, 76]])


vendas_totais_produto=vendas.sum(axis=1)

print(f'{vendas_totais_produto=}\n') # vendas_totais_produto=array([325, 433, 368]

for i,venda in enumerate(vendas_totais_produto):
    print('Número de vendas do {} foram {}'.format(lista_produtos[i],venda))




vendas_totais_dia=vendas.sum(axis=0)

print(f'{vendas_totais_dia=}\n') # vendas_totais_dia=array([207, 225, 216, 234, 244])

for i,venda in enumerate(vendas_totais_dia):
    print('Número de vendas do dia {} foram {}'.format(i+1,venda))