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

# AND, OR e NOT sao condicoes que podem ser utilizadas no FETCH para filtrar os emails disponiveis e desejados
from imap_tools import MailBox, AND, OR, NOT

usuario='jharbes@hotmail.com'
senha=password

# TODO: testando o todo

meu_email=MailBox('outlook.office365.com').login(usuario,senha)




"""
Link com ferramentas do IMAP tools com filtros que podem ser feitos para encontrar e-mails na caixa de entrada usando o fetch:

https://github.com/ikvk/imap_tools#search-criteria

"""

# pegar email que foram enviados por um remetente específico

lista_emails = meu_email.fetch(AND(from_="jorge.harbes@technipfmc.com", to="jharbes@hotmail.com"))

for email in lista_emails:
    print(email.subject)
    print(email.text)




# pegar anexo de um email

lista_emails = meu_email.fetch(AND(from_="jorgenamiharbes@gmail.com"))
for email in lista_emails:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if "RelatorioExcel" in anexo.filename:
                # att.payload  # bytes: b'\xff\xd8\xff\xe0\' - cria uma copia escrevendo o binario do arquivo
                informacoes_anexo = anexo.payload

                # usaremos o with no python para recriar o arquivo excel (ou qualquer outro tipo) por meio do seu binario extraido com o payload
                with open("RelatorioExceldoEmail.xlsx", "wb") as arquivo_excel:
                    arquivo_excel.write(informacoes_anexo)