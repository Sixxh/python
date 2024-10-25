# professor
from random  import randint
from time import sleep
computador = randint(0, 5) # escolhe numero aleatorio entre 0 e 5
print('-=-' * 20)
print('Adivinhe o numero entre 0 e 5')
print('-=-' * 20)
jogador = int(input('Adivinhe qual numero o computador escolheu: '))
print('Aguardando resposta...')
sleep(2)
if jogador == computador:
    print('Voce acertou!')
else:
    print('Voce errou, o numero era {}.'.format(computador))