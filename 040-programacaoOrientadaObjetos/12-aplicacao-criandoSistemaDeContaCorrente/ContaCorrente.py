from UI import ui
from NumeroConta import NumeroConta
from funcoesAuxiliares import *
from Cliente import *
from Agencia import *

class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        ativa (bool): Se a conta está ativa ou não
        banco (str): Número do banco
        agencia (str): Número da agência
        numero (int): Número da conta gerado automaticamente de forma aleatória
        nomeTitular (str): Nome do titular da conta
        cpfTitular (str): CPF do titular da conta com pontos e traço
        saldo (float): Saldo da conta
        limite (float): Limite de cheque especial da conta
        transacoes (list): Lista de transacoes a debito/credito lançados na conta
    """


    def __init__(self,agencia,nomeTitular,cpfTitular,depositoInicial=0) -> None:
        self.__ativa=True
        self.__banco='033'
        self.__agencia=agencia
        self.__numero=NumeroConta.gerarNumeroConta()
        self.__nomeTitular=nomeTitular
        self.__cpfTitular=cpfTitular
        self.__senha=None
        self.__saldo=depositoInicial
        self.__limite=0
        self.__transacoes=[]
        self.__cartoes=[]
        self.__emprestimos=[]
        ui('CONTA CORRENTE ABERTA COM SUCESSO COM OS SEGUINTES DADOS:\n{}'.format(self.__dict__))
        if depositoInicial>0:
            self.__transacoes.append((depositoInicial,self.saldo,dataHoraAtual()))


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
    def senha(self):
        return self.__senha
        
    @senha.setter
    def senha(self,senhaEscolhida):
        senhaEscolhida=str(senhaEscolhida)
        if len(senhaEscolhida)==4 and senhaEscolhida.isnumeric():
            self.__senha=senhaEscolhida
            ui('Senha alterada com sucesso!')
        else:
            ui('Senha Inválida, deve ser numérica e possuir quatro dígitos!')
    
    @property
    def saldo(self):
        return self.__saldo
    
    def fazerEmprestimo(self,valor,juros):
        if self.__agencia.dinheiroCaixa>=valor:
            self.__emprestimos.append((valor,juros))
            ui('Empréstimo no valor de {} disponibilizado na conta {} com sucesso!'.format(formatacaoMoeda(valor),self.numero))
            self.deposito(valor)
            return True
        else:
            ui('Empréstimo não é possivel, Valor não disponível em Caixa.')
            return False
    
    def adicionaCartaoCredito(self,cartao):
        self.__cartoes.append(cartao)
    
    def consultarSaldo(self):
        if self.confereAtiva():
            ui('O saldo da conta de número {} é de {}'.format(self.__numero,formatacaoMoeda(self.__saldo)))
    
    def limiteConta(self,valor):
        if self.confereAtiva():
            self.__limite=valor
            ui('Limite de Cheque Especial no valor de {} implantado com sucesso na conta de número {}.'.format(formatacaoMoeda(valor),self.numero))

    def consultarLimiteConta(self):
        if self.confereAtiva():
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
                self.__transacoes.append((-valor,self.saldo,dataHoraAtual()))
            else:
                ui('Saque de {} não permitido! Valores de saldo/limite insuficientes!'.format(formatacaoMoeda(valor)))

    def transferencia(self,valor,contaDestino):
        if self.confereAtiva() and contaDestino.confereAtiva():
            if self.__saldo+self.__limite>=valor:
                self.__saldo-=valor
                contaDestino.__saldo+=valor
                ui('Transferência de {} da conta número {} para a conta {} efetivada com sucesso!'.format(formatacaoMoeda(valor),self.numero,contaDestino.numero))
                self.__transacoes.append((-valor,self.saldo,dataHoraAtual()))
                contaDestino.__transacoes.append((valor,self.saldo,dataHoraAtual()))
            else:
                ui('Transferência de {} não permitida! Valores de saldo/limite insuficientes!'.format(formatacaoMoeda(valor)))
            

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self,novoNumero):
        if novoNumero not in NumeroConta.numerosConta:
                NumeroConta.numerosConta.append(novoNumero)
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
