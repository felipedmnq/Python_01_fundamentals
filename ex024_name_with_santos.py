# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "santo".

name = str(input('\033[4;33mDigite o nome de uma cidade: \033[m').strip())

print(name[:5].upper() == 'SANTO')

