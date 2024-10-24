#escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir
#qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario venceu ou perdeu.
from random import choice
escolha = int(input('Escolha um numero de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
random = choice(lista)
if random == escolha:
    print('Voce venceu')
else:
    print('Voce errou')