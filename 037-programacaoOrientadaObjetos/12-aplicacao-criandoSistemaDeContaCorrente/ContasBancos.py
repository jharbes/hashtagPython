from UI import ui
from NumerosConta import NumerosConta
from datetime import datetime
import pytz # faz o ajuste de fuso horario
import locale


# criando formatacao para os valores (em reais)
locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')


fusoHorarioBrasil=pytz.timezone('Brazil/East')

def formatacaoMoeda(valor):
    return locale.currency(valor,grouping=True)

def dataHoraAtual():
    return datetime.now(fusoHorarioBrasil).strftime('%d/%m/%Y %H:%M:%S') # metodo strftime mostra a data/hora em modo mais amigavel e legivel


class ContaCorrente:


    def __init__(self,agencia,nomeTitular,cpfTitular,saldo) -> None:
        self.__ativa=True
        self.__banco='033'
        self.__agencia=agencia
        self.__numero=NumerosConta.gerarNumeroConta()
        self.__nomeTitular=nomeTitular
        self.__cpfTitular=cpfTitular
        self.__saldo=saldo
        self.__limite=0
        self.__transacoes=[]
        ui('CONTA ABERTA COM SUCESSO COM OS SEGUINTES DADOS:\n{}'.format(self.__dict__))

    @property
    def ativa(self):
        return self.__ativa
    
    def confereAtiva(self):
        if self.ativa:
            return True
        else:
            ui('Operação não permitida, conta de número {} está inativa'.format(self.numero))
            return False
    
    @property
    def banco(self):
        return self.__banco
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def saldo(self):
        return self.__saldo
    
    def consultarSaldo(self):
        if self.confereAtiva():
            ui('O saldo da conta de número {} é de {}'.format(self.__numero,formatacaoMoeda(self.__saldo)))
    
    def limiteConta(self,valor):
        if self.ativa:
            self.__limite=valor
            ui('Limite de Cheque Especial no valor de {} implantado com sucesso na conta de número {}.'.format(formatacaoMoeda(valor),self.numero))
            self.__transacoes.append((valor,self.saldo,dataHoraAtual()))
        else:
            ui('Operação não permitida, conta de número {} está inativa'.format(self.numero))

    def consultarLimiteConta(self):
        ui('O limite da conta de número {} possui o valor de {}'.format(self.__numero,formatacaoMoeda(self.__limite)))

    def deposito(self,valor):
        if self.confereAtiva():
            self.__saldo+=valor
            ui('Depósito de {} efetivado com sucesso!'.format(formatacaoMoeda(valor)))
            self.consultarSaldo()
            self.__transacoes.append((valor,self.saldo,dataHoraAtual()))

    def saque(self,valor):
        if self.confereAtiva():
            if self.__saldo+self.__limite>=valor:
                self.__saldo-=valor
                ui('Saque de {} efetivado com sucesso!'.format(formatacaoMoeda(valor)))
                self.consultarSaldo()
                self.__transacoes.append((valor,self.saldo,dataHoraAtual()))
            else:
                ui('Saque de {} não permitido! Valores de saldo/limite insuficientes!'.format(formatacaoMoeda(valor)))

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
    
    @property
    def transacoes(self):
        ui(self.__transacoes)
