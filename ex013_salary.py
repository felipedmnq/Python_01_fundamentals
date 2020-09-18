#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.


cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[m',
         'verm':'\033[31m',
         'ngt':'\033[1m',
         'ngtverm':'\033[1;31m'}
nome = input('{}Digite o nome do funcionário: {}'.format(cores['verm'], cores['limpa']))
s = float(input('Digite o salário bruto de {} R$: '.format(nome)))
alm = float(input('Digite a porcentagem do aumento que será dado a {}: '.format(nome)))
s2 = (s*((100+alm)/100))
print('{}O salário de {} com aumento de {:.2f}% ficará R${:.2f}.{}'.format(cores['ngtverm'], nome, alm, s2, cores['limpa']))