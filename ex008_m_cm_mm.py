#escreva um programa que leia um valor em metros e exiba ele convertido em centimetros e milimetros.

val = float(input('\033[4;33mMedida a ser convertida (m): \033[m'))
cm = val * 100
mm = val * 1000
print('\033[4;33mMetros: {}.\nCentímetros: {}.\nMilímetros: {}.\033[m'.format(val, cm, mm))
