from pathlib import Path
import shutil

listaEstados=['RJ','SP','MG','GO','AM']

for estado in listaEstados:
    if Path('Pasta Auxiliar\\'+estado).exists():
        continue
    else:
        Path('Pasta Auxiliar\\'+estado).mkdir()


caminho=Path('C:\\Users\\Jorge\\Desktop\\hashtag\\hashtagPython\\022-integracaoPython-ArquivosPastasComputador\\Arquivos_Lojas')



for arquivo in caminho.iterdir():
    print(caminho)
    print(arquivo)
    print(arquivo.name)
    print(caminho.iterdir())
    for estado in listaEstados:
        if estado in arquivo.name:

            print(arquivo.name, type(arquivo.name))

            shutil.copy2(caminho / Path(arquivo.name),Path('Pasta Auxiliar\\'+estado+'\\'+arquivo.name))


