"""
# Vamos aprender a trabalhar com PDF usando o Python

- Regra geral: PDF foi feito justamente para bloquear muita coisa, então não é fácil "brincar" com um pdf
- Mesmo assim, Python tem várias bibliotecas que vão nos ajudar, vamos focar em 2:
    - PyPDF2
    - Tabula
- Ler e extrair informações de um PDF a gente consegue fazer.
- Escrever e Editar, aí já é outra história

### Para os nossos exemplos, vamos avaliar o Release de Resultados do 3º e 4º Trimestre de 2020 da Magazine Luiza
"""

# importando as bibliotecas:

import PyPDF2 as pyf
from pathlib import Path

pyf.PdfFileReader # para ler um arquivo em PDF
pyf.PdfFileWriter # criar/escrever um arquivo em PDF
pyf.PdfFileMerger # mesclar arquivos PDF

# #### 1º Objetivo: Queremos conseguir separar apenas o DRE do Release de Resultados (Página 14) para enviar para a Diretoria, como fazemos?

# - Separar as páginas de um pdf

nomeArquivoPdf='MGLU_ER_3T20_POR.pdf'
arquivoPdf=pyf.PdfReader(nomeArquivoPdf)
print(arquivoPdf)

# torna o arquivo iteravel, o for vai rolar pagina por pagina
numPagina=1
for pagina in arquivoPdf.pages: 
    # cria o arquivo com uma pagina apenas
    arquivoNovo=pyf.PdfWriter()
    arquivoNovo.add_page(pagina)
    # salva o arquivo
    # abre o arquivo Arquivo1.pdf em paginas\\ no mode='wb' (modo writable)
    # escreve/salva o arquivo novo no arquivo final
    with Path(f'paginas\\Arquivo{numPagina}.pdf').open(mode='wb') as arquivoFinal:
        arquivoNovo.write(arquivoFinal)
        numPagina+=1



# #### 2º Objetivo: Com o Release de Resultados já separado página por página, queremos incluir apenas as Páginas de Destaque (Página 1), DRE (Página 14) e Balanço (Página 16).

# - Juntar vários pdfs em 1

paginasSolicitadas=[1,14,16]

arquivoNovo=pyf.PdfWriter()
for numPagina in paginasSolicitadas:
    # Pegar o arquivo numero da pagina
    # Adicionar no novo PDF
    nomeArquivo=f'paginas\\Arquivo{numPagina}.pdf'
    arquivoPdf=pyf.PdfReader(nomeArquivo)
    pagina=arquivoPdf.pages[0] # tem que ter o indice zero porque por natureza é uma lista de paginas, na ausencia desse passara a lista inteira (mesmo que so haja um elemento)
    arquivoNovo.add_page(pagina)

# salvar o novo PDF
with Path(f'Consolidado.pdf').open(mode='wb') as arquivoFinal:
    arquivoNovo.write(arquivoFinal)




# ### Extra: Para adicionar todas as páginas de 2 pdfs
## como unir qualquer PDF entre si em um só:

pdfMesclado=pyf.PdfMerger()

arquivo1='MGLU_ER_3T20_POR.pdf'
arquivo2='MGLU_ER_4T20_POR.pdf'

# so funciona com um append de cada vez
pdfMesclado.append(arquivo1)
pdfMesclado.append(arquivo2)

with Path(f'ConsolidadoAppend.pdf').open(mode='wb') as arquivoFinal:
    pdfMesclado.write(arquivoFinal)




## # Funcionalidades que podem ser úteis:

# - Inserir arquivo no meio do outro
# - Quero colocar dentro do Resultado do 4T20 os destaques do 3T20 para poder comparar os 2 dentro do mesmo relatório

pdfMesclado=pyf.PdfMerger()

pdfMesclado.append(arquivo1)

# adiciona o arquivo 2 APÓS a pagina número 1 do arquivo 1, nesse caso 1 seria efetivamente a primeira folha e nao 0 como de costume
pdfMesclado.merge(1,arquivo2)

with Path(f'ConsolidadoMerge.pdf').open(mode='wb') as arquivoFinal:
    pdfMesclado.write(arquivoFinal)



## - Rodar Página

pdfRodar=pyf.PdfReader(arquivo1)

pdfFinal=pyf.PdfWriter()
for pagina in pdfRodar.pages:
    # 90 deita a pagina, 180 coloca ao contrario
    pagina.rotate(90)
    pdfFinal.add_page(pagina)

with Path(f'Rodado.pdf').open(mode='wb') as arquivoFinal:
    pdfFinal.write(arquivoFinal)




#### Trabalhando com Textos e Informações Dentro do PDF

#### 1º Objetivo: Quero identificar como foram as Despesas com Vendas da MGLU

# - Pegar texto da página e identificar onde está essa informação

nomeArquivo='MGLU_ER_3T20_POR.pdf'
arquivo=pyf.PdfReader(nomeArquivo)

# imprime o numero de paginas do arquivo
numPaginas=len(arquivo.pages)
print(numPaginas)

# imprime as informacoes do arquivo
informacoesArquivo=arquivo.metadata
print(informacoesArquivo)


textoProcurado='| Despesas com Vendas'

# percorrendo todas as páginas
numPagina=1
for pagina in arquivo.pages:
    # pegar o que está escrito na página
    textoPagina=pagina.extract_text()
    # textoPagina=pagina.extract_text().replace('  ',' ').replace('\n \n ','&&&&&&').replace('\n','').replace('&&&&&&','\n') # tentativa de padronizar o texto

    # verificar se dentro do texto da pagina tem o texto procurado
    if textoProcurado in textoPagina:
        print(f'Está na página {numPagina}')
        textoFinal=textoPagina

    # se tiver, retornar qual o numero da pagina

    numPagina+=1

# print(textoFinal)

# descobre a posicao do primeiro caractere referente ao texto procurado
posicaoInicialTexto=textoFinal.find('| Despesas com Vendas')
print(posicaoInicialTexto)

# pesquisa a proxima barrinha do texto, o segundo argumento é a partir de que posicao ele vai procurar
posicaoFinalTexto=textoFinal.find('|', posicaoInicialTexto+1)
print(posicaoFinalTexto)

textoDespesa=textoFinal[posicaoInicialTexto:posicaoFinalTexto]
print(textoDespesa)




### #### 2º Objetivo: Quero analisar o DRE (sem ajuste - Página 5)

#- Para ler tabelas em pdf, use o tabula (é ninja)

import tabula.io


# o numero da pagina nao segue a logica dos arrays/listas e comeca por 1
df=tabula.io.read_pdf('MGLU_ER_3T20_POR.pdf', pages=5)
print(df)

# o tabula procura todas as tabelas que estao na pagina, sendo assim ela tem indices, pois cada indice será uma tabela da pagina comecando pelo indice [0], se houver apenas uma sera apenas esse elemento na lista de tabelas
tabela=df[0]

tabela=tabela.dropna(how='all') # deleta todas as LINHAS que estejam com tudo em branco (NaN), utiliza default axis=0 (linha)

tabela=tabela.dropna(how='all',axis=1) # deleta todas as COLUNAS que estejam com tudo em branco (NaN)

tabela.columns=tabela.iloc[0]
tabela=tabela.drop(tabela.index[0])
tabela=tabela.reset_index(drop=True)

print(tabela)

tabela.to_excel('TabelaExtraidaPDF.xlsx')




## #### 3º Objetivo: Quero analisar o Capital de Giro e os Investimentos (ambas as tabelas na página 12)
#    - Páginas com mais de 1 tabela

df=tabula.io.read_pdf('MGLU_ER_3T20_POR.pdf', pages=12)

for tabela in df:
    tabela=tabela.dropna(how='all')
    tabela=tabela.dropna(how='all',axis=1)
    print(tabela)



## #### O que fazer quando o tabula não consegue ler alguma linha da tabela? Como o cabeçalho, no nosso caso?

# primeira tabela da pagina 5 extraida da maneira normal
capitalGiro=df[0]
capitalGiro=capitalGiro.dropna(how='all')
capitalGiro=capitalGiro.dropna(how='all',axis=1)
print(capitalGiro)

# outro metodo para ler a tabela, mais desorganizado porem inclui mais coisas, entao dependendo do caso pode ser util
df2=tabula.io.read_pdf('MGLU_ER_3T20_POR.pdf', pages=12, lattice=True)
tituloCapitalGiro=df2[0]
tituloCapitalGiro=tituloCapitalGiro.dropna(how='all')
tituloCapitalGiro=tituloCapitalGiro.dropna(how='all',axis=1)
tituloCapitalGiro=tituloCapitalGiro.iloc[0]
tituloCapitalGiro=tituloCapitalGiro.dropna()
capitalGiro.columns=tituloCapitalGiro
print(tituloCapitalGiro)