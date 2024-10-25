# faca um programa que jogue par ou impar com o computador. o jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint
ganhou = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um numero: '))
    escolha = str(input('Voce escolhe par ou impa? ')).strip().upper()[0]
    soma = computador + jogador
    resultado = ''
    print(f'Voce jogou {jogador} e o computador {computador} o total e {soma}', end=' ')
    if soma % 2 == 0:
        resultado = 'P'
        print('Par')
    else:
        resultado = 'I'
        print('Impar')
    if escolha == resultado:
        print('Voce Ganhou')
        ganhou += 1
    else:
        print(f'Voce perdeu! Mas ganhou {ganhou}x vezes.')
        break