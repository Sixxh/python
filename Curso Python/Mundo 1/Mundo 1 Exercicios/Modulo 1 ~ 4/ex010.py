# crie um porgarama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# considere 
# US$ 1,00 = 3,27
# carteira = float(input('Quantos reais voce tem? R$'))
# dolar = 3.27
# converter = carteira / 3.27
# print('Com R${:.2f} voce consegue comprar ${:.2f}.'.format(carteira,converter))
#professor
carteira = float(input('Quantos reais voce tem? R$'))
dolar = carteira / 4.96
euro = carteira / 5.35
print('Com R${:.2f} voce consegue comprar US${:.2f}.'.format(carteira, dolar))
print('Com R${:.2f} voce consegue comprar EU${:.2f}.'.format(carteira, euro))