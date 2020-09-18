#programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente.
#import math

from math import sin, cos, tan, radians

colors = {'limpa':'\033[m',
          'roxo':'\033[1;35m',
          'red':'\033[1;31m'}

angle = float(input('Digite o valor do ângulo: '))
print('{}Seno do ângulo {}: {:.2f}{}'.format(colors['red'], angle, sin(angle), colors['limpa']))
print('{}Cosseno do ângulo {}: {:.2f}{}'.format(colors['roxo'], angle, cos(angle), colors['limpa']))
print('{}Tangente do ângulo {}: {:.2f}{}'.format(colors['red'], angle, tan(angle), colors['limpa']))
print('{}Seno (radianos): {:.2f}{}'.format(colors['red'], sin(radians(angle)), colors['limpa']))
print('{}Cosseno (radianos): {:.2f}{}'.format(colors['roxo'], cos(radians(angle)), colors['limpa']))
print('{}Tangente (radianos): {:.2f}{}'.format(colors['red'], tan(radians(angle)), colors['limpa']))

