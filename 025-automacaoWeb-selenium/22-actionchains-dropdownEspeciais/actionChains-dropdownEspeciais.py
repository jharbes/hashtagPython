from selenium import webdriver
import time

navegador=webdriver.Chrome()

import os
import time

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)



#### Dropdown diferente em um site real

