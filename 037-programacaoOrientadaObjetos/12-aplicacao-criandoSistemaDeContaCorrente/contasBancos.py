import numerosConta
from numerosConta import NumerosConta


# criando formatacao para os valores (em reais)
import locale
locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')

def formatacaoMoeda(valor):
    return locale.currency(valor,grouping=True)


class ContaCorrente:

    def __init__(self,nomeTitular,cpfTitular,saldo) -> None:
        self.__numero=numerosConta.NumerosConta.gerarNumeroConta()
        self.__nomeTitular=nomeTitular
        self.__cpfTitular=cpfTitular
        self.__saldo=saldo
        self.__limite=0

    @property
    def saldo(self):
        return self.__saldo
    
    def consultarSaldo(self):
        return 'O saldo da conta de número {} é de {}'.format(self.__numero,formatacaoMoeda(self.__saldo))
    
    def limiteConta(self,valor):
        self.__limite=valor

    def consultarLimiteConta(self):
        return 'O limite da conta de número {} possui o valor de {}'.format(self.__numero,formatacaoMoeda(self.__limite))

    def deposito(self,valor):
        self.__saldo+=valor

    def saque(self,valor):
        if self.__saldo+self.__limite>=valor:
            self.__saldo-=valor
            return 'Saque de {} efetivado com sucesso! {}'.format(formatacaoMoeda(valor),self.consultarSaldo())

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
