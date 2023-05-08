"""
# Integração Python com Outlook

### Funciona para qualquer e-mail: corporativo, gmail, hotmail, etc.

"""

# - Passo 1: Importar win32 e inicializar o outlook

import win32com.client as win32
outlook = win32.Dispatch('outlook.application')




# - Passo 2: Escrever o e-mail e disparar

mail = outlook.CreateItem(0)
mail.To = 'jharbes@hotmail.com'
mail.CC = 'jharbes@icloud.com'
mail.BCC = 'jorge.harbes@technipfmc.com'
mail.Subject = 'Email vindo do Outlook'
mail.Body = 'Texto do E-mail'
#ou mail.HTMLBody = '<p>Corpo do Email em HTML</p>'

# Anexos (pode colocar quantos quiser):
attachment  = r'C:\Users\joaop\Google Drive\Python Impressionador\Financeiro.xlsx'
mail.Attachments.Add(attachment)

mail.Send()