from selenium import webdriver
import time
import pyautogui
import pyperclip

navegador=webdriver.Chrome()

# options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs", {
#   "download.default_directory": r"C:\Users\jharbes\downloads",
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
# })

import os
import time
from selenium.webdriver.common.by import By
import pandas as pd


# entrar na página de login (no nosso caso é login.html)
caminho = os.getcwd()
arquivo = caminho + r"\login.html"
navegador.get(arquivo)



def escreverTexto(texto):
    texto=str(texto)
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl','v')

time.sleep(2)


# fazendo login na pagina
navegador.find_element(By.XPATH,'/html/body/div/form/input[1]').send_keys('jharbes')
navegador.find_element(By.XPATH,'/html/body/div/form/input[2]').send_keys('123456')
navegador.find_element(By.XPATH,'/html/body/div/form/button').click()

time.sleep(3)


# importando base de dados
tabela=pd.read_excel('NotasEmitir.xlsx')



# para cada cliente - rodar o processo de emissao de nota fiscal
for linha in range(len(tabela)):
    # preenchendo os dados para cada cliente

    # nome/razao social
    navegador.find_element(By.NAME,'nome').clear()
    navegador.find_element(By.NAME,'nome').send_keys(tabela['Cliente'][linha])
    time.sleep(0.2)

    # endereco
    navegador.find_element(By.NAME,'endereco').clear()
    navegador.find_element(By.NAME,'endereco').send_keys(tabela['Endereço'][linha])
    time.sleep(0.2)

    # bairro
    navegador.find_element(By.NAME,'bairro').clear()
    navegador.find_element(By.NAME,'bairro').send_keys(tabela['Bairro'][linha])
    time.sleep(0.2)

    # municipio
    navegador.find_element(By.NAME,'municipio').clear()
    navegador.find_element(By.NAME,'municipio').send_keys(tabela['Municipio'][linha])
    time.sleep(0.2)
    
    # cep
    navegador.find_element(By.NAME,'cep').clear()
    navegador.find_element(By.NAME,'cep').send_keys(str(tabela['CEP'][linha]))
    time.sleep(0.2)

    # uf
    navegador.find_element(By.NAME,'uf').send_keys(tabela['UF'][linha])
    time.sleep(0.2)

    # cnpj/cpf
    navegador.find_element(By.NAME,'cnpj').clear()
    navegador.find_element(By.NAME,'cnpj').send_keys(str(tabela['CPF/CNPJ'][linha]))
    time.sleep(0.2)

    # Inscricao estadual
    navegador.find_element(By.NAME,'inscricao').clear()
    navegador.find_element(By.NAME,'inscricao').send_keys(str(tabela['Inscricao Estadual'][linha]))
    time.sleep(0.2)

    # Descricao
    navegador.find_element(By.NAME,'descricao').clear()
    navegador.find_element(By.NAME,'descricao').send_keys(str(tabela['Descrição'][linha]))
    time.sleep(0.2)

    # Quantidade   
    navegador.find_element(By.NAME,'quantidade').clear()
    navegador.find_element(By.NAME,'quantidade').send_keys(str(tabela['Quantidade'][linha]))
    time.sleep(0.2)

    # Valor Unitario
    navegador.find_element(By.NAME,'valor_unitario').clear()
    navegador.find_element(By.NAME,'valor_unitario').send_keys(str(tabela['Valor Unitario'][linha]))
    time.sleep(0.2)

    # Valor total
    navegador.find_element(By.NAME,'total').clear()
    navegador.find_element(By.NAME,'total').send_keys(str(tabela['Valor Total'][linha]))
    time.sleep(0.2)

    # clicar no botao 'emitir nota'
    navegador.find_element(By.XPATH,'//*[@id="formulario"]/button').click()
    time.sleep(0.2)

    # escreverTexto(f'notaNumero{linha+1}')
    # time.sleep(0.5)
    # pyautogui.press('tab')
    # time.sleep(0.5)
    # pyautogui.press('tab')
    # time.sleep(0.5)
    # pyautogui.press('tab')
    # time.sleep(0.5)
    # pyautogui.press('enter')
    # time.sleep(0.5)




print(len(tabela))
print(tabela[0:1])
print(tabela[0:1]['Cliente'])






time.sleep(10)