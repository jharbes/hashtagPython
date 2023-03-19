from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# navegador.get(r'C:\Users\Jorge\Desktop\hashtag\hashtagPython\025-automacaoWeb-selenium\03-acessarPaginaComSelenium\teste.html')

navegador.get(r'C:\Users\Jorge\Desktop\hashtag\hashtagPython\025-automacaoWeb-selenium\03-acessarPaginaComSelenium\Pagina Hashtag.html')

time.sleep(5)