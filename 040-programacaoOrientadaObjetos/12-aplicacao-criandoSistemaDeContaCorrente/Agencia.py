from UI import ui
from Cliente import *
from ContaCorrente import *

class Agencia:

    def __init__(self,numero,nome,cnpj,telefone) -> None:
        self.__numero=numero
        self.__nome=nome
        self.__cnpj=cnpj
        self.__telefone=telefone
        self._dinheiroCaixa=0
        ui('AGENCIA ABERTA COM SUCESSO COM OS SEGUINTES DADOS:\n{}'.format(self.__dict__))
        self.verificarCaixa()

    @property
    def numero(self):
        return self.__numero
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @property
    def telefone(self):
        return self.__telefone

    @property
    def dinheiroCaixa(self):
        return self._dinheiroCaixa
    
    @dinheiroCaixa.setter
    def dinheiroCaixa(self,valor):
        self._dinheiroCaixa=valor

    def verificarCaixa(self):
        ui('Caixa da Agência {} abaixo do nível recomendado. Caixa Atual: {}'.format(self.__numero,formatacaoMoeda(self.dinheiroCaixa))) if self.dinheiroCaixa<10000000 else ui('O valor do Caixa da Agência {} está ok. Caixa Atual: {}'.format(self.__numero,formatacaoMoeda(self.dinheiroCaixa)))




# Vamos criar AgenciaVirtual, AgenciaComum e AgenciaPremium, todas sao subclasses de Agencia

class AgenciaVirtual(Agencia):

    def __init__(self, numero, nome, cnpj, telefone, site) -> None:
        self.__site=site
        super().__init__(numero, nome, cnpj, telefone)
        self._dinheiroCaixa=1000000
        self.__caixaPaypal=0

    @property
    def site(self):
        return self.__site
    
    @property
    def caixaPaypal(self):
        return self.__caixaPaypal

    def depositarPaypal(self,valor):
        if valor<=self.dinheiroCaixa:
            self._dinheiroCaixa-=valor
            self.__caixaPaypal+=valor
            ui('Caixa do Paypal da Agência {} recebeu o crédito de {} reais.'.format(self.numero,formatacaoMoeda(valor)))

    def sacarPaypal(self,valor):
        if valor<=self.__caixaPaypal:
            self.__caixaPaypal-=valor
            self._dinheiroCaixa+=valor
            ui('Caixa do Paypal da Agência {} recebeu o débito de {} reais.'.format(self.numero,formatacaoMoeda(valor)))



class AgenciaComum(Agencia):

    def __init__(self, numero, nome, cnpj, telefone) -> None:
        super().__init__(numero, nome, cnpj, telefone)
        self._dinheiroCaixa=1000000



class AgenciaPremium(Agencia):

    def __init__(self, numero, nome, cnpj, telefone) -> None:
        super().__init__(numero, nome, cnpj, telefone)
        self._dinheiroCaixa=10000000