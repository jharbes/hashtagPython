# SELECIONANDO ELEMENTOS DA PAGINA COM SELENIUM

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

import os
import time

caminho=os.getcwd()
print(os.getcwd())
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)


"""
MANEIRAS DE SELECIONAR NO SELENIUM:

id
xpath
class_name
text (texto que está no corpo)
tipo de informacao

Preferencia de uso:
id
"""

# Duas maneiras de selecionar um elemento no selenium:

navegador.find_element # retorna um unico elemento (nao lista)

navegador.find_elements # retorna uma lista (lista python) com varios itens, se so houver um retornara uma lista com apenas um elemento


# necessario importar esse elemento para selecionar elementos no selenium, o By é o elemento que escolhe a maneira como serao selecionados os elementos
from selenium.webdriver.common.by import By

campoNome=navegador.find_element(By.ID,'fullname')
campoNome.send_keys('Jorge')

campoEmail=navegador.find_element(By.ID,'email')
campoEmail.send_keys('jharbes@hotmail.com')

botaoEnviar=navegador.find_element(By.ID,'_form_176_submit')
botaoEnviar.click()


time.sleep(5)
