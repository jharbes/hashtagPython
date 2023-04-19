import xmltodict
import time

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
print()

print(documento['nfeProc']['NFe']['infNFe']['ide']['cUF'])
nome=documento['nfeProc']['NFe']['infNFe']['dest']['xNome']
print(nome)


# agora vamos buscar os seguintes valores:
# valorTotal, produtos/servicos(valores), cnpjVendeu, nomeVendeu, cpf/cnpjComprou, nomeComprou
