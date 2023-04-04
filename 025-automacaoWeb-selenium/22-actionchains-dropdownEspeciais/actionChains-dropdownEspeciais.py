from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador=webdriver.Chrome()

import os
import time

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)



#### Dropdown diferente em um site real


# faremos um caminho alternativo ao mero clique no link, faremos a captura do link por meio do get atribute e depois utilizaremos no comando navegador.get(linkSql)

linkSql=navegador.find_element(By.XPATH,'//*[@id="menu-item-17042"]/a').get_attribute('href')
print(linkSql)

navegador.get(linkSql)


time.sleep(5)