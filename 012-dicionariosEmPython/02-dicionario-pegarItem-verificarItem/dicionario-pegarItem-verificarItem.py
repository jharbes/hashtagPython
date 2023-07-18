"""
# Não confie na ordem dos dicionários, use as chaves

### Python Versões Antigas x Versões Novas

- Dicionários eram "sem ordem". Atualmente tem ordem, mas o certo é usar as chaves
- 2 formas de pegar um valor:
    - dicionario[chave]
    - .get(chave)

"""

mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}



# - Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?
# - Quanto foi vendido de 'notebook asus' e de 'ipad'?

print(mais_vendidos['livros']) # o alquimista
print(mais_vendidos['lazer']) # prancha surf


print(vendas_tecnologia.get('notebook asus')) # 2450
print(vendas_tecnologia.get('ipad')) # 1000




### Verificar se item está no dicionário:

# - if
# - .get(chave) = None

# Se tentarmos procurar as vendas de "copo" na lista de vendas tecnologia, o que acontece?

print(vendas_tecnologia.get('copo')) # None


# Nao funciona como o get, da erro:
# print(vendas_tecnologia['copo'])


print('copo' if 'copo' in vendas_tecnologia else 'Copo nao está na lista de produtos de tecnologia')