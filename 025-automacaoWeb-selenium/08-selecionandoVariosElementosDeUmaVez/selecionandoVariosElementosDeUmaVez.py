from selenium import webdriver
import time

navegador=webdriver.Chrome()

import os
import time

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)

"""
MANEIRAS DE SELECIONAR NO SELENIUM:

id                      .ID
xpath                   .XPATH
class_name              .CLASS_NAME
texto inteiro de link   .LINK_TEXT
pedaço de texto de link .PARTIAL_LINK_TEXT
name                    .NAME
tag name                .TAG_NAME
css selector            .CSS_SELECTOR

Preferencia de uso:
id
class
xpath
"""


from selenium.webdriver.common.by import By


# #### Selecionar vários elementos de uma vez

# - Vamos selecionar pelo find_elements
# - Vamos clicar no item Blog do menu

lista_elementos = navegador.find_elements(By.CLASS_NAME, 'nav-link')
print(lista_elementos)

for elemento in lista_elementos:
    if "blog" in elemento.text.lower():
        elemento.click()
        break # importante usar o break  apos encontrar o elemento pois ele vai trocar de pagina e os proximos elementos nao irao mais existir, podendo ocasionar erro e quebrar o programa




time.sleep(5)