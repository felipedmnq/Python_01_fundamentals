# DOBRO, TRIPLO E RAIZ DE UM NÚMERO

n1 = int(input('\033[1;31mDigite um número: \033['))
d = n1 * 2
t = n1 * 3
r = (n1**(1/2))
print('\033[1;31mVocê escolheu o número {}.\nO seu dobro é {}.\nSeu triplo é {}.\nSua raiz quadrada é {:.2f}.\033[m'.format(n1, d, t, r))

