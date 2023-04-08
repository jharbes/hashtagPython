"""

### iFrames - Atualização

- Às vezes, você vai fazer tudo certo no Selenium e aparentemente não vai funcionar o seu código

- Possivelmente o elemento que você está tentando selecionar está dentro de um iframe

"""

# Queremos pegar o pontos por jogo mandante da 1ª linha da tabela

link = "https://pbdatatrader.com.br/jogosdodia"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os, time

options=webdriver.ChromeOptions()
# chrome://version
options.add_argument(r'user-data-dir=C:\Users\Jorge\AppData\Local\Google\Chrome\User Data\Profile Selenium')
navegador=webdriver.Chrome(options=options)


navegador.get(link) # entrando no site