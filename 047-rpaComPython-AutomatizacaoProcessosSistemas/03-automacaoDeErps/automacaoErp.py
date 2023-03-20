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
import pandas as pd


pyautogui.PAUSE=0.2

pastaApp='C:\\Users\\Jorge\\Desktop\\hashtag\\hashtagPython\\047-rpaComPython-AutomatizacaoProcessosSistemas\\03-automacaoDeErps\\'

arquivoExcel='Produtos.xlsx'

# pasta onde ficarao as imagens pertinentes ao reconhecimento de tela do pyautogui
pastaImagensTrabalho='C:\\Users\\jharbes\\Documents\\GitHub\\hashtagPython\\047-rpaComPython-AutomatizacaoProcessosSistemas\\03-automacaoDeErps\\imagensApp\\'
pastaImagensCasa='C:\\Users\\Jorge\\Desktop\\hashtag\\hashtagPython\\047-rpaComPython-AutomatizacaoProcessosSistemas\\03-automacaoDeErps\\imagensApp\\'

pastaImagensAtual=pastaImagensCasa

pastaImagensProdutos='C:\\Users\\Jorge\\Desktop\\hashtag\hashtagPython\\047-rpaComPython-AutomatizacaoProcessosSistemas\\03-automacaoDeErps\\Imagens Produtos\\'

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
    texto=str(texto)
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl','v')


def escreverTextoComVirgula(texto):
    texto=str(texto)+',00'
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl','v')




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


tabelaProdutos=pd.read_excel(pastaApp+arquivoExcel)
print(tabelaProdutos)


for linha in tabelaProdutos.index:
    id=tabelaProdutos.loc[linha,'ID']
    nome=tabelaProdutos.loc[linha,'Nome']
    categoria=tabelaProdutos.loc[linha,'Categoria']
    gtin=tabelaProdutos.loc[linha,'GTIN']
    supplier=tabelaProdutos.loc[linha,'Supplier']
    descricao=tabelaProdutos.loc[linha,'Descrição']
    imagem=tabelaProdutos.loc[linha,'Imagem']
    preco=tabelaProdutos.loc[linha,'Preço']
    custo=tabelaProdutos.loc[linha,'Custo']
    estoque=tabelaProdutos.loc[linha,'Estoque']

    # clica no item New do Menu superior
    encontrou=encontrarImagem('newMenu.png')
    print(encontrou)
    clicarCentroImagem(encontrou)

    # clica na opcao New Product do item New do menu superior para abrir o formulario
    encontrou=encontrarImagem('newProduct.png')
    clicarCentroImagem(encontrou)

    # Preenchimento do formulario

    # Item number
    encontrou=encontrarImagem('newProduct-itemNumber.png')
    clicarDireitaImagem(encontrou)
    escreverTexto(id)

    # Name
    pyautogui.press('tab')
    escreverTexto(nome)

    # Category
    pyautogui.press('tab')
    escreverTexto(categoria)

    # GTIN
    pyautogui.press('tab')
    escreverTexto(gtin)

    # supplier code
    pyautogui.press('tab')
    escreverTexto(supplier)

    # Description
    pyautogui.press('tab')
    escreverTexto(descricao)

    # Price
    pyautogui.press('tab')
    escreverTextoComVirgula(preco)

    # Cost price
    pyautogui.press('tab')
    escreverTexto(str(custo).replace('.',',')+'0')

    # Stock
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    escreverTextoComVirgula(estoque)

    # Select a picture
    encontrou=encontrarImagem('selectPicture.png')
    clicarCentroImagem(encontrou)

    # Anexando a foto
    time.sleep(2)
    escreverTexto(pastaImagensProdutos+imagem)
    pyautogui.press('enter')

    # Salvando o produto
    encontrou=encontrarImagem('saveButton.png')
    clicarCentroImagem(encontrou)


print('\nSistema finalizado com sucesso')