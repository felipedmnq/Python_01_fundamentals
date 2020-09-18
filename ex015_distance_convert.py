#PROGRAMA QUE SOCILITE A QTDADE DE KM RODADOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS USADO.
#CALCULE O PREÇO A PAGAR  - CARRO (r$60/DIA) - KM (R$0.15).

cores = {'limpa':'\033[m',
         'azul':'\033[1;34[m',
         'vermelho':'\033[1;31[m'}

kmi = float(input('{}Quilometragem inicial: {}'.format(cores['azul'], cores['limpa'])))
kmf = float(input('Quilometragem final: '))
km = float(kmf - kmi)
dias = input('Quantidade de diárias: ')
d = int(60)
vd = float(dias * 60)
kmrv = float(km * 0.15)
vt = (vd + kmrv)
print('{}O automóvel foi alugado por {} dias.\nForam rodados {}Km.\nO valor total a ser pago pelo aluguel será de R${:.2f}.{}'
      .format(cores['vermelho']dias, km, (vd + vt, cores['limpa'])))