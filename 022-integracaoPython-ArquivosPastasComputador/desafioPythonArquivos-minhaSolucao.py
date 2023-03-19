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

            # observe que caminho é um path, ao fazermos 'caminho / Path('202004_Shopping Cidade_MG.csv')' estamos fazendo uma concatenacao de Paths que NAO SAO o mesmo que strings 
            shutil.copy2(caminho / Path(arquivo.name),Path('Pasta Auxiliar\\'+estado+'\\'+arquivo.name))



"""
Obs: Para pegar o nome de um arquivo como um texto no pathlib, você pode usar Path.name ou arquivo.name:<br>
caminho = Path('Pasta/Arquivo.csv')
print(caminho.name) -> resposta: 'Arquivo.csv'
"""