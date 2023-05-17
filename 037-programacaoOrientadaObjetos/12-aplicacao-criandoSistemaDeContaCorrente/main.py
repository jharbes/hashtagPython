from contasBancos import *
from numerosConta import *
from UI import ui

cc=[]

cc.append(ContaCorrente('Jorge Nami Harbes',10231086741,500))
cc.append(ContaCorrente('Carolina Ferreira Alcantara',16242112752,1500))
cc.append(ContaCorrente('Elizabeth Barreto Ramos Ferreira Harbes',39634299768,500000))


ui(cc[0].__dict__)

ui(numerosConta.NumerosConta.numerosConta)

cc[0].saque(200)
cc[2].deposito(10000000000000)

cc[0].limiteConta(1000)

cc[0].saque(800)

cc[0].saque(700)

cc[0].saque(300)

cc[0].consultarSaldo()



cc[0].numero=55555



ui(numerosConta.NumerosConta.numerosConta)


cc.append(ContaCorrente('Matheus Attilio',96564512785,800))


ui(cc)

for conta in cc:
    ui(conta.__dict__)