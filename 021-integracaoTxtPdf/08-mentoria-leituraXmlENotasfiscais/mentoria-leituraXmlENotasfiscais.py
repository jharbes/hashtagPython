import xmltodict
import pandas as pd
import os


# dicionarios nao sao iteraveis, mas o python entrega a chave quando feito um for no dicionario facilitando sua utilizacao nessa logica de repeticao
def printDict(dicionario):
    for chave in dicionario:
        print(chave, dicionario[chave],sep=': ')
    print()




def lerXmlDanfe(nota):
    # with abre o arquivo e ja garante que no final dela o arquivo sera fechado automaticamente
    print(nota)
    try:
        with open(nota,'rb') as arquivo:
            documento=xmltodict.parse(arquivo)
    


        # o documento em xml se tornara um grande dicionario onde poderemos capturar os dados de cada campo
        # print(documento['nfeProc']['NFe']['infNFe']['ide']['cUF'])
        # nome=documento['nfeProc']['NFe']['infNFe']['dest']['xNome']
        # print(nome)


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

        return dictNf 

    except:
        print('Arquivo inexistente')


# salva os nomes dos arquivos da pasta solicitada em uma lista de strings
listaArquivos=os.listdir('NFs Finais') 

print(listaArquivos) # ['DANFEBrota.pdf', 'DANFEBrota.xml', 'DANFENespresso.pdf', 'DANFENespresso.xml', 'NotaCariocaHashtag.pdf', 'NotaCariocaHashtag.xml']

for arquivo in listaArquivos:
    if '.xml' in arquivo and 'DANFE' in arquivo:
        lerXmlDanfe(f'NFs Finais\\{arquivo}')


# tabela=pd.DataFrame.from_dict(lerXmlDanfe(caminhoArquivoXml))
# print(tabela)
# tabela.to_excel('NFs.xlsx')