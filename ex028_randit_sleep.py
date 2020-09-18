# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NUMERO INT ENTRE 0 E 5 E PEÇA
# PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NUMERO ESCOLHIDO.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE VOCÊ GANHOU OU PERDEU.

from random import randint
from time import sleep  # faz o computador "esperar".
computador = int(randint(0,5)) # FAZ O SORTEIO ENTRE 0 E 5
print('#' * 65)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADIVINHAR ESSE NUMERO!')
print('#' * 65)
print('PROCESSANDO...')
sleep(2)
print('#' * 65)
jogador = int(input('Digite um número entre 1 e 5: ')) # O JOGADOR TENTA ADIVINHAR.
print('#' * 65)
if jogador == computador:
    print('Você escolheu o número {}, parabéns, você acertou!!!'.format(computador))
else:
    print('Você escolheu o número {}, infelizmente você errou, tente novamente!'. format(computador))