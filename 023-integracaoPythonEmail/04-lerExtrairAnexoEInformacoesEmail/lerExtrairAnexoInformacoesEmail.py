"""
Ler e extrair anexo e informacoes do Email

"""

"""
Lista de sites com servidores IMAP de vários tipos de email:
https://www.systoolsgroup.com/imap/

"""

import sys
sys.path.append('C:\\Users\\Jorge\\Desktop\\hashtag')
print(sys.path) # imprimindo todos os sys.path disponiveis após a adicao acima

# importacao da senha em arquivo nao disponivel no github
from passwd import password

from imap_tools import MailBox, AND

usuario='jharbes@hotmail.com'
senha=password

# TODO: testando o todo

meu_mail=MailBox('outlook.office365.com').login(usuario,senha)




"""
Link com ferramentas do IMAP tools com filtros que podem ser feitos para encontrar e-mails na caixa de entrada usando o fetch:

https://github.com/ikvk/imap_tools#search-criteria

"""

# pegar email que foram enviados por um remetente específico

