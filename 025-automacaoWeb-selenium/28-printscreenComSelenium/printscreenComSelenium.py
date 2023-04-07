from selenium import webdriver
from selenium.webdriver.common.by import By

navegador=webdriver.Chrome()

import os

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)


### Tirando print da tela inteira

