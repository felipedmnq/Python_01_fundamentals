# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM 'SILVA' NO NOME.
#nome = input('Digite seu nome: ').strip().upper() #.strip tira espaços; .upper deixa tudo em maiusculo.
#n = ('SILVA' in nome) # com o nome inteiro colocado em maisvulo ele le de qualquer forma.
#print('Seu nome tem Silva? {}'.format(n))

name = input('\033[1;35mDigite seu nome completo: \033[m').split()

print('\033[1;35mSeu nome tem Silva?: {}\033[m'.format('SILVA' in name.upper()))