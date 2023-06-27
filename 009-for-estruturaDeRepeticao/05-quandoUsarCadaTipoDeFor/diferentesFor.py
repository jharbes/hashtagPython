#!/usr/bin/env python
# coding: utf-8

# In[ ]:


produtos = ["iphone", "ipad", "airpod", "macbook"]
precos = [7000, 10000, 2500, 14000]


# ### For item in lista

# In[ ]:


# preco com imposto
for preco in precos:
    print(preco*1.1)

# ### For i in range

# In[ ]:


# preco de cada produto
for i in range(len(precos)):
    print(produtos[i],precos[i])

# ### For item in lista com enumerate

# In[ ]:


# preco de cada produto com imposto
for i, preco in enumerate(precos):
    print(produtos[i],preco)

# In[ ]:




