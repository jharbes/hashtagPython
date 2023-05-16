import numerosConta

class ContaCorrente:

    def __init__(self,nomeTitular,cpfTitular,saldo) -> None:
        self.numero=numerosConta.NumerosConta.gerarNumeroConta()
        self.nomeTitular=nomeTitular
        self.cpfTitular=cpfTitular
        self.saldo=saldo




