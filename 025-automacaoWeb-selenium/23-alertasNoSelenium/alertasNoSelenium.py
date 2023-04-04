from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador=webdriver.Chrome()

import os
import time

caminho = os.getcwd()
arquivo = caminho + r"\alertas.html"
navegador.get(arquivo)


#### Alertas Básicos

