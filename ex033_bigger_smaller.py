# LEIA 3 NUMEROS E MOSTRE O MAIOR E O MENOR.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número '))
#ns = [n1, n2, n3]
print('*' * 20)
print('1º número: {}.\n2º número: {}.\n3º número: {}.'.format(n1, n2, n3))
print('*' * 20)
print('ANÁLISE DOS NÚMEROS:')
print('*' * 20)
if n1 > n2 and n1 > n3:
    print('O maior número é: {}.'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('O maior número é: {}.'.format(n2))
    else:
        if n3 > n1 and n3 > n2:
            print('O maior número é: {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor número é: {}'.format(n1))
else:
    if n2< n1 and n2 < n3:
        print('O menor número é: {}'.format(n2))
    else:
        if n3 < n2 and n3 < n1:
            print('O menor numero é: {}'.format(n3))

