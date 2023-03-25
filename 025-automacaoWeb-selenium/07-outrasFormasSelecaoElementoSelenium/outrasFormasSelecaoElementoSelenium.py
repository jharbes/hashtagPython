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
text                .LINK_TEXT
tipo de informacao  .PARTIAL_LINK_TEXT
name                .NAME
tag name            .TAG_NAME
css selector        .CSS_SELECTOR

Preferencia de uso:
id
"""


from selenium.webdriver.common.by import By