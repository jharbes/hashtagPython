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