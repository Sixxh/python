#escreva um programa que leia a velocidad de um carro
#se ele ultrapasasr 80km/hr, mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$7,00 por cada km acima do limite
velo = float(input('Qual a velocidade do carro: '))
if velo > 80:
    print('Voce passou do limite e vai ter q pagar uma multa de {:.2f}'.format((velo - 80) * 7.00))
else:
    print('Voce esta abaixo do limite.')