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

import time
import pyautogui
import subprocess # utilizado para rodar um processo no computador, usaremos para abrir o ERP


# 1- Abrir o ERP (Fakturama)
# subprocess.Popen([r"C:\Program Files\Fakturama2\Fakturama.exe"]) # acertar o diretorio

# grayscale=True - ignora as cores para a comparacao
# confidence=0.9 - aceita ate 90% de semelhanca entre as imagens
# reconhecimento de imagem, passamos os argumentos grayscale e confidence para que ele aceita imperfeicoes na comparacao entre imagens porque elas nunca serao 100% iguais mesmo que feitas na mesma tela 
# Enquanto ele nao reconhece a imagem selecionado ele fica esperando pra seguir com o codigo
while not pyautogui.locateOnScreen(r'C:\Users\jharbes\Documents\GitHub\hashtagPython\047-rpaComPython-AutomatizacaoProcessosSistemas\03-automacaoDeErps\testeDeLocateOnScreen.png', grayscale=True, confidence=0.9):
    time.sleep(1)

encontrou=pyautogui.locateOnScreen(r'C:\Users\jharbes\Documents\GitHub\hashtagPython\047-rpaComPython-AutomatizacaoProcessosSistemas\03-automacaoDeErps\testeDeLocateOnScreen.png', grayscale=True, confidence=0.9)
print(encontrou)