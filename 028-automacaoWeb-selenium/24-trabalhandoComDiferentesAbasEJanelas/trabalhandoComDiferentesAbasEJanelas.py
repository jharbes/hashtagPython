from selenium import webdriver
from selenium.webdriver.common.by import By

navegador=webdriver.Chrome()

import os, time

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)

"""

Por padrão o selenium não troca de aba automaticamente quando ao clicar em algum link uma nova aba ou janela é aberta, para isso teremos que fazer a intervencao por meio de codigo.

"""

#### Botão que abre outra janela

navegador.find_element(By.XPATH,'/html/body/section[2]/div/div[6]/figure/a').click()

# tentando preencher o formulario que esta na nova aba sem sucesso
try:
    navegador.find_element(By.NAME,'firstname').send_keys('Jorge')
    navegador.find_element(By.NAME,'email').send_keys('jharbes@hotmail.com')
except:
    print('Elemento inexistente na aba/pagina atual')


### Outra aba

# o window handles vai listar todos os navegadores que estao sendo controlados pelo selenium
listaAbas=navegador.window_handles

abaOriginal=navegador.window_handles[0]
novaAba=navegador.window_handles[1]

navegador.switch_to.window(novaAba)

try:
    navegador.find_element(By.NAME,'firstname').send_keys('Jorge')
    navegador.find_element(By.NAME,'email').send_keys('jharbes@hotmail.com')
except:
    print('Elemento inexistente na aba/pagina atual')


time.sleep(2)
# voltando para a aba original
navegador.switch_to.window(abaOriginal)

navegador.find_element(By.XPATH,'/html/body/section[2]/div/div[4]/figure/a/img').click()



# observe que o listaAbas criado tera que ser recriado para que ele obtenha os novos elementos de abas abertos

print(listaAbas) # ['2754369FD71C6788DD409D06DCAAE3D3', '61E7D2632071A06F6A3C957801E06D7C']

print(navegador.window_handles) # ['2754369FD71C6788DD409D06DCAAE3D3', '61E7D2632071A06F6A3C957801E06D7C', 'F718CB13500E8C9E9ED44F7545508BBB']

# vendo o titulo de todas as abas para melhor controle
for aba in navegador.window_handles:
    navegador.switch_to.window(aba)
    print(navegador.title)


# *** NOVAS JANELAS SERAO TRATADAS EXATAMENTE COMO NOVAS ABAS ***

# *** fechar a janela ou aba atual
navegador.close()

# *** fecha todo o navegador
navegador.quit()




time.sleep(5)