from contasBancos import *
from numerosConta import *
from UI import ui

contasCorrentes=[]

c1=ContaCorrente('Jorge Nami Harbes',10231086741,500)
c2=ContaCorrente('Carolina Ferreira Alcantara',16242112752,1500)
c3=ContaCorrente('Elizabeth Barreto Ramos Ferreira Harbes',39634299768,500000)

ui(c1.__dict__)

ui(numerosConta.NumerosConta.numerosConta)

c1.saque(200)
c3.deposito(10000000000000)

c1.limiteConta(1000)
c1.saque(800)
c1.consultarSaldo()



c1.numero=55555



ui(numerosConta.NumerosConta.numerosConta)


contasCorrentes.append(ContaCorrente('Jorge Nami Harbes',10231086741,500))


ui(contasCorrentes)

for conta in contasCorrentes:
    ui(conta.__dict__)