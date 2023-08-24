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
time.sleep(10)

i=0
while len(navegador.find_elements(By.TAG_NAME,'iframe'))<1:
    time.sleep(3)
    i+=1
    if i>30:
        break

# devemos usar duas vezes para entrar no primeiro iframe e depois entrar no segundo iframe que está dentro do primeiro iframe
iframe = navegador.find_element(By.TAG_NAME, 'iframe')
navegador.switch_to.frame(iframe)
iframe = navegador.find_element(By.TAG_NAME, 'iframe')
navegador.switch_to.frame(iframe)

valor_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div[1]/div[4]/div/div[1]/div[8]'
texto = navegador.find_element(By.XPATH, valor_xpath).text
print(texto)









time.sleep(7)