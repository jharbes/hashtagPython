import xmltodict
import pandas as pd


# dicionarios nao sao iteraveis, mas o python entrega a chave quando feito um for no dicionario facilitando sua utilizacao nessa logica de repeticao
def printDict(dicionario):
    for chave in dicionario:
        if isinstance(dicionario[chave],list):
            print(chave,': ')
            for item in dicionario[chave]:
                print(item,end='\n')
        else:
            print(chave, dicionario[chave],sep=': ')



# with abre o arquivo e ja garante que no final dela o arquivo sera fechado automaticamente
try:
    caminhoArquivoXml='.\\021-integracaoTxtPdf\\08-mentoria-leituraXmlENotasfiscais\\NFs Finais\\DANFENespresso.xml'
    with open(caminhoArquivoXml,'rb') as arquivo:
        documento=xmltodict.parse(arquivo)
except:
    caminhoArquivoXml='NFs Finais\\DANFEBrota.xml'
    with open(caminhoArquivoXml,'rb') as arquivo:
        documento=xmltodict.parse(arquivo)


# o documento em xml se tornara um grande dicionario onde poderemos capturar os dados de cada campo
print(documento['nfeProc']['NFe']['infNFe']['ide']['cUF'])
nome=documento['nfeProc']['NFe']['infNFe']['dest']['xNome']
print(nome)


# agora vamos buscar os seguintes valores:
# valorTotal, produtos/servicos(valores), cnpjVendeu, nomeVendeu, cpf/cnpjComprou, nomeComprou

caminho=documento['nfeProc']['NFe']['infNFe']

valorTotal=caminho['total']['ICMSTot']['vNF']
cnpjVendeu=caminho['emit']['CNPJ']
nomeVendeu=caminho['emit']['xNome']
cpfCnpjComprou=caminho['dest']['CPF']
nomeComprou=caminho['dest']['xNome']

dictProdutos=caminho['det']
listaProdutos=[]
for produto in dictProdutos:
    valorProduto=produto['prod']['vProd']
    nomeProduto=produto['prod']['xProd']
    listaProdutos.append((nomeProduto,valorProduto))

# transformaremos todos os itens em listas para que no excel todos os produtos se mantenham na mesma linha com apenas uma copia da nota fiscal
dictNf={
    'Valor Total':[valorTotal],
    'CNPJ Vendedor':[cnpjVendeu],
    'Nome do Vendedor':[nomeVendeu],
    'CPF ou CNPJ do Comprador':[cpfCnpjComprou],
    'Nome do Comprador':[nomeComprou],
    'Lista de Produtos':[listaProdutos]
}


printDict(dictNf)
print()


tabela=pd.DataFrame.from_dict(dictNf)
print(tabela)
tabela.to_excel('NFs.xlsx')