"""
# Exercícios

## 1. Tamanho do Pedido de Compras

Nesse exercício vamos avaliar o estoque de uma empresa. Vamos considerar que todos os produtos dessa empresa são comprados em lotes de 500 unidades.

- Caso o estoque esteja abaixo de 1000 unidades, devemos fazer um pedido de 500 unidades.
- Caso o estoque esteja abaixo de 200 unidades, devemos fazer um pedido de 1000 unidades.

Defina o valor a ser pedido de cada produto para enviar ao time de compras.

"""
estoque = [('BSA2199',396),('PPF5239',251),('BSA1212',989),('PPF2154',449),('BEB3410',241),('PPF8999',527),('EMB9591',601),('BSA2006',314),('EMB3604',469),('EMB2070',733),('PPF9018',339),('PPF1468',906),('BSA5819',291),('PPF8666',850),('BEB2983',353),('BEB5877',456),('PPF5008',963),('PPF3877',185),('PPF7321',163),('BSA8833',644),('PPF4980',421),('PPF3063',757),('BSA2089',271),('BSA8398',180),('EMB4622',515),('EMB9814',563),('PPF3784',229),('PPF2398',270),('BEB3211',181),('PPF8655',459),('PPF1874',799),('PPF8789',126),('PPF6324',375),('EMB9290',883),('BSA5516',555),('BSA8451',243),('BSA8213',423)]



pedido=[(produto,1000) if quantidade<200 else (produto,500)  for produto,quantidade in estoque]

print(pedido) # [('BSA2199', 500), ('PPF5239', 500), ('BSA1212', 500), ('PPF2154', 500), ('BEB3410', 500), ('PPF8999', 500), ('EMB9591', 500), ('BSA2006', 500), ('EMB3604', 500), ('EMB2070', 500), ('PPF9018', 500), ('PPF1468', 500), ('BSA5819', 500), ('PPF8666', 500), ('BEB2983', 500), ('BEB5877', 500), ('PPF5008', 500), ('PPF3877', 1000), ('PPF7321', 1000), ('BSA8833', 500), ('PPF4980', 500), ('PPF3063', 500), ('BSA2089', 500), ('BSA8398', 1000), ('EMB4622', 500), ('EMB9814', 500), ('PPF3784', 500), ('PPF2398', 500), ('BEB3211', 1000), ('PPF8655', 500), ('PPF1874', 500), ('PPF8789', 1000), ('PPF6324', 500), ('EMB9290', 500), ('BSA5516', 500), ('BSA8451', 500), ('BSA8213', 500)]

print()
for item in pedido:
    print(item)