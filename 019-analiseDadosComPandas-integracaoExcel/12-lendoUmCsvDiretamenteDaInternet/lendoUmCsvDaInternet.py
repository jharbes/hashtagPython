"""

# pandas lendo csv da internet

### Essa é uma das formas de importar arquivos da internet, direto do pandas. Mas nem sempre você vai conseguir abrir assim direto.

### 2 situações principais em que você consegue fazer direto

1. Arquivo csv direto no link (melhor dos mundos)

2. O arquivo csv é gerado para você, mas fica no meio de uma requisição que precisa ser tratada.

"""

### Caso 1: csv direto no link

# - Criei um arquivo csv e disponibilizei o link para download no Drive: https://drive.google.com/uc?authuser=0&id=1Ru7s-x3YJuStZK1mqr_qNqiHVvdHUN66&export=download

import pandas as pd

url='https://drive.google.com/uc?authuser=0&id=1Ru7s-x3YJuStZK1mqr_qNqiHVvdHUN66&export=download'

cotacaoDf=pd.read_csv(url)
print(cotacaoDf)




### Caso 2: csv em uma requisição que precisa ser tratada

# Pesquisei por histórico de preços do café no Google e cheguei nesse site: http://portalweb.cooxupe.com.br:8080/portal/precohistoricocafe_2.jsp

### Apenas para lembrar os tipos de encoding principais que vamos usar:

# - encoding='latin1'
# - encoding='ISO-8859-1'
# - encoding='utf-8'
# - encoding='cp1252'

import pandas as pd
import requests
import io

url='http://portalweb.cooxupe.com.br:8080/portal/precohistoricocafe_2.jsp'

# iremos utilizar a biblioteca requests que ajuda a puxar o conteudo de um link
conteudoUrl=requests.get(url).content

print(conteudoUrl) # observe que a formatacao ainda nao esta amigavel para utilizacao  

arquivo=io.StringIO(conteudoUrl.decode('latin1')) # usaremos a biblioteca io para acerto de formatacao das informacoes recebidas 


cafeDf=pd.read_html(arquivo) # na nova versao o arquivo esta em html, por isso fazemos uma leitura nesse sentido
print(cafeDf)