from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os, time


options=webdriver.ChromeOptions()

# chrome://version
options.add_argument(r'user-data-dir=C:\Users\Jorge\AppData\Local\Google\Chrome\User Data\Profile Selenium')


navegador=webdriver.Chrome(options=options)

navegador.get('https://web.whatsapp.com')

time.sleep(20)

import pandas as pd

tabela=pd.read_excel('Envios.ods',engine='odf')
print(tabela)

i=0
while len(navegador.find_elements(By.ID,'side'))<1:
    time.sleep(3)
    i+=1
    if i>30:
        break

time.sleep(2)

# o whatsapp ja carregou

import urllib

for linha in tabela.index:
    nome=tabela.loc[linha,'nome']
    mensagem=tabela.loc[linha,'mensagem']
    arquivo=tabela.loc[linha,'arquivo']
    telefone=tabela.loc[linha,'telefone']

    texto=mensagem.replace('fulano',nome) # alteramos o fulano da mensagem pelo nome da pessoa a ser enviado

    texto=urllib.parse.quote(texto) # aqui formatamos o texto a ser enviado para que ele tenha o formato de link e possa ser enviado como um link

    # enviar a mensagem
    link=f'https://web.whatsapp.com/send?phone={telefone}&text={texto}'

    navegador.get(link)

    # esperar a tela do whatsapp carregar: espera um elemento que so existe na tela ja carregada aparecer

    i=0
    while len(navegador.find_elements(By.ID,'side'))<1:
        time.sleep(3)
        i+=1
        if i>30:
            break

    time.sleep(2)

    # voce tem que verificar se o numero é invalido
    if len(navegador.find_elements(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]'))<1:
        # enviar a mensagem
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(3)

        if arquivo!='N':
            # salvando o caminho do arquivo a ser enviado
            caminhoArquivo = os.path.abspath(f'arquivos\\{arquivo}')
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
            time.sleep(1)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(caminhoArquivo)
            time.sleep(2)
            navegador.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()

    else:
        continue
    





time.sleep(20)