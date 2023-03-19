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

# Importando os módulos

from pathlib import Path

Path.cwd() # cwd = current working directory

print(Path.cwd()) # C:\Users\Jorge\Desktop\hashtag\hashtagPython\022-integracaoPython-ArquivosPastasComputador\001-pathlib-shutil-pythonNavegarNoComputador

