from ContasBancos import *
from NumerosConta import *
from UI import ui

agenciaLocal='2290'

cc=[]

cc.append(ContaCorrente(agenciaLocal,'Jorge Nami Harbes','10231086741',500))
cc.append(ContaCorrente(agenciaLocal,'Carolina Ferreira Alcantara','16242112752',1500))
cc.append(ContaCorrente(agenciaLocal,'Elizabeth Barreto Ramos Ferreira Harbes','39634299768',500000))

ui(cc[0].agencia)
ui(vars(cc[0]))
ui(cc[0].__dict__)

ui(NumerosConta.numerosConta)

cc[0].saque(200)
cc[2].deposito(10000000000000)

cc[0].limiteConta(1000)

cc[0].saque(800)

cc[0].saque(700)

cc[0].saque(300)

cc[0].consultarSaldo()



cc[0].numero=55555



ui(NumerosConta.numerosConta)


cc.append(ContaCorrente(agenciaLocal,'Matheus Attilio','96564512785',800))


ui(cc)

# for conta in cc:
#     ui(conta.__dict__)