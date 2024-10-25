from time import sleep
from random import randint
print('Valores Sorteados:')
sleep(1)
jogadores = dict()
for c in range(1, 5):
    num = randint(1, 6)
    print(f'O jogador{c} tirou {num}')
    sleep(1)
    jogadores[f'jogador{c}'] = num
print('Ranking dos jogadores')
print(jogadores)