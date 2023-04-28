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


"""
### Atenção no resultado

Repare que o programa final vai ficar extremamente pesado.

Isso porque o pyinstaller vai incluir todas as bibliotecas que temos instaladas no programa final, para garantir que ele vai funcionar.

Para evitar isso, precisaremos criar um ambiente virtual exclusivo para esse programa, vamos ver na prática como funciona na próxima aula


### Observações Úteis

- Se o nome do seu arquivo .py tiver mais de uma palavra, na hora de testar, coloque o nome dele entre aspas duplas.<br>Ex:  python "Gabarito - SMS.py"
- Se o seu antivírus verificar o pyinstaller, não precisa se preocupar, é normal e tá tudo certo
- Provavelmente a 1ª vez que você rodar o seu programa, o antivírus vai verificar ele também
- A pasta dist é o que pode ser distribuído. Você pode compactar ela em um zip e mandar para quem você quiser

"""