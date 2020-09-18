#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dolares ela pode comprar (UU$3,27).

m = float(input('\033[1mValor a ser convertido: R$\033[m'))
cot = float(input('\033[1mCotação atualdo dólar: R$\033[m'))
conv = m / cot
print('\033[1m-------------------\nValor: R${:.2f}.\nCootação do dólar do dia: R${:.2f}.\n-----------------------\nU$${:.2f}.\033[m'.format(m, cot, conv))
