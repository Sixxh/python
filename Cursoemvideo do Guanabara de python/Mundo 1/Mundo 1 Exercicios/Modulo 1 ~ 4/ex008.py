# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
#metro = int(input('Escreva quantos mestros sao: '))
#cent = metro * 100
#mili = metro * 1000
#print('{} Metros convertido para centimetros fica {} e para milimetros fica {}'.format(metro, cent, mili))
medida = float(input('Digite um valor em metro:'))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}dm.'.format(medida, (medida*10)))
print('A medida de {}m corresponde a {:.0f}cm e a {:.0f}mm.'.format(medida, cm, mm))
print('A medida de {}m corresponde a {}dam.'.format(medida, (medida/10)))
print('A medida de {}m corresponde a {}hm.'.format(medida, (medida/100)))
print('A medida de {}m corresponde a {}km.'.format(medida, (medida/1000)))