from UI import ui
from Cliente import *
from ContaCorrente import *

class Agencia:

    def __init__(self,numero,nome,cnpj,telefone) -> None:
        self.__numero=numero
        self.__nome=nome
        self.__cnpj=cnpj
        self.__telefone=telefone
        self.__dinheiroCaixa=0
        ui('AGENCIA ABERTA COM SUCESSO COM OS SEGUINTES DADOS:\n{}'.format(self.__dict__))
        self.verificarCaixa()

    @property
    def dinheiroCaixa(self):
        return self.__dinheiroCaixa
    
    @dinheiroCaixa.setter
    def dinheiroCaixa(self,valor):
        self.__dinheiroCaixa=valor

    def verificarCaixa(self):
        ui('Caixa da Agência {} abaixo do nível recomendado. Caixa Atual: {}'.format(self.__numero,self.dinheiroCaixa)) if self.dinheiroCaixa<10000000 else ui('O valor do Caixa da Agência {} está ok. Caixa Atual: {}'.format(self.__numero,self.dinheiroCaixa))




# Vamos criar AgenciaVirtual, AgenciaComum e AgenciaPremium

class AgenciaVirtual(Agencia):

    pass



class AgenciaComum(Agencia):

    pass



class AgenciaPremium(Agencia):

    pass