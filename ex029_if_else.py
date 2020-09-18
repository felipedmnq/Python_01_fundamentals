# LEIA A VELOCIDADE DE UM CARRO
# SE MAIOR QUE 80KM/H - MULTADO
# MULTA = R$7 PARA CADA KM ACIMA DE 80.

vel = float(input('Qual a velocidade registrada (Km/h): '))
vel2 = (vel - 80)
multa = vel2 * 7
print('*' * 25)
print('          RADAR')
print('*' * 25)
print('Velovidade: ', vel, ' Km/h')
if vel > 80:
    print('Você ultrapassou o limite de velidade em {}Km/h\nMulta: R${:.2f}.'.format(vel2, multa))
else:
    print('BOA VIAGEM!!')
print('*' * 25)
