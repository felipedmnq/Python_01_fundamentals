# FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA UM DOS DÍGITOS SEPARADOS

#EX: unidade: 9; dezena 9; centena 9; milhar 9. - fazer como str e matematicamente.
#n1 = input('Digite um número de 0 a 9999: ')

n1 = (int(input('\033[1;34mDigite um número inteiro de 4 digitos (xxxx): \033[m')))

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('\033[1;34mUNIDADE: {}.\nDEZENA: {}.\nCENTENA: {}.\nMILHAR: {}.\033[m'.format(u, d, c, m))

