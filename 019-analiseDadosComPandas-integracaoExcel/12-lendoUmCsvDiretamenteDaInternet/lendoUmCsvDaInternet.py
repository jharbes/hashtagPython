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