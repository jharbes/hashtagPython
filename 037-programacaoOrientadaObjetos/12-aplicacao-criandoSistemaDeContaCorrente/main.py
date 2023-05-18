from ContaCorrente import *
from NumeroConta import *
from UI import ui

agenciaLocal='2290'

cc=[]

cc.append(ContaCorrente(agenciaLocal,'Jack Brown','272.628.000-51',500))
cc.append(ContaCorrente(agenciaLocal,'Lisa White','433.782.620-36',1500))
cc.append(ContaCorrente(agenciaLocal,'Johnie Walker','698.133.970-63',500000))

ui(cc[0].agencia)
ui(vars(cc[0]))
ui(cc[0].__dict__)

ui(NumeroConta.numerosConta)

cc[0].saque(200)
cc[2].deposito(10000000000000)

cc[0].limiteConta(1000)

cc[0].saque(800)

cc[0].saque(700)

cc[0].saque(300)

cc[0].consultarSaldo()

cc[0].transacoes



cc[0].numero=55555



ui(NumeroConta.numerosConta)


cc.append(ContaCorrente(agenciaLocal,'Jack Daniels','673.843.680-73',800))


ui(cc)

cc[0].transferencia(500,cc[2])
cc[2].transferencia(1000,cc[0])

cc[2].transacoes

# for conta in cc:
#     ui(conta.__dict__)

help(ContaCorrente)