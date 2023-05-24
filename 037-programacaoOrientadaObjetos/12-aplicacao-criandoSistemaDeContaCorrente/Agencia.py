from UI import ui
from Cliente import *
from ContaCorrente import *

class Agencia:

    def __init__(self,numero,nome,cnpj,telefone) -> None:
        self.__numero=numero
        self.__nome=nome
        self.__cnpj=cnpj
        self.__telefone=telefone
        self.__clientes=[]
        self.__dinheiroCaixa=0

    @property
    def dinheiroCaixa(self):
        return self.__dinheiroCaixa
    
    @dinheiroCaixa.setter
    def dinheiroCaixa(self,valor):
        self.__dinheiroCaixa=valor

    def verificarCaixa(self):
        ui('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.dinheiroCaixa)) if self.dinheiroCaixa<10000000 else ui('O valor do Caixa está ok. Caixa Atual: {}'.format(self.dinheiroCaixa))

    
        