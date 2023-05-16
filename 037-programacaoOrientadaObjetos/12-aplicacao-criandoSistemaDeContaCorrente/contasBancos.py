import numerosConta

class ContaCorrente:

    numerosConta=[]

    def __init__(self,nomeTitular,cpfTitular,saldo) -> None:
        self.numero=numerosConta.NumerosConta.gerarNumeroConta()
        self.nomeTitular=nomeTitular
        self.cpfTitular=cpfTitular
        self.saldo=saldo




c1=ContaCorrente('Jorge Nami Harbes',10231086741,500)

print(c1.__dict__)