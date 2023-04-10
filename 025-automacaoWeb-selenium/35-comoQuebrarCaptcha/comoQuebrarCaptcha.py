"""
COMO QUEBRAR CAPTCHA


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

chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(chaveApi)
solver.set_website_url(link)
solver.set_website_key(chave_captcha)

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print(resposta)
    # preencher o campo do token do captcha
    # g-recaptcha-response
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string)






time.sleep(30)