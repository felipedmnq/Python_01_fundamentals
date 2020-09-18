# LEIA UM NUMERO E MOSTRE SE É PAR OU IMPAR.
print('-=-' * 8)
n = int(input('Digite um número: '))
print('-=-' * 8)
if n % 2 == 1:
    print('O número {} é IMPAR.'.format(n))
else:
    print('O número {} é PAR.'.format(n))