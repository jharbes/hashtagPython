#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message
import sys
sys.path.append('C:\\Users\\Jorge\\Desktop\\hashtag')
print(sys.path) # imprimindo todos os sys.path disponiveis após a adicao acima

from passwd import senha_app_gmail

def enviar_email():  
    corpo_email = """
    <h3>Teste de email</h3>
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'jorgenamiharbes@gmail.com'
    msg['To'] = 'jharbes@hotmail.com'
    password = senha_app_gmail
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()

