from selenium import webdriver
from selenium.webdriver.common.by import By

navegador=webdriver.Chrome()

# abrir a página index (entrar no site da busca jurídica)
import os
import time
import pandas as pd

tabela=pd.read_excel('Processos.xlsx')
print(tabela)

caminho = os.getcwd()
arquivo = caminho + r"\index.html"

navegador.get(arquivo)

xpathDf='/html/body/div/div/div/a[1]'
xpathRio='/html/body/div/div/div/a[2]'
xpathSp='/html/body/div/div/div/a[3]'
menu=navegador.find_element(By.XPATH,'/html/body/div/div/button')

from selenium.webdriver import ActionChains

for linha in tabela.index:
    if tabela.loc[linha,'Cidade']=='Distrito Federal':
        item=navegador.find_element(By.XPATH,xpathDf)
    elif tabela.loc[linha,'Cidade']=='Rio de Janeiro':
        item=navegador.find_element(By.XPATH,xpathRio)
    else:
        item=navegador.find_element(By.XPATH,xpathSp)
    ActionChains(navegador).move_to_element(menu).perform()
    time.sleep(0.5)
    item.click()
    time.sleep(0.5)
    navegador.get(arquivo)






time.sleep(5)