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


# #### Selecionar pela tag

# - Vamos selecionar o título

# Extrai o texto do titulo da pagina hashtag
titulo = navegador.find_element(By.TAG_NAME, 'h2').text
print(titulo)



#### Selecionar pelo Partial Link Text (ou LINK_TEXT)

# - Quero conseguir pegar o número de whatsapp de contato
# sendo assim iremos procurar em algum lugar o elemento cujo texto DE LINK possua o valor desejado (WhatsApp)

# Extrai o texto do elemento cujo texto DE LINK tenha em alguma das suas partes a palavra escolhida
numero_whatsapp = navegador.find_element(By.PARTIAL_LINK_TEXT, 'WhatsApp').text # o elemento procurado é case sensitive
print(numero_whatsapp)



# #### Selecionar pelo name
# - Preencher o formulário

navegador.find_element(By.NAME, 'email').send_keys("pythonimpressionador@gmail.com")




# #### Selecionar pelo CSS Selector
# - Parecido com o XPATH, acaba não usando tanto, mas caso queira, tem uma referência aqui:
# https://saucelabs.com/resources/articles/selenium-tips-css-selectors



time.sleep(5)