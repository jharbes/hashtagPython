"""

### Executar Comandos Javascript (Scroll da tela)

- Você consegue, por meio do Selenium, executar comandos javascript no seu navegador

- Isso é essencial para dar scroll na tela, por exemplo, caso seja necessário, como no youtube

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os, time

options=webdriver.ChromeOptions()
# chrome://version
options.add_argument(r'user-data-dir=C:\Users\Jorge\AppData\Local\Google\Chrome\User Data\Profile Selenium')
navegador=webdriver.Chrome(options=options)


navegador.get("https://www.youtube.com/results?search_query=python")






time.sleep(7)