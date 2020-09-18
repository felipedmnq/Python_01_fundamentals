#Converta a temperatura atual em Cº para Fº.

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[m',
         'verm':'\033[31m',
         'ngt':'\033[1m',
         'ngtverm':'\033[1;31m'}
ta = float(input('Digite a temperatura em graus Céucius: '))
f = (ta * (9/5) + 32)
print('{}{}º Céucius são equivalentes a {}º Fahrenheit.{}'.format(cores['azul'], ta, f, cores['limpa']))
