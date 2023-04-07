from selenium import webdriver
from selenium.webdriver.common.by import By

navegador=webdriver.Chrome()

import os

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)


### Tirando print da tela inteira

navegador.save_screenshot('print-telaInteira.png')




### Tirando print de parte da tela

from PIL import Image

imagem=Image.open('print-telaInteira.png')

elemento=navegador.find_element(By.ID,'header')
posicao=elemento.location
tamanho=elemento.size
print(posicao)
print(tamanho)

xInicial=posicao['x']
yInicial=posicao['y']

xFinal=posicao['x']+tamanho['width']
yFinal=posicao['y']+tamanho['height']

imagem=imagem.crop((xInicial,yInicial,xFinal,yFinal))
imagem.save('print-pedacoTela.png')