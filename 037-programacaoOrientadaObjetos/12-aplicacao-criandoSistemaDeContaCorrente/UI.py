from ContaCorrente import *
# from CartaoCredito import CartaoCredito

def ui(conteudo):
        if isinstance(conteudo,list):
            for item in conteudo:
                  print(item)
            print('-'*40)
        # elif isinstance(conteudo,CartaoCredito):
        #     for item in conteudo:
        #         print(conteudo[item])
        else:
            return print('-'*40+'\n{}\n'.format(conteudo))