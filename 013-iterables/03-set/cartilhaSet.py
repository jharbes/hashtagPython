"""
# Métodos de Sets

### Esses são os métodos mais usados de set

"""

# - add -> adiciona um item no set

meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.add('airpod')
print(meu_set) # {'macbook', 'airpod', 'ipad', 'iphone'}




# - remove -> retira um item de um set

meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.remove('iphone')
print(meu_set) # {'macbook', 'ipad'}




# - clear -> retira todos os itens de um set

meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.clear()
print(meu_set) # set()




# - union -> junta as informações de 2 sets. Se houver algum valor duplicado, ele constará apenas 1 vez no set final

produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
todos_produtos = produtos.union(lancamentos)
print(todos_produtos) # {'macbook', 'apple watch', 'ipad', 'airpod', 'iphone', 'ipod'}




# - intersection -> pega apenas as informações que existem nos 2 sets ao mesmo tempo

produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
intersecao = produtos.intersection(lancamentos)
print(intersecao) # {'ipad'}




# - difference -> retorna todas as informações de um set que não fazem parte de outro set

produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
produtos_nao_lancamentos = produtos.difference(lancamentos)
print(produtos_nao_lancamentos) # {'macbook', 'iphone'}
# repare que ipad foi retirado do resultado porque ele estava contido no set de lançamentos