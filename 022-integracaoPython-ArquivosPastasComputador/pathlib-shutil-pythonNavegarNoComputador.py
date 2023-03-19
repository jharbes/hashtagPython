"""

# Python e Arquivos do Computador

### Módulo os e pathlib

Os módulos os e pathlib são uns dos melhores módulos/bibliotecas para controlar as pastas e arquivos do seu computador. Existem alguns outros módulos que podem auxiliar dependendo do que você está querendo fazer, mas em essência conseguiremos usar esses módulos para resolver nossos desafios.

Usaremos aqui o pathlib por ele funcionar bem independente do sistema operacional que você está usando.

### Atenção Especial

Normalmente os caminhos em computadores Windows, Mac ou Linux são diferentes, mas isso é algo que o pathlib vai resolver para a gente

### Módulo shutil

Para as ações de copiar e colar arquivo, até conseguimos fazer com os módulos os e pathlib, mas é mais difícil e com maior margem de erro. MAS, existe o módulo shutil para ajudar nisso

"""

## Importando os módulos

from pathlib import Path

Path.cwd() # cwd = current working directory, mostra o diretorio atual onde o programa esta rodando

print(Path.cwd()) # C:\Users\Jorge\Desktop\hashtag\hashtagPython\022-integracaoPython-ArquivosPastasComputador



## Descobrindo onde está o nosso arquivo

# caminho=Path('Arquivos_Lojas') # sem o caminho completo so funciona no jupiter
caminho=Path('C:\\Users\\Jorge\\Desktop\\hashtag\\hashtagPython\\022-integracaoPython-ArquivosPastasComputador\\Arquivos_Lojas')
# caminho=Path('C:/Users/Jorge/Desktop/hashtag/hashtagPython/022-integracaoPython-ArquivosPastasComputador/Arquivos_Lojas')
print(caminho) # C:\Users\Jorge\Desktop\hashtag\hashtagPython\022-integracaoPython-ArquivosPastasComputador\



## Vamos listar todos os arquivos de uma pasta

arquivos=caminho.iterdir()
print(arquivos) # printa apenas o objeto

for arquivo in arquivos: # printa todos os arquivos do diretorio (ls)
    print(arquivo)



## Agora, vamos verificar se um arquivo que estamos procurando existe na pasta

print('\nArquivo existe\n') if Path('Arquivos_Lojas\\202004_Shopping Cidade_MG.csv').exists() else print('\nNão existe\n')

# ou

print('\nArquivo existe\n') if (caminho / Path('202004_Shopping Cidade_MG.csv')).exists() else print('\nNão existe\n')




## Criando uma nova pasta

# Path('Pasta Auxiliar\\Pasta2').mkdir()


## Criando uma cópia do nosso arquivo na nova pasta que criamos

# copia o arquivo para a pasta selecionada com o nome novo que escolhemos, sobreescreve o arquivo se eles ja existir
import shutil
arquivoCopiar=Path('Arquivos_Lojas\\201801_Amazonas Shopping_AM.csv')
arquivoColar=Path('Pasta Auxiliar\\201801_Amazonas Shopping_AM_versao2.csv')
shutil.copy2(arquivoCopiar,arquivoColar)



## Movendo um arquivo

# 2 formas:

# Path('caminho/arquivo.extensao').rename('caminho_novo/arquivo.extensao')<br>

# ou

# shutil.move(Path('caminho/arquivo.extensao'), Path('caminho_novo/arquivo.extensao'))

shutil.move(Path('Pasta Auxiliar\\201801_Amazonas Shopping_AM_versao2.csv'), Path('Pasta Auxiliar\\Pasta2\\201801_Amazonas Shopping_AM_versao2.csv'))