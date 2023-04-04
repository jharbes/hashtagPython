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



"""
### ActionChains

# action chains simula acoes com o mouse sem efetivamente usar o mouse, isso significa que o computador nao precisa estar dedicado a isso para que seja efetivamente efetuada a operacao

# diversas outras funcionalidades do ActionChains estao disponiveis, sejam elas clicar e arrastar, duplo clique, clicar e largar etc

# Link com a referência: https://www.selenium.dev/pt-br/documentation/webdriver/actions_api/mouse/

"""

from selenium.webdriver import ActionChains

menu=navegador.find_element(By.XPATH,'//*[@id="menu-item-dropdown-16313"]')
item=navegador.find_element(By.XPATH,'//*[@id="menu-item-17042"]/a')

# primeiro colocamos o mouse no menu

ActionChains(navegador).move_to_element(menu).perform() # no action chains a acao de hover tem o nome de move_to_element e as acoes so serao finalizadas com o .perform() no final

time.sleep(0.5) # o drop down pode levar algum tempo para ocorrer dependendo do site
#  para depois clicar no item

item.click()



time.sleep(5)