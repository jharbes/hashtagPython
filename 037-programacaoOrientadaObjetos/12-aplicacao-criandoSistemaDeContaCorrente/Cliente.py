from Agencia import *
from ContaCorrente import *

class Cliente:

    def __init__(self,nomeTitular,cpfTitular) -> None:
        self.__nomeTitular=nomeTitular
        self.__cpfTitular=cpfTitular
        self.__rendaMensal=None
        self.__emprestimos=[]

