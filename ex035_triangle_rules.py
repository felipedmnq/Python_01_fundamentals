# LEIA O COMPRIMENTO DE 3 RETAS E DIGA SE PODE OU NAO FORMAR UM TRIÂNGULO.
print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
r1 = float(input('1ª RETA (cm): '))
r2 = float(input('2ª RETA (cm): '))
r3 = float(input('3ª RETA (cm): '))
print('-=-' * 20)
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Com as retas de {}cm, {}cm e {}cm, É POSSÍVEL formar um triângulo!'.format(r1, r2, r3))
    #if r1 == r3 and r1 == r2 and r2 == r3:
        #print('O triângulo é equilátero.')
        #if r1 == r2 and r2 != r3 or r2 == r3 and r3 != r1 or r1 == r3 and r1 != r2:
            #print('O triângulo é isóceles.')
            #if r1 != r2 != r3:
                #print('O triângulo é escaleno.')
else:
    print('Com as retas de {}cm, {}cm e {}cm, NÃO É POSSÍVEL formar um triângulo!'.format(r1, r2, r3))
