"""
# Exemplos de parâmetros


- upper() -> não tem parâmetros 
- sort() -> apenas parâmetros keyword
- extend(lista) -> 1 parâmetro obrigatório
- nossa função eh_da_categoria(bebida, cod_categoria) -> 2 parâmetros de posição obrigatórios

"""

def eh_da_categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False
    


# texto para upper
cod_produto = 'beb12304'
print(cod_produto.upper()) # BEB12304
print(cod_produto) # beb12304

# lista para sort e extend
vendas_ano = [100, 200, 50, 90, 240, 300, 55, 10, 789, 60]
vendas_novdez = [500, 1555]

vendas_ano.sort()
print(vendas_ano) # [10, 50, 55, 60, 90, 100, 200, 240, 300, 789]

vendas_ano.sort(reverse=True)
print(vendas_ano) # [789, 300, 240, 200, 100, 90, 60, 55, 50, 10]

vendas_ano.extend(vendas_novdez)
print(vendas_ano) # [789, 300, 240, 200, 100, 90, 60, 55, 50, 10, 500, 1555]