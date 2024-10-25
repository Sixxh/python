#melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.
#so que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.
from random  import randint
from time import sleep
computador = randint(0, 5) # escolhe numero aleatorio entre 0 e 5
print('-=-' * 20)
print('Adivinhe o numero entre 0 e 5')
print('-=-' * 20)
jogador = 8
tentativas = 0
jogador = int(input('Adivinhe qual numero o computador escolheu: '))
while jogador != computador:
    tentativas += 1
    if jogador < computador:
        jogador = int(input('O numero e maior do que {}: '.format(jogador)))
    if jogador > computador:
        jogador = int(input('O numero e menor que {}: '.format(jogador)))
if jogador == computador:
    print('Voce acertou!')
    print('Voce tentou {}x Vezes ate vencer.'.format(tentativas))