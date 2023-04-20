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



print(documento['nfeProc']['NFe']['infNFe']['ide']['cUF'])
nome=documento['nfeProc']['NFe']['infNFe']['dest']['xNome']
print(nome)


# agora vamos buscar os seguintes valores:
# valorTotal, produtos/servicos(valores), cnpjVendeu, nomeVendeu, cpf/cnpjComprou, nomeComprou

caminho=documento['nfeProc']['NFe']['infNFe']
valorTotal=caminho['total']['ICMSTot']['vNF']
print(valorTotal)

cnpjVendeu=caminho['emit']['CNPJ']
print(cnpjVendeu)

nomeVendeu=caminho['emit']['xNome']
print(nomeVendeu)

cpfCnpjComprou=caminho['dest']['CPF']
print(cpfCnpjComprou)

nomeComprou=caminho['dest']['xNome']
print(nomeComprou)