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
navegador.find_element(By.NAME,'firstname').send_keys('Jorge')



### Outra aba

# o window handles vai listar todos os navegadores que estao sendo controlados pelo selenium
listaAbas=navegador.window_handles

abaOriginal=navegador.window_handles[0]
novaAba=navegador.window_handles[1]

navegador.switch_to.window(novaAba)






time.sleep(5)