"""

# Python para exe com códigos simples

### Códigos que não interagem com outros arquivos ou ferramentas do computador

Usaremos a biblioteca pyinstaller

- Passo 1 - Instalar o pyinstaller

- Passo 2 - Executar o pyinstaller

pyinstaller -w nome_do_programa.py


A flag -w no comando PyInstaller é usada para criar um executável sem console no Windows.

Quando a opção -w é usada, o PyInstaller cria um executável que não abre uma janela do console ao ser executado. Em outras palavras, a opção -w é usada para ocultar a janela do console, o que significa que o usuário não verá nenhuma janela de prompt de comando ou de console enquanto o programa estiver sendo executado.

Essa opção é útil quando se deseja criar um executável para uma aplicação gráfica ou de interface do usuário que não requer uma janela do console. Por exemplo, se você estiver criando um jogo em Python usando uma biblioteca como Pygame, pode ser útil usar a opção -w para criar um executável sem console para a sua aplicação.

No entanto, se o seu programa produz saída de console ou se você precisar depurar o programa, pode ser necessário desativar a opção -w para que a janela do console seja exibida e as mensagens possam ser visualizadas.

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