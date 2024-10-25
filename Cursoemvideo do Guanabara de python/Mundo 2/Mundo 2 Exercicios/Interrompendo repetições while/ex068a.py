# faca um programa que jogue par ou impar com o computador. o jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador} total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu!')
            v += 1
        else:
            print('Voce Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Voce Venceu!')
            v += 1
        else:
            print('Voce Perdeu')
    print('Vamos Jogar Novamente...')
print(f'Game Over! Voce Venceu {v} vezes')