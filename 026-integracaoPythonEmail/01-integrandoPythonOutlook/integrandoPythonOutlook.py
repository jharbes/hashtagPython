"""
# Integração Python com Outlook

### Funciona para qualquer e-mail: corporativo, gmail, hotmail, etc.

"""

# - Passo 1: Importar win32 e inicializar o outlook

import win32com.client as win32
outlook = win32.Dispatch('outlook.application')




# - Passo 2: Escrever o e-mail e disparar (nao precisa preencher o remetente, será o padrao do outlook)

mail = outlook.CreateItem(0)
mail.To = 'jharbes@hotmail.com'
mail.CC = 'jharbes@icloud.com'
mail.BCC = 'jorge.harbes@technipfmc.com' # BCC é copia oculta
mail.Subject = 'Email vindo do Outlook'
mail.Body = 'Texto de email, teste de automação'
#ou mail.HTMLBody = '<p>Corpo do Email em HTML</p>'

# Anexos (pode colocar quantos quiser):
# ***OBS: o path do arquivo deve ser completo OBRIGATORIAMENTE, pois a pasta padrao sempre será a do outlook
attachment  = r'C:\Users\jharbes\Documents\GitHub\hashtagPython\023-integracaoPythonEmail\01-integrandoPythonOutlook\Financeiro.xlsx'
mail.Attachments.Add(attachment)

mail.Send()