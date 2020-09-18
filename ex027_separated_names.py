# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE OS NOME SEPARADOS.
#1º ANA
#2º MARIA

name = input('DIGITE SEU NOME: ').strip()
lstname = name.split()

print('SEU PRIMEIRO NOME É: {}.'.format(lstname[0]))
print('SEU ULTIMO NOME É: {}.'.format(lstname[len(lstname) -1]))