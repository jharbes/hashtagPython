from selenium import webdriver
from selenium.webdriver.common.by import By

navegador=webdriver.Chrome()

import os, time

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)


### Editando a tela do navegador

#### maximizar

navegador.maximize_window()




#### minimizar

# nao é clicar no minimizar e sim voltar ao tamanho normal no qual ele abriu
navegador.minimize_window()




#### headless

# Atenção que nem sempre funciona igual

options=webdriver.ChromeOptions()
options.add_argument('--headless')

"""
Argumentos extras que podem ser adicionados ao incializar um navegador:

Desabilitar extensoes:  --disable-extensions
Comecar maximizado:     --start-maximized
"""

novoNavegador=webdriver.Chrome(options=options)

novoNavegador.get('https://facebook.com')
print(novoNavegador.title)




time.sleep(5)