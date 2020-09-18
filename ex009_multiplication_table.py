#faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('\033[1;36mTABUADA DE: \33[m'))
aux = 0
print('\033[1;36m-\033[m' * 20)
while(aux <= 10):
    print('\033[1;36m{} X {} = {}\033[m'.format(n1, aux, (aux + 1)))
    aux = aux + 1
