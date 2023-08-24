"""
# Desafio Python e E-mail

### Descrição

Digamos que você trabalha em uma indústria e está responsável pela área de inteligência de negócio.

Todo dia, você, a equipe ou até mesmo um programa, gera um report diferente para cada área da empresa:
- Financeiro
- Logística
- Manutenção
- Marketing
- Operações
- Produção
- Vendas

Cada um desses reports deve ser enviado por e-mail para o Gerente de cada Área.

Crie um programa que faça isso automaticamente. A relação de Gerentes (com seus respectivos e-mails) e áreas está no arquivo 'Enviar E-mails.xlsx'.

Dica: Use o pandas read_excel para ler o arquivo dos e-mails que isso vai facilitar.

"""

import pandas as pd
import win32com.client as win32

enviarEmailsDf=pd.read_excel('Enviar E-mails.xlsx')

print(enviarEmailsDf)

outlook = win32.Dispatch('outlook.application')

# for indice in enviarEmailsDf.index:
#     print(enviarEmailsDf.loc[indice,'E-mail'])

css = ''' 
<style>   
.email p {
    font-size: 20px;
    font-family: Arial, Helvetica, sans-serif;
}
</style>
'''

for indice in enviarEmailsDf.index:
    mail = outlook.CreateItem(0)
    mail.To = enviarEmailsDf.loc[indice,'E-mail']
    # mail.CC = 'email@gmail.com'
    # mail.BCC = 'email@gmail.com' # BCC é copia oculta
    mail.Subject = f'Relatório do Setor {enviarEmailsDf.loc[indice,"Relatório"]}'
    # mail.Body = 'Texto do E-mail'
    mail.HTMLBody = f'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                {css}
            </head>
            <body>
                <section class="email">

                    <h3>Senhor {enviarEmailsDf.loc[indice,'Gerente']},</h3>

                        <p>Segue, em anexo, o relatório do setor {enviarEmailsDf.loc[indice,"Relatório"]}<p>

                        
                    <p>Atenciosamente,</p>

                    <h3>Jorge Nami Harbes</h3>

                </section>
            </body>
        </html>
    '''

    # Anexos (pode colocar quantos quiser):
    # ***OBS: o path do arquivo deve ser completo OBRIGATORIAMENTE, pois a pasta padrao sempre será a do outlook
    attachment  = f'C:\\Users\\jharbes\\Documents\\GitHub\\hashtagPython\\023-integracaoPythonEmail\\01-integrandoPythonOutlook\\{enviarEmailsDf.loc[indice,"Relatório"]}.xlsx'
    mail.Attachments.Add(attachment)

    mail.Send()



