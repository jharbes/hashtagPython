"""
COMO QUEBRAR CAPTCHA

IMPORTANTE: Este exemplo está preenchido para o captcha do tipo recaptchav2proxyless, modificacoes serao necessarias para utilizacao com outros tipos de captchas, a lista de tipos de captcha está presente na documentacao do anticaptchaofficial
https://anti-captcha.com/apidoc

"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os, time

from anticaptchaofficial.recaptchav2proxyless import *
from chave import chaveApi # importando a chave do arquivo chave.py

navegador=webdriver.Chrome()

link = "https://google.com/recaptcha/api2/demo"
navegador.get(link)

chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey') # buscaremos o valor do atributo data-sitekey ao identificar primeiramente o elemento inteiro onde está o captcha, logo acima deste elemento deve haver uma tag iframe, imediatamente acima desse iframe have um elemento que possui esse atributo

solver = recaptchaV2Proxyless() # uma instancia da classe recaptchaV2Proxyless

solver.set_verbose(1) # parametro 0 ou 1, verbose = 1 imprime o status do servico, verbose = 0 nao imprime nada (dificulta o acompanhamento)

solver.set_key(chaveApi) 
solver.set_website_url(link)
solver.set_website_key(chave_captcha)

resposta = solver.solve_and_return_solution() # solicita a resolucao e a resposta na variavel resposta

if resposta != 0:
    print(resposta) # imprime o token do captcha

    # preencher o campo do token do captcha com javascript
    # g-recaptcha-response - campo onde entra a resposta do token
    # como o campo a ser preenchido está escondido (display: none;) nao podemos fazer um preenchimento padrao via selenium, por isso utilizaremos o metodo execute_script pelo qual faremos o preenchimento por meio de um codigo javascript conforme abaixo, exatamente como se estivessemos preenchendo por meio do console do browser. Outra opcao seria desabilitar o display none do elemento por meio de javascript e depois preencher a resposta por meio do selenium
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string) # vai imprimir a mensagem de erro






time.sleep(10)