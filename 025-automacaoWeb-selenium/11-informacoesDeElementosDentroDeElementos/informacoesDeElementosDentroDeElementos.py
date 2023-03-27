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

# Pegar todos os links das imagens:

# aqui pegamos todos os elementos que possuem a tag figure, que é o que envolve as imagens grandes do site
listaElementos=navegador.find_elements(By.TAG_NAME,'figure') # lista de figures
print(listaElementos)
print(len(listaElementos))


# buscaremos os links de cada imagem dentro da tag <a> que esta dentro da tag <figure>, atributo href
# usaremos o try para caso ele nao encontre algum link dentro de <figure> ele nao de erro e quebre o programa
for elemento in listaElementos:
    try: 
        link=elemento.find_element(By.TAG_NAME,'a').get_attribute('href')
        print(link)
    except:
        continue


# como alternativa ao try tambem podemos pegar uma lista com find_elements em vez de find_element, sendo assim depois percorremos a lista com um if impedindo de acessar os elementos vazios da lista


time.sleep(5)