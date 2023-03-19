# pip install --upgrade selenium

# baixar o webdriver do navegador correspondente (inclusive mesma versao) e instalar seu executavel no diretorio onde está o python.exe da maquina

"""

Caso o arquivo do webdriver nao seja reconhecido pode se fazer o seguinte procedimento:

servico=Service(r'c:\users\xyz\chromedriver.exe') # path onde está o chromedriver

driver=webdriver.Chrome(service=servico)

"""

from selenium import webdriver
import time

navegador=webdriver.Chrome()
time.sleep(5)