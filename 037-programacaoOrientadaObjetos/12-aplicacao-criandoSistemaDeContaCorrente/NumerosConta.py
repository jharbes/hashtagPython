import random

class NumerosConta:

    numerosConta=[]

    @staticmethod
    def gerarNumeroConta():
        while True:
            numeroConta=random.randint(10000,99999)
            if numeroConta not in NumerosConta.numerosConta:
                NumerosConta.numerosConta.append(numeroConta)
                return numeroConta
        