def ui(conteudo):
        if isinstance(conteudo,list):
            for item in conteudo:
                  print(item)
            print('-'*20)
        else:
            return print('-'*20+'\n{}\n'.format(conteudo))