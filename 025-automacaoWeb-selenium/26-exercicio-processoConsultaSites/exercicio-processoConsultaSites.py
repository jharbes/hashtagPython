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
    time.sleep(2)
    item.click()
    time.sleep(2)
    listaAbas=navegador.window_handles

    abaOriginal=navegador.window_handles[0]
    novaAba=navegador.window_handles[1]
    navegador.switch_to.window(novaAba)

    try:
        navegador.find_element(By.ID,'nome').send_keys(tabela.loc[linha,'Nome'])
        navegador.find_element(By.ID,'advogado').send_keys(tabela.loc[linha,'Advogado'])
        navegador.find_element(By.ID,'numero').send_keys(tabela.loc[linha,'Processo'])
        navegador.find_element(By.XPATH,'//*[@id="formulario"]/div/button').click()
    except:
        print('Elemento inexistente na aba/pagina atual')
    time.sleep(0.5)
    alerta=navegador.switch_to.alert
    alerta.accept()
    time.sleep(3)
    i=0
    while i<30:
        try:
            alerta=navegador.switch_to.alert
            alerta.accept()
            break
        except:
            time.sleep(2)
            i+=1
    navegador.close()
    navegador.switch_to.window(abaOriginal)







time.sleep(5)