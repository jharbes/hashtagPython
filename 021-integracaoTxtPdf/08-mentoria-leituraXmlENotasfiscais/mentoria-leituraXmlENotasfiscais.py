import xmltodict

# with abre o arquivo e ja garante que no final dela o arquivo sera fechado automaticamente
with open('.\\021-integracaoTxtPdf\\08-mentoria-leituraXmlENotasfiscais\\NFs Finais\\DANFEBrota.xml','rb') as arquivo:
    documento=xmltodict.parse(arquivo)

print(documento)