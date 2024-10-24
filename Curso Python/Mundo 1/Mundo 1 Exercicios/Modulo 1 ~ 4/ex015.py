#dia = int(input('Quantos dias ficou com o carro? '))
#km = float(input('Quantos kilometros rodou? '))
#dia_rodado = dia * 60
#km_rodado = km * 0.15
#pagar = dia_rodado + km_rodado
#print('Voce deve pagar R${:.2f} por ter rodado {:.0f}dias e {}kms'.format(pagar, dia, km))
#professor
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar e de R${:.2f}'.format(pago))