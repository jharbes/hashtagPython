from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador=webdriver.Chrome()

import os
import time

caminho = os.getcwd()
arquivo = caminho + r"\alertas.html"
navegador.get(arquivo)

"""

Alertas são diferentes de POP Ups, os alertas não possuem elementos pois não fazem parte do site e sim do navegador, os POP Ups possuem elementos pois não fazem parte do navegador e sim do site

"""

#### Alertas Básicos

# selecionar um alerta
navegador.find_element(By.XPATH,'/html/body/div[1]/input').click()

time.sleep(0.5)
# forma simples de mudar para um alerta para interagir com ele
alerta=navegador.switch_to.alert
alerta.accept()

# forma "completa" de mudar para um alerta para interagir com ele
time.sleep(0.5)

from selenium.webdriver.common.alert import Alert

navegador.find_element(By.XPATH,'/html/body/div[1]/input').click()

time.sleep(0.5)

alerta=Alert(navegador)
alerta.accept()




#### Alertas de Confirmação






time.sleep(5)