def ui(conteudo):
        if isinstance(conteudo,list):
            for item in conteudo:
                  print(item)
            print('-'*40)
        else:
            return print('-'*40+'\n{}\n'.format(conteudo))