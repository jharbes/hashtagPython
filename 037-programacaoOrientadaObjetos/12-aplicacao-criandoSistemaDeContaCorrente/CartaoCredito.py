from UI import *

class CartaoCredito:

    def __init__(self,nomeTitular,contaCorrente) -> None:
        self.__numero=None
        self.__nomeTitular=nomeTitular
        self.__dataValidade=None
        self.__codSeguranca=None
        self.__limite=None
        self.__contaCorrente=contaCorrente
        contaCorrente.adicionaCartaoCredito(self)
        ui('CARTAO DE CREDITO CRIADO COM SUCESSO COM OS SEGUINTES DADOS:\n{}'.format(self.__dict__))

        @property
        def numero(self):
            return self.__numero
        
        @property
        def nomeTitular(self):
            return self.__nomeTitular
        
        @property
        def limite(self):
            return self.__limite
        
        @property
        def contaCorrente(self):
            return self.__contaCorrente