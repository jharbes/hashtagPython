from selenium import webdriver
from selenium.webdriver.common.by import By

navegador=webdriver.Chrome()



# na marra, colocando um time.sleep fixo
import time

navegador.get("https://www.hashtagtreinamentos.com/")
time.sleep(15)
navegador.find_element(By.CLASS_NAME, 'eicon-close').click()

time.sleep(2)




# loop
# fica tentando encontrar o elemento que possui aquela class name dentro do loop, quando a lista tiver pelo menos um elemento significa que o pop up apareceu e ele clica
navegador.get("https://www.hashtagtreinamentos.com/")

while len(navegador.find_elements(By.CLASS_NAME, 'eicon-close')) < 1:
    time.sleep(1)
time.sleep(1) # garantia

navegador.find_element(By.CLASS_NAME, 'eicon-close').click()



time.sleep(2)

# EC WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador.get("https://www.hashtagtreinamentos.com/")

# nesse caso ele vai esperar pelo aparecimento do elemento por até 20 segundos, quando aparecer ele vai seguir com o codigo
# a informacao passada do elemento sera uma tupla, por isso possui dois parenteses
elemento = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'eicon-close')))
time.sleep(1) # garantia

elemento.click()


time.sleep(5)