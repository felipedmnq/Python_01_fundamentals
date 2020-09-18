# PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM SENDO R$0.50 POR KM ATÉ 200 KM
# R$ 0.45 ACIMA DE 200KM.

d = float(input('Qual a distância em quilômetros entre a cidade de partida e a cidade de destino? '))
v1 = d * 0.5
v2 = d * .45
print('DISTÂNCIA ENTRE AS CIDADES: {}Km'.format(d))
if d > 200:
    print('VALOR DA PASSAGEM: R${:.2f}.'.format(v2))
else:
    print('VALOR DA PASSAGEM: R${:.2f}.'.format(v1))
print('     BOA VIAGEM!')