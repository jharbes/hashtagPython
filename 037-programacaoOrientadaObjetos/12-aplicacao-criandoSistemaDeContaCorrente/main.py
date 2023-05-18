from ContasBancos import *
from NumerosConta import *
from UI import ui

agenciaLocal='2290'

cc=[]

cc.append(ContaCorrente(agenciaLocal,'Jack Brown','272.628.000-51',500))
cc.append(ContaCorrente(agenciaLocal,'Lisa White','433.782.620-36',1500))
cc.append(ContaCorrente(agenciaLocal,'Johnie Walker','698.133.970-63',500000))

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

cc[0].transacoes



cc[0].numero=55555



ui(NumerosConta.numerosConta)


cc.append(ContaCorrente(agenciaLocal,'Jack Daniels','673.843.680-73',800))


ui(cc)

# for conta in cc:
#     ui(conta.__dict__)