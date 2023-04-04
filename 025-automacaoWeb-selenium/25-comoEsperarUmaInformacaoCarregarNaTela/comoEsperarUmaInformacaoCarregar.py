from selenium import webdriver
from selenium.webdriver.common.by import By

navegador=webdriver.Chrome()



# na marra, colocando um time.sleep fixo
import time

navegador.get("https://www.hashtagtreinamentos.com/")
time.sleep(5)
navegador.find_element(By.CLASS_NAME, 'eicon-close').click()







time.sleep(5)