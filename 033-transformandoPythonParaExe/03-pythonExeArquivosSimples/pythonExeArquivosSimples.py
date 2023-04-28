"""

# Python para exe com códigos simples

### Códigos que não interagem com outros arquivos ou ferramentas do computador

Usaremos a biblioteca pyinstaller

- Passo 1 - Instalar o pyinstaller

- Passo 2 - Executar o pyinstaller

pyinstaller -w nome_do_programa.py

"""

# rodar o código de um programa que fazemos durante o curso que funcione. Exemplo o do outlook de enviar email
from twilio.rest import Client

account_sid = 'AC274236461c28f62d429961289af45b82'
token = '6a2d1ea365d3674c749ce4cb7367d823'

client = Client(account_sid, token)

remetente = '+18126153399'
destino = '+5521972795556'

message = client.messages.create(
    to=destino, 
    from_=remetente,
    body="Coe, é o Lira aqui!")

print(message.sid)