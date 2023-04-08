from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options=webdriver.ChromeOptions()

# chrome://version
options.add_argument(r'user-data-dir=C:\Users\Jorge\AppData\Local\Google\Chrome\User Data\Profile Selenium')


navegador=webdriver.Chrome(options=options)

navegador.get('https://web.whatsapp.com')

import os, time
import pandas as pd

tabela=pd.read_excel('Envios.xlsx')
print(tabela)

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

    # esperar a tela do whatsapp carregar
    







time.sleep(20)