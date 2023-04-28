"""

# Python para executável em programas mais complexos

### Objetivo:

Muitas vezes nossos códigos puxam informações de outros arquivos ou, no caso de webscraping, usam outros arquivos como o chromedriver.exe para funcionar.

Nesses casos, precisamos não só tomar alguns cuidados, mas também adaptar o nosso código para funcionar.

### O que usaremos:

- auto-py-to-exe para transformar o arquivo python em executável
- pathlib ou os para adaptar todos os "caminhos dos arquivos"
- Alternativamente, podemos usar o tkinter para permitir a gente escolher manualmente o arquivo, independente do computador que vamos rodar o programa

Vamos ver como isso funciona na prática

- Referências Úteis:
    1. https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi
    2. https://pypi.org/project/auto-py-to-exe/


"""

### Vamos rodar com um exemplo que temos na hashtag. Como pegar os links de vídeos do youtube

# Importações