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


# #### Selecionar pela tag

# - Vamos selecionar o título

# Extrai o texto do titulo da pagina hashtag
titulo = navegador.find_element(By.TAG_NAME, 'h2').text
print(titulo)



#### Selecionar pelo Partial Link Text (ou LINK_TEXT)

# - Quero conseguir pegar o número de whatsapp de contato
# sendo assim iremos procurar em algum lugar o elemento cujo texto possua o valor desejado (WhatsApp)

# Extrai o texto do elemento cujo texto tenha em alguma das suas partes a palavra escolhida
numero_whatsapp = navegador.find_element(By.PARTIAL_LINK_TEXT, 'WhatsApp').text
print(numero_whatsapp)


time.sleep(5)