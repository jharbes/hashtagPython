"""

# Ambientes Virtuais no Python

### Essencialmente usamos o virtualenv, mas o anaconda tem um método próprio para isso

### Objetivo: Ter outras versões do Python instalados no computador com 2 objetivos:
    
    1. Usar ferramentas que funcionam apenas com versões específicas do Python
    2. Isolar de todo o resto tudo aquilo que é estritamente necessário para o programa rodar. Importante para sites e programas que vão ser distribuídos
    
### Observação Importante:

Quando você cria um ambiente virtual, ele vem praticamente sem nada, então você precisa usar o pip ou o conda para instalar cada pacote que for usar

"""

### Comandos importantes do cmd:

# - Windows:
# cd Pasta -> navega até aquela pasta
# cd .. -> volta para a pasta anterior
# dir -> lista os arquivos contidos na pasta

# - Mac ou Linux
# cd Pasta -> navega até aquela pasta
# cd .. -> volta para a pasta anterior
# ls -> lista os arquivos contidos na pasta

# Obs: Caso o nome da pasta tenha espaço, talvez seja necessário substituir o espaço por \, exemplo:
# cd Python Impressionador -> navega até a pasta "Python Impressionador"
# talvez seja necessário fazer:
# cd Python\Impressionador


# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
#


# Como criar ambientes virtuais
# Abra a pasta do seu projeto no terminal
# e digite:

# -m executa como script
python -m venv nome_do_ambiente_virtual

# podemos colocar python=versao no fim do comando para especificar qual a versao do python que queremos instalar



# Ativando e desativando meu ambiente virtual

Windows: .\venv\Scripts\activate
Linux e Mac: source venv/bin/activate
Desativar: deactivate
#


# Quando o ambiente virtual está instalado que iremos instalar as dependencias que queremos que ele tenha com pip install, podendo escolher a versao de cada dependencia


# Replicando ambientes
# No início do artigo falamos sobre os ambientes virtuais trazerem a simplicidade de replicar o ambiente em outras máquinas e isso se deve a possibilidade de exportarmos um arquivo com todas bibliotecas que o nosso projeto contém. Veja como é simples:

pip freeze > requirements.txt


# Com o comando acima, será criado um arquivo com todas as bibliotecas presentes em nosso ambiente virtual. Por exemplo:

flake8==3.7.9
Flask==1.1.2
Flask-API==2.0


# Agora, se quisermos rodar o nosso projeto em outra máquina, não será necessário baixar as dependências uma a uma, basta fazer:

pip install -r requirements.txt  

# Com o comando acima, será instalado de forma automática todas as bibliotecas presentes no arquivo requirements.txt


# E por fim, para desativar o ambiente virtual:

deactivate