from selenium import webdriver
from selenium.webdriver.common.by import By

navegador=webdriver.Chrome()

import os, time

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)


### Editando a tela do navegador

#### maximizar










time.sleep(5)