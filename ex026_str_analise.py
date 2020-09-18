# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:

# QUANTAS VEZES APARECE A LETRA 'A'.
# EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ.
# EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ.

frase = input('Digite uma frase: ').upper()

print('QUANTAS LETRAS "A"?: {}'.format(frase.count('A')))
print('POSIÇÃO DO PRIMEIRO "A": {}'.format(frase.find('A') + 1))
print('POSIÇÃO DO ULTIMO "A": {}'.format(frase.rfind('A')))
