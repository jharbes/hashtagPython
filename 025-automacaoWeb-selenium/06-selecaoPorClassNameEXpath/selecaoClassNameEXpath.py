from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

import os
import time

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)

"""
MANEIRAS DE SELECIONAR NO SELENIUM:

id                  .ID
xpath               .XPATH
class_name          .CLASS_NAME
texto inteiro       .LINK_TEXT
pedaço de texto     .PARTIAL_LINK_TEXT
name                .NAME
tag name            .TAG_NAME
css selector        .CSS_SELECTOR

Preferencia de uso:
id
"""


from selenium.webdriver.common.by import By

# achando o elemento por classe
navegador.find_element(By.CLASS_NAME,'custom-logo').click() # clica no logo da hashtag na pagina inicial (esquerda superior)

# achando o mesmo elemento, agora por xpath
navegador.find_element(By.XPATH,'//*[@id="header"]/div/div/div[1]/a/img').click()


time.sleep(5)