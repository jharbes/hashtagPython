# pip install --upgrade selenium

# baixar o webdriver do navegador correspondente (inclusive mesma versao) e instalar seu executavel no diretorio onde está o python.exe da maquina

"""

Caso o arquivo do webdriver nao seja reconhecido pode se fazer o seguinte procedimento:

servico=Service(r'c:\users\xyz\chromedriver.exe') # path onde está o chromedriver, lembre-se que no linux ou mac o arquivo do chromedriver nao possui exe no final 

driver=webdriver.Chrome(service=servico)

"""

from selenium import webdriver
import time

navegador=webdriver.Chrome()
time.sleep(5)


"""

#### Alternativa

- Uma alternativa que surgiu recentemente é usar o webdriver-manager, uma outra biblioteca que faz o gerenciamento do seu chromedriver para você. Nesse caso, precisamos primeiro instalar o webdriver-manager

```
pip install webdriver-manager
```

- Em seguida, importamos o ChromeDriverManager e usamos ele no Serviço do nosso Selenium, assim:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


"""

