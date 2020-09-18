#faça um algotitmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

colors = {'bred':'\033[1;31m',
          'ulblue':'\033[4;34',
          'clean':'\033[m'}
name = str(input('{}Nome do produto: {}'.format(colors['ulblue'], colors['clean'])))
price = float(input('{}Preço do produto: R$ {}'.format(colors['ulblue'], colors['clean'])))
dct = float(input('{}Desconto a ser aplicado (%): {}'.format(colors['ulblue'], colors['clean'])))
pricef = price * ((100 - dct) / 100)
print('{}O valor de {} com desconto de {}% é R${}{}'.format(colors['bred'], name, dct, pricef, colors['clean']))

