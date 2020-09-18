# PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO
# CALCULE O AUMENTO NO SALÁRIO
# MAIOR DE R$ 1250 - 10%
# MENOR DE R$ 1250 - 15%

nome = str(input('Nome do funcionário: '))
sal = float(input('Qual o salário de {}?: R$'.format(nome)))
print('-=-' * 12)
print('CORREÇÃO SALARIAL')
print('EMPREGADO: {}'.format(nome))
print('-=-' * 12)
if sal < 1250:
    sal2 = sal + ((sal * 15) / 100)
else:
    sal2 = sal + ((sal * 10) / 100)
print('SALÁRIO CORRIGIDO: R${:.2f}.'.format(sal2))
print('-=-' * 12)