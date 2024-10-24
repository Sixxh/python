# faca um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria
# para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m2.
# largura = int(input('Qual a largura da parede: '))
# altura = int(input('Qual a altura da parede: '))
# area = largura * altura
# tinta = 2 ** 2
# quantidade = area / tinta
# print('Voce precisara de {:.1f} tintas para pintar a parede.'.format(quantidade))
#professor
larg = float(input('Qual larguda da parede: '))
alt = float(input('Qual a altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensao de {}x{} e sua area e de {}m2.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, voce precisara de {}l de tinta.'.format(tinta))