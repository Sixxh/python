# crie um programa que faca o jogo jogar jokenpo com voce.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Vamos Jogar JO-KEN-PO
Escolha uma das opcoes abaixo
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('O computador escolheu {}.'.format(itens[computador]))
print('O jogador escolheu {}.'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Invalida')
elif computador == 1:
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Invalida')
elif computador == 2:
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida')
