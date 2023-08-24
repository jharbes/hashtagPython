import random

class NumeroConta:

    numerosConta=[]

    @staticmethod
    def gerarNumeroConta():
        while True:
            numeroConta=random.randint(10000,99999)
            if numeroConta not in NumeroConta.numerosConta:
                NumeroConta.numerosConta.append(numeroConta)
                return numeroConta
        