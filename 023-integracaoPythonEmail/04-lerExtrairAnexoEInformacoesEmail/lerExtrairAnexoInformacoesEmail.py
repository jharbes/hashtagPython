"""
Ler e extrair anexo e informacoes do Email

"""

import sys
sys.path.append('C:\\Users\\Jorge\\Desktop\\hashtag')
print(sys.path)

from passwd import password

from imap_tools import MailBox, AND

usuario='jharbes@hotmail.com'
senha=password

# TODO: testando o todo

meuEmail=MailBox('outlook.office365.com').login(usuario,senha)