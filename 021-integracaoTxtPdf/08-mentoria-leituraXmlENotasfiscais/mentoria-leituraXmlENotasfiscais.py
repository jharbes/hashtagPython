import xmltodict

# with abre o arquivo e ja garante que no final dela o arquivo sera fechado automaticamente

try:
    caminhoArquivoXml='.\\021-integracaoTxtPdf\\08-mentoria-leituraXmlENotasfiscais\\NFs Finais\\DANFEBrota.xml'
    with open(caminhoArquivoXml,'rb') as arquivo:
        documento=xmltodict.parse(arquivo)
except:
    caminhoArquivoXml='NFs Finais\\DANFEBrota.xml'
    with open(caminhoArquivoXml,'rb') as arquivo:
        documento=xmltodict.parse(arquivo)


print(documento)