#CRIE UM PROGRAM QUE LEIA UM NUMERO REAL QUALQUER E MOSTRE NA TELA SUA PORÇÃO INTEIRA
#EXEMPLO - 6.124 => 6.

cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m'}

import math
n = float(input('{}Digite um número real qualquer: {}'.format(cores['vermelho'], cores['limpa'])))
print('{}A porção inteira do número digitado é: {}{}'.format(cores['azul'], math.trunc(n), cores['limpa']))
print('\033[1;31mA proção inteira do número digitado é: {}{}'.format(int(n), cores['limpa']))
