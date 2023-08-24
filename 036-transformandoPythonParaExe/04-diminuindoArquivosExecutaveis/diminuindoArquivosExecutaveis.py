"""

# Diminuindo o tamanho do executável final - Ambiente Virtual

### Objetivo

Para diminuir o tamanho do arquivo a ser distribuído no final, vamos criar um ambiente virtual para garantir que teremos apenas as bibliotecas importantes.

- Passo 1: Garantir que o código está funcionando
- Passo 2: Criar o ambiente virtual
- Passo 3: Executar o nosso código por dentro do ambiente virtual
- Passo 4: Identificar erros e instalar bibliotecas que faltam, apenas as que o programa pede.
- Passo 5: Instalar o pyinstaller e transformar em executável o programa Python

"""

# rodar o código de um programa que fazemos durante o curso que funcione. Exemplo o de envio de SMS

from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACe47cf7caf5d7f76d1c6f8a570230f5ee"
auth_token  = "b7bb60ef56cffcb7e9d28a2bd1fc1f9c"

remetente="+16205248958"
destino="+5521996481674"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=destino,
    from_=remetente,
    body="Hello from Python!")

print(message.sid)