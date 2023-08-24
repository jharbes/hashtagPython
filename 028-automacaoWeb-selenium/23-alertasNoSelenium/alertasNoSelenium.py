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
alerta.accept() # cada vez que aceitamos um alerta ele deixa de ser a opcao, caso seja necessario interagir novamente com o alerta precisamos reposicionar o elemento Alert ou switch to alert

# forma "completa" de mudar para um alerta para interagir com ele
time.sleep(0.5)

from selenium.webdriver.common.alert import Alert

navegador.find_element(By.XPATH,'/html/body/div[1]/input').click()

time.sleep(0.5)

alerta=Alert(navegador)
time.sleep(1)
alerta.accept() # cada vez que aceitamos um alerta ele deixa de ser a opcao, caso seja necessario interagir novamente com o alerta precisamos reposicionar o elemento Alert ou switch to alert



time.sleep(2)
#### Alertas de Confirmação

navegador.find_element(By.XPATH,'/html/body/div[2]/input').click()

alerta=Alert(navegador)

time.sleep(1)
# aceitar
alerta.accept()



time.sleep(2)

navegador.find_element(By.XPATH,'/html/body/div[2]/input').click()

alerta=navegador.switch_to.alert

time.sleep(1)
# cancelar
alerta.dismiss()



time.sleep(2)
#### Pegar o texto do alerta

navegador.find_element(By.XPATH,'/html/body/div[2]/input').click()

alerta=Alert(navegador)
texto=alerta.text
print(texto)
alerta.dismiss()



time.sleep(3)


#### Alertas de Input

navegador.find_element(By.XPATH,'/html/body/div[3]/button').click()

alerta=Alert(navegador)


# preenchendo o alerta com input
# ***IMPORTANTE: os dados preenchidos nao irao aparecer (fica em branco) mas eles terao sido preenchidos
alerta.send_keys('12312312312')

time.sleep(1)

# se o accept nao for por meio do codigo o preenchimento nao funcionara
alerta.accept()





time.sleep(5)