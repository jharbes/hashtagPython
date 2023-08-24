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
valor0=navegador.find_element(By.XPATH,'/html/body/form/input[4]').get_attribute('value')
print(valor0) # #000000

valor = navegador.find_element(By.XPATH, '/html/body/form/input[5]').get_attribute("value")
print(valor) # #000000


# preencher a cor
navegador.find_element(By.XPATH, '/html/body/form/input[4]').send_keys('#243DBC')

navegador.find_element(By.XPATH, '/html/body/form/input[5]').send_keys('#D11515')




#### Botão de Datas (enviar valor)

# preencher o valor, a maneira de preencher vai depender do formulario em questao, pode variar
navegador.find_element(By.XPATH, '/html/body/form/input[6]').send_keys('21/06/1983')


# pegar o valor, o valor armazenado, nesse caso é no formato universal de data com o ano/mes/dia, mas isso pode variar de site pra site
valor = navegador.find_element(By.XPATH, '/html/body/form/input[6]').get_attribute("value")
print(valor) # 1983-06-21




#### Botão de Datas com Horas (enviar valor)

# preenchendo
from selenium.webdriver.common.keys import Keys

# pra trocar de campo (data pra hora) e continuar o preenchimento precisamos usar a tecla tab, sendo assim usaremos o argumento Keys.TAB no metodo send_keys
navegador.find_element(By.XPATH, '/html/body/form/input[7]').send_keys('21/06/1983', Keys.TAB, '06:50')


# pegando o valor, nesse caso retorna o formato date time 1983-06-21T06:50
valor = navegador.find_element(By.XPATH, '/html/body/form/input[7]').get_attribute("value")
print(valor) # 1983-06-21T06:50




#### Botão para selecionar o arquivo (enviar valor com caminho completo)

# preenchendo

caminho = os.getcwd() # current working directory
arquivo = caminho + r"\formulario.html"

navegador.find_element(By.XPATH, '/html/body/form/input[8]').send_keys(arquivo)


# pegar o valor, se nao houver nenhum arquivo selecionado tera o retorno vazio
valor = navegador.find_element(By.XPATH, '/html/body/form/input[8]').get_attribute("value")
print(valor)




#### Botão para selecionar mês e ano (enviar valor)

# preenche
navegador.find_element(By.XPATH, '/html/body/form/input[9]').send_keys('junho', Keys.TAB, '1983')


# pegar o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[9]').get_attribute('value')
print(valor) # 1983-06




#### Campos Numéricos

# para apagar tudo que houver preenchido no campo, garantir que nao vai preencher por cima, serve pra qualquer campo
navegador.find_element(By.XPATH, '/html/body/form/input[10]').clear()

# preenchendo o campo numerico(aceita so numeros)
navegador.find_element(By.XPATH, '/html/body/form/input[10]').send_keys("123456")




#### Campos de Senha

# preencher
navegador.find_element(By.XPATH, '/html/body/form/input[11]').send_keys("123456")

# pegar o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[11]').get_attribute('value')
print(valor)




#### RadioButtons (botões que só consegue marcar 1)

# marcar, cada um dos botoes possui um xpath proprio
navegador.find_element(By.XPATH, '/html/body/form/input[14]').click()

# saber se está marcado
valor = navegador.find_element(By.XPATH, '/html/body/form/input[12]').is_selected()
print(valor)

valor = navegador.find_element(By.XPATH, '/html/body/form/input[13]').is_selected()
print(valor)

valor = navegador.find_element(By.XPATH, '/html/body/form/input[14]').is_selected()
print(valor)




#### Slider (enviar valor)

# pegar o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[15]').get_attribute('value')
print(valor)


# preencher o valor
elemento = navegador.find_element(By.XPATH, '/html/body/form/input[15]')

elemento.clear() # seta o slider em 50 (o padrao depende do site, nem sempre é 50)

# coloca o slider em 30: 50-30=20 Arrow left (cada vez que aperta seta pra esquerda ele anda um pra esquerda, ou seja, 20 vezes pra esquerda chega no 30)
for i in range(50 - 30):
    elemento.send_keys(Keys.ARROW_LEFT)


valor = navegador.find_element(By.XPATH, '/html/body/form/input[15]').get_attribute('value')
print(valor)




#### Caixa de Texto


# preencher
navegador.find_element(By.XPATH, '/html/body/form/input[16]').send_keys("Vasco")

# capturar valor preenchido
# embora o elemento em si de input normalmente nao possua esse atributo "value", ele retorna o valor com o valor preenchido do campo input, isso é valido para todo tipo de input
valor = navegador.find_element(By.XPATH, '/html/body/form/input[16]').get_attribute("value")
print(valor)




#### Caixa de Horas

# navegador.find_element(By.XPATH, '/html/body/form/input[17]').send_keys('15:15')

# ou

navegador.find_element(By.XPATH, '/html/body/form/input[17]').send_keys('1515')




#### Caixa de Data Personalizada (Semanal)

# navegador.find_element(By.XPATH, '/html/body/form/input[18]').send_keys('17', '2005')

# ou

navegador.find_element(By.XPATH, '/html/body/form/input[18]').send_keys('172005')




#### Blocos de texto (enviar valor)

# limpa o campo (garante que nao haja texto indesejado ja preenchido)
navegador.find_element(By.XPATH, '//*[@id="story"]').clear()

# preenchendo o campo de texto, com utilizacao de enter para mudar de linha
navegador.find_element(By.XPATH, '//*[@id="story"]').send_keys("Olá", Keys.ENTER, 'Meu nome é Lira', Keys.ENTER, 'Valeu, Tmj')

# pegando o valor preenchido
valor=navegador.find_element(By.XPATH, '//*[@id="story"]').get_attribute('value')
print(valor)




time.sleep(5)