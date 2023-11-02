"""
# Python e API


### O que é uma API?

- É um conjunto de códigos para usar um serviço/site/aplicativo específico. Cada site/ferramenta tem sua própria API. É importante que você saiba ler as APIs que precisar para saber usar

- Um dos padrões mais comuns em API é pegar informações em formato json, uma espécie de dicionário que precisa ser tratada no Python para podermos analisar

- As possibilidades de API são infinitas, vamos fazer 2 exemplos aqui: Cotação de Moedas e Envio de SMS.

- Sites como Google, Youtube, Facebook, Twitter, ArcGis e praticamente qualquer ferramenta/site grande tem uma API.



### O que precisamos:

- Quase sempre você precisa de uma conta para consumir uma API. Algumas APIs são abertas, como a https://docs.awesomeapi.com.br/api-de-moedas , mas em muitos casos (como veremos no caso do SMS) vamos precisar ter uma conta ativa para consumir a API

- A Documentação da API (ou exemplos da internet) é a chave para conseguir usar uma API 

"""

#### Pegar a Cotação Atual de Todas as Moedas 

# request é a biblioteca para utilizar requisicoes http
import requests
import json

cotacoes=requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

# a resposta 200 significa que o retorno foi recebido ok, 404 seria moeda inexistente 
print(cotacoes) # <Response [200]>

# transforma o arquivo json em um dicionario python
cotacoes_dic=cotacoes.json()

print(cotacoes_dic) # {'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '4.9545', 'low': '4.9543', 'varBid': '0.0009', 'pctChange': '0.02', 'bid': '4.9539', 'ask': '4.9548', 'timestamp': '1698872400', 'create_date': '2023-11-01 18:00:00'}, 'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '5.3119', 'low': '5.2478', 'varBid': '0.0107', 'pctChange': '0.2', 'bid': '5.2598', 'ask': '5.2678', 'timestamp': '1698939025', 'create_date': '2023-11-02 12:30:25'}, 'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '178935', 'low': '172851', 'varBid': '622', 'pctChange': '0.36', 'bid': '173293', 'ask': '173378', 'timestamp': '1698939042', 'create_date': '2023-11-02 12:30:42'}}

type(cotacoes_dic) # dict