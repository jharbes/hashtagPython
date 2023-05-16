import numerosConta
from numerosConta import NumerosConta

class ContaCorrente:

    def __init__(self,nomeTitular,cpfTitular,saldo) -> None:
        self.__numero=numerosConta.NumerosConta.gerarNumeroConta()
        self.__nomeTitular=nomeTitular
        self.__cpfTitular=cpfTitular
        self.__saldo=saldo

    @property
    def saldo(self):
        return self.__saldo

    def deposito(self,valor):
        self.__saldo+=valor

    def saque(self,valor):
        if self.saldo>=valor:
            self.__saldo-=valor

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self,novoNumero):
        if novoNumero not in NumerosConta.numerosConta:
                NumerosConta.numerosConta.append(novoNumero)
                self.__numero=novoNumero
    
    @property
    def nomeTitular(self):
        return self.__nomeTitular
    
    @property
    def cpfTitular(self):
        return self.__cpfTitular
