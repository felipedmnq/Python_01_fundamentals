#faça um programa que leia a largura e altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessáruia para pintá-la, sabendo que caa litro de tinta pinta 2m2.

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[m',
         'verm':'\033[31m',
         'ngt':'\033[1m',
         'ngtverm':'\033[1;31m'}
print('{}------CALCULADORA DE TINTA------{}'.format(cores['ngtverm'], cores['limpa']))
l = float(input('{}Insira a largura da superfície (m): {}'.format(cores['verm'], cores['limpa'])))
h = float(input('{}insira a altura da superfície (m): {}'.format(cores['verm'], cores['limpa'])))
area = l * h
tinta = area / 2
print('{}A área total da sua parede é {} mª e você precisará de {} litros de tinta para pintá-la.{}'
      .format(cores['ngtverm'], area, tinta, cores['limpa']))

