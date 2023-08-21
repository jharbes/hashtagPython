"""
# List Comprehension com if para escolher o resultado final

### Estrutura:

lista = [item if condicao else outro_resultado for item in iterable]


- Digamos que eu esteja analisando os vendedores de uma loja e queira criar uma lista para enviar para o RH com o bônus de cada vendedor.
- O bônus é dado por 10% do valor de vendas dele, caso ele tenha batido a meta

"""
vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90, 'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880, 'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300, 'Sandra': 450, 'Luis': 800}
meta = 1000


# - Fazendo por for

bonus_for={}
for vendedor in vendedores_dic:
    if vendedores_dic[vendedor]>meta:
        bonus_for[vendedor]=vendedores_dic[vendedor]*0.1  
    else:
        bonus_for[vendedor]=0

print(bonus_for) # {'Maria': 120.0, 'José': 0, 'Antônio': 0, 'João': 150.0, 'Francisco': 190.0, 'Ana': 275.0, 'Luiz': 0, 'Paulo': 0, 'Carlos': 0, 'Manoel': 0, 'Pedro': 0, 'Francisca': 0, 'Marcos': 110.0, 'Raimundo': 0, 'Sebastião': 0, 'Antônia': 0, 'Marcelo': 0, 'Jorge': 0, 'Márcia': 111.10000000000001, 'Geraldo': 0, 'Adriana': 0, 'Sandra': 0, 'Luis': 0}


bonus_for_list=[]
for vendedor in vendedores_dic:
    bonus_for_list.append((vendedor,vendedores_dic[vendedor]*0.1) if vendedores_dic[vendedor]>1000 else (vendedor,0))

print(bonus_for_list) # [('Maria', 120.0), ('José', 0), ('Antônio', 0), ('João', 150.0), ('Francisco', 190.0), ('Ana', 275.0), ('Luiz', 0), ('Paulo', 0), ('Carlos', 0), ('Manoel', 0), ('Pedro', 0), ('Francisca', 0), ('Marcos', 110.0), ('Raimundo', 0), ('Sebastião', 0), ('Antônia', 0), ('Marcelo', 0), ('Jorge', 0), ('Márcia', 111.10000000000001), ('Geraldo', 0), ('Adriana', 0), ('Sandra', 0), ('Luis', 0)]




# - Fazendo por List Comprehension

bonus2=[(vendedor,vendedores_dic[vendedor]*0.1) if vendedores_dic[vendedor]>meta else (vendedor,0) for vendedor in vendedores_dic]

print(bonus2) # [('Maria', 120.0), ('José', 0), ('Antônio', 0), ('João', 150.0), ('Francisco', 190.0), ('Ana', 275.0), ('Luiz', 0), ('Paulo', 0), ('Carlos', 0), ('Manoel', 0), ('Pedro', 0), ('Francisca', 0), ('Marcos', 110.0), ('Raimundo', 0), ('Sebastião', 0), ('Antônia', 0), ('Marcelo', 0), ('Jorge', 0), ('Márcia', 111.10000000000001), ('Geraldo', 0), ('Adriana', 0), ('Sandra', 0), ('Luis', 0)]




# - Fazendo por Dict Comprehension

