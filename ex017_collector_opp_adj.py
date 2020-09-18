#PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E  DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO.
#CALCULE A HIPOTENUSA

from math import hypot

colors = {'limpa':'\033[m',
          'roxo':'\033[1;35m',
          'vermelho':'\033[1;31m'}

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('{}Digite o valor do cateto asdjacente: {}'.format(colors['vermelho'], colors['limpa'])))
hyp = hypot(ca, co)
print('{}O valor da hipotenusa com Cateto Oposto {} e Cateto Adjacente {} é: {:.2f}{}'.format(colors['roxo'], co, ca, hyp, colors['limpa']))
