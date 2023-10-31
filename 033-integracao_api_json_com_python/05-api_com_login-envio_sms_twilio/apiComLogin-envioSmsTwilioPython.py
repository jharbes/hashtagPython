"""

Python e API com Login

O 1o passo de toda API com Login é criar uma conta e pegar suas credenciais

No seu código, o 1º passo é sempre estabelecer a conexão com a API, usando seu login e suas credenciais.

-- Como cada API é uma ferramenta diferente, cada uma delas pode exigir que voce faça algum tipo de configuração, que vai estar explicada na API. No nosso caso, teremos que validar um número e criar um número de envio.

-- Depois, usamos os métodos da API normalmente para fazer o que queremos. No nosso caso enviar um SMS.

"""

# 1- Vamos criar um login no Twilio

# https://www.twilio.com/docs/libraries/python


# 2- Depois do Login, vamos pegar 3 informações:

#   -- ID da conta
#   -- Token
#   -- Número de Envio


# 3- Agora vamos validar um número porque no Twilio, enviar SMS para um número válido é de graça.


# 4- Agora podemos fazer o nosso código de acordo com as orientações do Twilio

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