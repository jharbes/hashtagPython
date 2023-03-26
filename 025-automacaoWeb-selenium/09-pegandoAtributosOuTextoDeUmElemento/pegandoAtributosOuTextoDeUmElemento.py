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

# #### Pegar informações de um elemento

# - texto
# - atributos

# 
##### Ex1: Link do Whatsapp
# pega o atributo href do elemento, que é o link no caso
href = navegador.find_element(By.XPATH, '/html/body/footer/div/div[1]/div[2]/div/a[2]').get_attribute('href')
print(href)



##### Ex2: Imagens dos cursos

linkImagem=navegador.find_element(By.XPATH, '/html/body/section[2]/div/div[4]/figure/a/img').get_attribute('src')
print(linkImagem)

# o link nao esta no elemento em questao mas sim no elemento pai
link = navegador.find_element(By.XPATH, '/html/body/section[2]/div/div[4]/figure/a').get_attribute('href')
print(link)


time.sleep(5)