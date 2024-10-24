# crie um programa que faca o jogo jogar jokenpo com voce.
from random import randint
print('Vamos jogar jokenpo, as opcoes sao: ')
print('1. Pedra')
print('2. Papel')
print('3. Tesoura')
player = int(input('Qual sua escolha? '))
maquina = randint(1, 3)
if player == 1 and maquina == 1:
    print('Empate ambos escolheram a mesma coisa.')
elif player == 1 and maquina == 2:
    print('Voce Perdeu.')
elif player == 1 and maquina == 3:
    print('Voce Ganhou.')
elif player == 2 and maquina == 1:
    print('Voce Ganhou.')
elif player == 2 and maquina == 2:
    print('Empate ambos escolheram a mesma coisa.')
elif player == 2 and maquina == 3:
    print('Voce Perdeu.')
elif player == 3 and maquina == 1:
    print('Voce Perdeu.')
elif player == 3 and maquina == 2:
    print('Voce Ganhou')
elif player == 3 and maquina == 3:
    print('Empate ambos escolheram a mesma coisa.')
