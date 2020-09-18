#sortear a ordem de apresentação de trabalho, leia o nome de 4 alunos e mostre a ordem sorteada.

from random import shuffle

colors = {'limpa':'\033[m',
          'roxo':'\033[1;35m',
          'red':'\033[1;31m'}

a1 = str(input('ALUNO 01: '))
a2 = str(input('ALUNO 02: '))
a3 = str(input('ALUNO 03: '))
a4 = str(input('ALUNO 04: '))
list = [a1, a2, a3, a4]

sorteio = shuffle(list)

print('{}*{}'.format(colors['red'], colors['limpa']) * 35)
print('{}Ordem de apresentação dos trabalhos: {}'.format(colors['roxo'], colors['limpa']))
print('{}*{}'.format(colors['red'], colors['limpa']) * 35)
print(list)
print('{}*{}'.format(colors['red'], colors['limpa']) * 35)
