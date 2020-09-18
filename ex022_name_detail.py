# CRIE UM PROGRAMA QUE LIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

# O NOME COM TODAS AS LETRAS MAIUSCULAS.
# TODAS MINUSCULAS.
# QUANTAS LETRAS AO TOTAL SEM CONSIDERAR OS ESPAÇOS.
# QUANTAS LETRAS TEM O PRIMEIRO NOME.

name = str(input('\033[1;34mDigite um nome: \033[m'))
list = name.split()

print('TUDO MAISCULO: {}'.format(name.upper()))
print('TUDO MINUSCULO: {}'.format(name.lower()))
print('NOME SEM ESPAÇOS: {}'.format(name.replace(' ', '')))
print('TOTAL DE CARANTERES DE {}: {}'.format(name, (len(name))))
print('TOTAL DE CARACTERES SEM ESPAÇO: {}'.format(len(name.replace(' ', ''))))
print('TOTAL DE CARACTERES DO PRIMEIRO NOME: {}'.format(len(list[0])))