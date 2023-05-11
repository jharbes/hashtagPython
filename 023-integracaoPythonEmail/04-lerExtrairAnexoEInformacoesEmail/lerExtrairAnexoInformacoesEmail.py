"""
Ler e extrair anexo e informacoes do Email

"""

from imap_tools import MailBox, AND

usuario='jharbes@hotmail.com'
senha=''

meuEmail=MailBox('outlook.office365.com').login(usuario,senha)