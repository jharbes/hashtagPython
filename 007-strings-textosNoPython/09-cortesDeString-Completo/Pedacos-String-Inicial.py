#!/usr/bin/env python
# coding: utf-8

# ### Forma Básica

# In[ ]:

precos = "Jan: 25, Fev: 27, Mar: 29"

precos = "Jan: 25, Fev: 27, Mar: 29"

precos_lista=precos.split(',')
print(precos_lista)

precos_lista=[item[-2:] for item in precos_lista]
print(precos_lista)

# ### Posição Inicial e Final



# In[ ]:

# STEP NAS STRINGS

# posicoes [x,y,z]
# x -> posicao inicial do recorte
# y -> posicao final do recorte
# z -> STEP - de quantos em quantos ele vai buscar

codigo = "1.2.3.4,5,1,2.3.4,7.9"
num_codigos = codigo[-1::-1]

print(num_codigos) # 9.7,4.3.2,1,5,4.3.2.1



num_codigos = codigo[10:2:-2]

print(num_codigos) # 1543


