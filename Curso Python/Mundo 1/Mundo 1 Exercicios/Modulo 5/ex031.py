#desenvolva um programa que pergunte a distancia de uma viagem em km.
#calcule o preco da passagem, cobrando R$0,50 por km para viagens ate 200km
#e R$0.45 para viagens mais longas
viagem = float(input('Quantos km voce viajou: '))
if viagem <= 200:
    print('Voce tera que pagar {:.2f}'.format(viagem * 0.50))
else:
    print('Voce tera que pagar {:.2f}'.format(viagem * 0.45))