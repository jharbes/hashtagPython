import random

class NumeroCartao:

    numerosCartao=[]
    numerosCodigoSeguranca=[]

    @staticmethod
    def gerarNumeroCartao():
        while True:
            numeroCartao=random.randint(1000000000000000,9999999999999999)
            if numeroCartao not in NumeroCartao.numerosCartao:
                NumeroCartao.numerosCartao.append(numeroCartao)
                return numeroCartao
    
    @staticmethod
    def gerarNumeroCodigoSeguranca():
        while True:
            numeroCodigoSeguranca='{}{}{}'.format(random.randint(0,9),random.randint(0,9),random.randint(0,9))
            if numeroCodigoSeguranca not in NumeroCartao.numerosCodigoSeguranca:
                NumeroCartao.numerosCodigoSeguranca.append(numeroCodigoSeguranca)
                return numeroCodigoSeguranca
            
