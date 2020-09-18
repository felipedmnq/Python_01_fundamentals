#sortear alunos para apagar o quadro, lendo o nome dos 4 alunos e sorteando o escolhido.
#import random

colors = {'limpa':'\033[m',
          'roxo':'\033[1;35m',
          'red':'\033[1;31m'}

from random import choice

a1 = str(input('ALUNO 01: '))
a2 = str(input('ALUNO 02: '))
a3 = str(input('ALUNO 03: '))
a4 = str(input('ALUNO 04: '))
list = [a1, a2, a3, a4]

choice = choice(list)

print(('{}-=-{}'.format(colors['roxo'], colors['limpa'])) * 20)
print('{}ESCOLHA DO ALUNO: {}'.format(colors['red'], colors['limpa']))
print(('{}-=-{}'.format(colors['roxo'], colors['limpa'])) * 20)
print('{}ALUNO SORTEADO: {}{}'.format(colors['red'], choice, colors['limpa']))
