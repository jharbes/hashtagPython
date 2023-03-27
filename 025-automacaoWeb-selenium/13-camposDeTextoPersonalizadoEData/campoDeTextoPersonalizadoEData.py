from selenium import webdriver
import time

navegador=webdriver.Chrome()

import os
import time

caminho = os.getcwd()
arquivo = caminho + r"\formulario.html"
navegador.get(arquivo)

"""
MANEIRAS DE SELECIONAR NO SELENIUM:

id                      .ID
xpath                   .XPATH
class_name              .CLASS_NAME
texto inteiro de link   .LINK_TEXT
pedaço de texto de link .PARTIAL_LINK_TEXT
name                    .NAME
tag name                .TAG_NAME
css selector            .CSS_SELECTOR

Preferencia de uso:
id
class
xpath
"""


from selenium.webdriver.common.by import By


# #### Botão Padrão (clicar em botão)


# clica no botao "Clique em mim"
navegador.find_element(By.XPATH, '/html/body/form/input[1]').click()


# interage com o pop up de resposta
alerta = navegador.switch_to.alert # faz com que o navegador altere seu comando para o alerta e nao para o navegador em si

time.sleep(2) # apenas para dar tempo de ver o alerta abrindo se sendo fechado

alerta.accept() # aceita a resposta do pop up, para recursar seria alerta.dismiss()

time.sleep(2)


"""
#### Dica, esteja atento ao atributo "value" dos inputs, ele pode te ajudar

- .text
- .get_attribute("value")
- .is_selected
"""

#### Botão de Seleção estilo Checkbox (clicar no botão)

# clicar no botão
# observe o primeiro botao do checkbox sendo marcado
navegador.find_element(By.XPATH, '/html/body/form/input[2]').click() 


# verificar o valor do botão
# retorna um booleano dizendo se o botao esta selecionado ou nao (True ou False)
valor = navegador.find_element(By.XPATH, '/html/body/form/input[2]').is_selected()
print(valor) 




#### Botão de Seleção de Cores (enviar valor)

# verificar qual a cor está selecionada
valor0=navegador.find_element(By.XPATH,'/html/body/form/input[4]').get_attribute

valor = navegador.find_element(By.XPATH, '/html/body/form/input[5]').get_attribute("value")
print(valor)


# preencher a cor
navegador.find_element(By.XPATH, '/html/body/form/input[4]').send_keys('#243DBC')

navegador.find_element(By.XPATH, '/html/body/form/input[5]').send_keys('#D11515')




#### Botão de Datas (enviar valor)








#### Caixa de Texto


# preencher
navegador.find_element(By.XPATH, '/html/body/form/input[16]').send_keys("Vasco")

# capturar valor preenchido
# embora o elemento em si de input normalmente nao possua esse atributo "value", ele retorna o valor com o valor preenchido do campo input, isso é valido para todo tipo de input
valor = navegador.find_element(By.XPATH, '/html/body/form/input[16]').get_attribute("value")
print(valor)


time.sleep(5)