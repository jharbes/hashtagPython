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

# tentando preencher o formulario
navegador.find_element(By.NAME,'firstname').send_keys('Jorge')



### Outra aba

abaOriginal=
novaAba=






time.sleep(5)