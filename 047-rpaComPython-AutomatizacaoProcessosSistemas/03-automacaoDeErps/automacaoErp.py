"""
Existem duas maneiras de automatizar a integração com ERPs:

1a- Banco de dados (geralmente python com SQL, acesso improvavel de ser conseguido)

2a- Automacao via desktop (simular um usuario usando o PC para automatizar o processo, geralmente com selenium e/ou pyautogui)

ERP -> Sistema de gerenciamento da empresa, a maioria nao eh via web, nao acessivel por selenium (Totvs, SAP)


Nesse projeto utilizaremos reconhecimentos de imagens, para isso precisaremos das bibliotecas pyautogui, Pillow e opencv-python
"""

# fakturama -> link na descrição -> ERP de exemplo que vamos usar
# pyautogui -> é a ferramenta que a gente vai usar pra automatizar ERP 

"""
Passo a passo do processo:

1- Abrir o ERP (Fakturama)

2- Clicar no menu new

3- Clicar em new product

4- Preencher todos os campos

5- Selecionar a imagem

6- Clicar em salvar
"""

import sys
import time
import pyautogui
import subprocess # utilizado para rodar um processo no computador, usaremos para abrir o ERP
import pyperclip

# pasta onde ficarao as imagens pertinentes ao reconhecimento de tela do pyautogui
pastaImagensTrabalho='C:\\Users\\jharbes\\Documents\\GitHub\\hashtagPython\\047-rpaComPython-AutomatizacaoProcessosSistemas\\03-automacaoDeErps\\imagensApp\\'
pastaImagensCasa='C:\\Users\\Jorge\\Desktop\\hashtag\\hashtagPython\\047-rpaComPython-AutomatizacaoProcessosSistemas\\03-automacaoDeErps\\imagensApp\\'

pastaImagensAtual=pastaImagensCasa

pyautogui.FAILSAFE=True # caso o codigo falhe ou entre em loop infinito basta colocar o mouse em uma das extremidades da tela para que ele seja pausado

def encontrarImagem(imagem):
    temporizador=0
    while not pyautogui.locateOnScreen(pastaImagensAtual+imagem, grayscale=True, confidence=0.9) and temporizador<=29:
        time.sleep(1)    
        temporizador+=1
    if temporizador<=10:
        return pyautogui.locateOnScreen(pastaImagensAtual+imagem, grayscale=True, confidence=0.9)
    else:
        sys.exit(f'Tempo maximo de {temporizador} segundos ultrapassado, sistema sendo finalizado.')


def clicarCentroImagem(localizacao):
    pyautogui.click(pyautogui.center(localizacao))
    print(f'imagem {localizacao} clicada')


def clicarDireitaImagem(localizacao):
    # localizacao(Box) = (x, y, largura, altura) funciona com os indices (iteravel)
    pyautogui.click(localizacao[0]+localizacao[2],localizacao[1]+localizacao[3]/2)
    print(f'imagem {localizacao} clicada')


def escreverTexto(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl','v')



time.sleep(3)
#1- Abrir o ERP (Fakturama)
subprocess.Popen([r"C:\Program Files\Fakturama2\Fakturama.exe"])
"""

grayscale=True - ignora as cores para a comparacao

confidence=0.9 - aceita ate 90% de semelhanca entre as imagens

reconhecimento de imagem, passamos os argumentos grayscale e confidence para que ele aceita imperfeicoes na comparacao entre imagens porque elas nunca serao 100% iguais mesmo que feitas na mesma tela 

Enquanto ele nao reconhece a imagem selecionado ele fica esperando pra seguir com o codigo

encontrou=pyautogui.locateOnScreen('C:\\Users\\jharbes\\Documents\\GitHub\hashtagPython\\047-rpaComPython-AutomatizacaoProcessosSistemas\\03-automacaoDeErps\\imagensApp\\testeDeLocateOnScreen.png', grayscale=True, confidence=0.9)
print(encontrou)
 
"""


encontrou=encontrarImagem('fakturamaImagemLogin.png')

print(encontrou)
encontrou=encontrarImagem('newMenu.png')

print(encontrou)
clicarCentroImagem(encontrou)

encontrou=encontrarImagem('newProduct.png')
clicarCentroImagem(encontrou)

# Preenchimento do formulario

# Item number
encontrou=encontrarImagem('newProduct-itemNumber.png')
clicarDireitaImagem(encontrou)
escreverTexto('2')

# Name
pyautogui.press('tab')
escreverTexto('Computador')

# Category
pyautogui.press('tab')
escreverTexto('Acessórios')

# GTIN
pyautogui.press('tab')
escreverTexto('12345689')

# supplier code
pyautogui.press('tab')
escreverTexto('127')

# Description
pyautogui.press('tab')
escreverTexto('Computador novo do Lira')

# Price
pyautogui.press('tab')
escreverTexto('100,00')

# Cost price
pyautogui.press('tab')
escreverTexto('50,00')

# Stock
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
escreverTexto('5,00')

print('\nSistema finalizado com sucesso')